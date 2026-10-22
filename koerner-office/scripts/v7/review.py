#!/usr/bin/env python3
"""Opus quality review of a random sample of v7 extractions; applies corrections and records an audit.
Usage: python review.py --n 30 [--model opus] [--workers 3] [--ids a,b]"""
import argparse, concurrent.futures as cf, datetime as dt, json, random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *
from finalize import finalize

SYSTEM = (Path(__file__).parent / "review_prompt.md").read_text()
REV = V7 / "reviews"
CORE = ["summary", "speakers", "format", "has_business_idea", "ideas", "metric_claims", "tactics",
        "tools_mentioned", "warnings", "lessons", "evidence_quality"]


def strip_q(o):
    if isinstance(o, dict):
        return {k: strip_q(v) for k, v in o.items() if k not in ("verified", "match_score", "char_offset", "approx_timestamp_s")}
    if isinstance(o, list):
        return [strip_q(v) for v in o]
    return o


def set_path(obj, path, new):
    parts = [p for p in path.strip("/").split("/") if p]
    cur = obj
    for p in parts[:-1]:
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    last = parts[-1]
    if isinstance(cur, list):
        cur[int(last)] = new
    else:
        cur[last] = new


def review_one(vid, model):
    out = REV / f"{vid}.review.json"
    if out.exists():
        return vid, "cached", 0
    if total_cost() >= BUDGET_USD:
        return vid, "budget_stop", 0
    raw_p = WORK / "raw" / f"{vid}.json"
    raw = json.loads(raw_p.read_text())
    ext = {k: raw.get(k) for k in CORE}
    prompt = (f"<transcript>\n{tx_body(tx_text(vid))}\n</transcript>\n\n<extraction>\n"
              f"{json.dumps(strip_q(ext), ensure_ascii=False)}\n</extraction>\n\nReturn the audit JSON now.")
    try:
        res = run_claude(prompt, SYSTEM, model=model)
    except LimitHit:
        return vid, "limit", 0
    try:
        if res.get("is_error"):
            raise ValueError(str(res.get("result"))[:300])
        rv = parse_json_text(res["result"])
    except Exception as e:
        log_cost("review", vid, model, res, "fail")
        return vid, f"fail {e}", res.get("total_cost_usd", 0)
    log_cost("review", vid, model, res, "ok")
    applied, failed = [], []
    for c in rv.get("corrections", []):
        try:
            set_path(raw, c["path"], c["new"]); applied.append(c)
        except Exception as e:
            failed.append({**c, "apply_error": str(e)})
    if rv.get("add_ideas"):
        raw.setdefault("ideas", []).extend(rv["add_ideas"])
    if rv.get("add_metric_claims"):
        raw.setdefault("metric_claims", []).extend(rv["add_metric_claims"])
    m = raw.setdefault("_meta", {})
    m["reviewed_by"] = (list(res.get("modelUsage", {}).keys()) or [model])[0]
    m["review_notes"] = rv.get("notes")
    raw_p.write_text(json.dumps(raw, ensure_ascii=False, indent=1))
    rv.update(video_id=vid, reviewed_at=dt.datetime.now().isoformat(timespec="seconds"),
              cost_usd=res.get("total_cost_usd"), applied=len(applied), failed_to_apply=failed)
    REV.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rv, ensure_ascii=False, indent=1))
    finalize(vid)
    return vid, rv.get("verdict"), res.get("total_cost_usd", 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--model", default="opus")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--ids", default="")
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    done = sorted(p.stem for p in (WORK / "raw").glob("*.json"))
    ids = a.ids.split(",") if a.ids else random.Random(a.seed).sample(done, min(a.n, len(done)))
    print(f"reviewing {len(ids)}", flush=True)
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for f in cf.as_completed([ex.submit(review_one, v, a.model) for v in ids]):
            vid, st, c = f.result()
            print(f"{dt.datetime.now():%H:%M:%S} {vid} {st} ${c or 0:.3f} total=${total_cost():.2f}", flush=True)


if __name__ == "__main__":
    guarded(main)
