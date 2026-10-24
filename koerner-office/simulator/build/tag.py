"""Bulk-tag contexts.jsonl -> tagged/batch_XX.json via Codex (fallback Claude, pi). Resumable."""
import json, sys, concurrent.futures as cf
from pathlib import Path
here = Path(__file__).parent
sys.path.insert(0, str(here.parents[1] / "scripts/common"))
from runner import call_llm, BoxPending
schema = (here/"schema.md").read_text()
rows = [json.loads(l) for l in open(here/"contexts.jsonl")]
B = int(sys.argv[1]) if len(sys.argv) > 1 else 25
out = here/"tagged"; out.mkdir(exist_ok=True)
batches = [rows[i:i+B] for i in range(0, len(rows), B)]
def job(i):
    f = out/f"batch_{i:02d}.json"
    if f.exists(): return i, "cached"
    items = [{"id": r["id"], "ledger": {k: r["seen"][k] for k in ("name","source","first_seen","verdict","confidence","reason","evidence")}, "context": r["context"]} for r in batches[i]]
    prompt = schema + "\n\nINPUT RECORDS:\n" + json.dumps(items, ensure_ascii=False)
    try:
        data, who, secs = call_llm(prompt, effort="medium", tag=f"sim_{i:02d}", logf=str(here/"tag.log"))
    except BoxPending: return i, "box"
    recs = data.get("records", [])
    if len(recs) != len(items): return i, f"count mismatch {len(recs)}/{len(items)}"
    f.write_text(json.dumps({"runner": who, "secs": round(secs), "records": recs}, ensure_ascii=False)); return i, f"{who} {secs:.0f}s"
with cf.ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 6) as ex:
    for i, st in ex.map(job, range(len(batches))): print(i, st, flush=True)
