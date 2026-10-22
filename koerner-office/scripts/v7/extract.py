#!/usr/bin/env python3
"""v7 extraction: one structured learnings record per transcript, via Claude Code CLI.

Usage: python extract.py [--limit N] [--workers K] [--model sonnet] [--ids id1,id2] [--finalize-only]
Raw model JSON -> /tmp/v7/raw/<id>.json ; finalized record -> analysis/v7/transcripts/<id>.json + .md
"""
import argparse, concurrent.futures as cf, datetime as dt, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *
from finalize import finalize

SYSTEM = (Path(__file__).parent / "extract_prompt.md").read_text()


def build_prompt(vid, meta, text):
    return (f"VIDEO ID: {vid}\nTITLE: {meta.get('title')}\nCHANNEL: {meta.get('channel')}\n"
            f"TRANSCRIPT SOURCE: {meta.get('provider') or meta.get('status')}\n\n"
            f"<transcript>\n{tx_body(text)}\n</transcript>\n\n"
            "Return the JSON learnings object for this transcript now (JSON only).")


def extract_one(vid, meta, model, effort):
    raw_dir = WORK / "raw"; raw_dir.mkdir(parents=True, exist_ok=True)
    rp = raw_dir / f"{vid}.json"
    if rp.exists():
        return vid, "cached", 0.0
    text = tx_text(vid)
    last_err = None
    for attempt in range(2):
        if total_cost() >= BUDGET_USD:
            return vid, "budget_stop", 0.0
        t0 = time.time()
        res = run_claude(build_prompt(vid, meta, text), SYSTEM, model=model, effort=effort)
        try:
            if res.get("is_error"):
                raise ValueError("claude error: " + str(res.get("result"))[:300])
            data = parse_json_text(res["result"])
            data["_meta"] = dict(model=(list(res.get("modelUsage", {}).keys()) or [model])[0],
                                 extracted_at=dt.datetime.now().isoformat(timespec="seconds"),
                                 cost_usd=res.get("total_cost_usd"), attempt=attempt + 1)
            rp.write_text(json.dumps(data, ensure_ascii=False, indent=1))
            log_cost("extract", vid, model, res, "ok")
            return vid, "ok", res.get("total_cost_usd", 0)
        except Exception as e:
            last_err = str(e)[:300]
            log_cost("extract", vid, model, res, "fail:" + last_err[:60].replace(",", ";"))
    return vid, "fail " + (last_err or ""), 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--effort", default=None)
    ap.add_argument("--ids", default="")
    ap.add_argument("--order", default="size", help="size | name | shuffle")
    args = ap.parse_args()
    idx, dates = load_index()
    ids = sorted(p.stem for p in RAW_TX.glob("*.txt"))
    if args.ids:
        ids = args.ids.split(",")
    todo = [i for i in ids if not (WORK / "raw" / f"{i}.json").exists()]
    if args.order == "shuffle":
        import random; random.Random(7).shuffle(todo)
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(todo)} to extract; spent so far ${total_cost():.2f} of ${BUDGET_USD}", flush=True)
    with cf.ThreadPoolExecutor(args.workers) as ex:
        futs = [ex.submit(extract_one, v, idx.get(v, {}), args.model, args.effort) for v in todo]
        for f in cf.as_completed(futs):
            vid, st, c = f.result()
            if st in ("ok", "cached"):
                try:
                    finalize(vid)
                except Exception as e:
                    st = f"finalize_fail {e}"
            print(f"{dt.datetime.now():%H:%M:%S} {vid} {st} ${c:.3f} total=${total_cost():.2f}", flush=True)


if __name__ == "__main__":
    main()
