"""Extras that absorbed ledger rows (Google TV, COPA, ...): re-run the detail pass on the joined ledger bundle
plus the extras passage, so the listing/validation evidence isn't lost. -> details/batch_x.json"""
import json, sys, glob
from pathlib import Path
here = Path(__file__).parent
sys.path.insert(0, str(here.parents[1] / "scripts/common")); from runner import call_llm
opps = {o["id"]: o for o in json.load(open(here.parent/"opportunities.json"))["opportunities"]}
det = json.load(open(here.parent/"details.json"))
B = [json.loads(l) for l in open(here/"raw_bundles.jsonl")]
items = [{"id": b["id"], "name": b["name"], "sources": b["src"] + "\n\nBACKLOG/PLAYBOOK PASSAGE SUMMARY: " + json.dumps(det[b["id"]]["d"], ensure_ascii=False)}
         for b in B if b["x"] and opps[b["id"]].get("dupes")]
print(len(items), [i["id"] for i in items])
data, who, secs = call_llm((here/"detail_schema.md").read_text() + "\n\nINPUT RECORDS:\n" + json.dumps(items, ensure_ascii=False), effort="medium", tag="det_x", logf=str(here/"detail.log"))
assert [r["id"] for r in data["records"]] == [i["id"] for i in items]
(here/"details/batch_x.json").write_text(json.dumps({"runner": who, "records": data["records"]}, ensure_ascii=False)); print(who, round(secs))
