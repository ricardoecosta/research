#!/usr/bin/env python3
"""Finalize a raw model extraction: add video metadata, verify quotes against the transcript,
validate against the JSON Schema, and write analysis/v7/transcripts/<id>.json and <id>.md.
Re-runnable: python finalize.py [id ...] (no args = all raw files)."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *
import jsonschema
from rapidfuzz import fuzz

SCHEMA = json.loads(SCHEMA_PATH.read_text())
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA)
QKEYS = {"text", "speaker", "verified", "match_score", "char_offset", "approx_timestamp_s"}
_IDX = None


def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def verify_quote(q, body_n, dur):
    frags = [norm(f) for f in re.split(r"\.\.\.|…", q.get("text", "")) if len(norm(f)) >= 12]
    if not frags:
        frags = [norm(q.get("text", ""))]
    scores, offs = [], []
    for fr in frags:
        al = fuzz.partial_ratio_alignment(fr, body_n, score_cutoff=0)
        scores.append(al.score if al else 0)
        offs.append(al.dest_start if al else None)
    sc = min(scores) if scores else 0
    off = offs[0]
    q["match_score"] = round(sc, 1)
    q["verified"] = sc >= 90
    q["char_offset"] = off
    q["approx_timestamp_s"] = int(off / max(len(body_n), 1) * dur) if (off is not None and dur) else None
    return sc


def walk_quotes(o, out):
    if isinstance(o, dict):
        if "text" in o and set(o).issubset(QKEYS):
            out.append(o)
        else:
            for v in o.values():
                walk_quotes(v, out)
    elif isinstance(o, list):
        for v in o:
            walk_quotes(v, out)


def _int(x):
    try:
        return int(float(x))
    except Exception:
        return None


def finalize(vid):
    global _IDX
    if _IDX is None:
        _IDX = load_index()
    idx, dates = _IDX
    raw = json.loads((WORK / "raw" / f"{vid}.json").read_text())
    meta = raw.pop("_meta", {})
    m = idx.get(vid, {}); d = dates.get(vid, {})
    text = tx_text(vid); body = tx_body(text)
    title = m.get("title") or (text.splitlines()[0].lstrip("# ").strip() if text else vid)
    ud = d.get("upload_date")
    prov = m.get("provider") or m.get("status")
    dur = _int(d.get("duration")) or _int(m.get("duration"))
    rec = {"schema_version": "7.0",
           "video": {"id": vid, "title": title, "channel": m.get("channel") or d.get("channel") or "unknown",
                     "url": f"https://www.youtube.com/watch?v={vid}",
                     "upload_date": f"{ud[:4]}-{ud[4:6]}-{ud[6:8]}" if ud and len(ud) == 8 else None,
                     "duration_s": dur, "view_count": _int(d.get("views")),
                     "transcript_provider": prov, "transcript_chars": len(body),
                     "transcript_is_whisper": bool(prov and "whisper" in prov)}}
    for k in ["summary", "speakers", "format", "has_business_idea", "ideas", "metric_claims", "tactics",
              "tools_mentioned", "warnings", "lessons", "evidence_quality"]:
        rec[k] = raw.get(k, [] if k not in ("summary", "format", "has_business_idea", "evidence_quality") else None)
    body_n = norm(body)
    qs = []; walk_quotes({k: rec[k] for k in rec if k != "video"}, qs)
    for q in qs:
        q.pop("verified", None)
        verify_quote(q, body_n, dur)
    nver = sum(1 for q in qs if q["verified"])
    prev = {}
    op = OUT / f"{vid}.json"
    if op.exists():
        try:
            prev = json.loads(op.read_text()).get("extraction", {})
        except Exception:
            prev = {}
    ext = {**prev, **{"model": meta.get("model", prev.get("model", "unknown")),
                      "extracted_at": meta.get("extracted_at", prev.get("extracted_at", "")),
                      "cost_usd": meta.get("cost_usd", prev.get("cost_usd")),
                      "reviewed_by": meta.get("reviewed_by", prev.get("reviewed_by")),
                      "review_notes": meta.get("review_notes", prev.get("review_notes"))}}
    ext["quote_verification"] = {"quotes": len(qs), "verified": nver,
                                 "rate": round(nver / len(qs), 3) if qs else None}
    rec["extraction"] = ext
    errs = [f"{'/'.join(map(str, e.absolute_path))}: {e.message[:160]}" for e in VALIDATOR.iter_errors(rec)]
    rec["extraction"]["schema_errors"] = errs[:20]
    OUT.mkdir(parents=True, exist_ok=True)
    op.write_text(json.dumps(rec, ensure_ascii=False, indent=1))
    (OUT / f"{vid}.md").write_text(render_md(rec))
    return rec


def _q(q):
    if not q:
        return ""
    ts = q.get("approx_timestamp_s")
    t = f" (~{ts // 60}:{ts % 60:02d})" if isinstance(ts, int) else ""
    flag = "" if q.get("verified") else " [quote not matched verbatim]"
    return f"> \"{q['text']}\"{(' — ' + q['speaker']) if q.get('speaker') else ''}{t}{flag}"


def render_md(r):
    v = r["video"]; L = []
    L.append(f"# {v['title']}\n")
    L.append(f"- **Video:** [{v['id']}]({v['url']}) · **Channel:** {v['channel']} · **Uploaded:** {v.get('upload_date') or 'unknown'}"
             f" · **Length:** {(v.get('duration_s') or 0)//60} min · **Transcript:** {v.get('transcript_provider')}")
    sp = ", ".join(f"{s['name']} ({s['role']})" for s in r.get("speakers") or [])
    eq = r.get("evidence_quality") or {}
    L.append(f"- **Speakers:** {sp or 'not stated'} · **Format:** {r.get('format')}")
    L.append(f"- **Evidence quality:** {eq.get('rating')} — {eq.get('rationale')}" + (f" · Promotional conflict: {eq['promotional_conflict']}" if eq.get('promotional_conflict') else ""))
    qv = r["extraction"].get("quote_verification") or {}
    L.append(f"- **Extraction:** {r['extraction'].get('model')} · quotes verified {qv.get('verified')}/{qv.get('quotes')}"
             + (f" · reviewed by {r['extraction']['reviewed_by']}" if r['extraction'].get('reviewed_by') else "") + "\n")
    L.append(f"## Summary\n\n{r.get('summary')}\n")
    ideas = r.get("ideas") or []
    if ideas:
        L.append("## Business ideas\n")
        L.append("| # | Idea | Category | Depth | Automation [E] A/O/D/B/S | UK [E] |\n|---|---|---|---|---|---|")
        for i in ideas:
            a = i.get("automation", {})
            sc = "/".join(str(a.get(k, {}).get("score_e", "?")) for k in ["acquisition", "onboarding", "delivery", "billing", "support"])
            L.append(f"| {i['local_id']} | **{i['name']}** — {i['one_liner']} | {i['category']} | {i['depth']} | {sc} | {i.get('uk_applicability', {}).get('score_e')} |")
        L.append("")
        for i in ideas:
            if i.get("depth") == "mention":
                continue
            L.append(f"### {i['local_id']}. {i['name']}\n")
            pp = "; ".join(f"{p.get('label') or ''} {p.get('currency') or ''} {p.get('amount')}{('-' + str(p['amount_max'])) if p.get('amount_max') else ''} {p.get('unit') or ''}".strip() for p in i['pricing'].get('price_points', []))
            for lab, val in [("Customer", i['customer']), ("Problem", i['problem']), ("Offer", i['offer']),
                             ("Business model", i['business_model']), ("Pricing", f"{i['pricing'].get('model')}. {pp} {i['pricing'].get('notes') or ''}"),
                             ("Acquisition", "; ".join(f"{c['channel']}: {c['details']}" for c in i['acquisition_channels'])),
                             ("Delivery", i['delivery']), ("Unit economics (claims)", "; ".join(i['unit_economics_claims'])),
                             ("Tools", ", ".join(i['tools'])), ("Startup cost", i['startup_cost']), ("Time to first revenue", i['time_to_first_revenue']),
                             ("UK applicability [E]", f"{i['uk_applicability']['score_e']}/5 — {i['uk_applicability']['notes']}"),
                             ("Risks", "; ".join(i['risks']))]:
                L.append(f"- **{lab}:** {val}")
            a = i["automation"]
            L.append("- **Automation [E]:** " + "; ".join(f"{k} {a[k]['score_e']}/5 ({a[k]['how']})" for k in a))
            for q in i.get("quotes", []):
                L.append(_q(q))
            L.append("")
    if r.get("metric_claims"):
        L.append("## Revenue and metric claims (unverified claims)\n")
        for c in r["metric_claims"]:
            v_ = c.get("value") or {}
            tag = "first-hand" if c.get("first_hand") else "second-hand"
            if c.get("hypothetical"):
                tag += ", hypothetical"
            L.append(f"- **{c['claim']}** ({c['metric']}, {tag}, claimant: {c['claimant']})")
            L.append("  " + _q(c.get("quote")))
        L.append("")
    if r.get("tactics"):
        L.append("## Tactics and playbook steps\n")
        for t in r["tactics"]:
            L.append(f"**{t['name']}**" + (f" ({t['area']})" if t.get('area') else ""))
            for n, s in enumerate(t["steps"], 1):
                L.append(f"{n}. {s}")
            if t.get("quote"):
                L.append(_q(t["quote"]))
            L.append("")
    if r.get("lessons"):
        L.append("## Lessons\n")
        for l in r["lessons"]:
            L.append(f"- *{l['theme']}*: {l['lesson']}")
        L.append("")
    if r.get("warnings"):
        L.append("## Warnings and mistakes\n")
        for w in r["warnings"]:
            L.append(f"- {w['warning']}")
        L.append("")
    if r.get("tools_mentioned"):
        L.append("## Tools mentioned\n")
        L.append(", ".join(f"{t['name']} ({t['purpose']}{'; ' + t['cost_stated'] if t.get('cost_stated') else ''})" for t in r["tools_mentioned"]))
        L.append("")
    return "\n".join(L)


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(p.stem for p in (WORK / "raw").glob("*.json"))
    bad = 0
    for v in ids:
        r = finalize(v)
        if r["extraction"]["schema_errors"]:
            bad += 1
    print(f"finalized {len(ids)}; with schema errors: {bad}")
