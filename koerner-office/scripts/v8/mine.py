#!/usr/bin/env python3
"""v8 steps 4-5: structured mining per transcript (Codex xhigh -> pi fallback), UK legal filter at mining.
Input: analysis/v8/ingest/records/<id>.json. Output: analysis/v8/mined/<id>.json (resumable).
Usage: mine.py [--ids=a,b] [--workers 6]"""
import argparse, concurrent.futures as cf, datetime as dt, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *

LOGF = WORK / "mine.log"
SYSTEM = (Path(__file__).parent / "mine_prompt.md").read_text()
OUT = V8 / "mined"
REQ = ["record_id", "depth", "stated_problem", "idea", "citation", "claims", "feature_request", "specifics", "uk_legal_risk"]


def validate(data, n):
    errs = []
    if not isinstance(data.get("ideas"), list): return ["ideas missing"]
    for k, i in enumerate(data["ideas"]):
        for r in REQ:
            if r not in i: errs.append(f"idea{k} missing {r}")
        c = i.get("citation") or {}
        if not c.get("lines"): errs.append(f"idea{k} no citation")
        if (i.get("idea") or {}).get("category") not in CATS:
            i.setdefault("idea", {})["category"] = "other"
    return errs


def mine_one(vid):
    op = OUT / f"{vid}.json"
    if op.exists(): return vid, "cached"
    ing = json.loads((V8 / "ingest" / "records" / f"{vid}.json").read_text())
    if ing["status"] != "ingested": return vid, "skip-quarantined"
    dates = load_dates()
    meta, body, rows = numbered(vid, dates)
    removed = {l for r in ing["removed"] for l in range(r["from"], r["to"] + 1)}
    keep = {r["line"] for r in rows} - removed
    recs = "\n".join(f"- {r['record_id']}: {r['business']} | lines {r['ranges']}" for r in ing["records"]) or "(none found at ingest)"
    prompt = (SYSTEM + f"\n\nVIDEO ID: {vid}\nTITLE: {ing.get('title')}\nCHANNEL: {ing.get('channel')}\nPUBLISHED: {ing['publish_date']}\n"
              f"RECORDS:\n{recs}\n\n<transcript>\n{fmt_lines(rows, keep)}\n</transcript>\n\nReturn the JSON now.")
    last = ""
    for attempt in range(3):
        try:
            data, runner, secs = call_llm(prompt, "xhigh", LOGF, vid)
            errs = validate(data, len(rows))
            if errs and attempt < 2:
                last = "; ".join(errs[:3]); log(LOGF, f"{vid} schema errors {last}; retry"); continue
            nid = 0
            for i in data["ideas"]:
                nid += 1
                i["idea_id"] = f"{vid}:i{nid}"
                if i.get("record_id") == "new" or i.get("record_id") not in {r["record_id"] for r in ing["records"]}:
                    i["record_added_at_mining"] = True
                    i["record_id"] = f"{vid}#m{nid}"
                sp = i.get("specifics") or {}
                i["specifics_flag"] = bool(sp.get("tools") or sp.get("prices") or sp.get("platforms"))
                i["publish_date"] = ing["publish_date"]
                i["stale_age"] = ing["publish_date"] < STALE_BEFORE
                i["recheck"] = i["specifics_flag"]
            out = dict(id=vid, title=ing.get("title"), channel=ing.get("channel"), publish_date=ing["publish_date"],
                       miner=runner, mined_at=dt.datetime.now().isoformat(timespec="seconds"), secs=round(secs),
                       schema_errors=errs, **data)
            op.write_text(json.dumps(out, ensure_ascii=False, indent=1))
            return vid, f"ok ideas={len(data['ideas'])} {runner} {secs:.0f}s errs={len(errs)}"
        except Exception as e:
            last = str(e)[:200]; log(LOGF, f"{vid} attempt {attempt + 1} failed {last}")
    (V8 / "mined" / "_failed").mkdir(parents=True, exist_ok=True)
    (V8 / "mined" / "_failed" / f"{vid}.txt").write_text(last)
    return vid, "FAILED " + last


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ids", default=""); ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args(); OUT.mkdir(parents=True, exist_ok=True)
    ids = a.ids.split(",") if a.ids else sorted(p.stem for p in (V8 / "ingest" / "records").glob("*.json"))
    todo = [i for i in ids if not (OUT / f"{i}.json").exists()]
    log(LOGF, f"START mine {len(todo)} workers={a.workers}")
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for f in cf.as_completed([ex.submit(mine_one, v) for v in todo]):
            try: vid, st = f.result()
            except Exception as e: vid, st = "?", f"crash {e}"
            log(LOGF, f"DONE {vid} {st} total={len(list(OUT.glob('*.json')))}")
    log(LOGF, "END")


if __name__ == "__main__":
    main()
