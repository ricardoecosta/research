#!/usr/bin/env python3
"""v8 steps 1-3 at ingest: quarantine checks, numbered original lines, Codex labelling of removed ranges
(sponsor/intro_outro/filler/tangent) and one record per business. Writes analysis/v8/ingest/<id>.json.
Usage: ingest.py [--ids a,b] [--effort medium] [--outdir DIR] [--workers 6]"""
import argparse, collections, concurrent.futures as cf, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *

LOGF = WORK / "ingest.log"
PROMPT = """You label ONE YouTube business/side-hustle transcript for a research pipeline. You do not run commands or read files; everything is below.
The transcript is given as numbered ORIGINAL lines: `L0001 [m:ss] text` (minutes are approximate).

Task A (cleaning): list the line ranges to REMOVE before mining, each with a reason:
- "sponsor": sponsor reads, ad segments, promo codes for a sponsor
- "intro_outro": channel intros/outros, subscribe/like/comment requests, plugs for the host's own newsletter/course/community
- "filler": throat-clearing, greetings and small talk with no information
- "tangent": personal stories, banter or off-topic chat unrelated to any business, money-making method or business lesson
Be conservative: if a line has ANY business information (an idea, number, tactic, customer, tool, warning or lesson), keep it.

Task B (splitting): list every distinct BUSINESS discussed (including ones mentioned in passing, and the guest's main business). One record per business; never mix two businesses in one record. For each give the business as the speaker names/describes it, and the line ranges where it is discussed (ranges may be non-contiguous). If the video is general advice with no specific business, return an empty list.

Output ONLY this JSON:
{"removed":[{"from":int,"to":int,"reason":"sponsor|intro_outro|filler|tangent"}],
 "records":[{"business":"as the speaker describes it","ranges":[[from,to],...],"is_primary":bool}],
 "multi_business":bool, "has_business_content":bool, "language_ok":bool, "notes":"short"}

TITLE: {title}
CHANNEL: {channel}
<transcript>
{lines}
</transcript>"""


def checks(vid, dates):
    try:
        text, meta, body = parse_raw(vid)
    except Exception as e:
        return f"unreadable: {e}", None
    if text.count("\ufffd") > 0.01 * max(len(text), 1): return "decode errors >1%", None
    if len(body) < 1500: return f"body too short ({len(body)} chars)", None
    letters = [c for c in body if c.isalpha()]
    if letters and sum(c.isascii() for c in letters) / len(letters) < 0.85: return "not English (<85% ASCII letters)", None
    w = norm(body).split()
    grams = [tuple(w[i:i + 5]) for i in range(max(len(w) - 4, 0))]
    if grams and len(set(grams)) / len(grams) < 0.35: return f"whisper loop ({len(set(grams)) / len(grams):.2f} unique 5-grams)", None
    if vid not in dates or not dates[vid]["date"] or dates[vid]["date"] == "NA": return "no publish date", None
    return None, meta


def ingest_one(vid, dates, effort, outdir):
    op = outdir / f"{vid}.json"
    if op.exists(): return vid, "cached"
    q, meta = checks(vid, dates)
    base = dict(id=vid, publish_date=dates.get(vid, {}).get("date"), channel=dates.get(vid, {}).get("channel"))
    if q:
        op.write_text(json.dumps({**base, "status": "quarantined", "quarantine_reason": q}, indent=1)); return vid, "quarantined " + q
    meta, body, rows = numbered(vid, dates)
    prompt = PROMPT.replace("{title}", meta.get("title", "")).replace("{channel}", meta.get("channel", "")).replace("{lines}", fmt_lines(rows))
    try:
        data, runner, secs = call_llm(prompt, effort, LOGF, vid)
        n = len(rows)
        for r in data.get("removed", []): r["from"], r["to"] = max(1, int(r["from"])), min(n, int(r["to"]))
        recs = []
        for k, r in enumerate(data.get("records", []), 1):
            rg = [[max(1, int(a)), min(n, int(b))] for a, b in r.get("ranges", []) if int(a) <= int(b)]
            recs.append(dict(record_id=f"{vid}#r{k}", business=r.get("business", ""), ranges=rg, is_primary=bool(r.get("is_primary"))))
        removed_lines = sorted({l for r in data.get("removed", []) for l in range(r["from"], r["to"] + 1)})
        out = {**base, "status": "ingested", "title": meta.get("title"), "provider": meta.get("provider"),
               "duration_s": dates[vid]["duration"], "n_lines": n, "n_removed_lines": len(removed_lines),
               "removed": data.get("removed", []), "records": recs, "multi_business": len(recs) > 1,
               "has_business_content": data.get("has_business_content"), "language_ok": data.get("language_ok"),
               "notes": data.get("notes"), "stale_age": dates[vid]["date"] < STALE_BEFORE,
               "ingest_runner": runner, "ingest_secs": round(secs)}
        op.write_text(json.dumps(out, ensure_ascii=False, indent=1))
        return vid, f"ok lines={n} removed={len(removed_lines)} records={len(recs)} {runner} {secs:.0f}s"
    except Exception as e:
        op.write_text(json.dumps({**base, "status": "quarantined", "quarantine_reason": f"ingest failed on all runners: {str(e)[:200]}"}, indent=1))
        return vid, "quarantined ingest-fail"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default=""); ap.add_argument("--effort", default="xhigh")
    ap.add_argument("--outdir", default=str(V8 / "ingest" / "records")); ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    outdir = Path(a.outdir); outdir.mkdir(parents=True, exist_ok=True)
    dates = load_dates()
    ids = a.ids.split(",") if a.ids else sorted(p.stem for p in RAW_TX.glob("*.txt"))
    log(LOGF, f"START ingest {len(ids)} effort={a.effort} out={outdir}")
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for f in cf.as_completed([ex.submit(ingest_one, v, dates, a.effort, outdir) for v in ids]):
            vid, st = f.result(); log(LOGF, f"DONE {vid} {st} total={len(list(outdir.glob('*.json')))}")
    log(LOGF, "END")


if __name__ == "__main__":
    main()
