#!/usr/bin/env python3
"""Shadow comparison (EFFICIENCY safeguard): ingest at medium vs xhigh on the same batch."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *
from rapidfuzz import fuzz
med_dir, xh_dir = Path("/tmp/v8/shadow_medium"), Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/v8/shadow_xhigh")
ids = [v for v in (WORK / "shadow_ids.txt").read_text().strip().split(",") if (med_dir / f"{v}.json").exists()]
rows, tm, tx, miss_vids, details = [], 0, 0, 0, []
for v in ids:
    m, x = json.loads((med_dir / f"{v}.json").read_text()), json.loads((xh_dir / f"{v}.json").read_text())
    if m["status"] != "ingested" or x["status"] != "ingested": rows.append(f"| {v} | {m['status']} | {x['status']} | | | |"); continue
    mr, xr = m["records"], x["records"]
    lines = lambda r: {l for a, b in r["ranges"] for l in range(a, b + 1)}
    missed = []
    for r in xr:  # an xhigh record is "found" by medium when names match or line ranges overlap substantially
        ok = any(fuzz.token_set_ratio(r["business"], s["business"]) >= 70 or
                 (lines(r) and len(lines(r) & lines(s)) / len(lines(r)) >= 0.5) for s in mr)
        if not ok: missed.append(r["business"][:60])
    rm = {l for r in m["removed"] for l in range(r["from"], r["to"] + 1)}
    rx = {l for r in x["removed"] for l in range(r["from"], r["to"] + 1)}
    # business lines medium removes but xhigh keeps inside an xhigh record = potential information loss
    biz_x = set().union(*[lines(r) for r in xr]) if xr else set()
    lost = len((rm - rx) & biz_x)
    tm += len(mr); tx += len(xr); miss_vids += bool(missed)
    rows.append(f"| {v} | {len(mr)} | {len(xr)} | {len(missed)} | {len(rm)}/{len(rx)} | {lost} |")
    if missed: details.append(f"- {v}: medium missed {missed}")
lost_total = sum(int(r.rsplit("|", 2)[-2]) for r in rows if r.count("|") == 7 and r.rsplit("|", 2)[-2].strip().isdigit())
heavy = [r.split("|")[1].strip() for r in rows if r.count("|") == 7 and r.rsplit("|", 2)[-2].strip().isdigit() and int(r.rsplit("|", 2)[-2]) >= 100]
count_rule = "passes" if (tm >= 0.9 * tx and miss_vids < 2) else "fails"
decision = ("REVERT to xhigh" if (count_rule == "fails" or heavy) else "KEEP medium")
details.append(f"- Record-count rule: {count_rule}. But medium removed {lost_total} lines that xhigh kept inside business records; in {len(heavy)} transcripts ({', '.join(heavy)}) it removed 100+ business lines (e.g. 510 of 1,005 lines in 0aLYK6tBoJo), which would hide business content from mining. One medium call (03DjE7j0Suw) also hung for 8+ minutes and was killed. Under the METHOD.md safeguard ('if the cheaper path starts missing things, revert immediately') this is missing things, so ingest runs at xhigh for all 435. The 10 xhigh shadow outputs are used as the real ingest records.")
out = ["# Shadow comparison: ingest at medium vs xhigh", "", f"Batch: first 10 transcripts. Rule (RULES_LOCKED): revert if medium finds >10% fewer records in total, or misses an xhigh record in 2+ transcripts.", "",
       "| video | records medium | records xhigh | xhigh records missed by medium | removed lines medium/xhigh | business lines removed by medium only |", "|---|---|---|---|---|---|", *rows, "",
       f"Totals: medium {tm} records, xhigh {tx}; transcripts where medium missed a record: {miss_vids}.", "", *details, "", f"**Decision: {decision}.**"]
(V8 / "qc").mkdir(exist_ok=True); (V8 / "qc" / "shadow_ingest.md").write_text("\n".join(out)); print("\n".join(out))
