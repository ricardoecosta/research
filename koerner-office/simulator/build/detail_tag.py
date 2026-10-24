"""raw_bundles.jsonl (non-extras) -> details/batch_XX.json via Codex low/medium; fallback Claude -> pi. Resumable."""
import json, sys, concurrent.futures as cf
from pathlib import Path
here = Path(__file__).parent
sys.path.insert(0, str(here.parents[1] / "scripts/common"))
from runner import call_llm, BoxPending
schema = (here/"detail_schema.md").read_text()
ONLY = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
rows = [json.loads(l) for l in open(here/"raw_bundles.jsonl") if not json.loads(l)["x"]]
if ONLY: rows = [r for r in rows if r["id"] in ONLY]
out = here/"details"; out.mkdir(exist_ok=True)
batches, cur, size = [], [], 0
for r in rows:  # ~60k chars per batch
    if cur and (size + len(r["src"]) > 60000 or len(cur) >= 20): batches.append(cur); cur, size = [], 0
    cur.append(r); size += len(r["src"])
batches.append(cur)
def job(i):
    f = out/(f"batch_{sys.argv[1]}_{i:02d}.json" if ONLY else f"batch_{i:02d}.json")
    if f.exists(): return i, "cached"
    items = [{"id": r["id"], "name": r["name"], "sources": r["src"]} for r in batches[i]]
    try: data, who, secs = call_llm(schema + "\n\nINPUT RECORDS:\n" + json.dumps(items, ensure_ascii=False), effort="medium", tag=f"det_{i:02d}", logf=str(here/"detail.log"))
    except BoxPending: return i, "box"
    recs = data.get("records", [])
    if [x.get("id") for x in recs] != [x["id"] for x in items]: return i, f"id mismatch {len(recs)}/{len(items)}"
    f.write_text(json.dumps({"runner": who, "records": recs}, ensure_ascii=False)); return i, f"{who} {secs:.0f}s"
print(len(batches), "batches", flush=True)
with cf.ThreadPoolExecutor(6) as ex:
    for i, st in ex.map(job, range(len(batches))): print(i, st, flush=True)
