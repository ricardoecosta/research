import json, collections
from pathlib import Path
W = Path("/tmp/loop/v10"); V = Path(__file__).resolve().parents[2] / "analysis/v10"
L = {json.loads(l)["id"]: json.loads(l) for l in open(V / "leads.jsonl")}
x = {r["id"]: r for r in json.load(open(W / "kc.json"))}; sh = json.load(open(W / "shadow.json"))
c = lambda t: str(t or "").replace("|", "/").replace("\n", " ")
o = ["# v10 kill-check", "", "**Run:** 23 Oct 2026, 19:16–19:30 BST. A single Codex xhigh pass with live web, 3 leads per call, run under `RULES_LOCKED.md` (K0 moat gate, K1–K6, buy checklist B1–B6).", "",
     f"- **Survived: {sum(r['verdict']=='survive' for r in x.values())}/88.**",
     f"- **Shadow check** (10 random kills re-judged by Claude Opus with live web, seed 10): **{sum(s['shadow'].get('verdict')=='survive' for s in sh)}/10 wrong kills.**", "", "## Kills by rule", "", "| Rule | Kills |", "|---|---|"]
o += [f"| {k} | {v} |" for k, v in collections.Counter(r["kill_rule"] for r in x.values() if r["verdict"] == "kill").most_common()]
o += ["", "## Funnel by source", "", "| Source | Track | Leads | Survived |", "|---|---|---|---|"]
for s in ["G1", "G2", "G3", "G4", "A1", "A2", "A3", "A4"]:
    ids = [i for i in L if L[i]["source"] == s]
    if ids: o.append(f"| {s} | {L[ids[0]]['track']} | {len(ids)} | {sum(x[i]['verdict']=='survive' for i in ids)} |")
o += ["", "## Shadow sample", "", "| Lead | Codex kill | Claude shadow | Shadow reason |", "|---|---|---|---|"]
o += [f"| {s['id']} {c(s['name'])} | {s['cheap']['kill_rule']} | {s['shadow'].get('verdict')} {s['shadow'].get('kill_rule')} | {c(s['shadow'].get('reason'))} |" for s in sh]
o += ["", "## All leads", "", "| ID | Src | Lead | Verdict | Rule | Moat /10 | Reason | Launches since Apr 2026 | URL |", "|---|---|---|---|---|---|---|---|---|"]
for i in sorted(x):
    r = x[i]
    o.append(f"| {i} | {L[i]['source']} | {c(L[i]['name'])} | **{r['verdict']}** | {r['kill_rule']} | {r.get('defensible_asset')} | {c(r['reason'])} | {c(r.get('launches_last_6m'))} | {(r.get('urls') or [''])[0]} |")
(V / "KILLCHECK.md").write_text("\n".join(o) + "\n")
json.dump({"xhigh": list(x.values()), "shadow": sh}, open(V / "killcheck.json", "w"), indent=1, ensure_ascii=False)
