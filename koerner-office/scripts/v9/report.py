import json, collections, sys
from pathlib import Path
W = Path("/tmp/loop/v9"); V9 = Path(__file__).resolve().parents[2] / "analysis/v9"
L = {json.loads(l)["id"]: json.loads(l) for l in open(V9 / "leads.jsonl")}
m = {r["id"]: r for r in json.load(open(W / "kc.json"))}; x = {r["id"]: r for r in json.load(open(W / "kc_x.json"))}
sh = json.load(open(W / "shadow.json"))
def cell(t): return str(t or "").replace("|", "/").replace("\n", " ")
o = ["# v9 kill-check", "", "**Run:** 23 Oct 2026, 16:43–17:08 BST. Rules: `RULES_LOCKED.md` (K1–K6).", "",
     "## What happened", "",
     f"- **Medium pass** (Codex medium + live web, 20 calls of 4 leads): {sum(r['verdict']=='survive' for r in m.values())}/77 survived.",
     f"- **Shadow check** (10 random medium kills re-judged at Codex xhigh, seed 9): **{sum(o_['shadow'].get('verdict')=='survive' for o_ in sh)}/10 wrong kills** → the locked safeguard (≥2 of 10) fired.",
     f"- **Safeguard re-run** of the whole kill-check at Codex xhigh: **{sum(r['verdict']=='survive' for r in x.values())}/77 survived.** This result is the one used downstream.",
     f"- Medium vs xhigh disagreed on **{sum(m[i]['verdict']!=x[i]['verdict'] for i in x)}/77** leads (medium killed {sum(m[i]['verdict']=='kill' and x[i]['verdict']=='survive' for i in x)} that xhigh kept; medium kept {sum(m[i]['verdict']=='survive' and x[i]['verdict']=='kill' for i in x)} that xhigh killed).",
     "", "## Kills by rule (xhigh)", ""]
c = collections.Counter(r["kill_rule"] for r in x.values() if r["verdict"] == "kill")
o += [f"| Rule | Kills |", "|---|---|"] + [f"| {k} | {v} |" for k, v in c.most_common()]
o += ["", "## Funnel by source (xhigh)", "", "| Source | Leads | Survived |", "|---|---|---|"]
for s in ["S1", "S2", "S3", "S4"]:
    ids = [i for i in L if L[i]["source"] == s]
    o.append(f"| {s} | {len(ids)} | {sum(x[i]['verdict']=='survive' for i in ids)} |")
o += ["", "## Shadow sample", "", "| Lead | Medium kill | xhigh shadow | Shadow reason |", "|---|---|---|---|"]
for s_ in sh:
    o.append(f"| {s_['id']} {cell(s_['name'])} | {s_['cheap']['kill_rule']} | {s_['shadow'].get('verdict')} {s_['shadow'].get('kill_rule')} | {cell(s_['shadow'].get('reason'))} |")
o += ["", "## All leads (xhigh verdict; medium verdict in brackets)", "", "| ID | Src | Lead | Verdict | Rule | Reason | URL |", "|---|---|---|---|---|---|---|"]
for i in sorted(x):
    r = x[i]; u = (r.get("urls") or [""])[0]
    o.append(f"| {i} | {L[i]['source']} | {cell(L[i]['name'])} | **{r['verdict']}** ({m[i]['verdict']}) | {r['kill_rule']} | {cell(r['reason'])} | {u} |")
(V9 / "KILLCHECK.md").write_text("\n".join(o) + "\n")
json.dump({"medium": list(m.values()), "xhigh": list(x.values()), "shadow": sh}, open(V9 / "killcheck.json", "w"), indent=1, ensure_ascii=False)
print("ok")
