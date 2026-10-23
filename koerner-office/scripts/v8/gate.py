#!/usr/bin/env python3
"""Manifest + completeness gate: writes analysis/v8/MANIFEST.csv, QUARANTINE.csv, GATE.md.
Exit 0 only when all 435 transcripts are mined or quarantined."""
import csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common8 import *
ids = sorted(p.stem for p in RAW_TX.glob("*.txt"))
rows, q = [], []
for v in ids:
    ip, mp, fp = V8 / "ingest" / "records" / f"{v}.json", V8 / "mined" / f"{v}.json", V8 / "mined" / "_failed" / f"{v}.txt"
    ing = json.loads(ip.read_text()) if ip.exists() else None
    m = json.loads(mp.read_text()) if mp.exists() else None
    st, reason = "pending", ""
    if ing and ing["status"] == "quarantined": st, reason = "quarantined", ing["quarantine_reason"]
    elif m: st = "mined"
    elif fp.exists(): st, reason = "quarantined", "mining failed on all runners: " + fp.read_text()[:150]
    elif ing: st = "ingested"
    rows.append(dict(id=v, publish_date=(ing or {}).get("publish_date"), status=st, n_lines=(ing or {}).get("n_lines"),
                     removed_lines=(ing or {}).get("n_removed_lines"), records=len((ing or {}).get("records") or []),
                     ingest_runner=(ing or {}).get("ingest_runner"), ideas=len((m or {}).get("ideas") or []),
                     miner=(m or {}).get("miner"), stale_age=(ing or {}).get("stale_age"), reason=reason))
    if st == "quarantined": q.append(dict(id=v, reason=reason))
with open(V8 / "MANIFEST.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
with open(V8 / "QUARANTINE.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "reason"]); w.writeheader(); w.writerows(q)
from collections import Counter
c = Counter(r["status"] for r in rows)
ok = len(ids) == 435 and c["mined"] + c["quarantined"] == 435
txt = (f"# Completeness gate\n\nTranscripts: {len(ids)}. Ingested (incl. mined): {c['ingested'] + c['mined']}. Mined: {c['mined']}. "
       f"Quarantined: {c['quarantined']}. Pending: {c['pending'] + c['ingested']}.\n"
       f"Records after splitting: {sum(r['records'] for r in rows)}. Ideas mined: {sum(r['ideas'] for r in rows)}.\n\n"
       f"**Gate: {'OPEN (every transcript processed)' if ok else 'CLOSED (no clustering, scoring or ranking yet)'}**\n")
(V8 / "GATE.md").write_text(txt); print(txt)
sys.exit(0 if ok else 1)
