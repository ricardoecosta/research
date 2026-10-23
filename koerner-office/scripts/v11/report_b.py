import json
from pathlib import Path
W = Path("/tmp/loop/v11"); V = Path(__file__).resolve().parents[2] / "analysis/v11"
R = json.load(open(W / "checklists.json")); c = lambda t: str(t if t is not None else "").replace("|", "/").replace("\n", " ")
o = ["# v11 Track B: listing checklists", "",
     f"**Run:** 23 Oct 2026, 23:27–23:30 BST. 177 Flippa SaaS and app listings were harvested from the public search without the LLM (`harvest_listings.py`). Code filters left 100 in scope: the $20k–$150k asking-price band, with content, affiliate, ecommerce and agency listings excluded, capped at 100. Codex medium turned each into a checklist from the listing text only; it did not rank them.", "",
     "**Mechanical pass rule** (`RULES_LOCKED.md`):",
     "- A hard fail is C1, C2, C3, C7 or C9 marked \"looks off\", or C1 or C2 marked \"missing\".",
     "- A listing passes if it has no hard fail and 3 or fewer rows marked \"missing\".",
     "- Note: Flippa hides detailed financials, traffic and seller notes behind a login. C1 therefore relies on Flippa's \"Verified / Vetted / Data Verified\" badges and the summary metrics on the public page.", "",
     f"**Result: {sum(r['pass'] for r in R)} of {len(R)} pass.**", "",
     "| Pass | Listing | Price (USD) | Rev/mo | Profit/mo | Verification | Hard fails | Missing |", "|---|---|---|---|---|---|---|---|"]
for r in sorted(R, key=lambda r: (not r["pass"], r["missing"])):
    o.append(f"| {'**PASS**' if r['pass'] else 'fail'} | [{c(r.get('name'))[:60]}]({r['url']}) | {c(r.get('asking_price_usd'))} | {c(r.get('monthly_revenue_usd'))} | {c(r.get('monthly_profit_usd'))} | {c(r.get('verification'))[:80]} | {', '.join(r['hard_fails']) or '–'} | {r['missing']} |")
for r in [r for r in R if r["pass"]]:
    o += ["", f"## {r.get('name')}", "", r["url"], "", "| Row | Status | Evidence | Note |", "|---|---|---|---|"]
    o += [f"| {x['id']} | {x['status']} | {c(x.get('evidence'))} | {c(x.get('note'))} |" for x in r.get("rows", [])]
    o += ["", "**90-day handover plan (draft):**"] + [f"- {s}" for s in r.get("handover_plan", [])] + [f"\nSteady-state hours: {c(r.get('steady_state_hours'))}", "", "**Questions for the seller:**"] + [f"{i+1}. {q}" for i, q in enumerate(r.get("questions", []))]
(V / "CHECKLISTS.md").write_text("\n".join(o) + "\n"); json.dump(R, open(V / "checklists.json", "w"), indent=1, ensure_ascii=False)
