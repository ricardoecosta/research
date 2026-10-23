import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mine
from mine import *
OUTD = Path("/tmp/v8/box_prompts")
captured = {}
def fake(prompt, effort="xhigh", logf=None, tag=""):
    captured[tag] = prompt; raise RuntimeError("dump")
mine.call_llm = fake
mine.log = lambda *a, **k: None
n = 0
for p in sorted((V8 / "ingest" / "records").glob("*.json")):
    vid = p.stem
    if (V8 / "mined" / f"{vid}.json").exists(): continue
    if json.loads(p.read_text())["status"] != "ingested": continue
    captured.clear()
    try:
        ing = json.loads(p.read_text())
        dates = load_dates(); meta, body, rows = numbered(vid, dates)
        removed = {l for r in ing["removed"] for l in range(r["from"], r["to"] + 1)}
        keep = {r["line"] for r in rows} - removed
        recs = "\n".join(f"- {r['record_id']}: {r['business']} | lines {r['ranges']}" for r in ing["records"]) or "(none found at ingest)"
        prompt = (SYSTEM + f"\n\nVIDEO ID: {vid}\nTITLE: {ing.get('title')}\nCHANNEL: {ing.get('channel')}\nPUBLISHED: {ing['publish_date']}\n"
                  f"RECORDS:\n{recs}\n\n<transcript>\n{fmt_lines(rows, keep)}\n</transcript>\n\nReturn the JSON now.")
        (OUTD / f"{vid}.txt").write_text(prompt); n += 1
    except Exception as e:
        print("ERR", vid, e)
print("dumped", n)
