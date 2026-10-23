"""v11 loop iteration pipeline (LOOP.md §6). Stages: harvest, killcheck, shadow, evidence, score, validate.
Resumable: each LLM answer cached in /tmp/loop/v9/out/<tag>.json. Calls logged to calls.jsonl."""
import csv, json, os, random, sys, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from runner import call_llm, BoxPending
from rapidfuzz import fuzz

REPO = Path(__file__).resolve().parents[2]
AN = REPO / "analysis"; V9 = AN / "v11"; W = Path("/tmp/loop/v11"); OUT = W / "out"; OUT.mkdir(parents=True, exist_ok=True)
LOG = W / "run.log"; CALLS = W / "calls.jsonl"
TODAY = "23 Oct 2026"
RULES = (V9 / "RULES_LOCKED.md").read_text()
CONSTRAINTS = """Owner: Ricardo, a UK-based (Bromley) technical founder. MARKET SCOPE: ANY COUNTRY (US, EU, UK, global customers all fine).
Hard constraints: mostly run by AI agents (>=50% of all work automated, <=5 h/week of his time, also for a bought business);
software/digital/data product; NOT selling to local businesses; NOT needing his face or personal brand;
NO cold outreach (no cold email/SMS/DM/calls) - channels must be lawful in UK and recipient's country: SEO, app stores, marketplaces, integrations, paid ads, partnerships.
BUILD track: TIME-TO-MOAT required - agents can build the defensible asset (compiled data, maintained rules engine, network, switching costs) within 3 months, a rival needs 3+ months to copy it, and nobody owns it yet.
BUY track (preferred): a listed business at $20k-$150k with VERIFIED revenue (marketplace badge / Stripe connect / verified P&L), >= $1k/month revenue, <=5x annual profit, which a 90-day handover-to-agents plan can bring to <=5 h/week of owner time (more hours during the 90 days are fine)."""

def log(m):
    line = f"{dt.datetime.now():%H:%M:%S} {m}"; print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def ask(tag, prompt, effort, web=True, order=None):
    f = OUT / f"{tag}.json"
    if f.exists(): return json.loads(f.read_text())
    try:
        data, runner, secs = call_llm(prompt, effort=effort, logf=str(LOG), tag=f"v11_{tag}", web=web, order=order)
    except BoxPending:
        log(f"{tag} BOX PENDING"); return None
    f.write_text(json.dumps(data, indent=1))
    with open(CALLS, "a") as c: c.write(json.dumps({"tag": tag, "runner": runner, "effort": effort, "secs": round(secs), "t": f"{dt.datetime.now():%H:%M}"}) + "\n")
    log(f"{tag} done via {runner} in {secs:.0f}s"); return data

def seen_rows():
    return list(csv.DictReader(open(AN / "loop/SEEN.csv")))

def seen_names():
    return "; ".join(r["name"] for r in seen_rows())

LEAD_SCHEMA = """Return ONLY JSON: {"leads":[{"name":"short product/opportunity name","source":"A1|A2|A3|D1|G1","track":"build|buy|demand",
"moat":"build: the asset agents would build in <=3 months and why a rival needs 3+ months; buy: the customer base / integrations / data switching costs",
"listing":"buy/demand: listing_url, asking price, TTM or monthly revenue, profit, verification evidence, multiple, owner hours, owner work, listing date; else null","sub_source":"e.g. WordPress.org / Flippa / HMRC",
"what":"one sentence: the product we would build/buy and who pays","trigger":"the regulation, decaying product, listing or complaint behind it",
"urls":["1-3 source URLs you actually opened"],"evidence_of_payment":"price/revenue/installs/users as stated, with numbers only if seen on the page",
"claim_event_date":"YYYY-MM or 'unverified'","notes":"anything unverified marked 'unverified'"}]}"""

HARVEST = {
 "A1": ("Acquire.com verified listings $20k-$150k", 20, """Find CURRENT public Acquire.com listings (app.acquire.com/startup/... or /public/...; also Acquire 'verified' / 'Stripe-connected' / 'revenue verified' badges, and Acquire blog/newsletter roundups Jun-Oct 2026) for small SaaS, plugins, extensions, apps, APIs, data products with asking price $20k-$150k, revenue >= $1k/month, profitable, and VERIFIED revenue (badge or Stripe/ProfitWell connected). Any country. Record listing URL, asking price, TTM revenue, TTM profit, verification evidence, multiple, owner hours, listing date, churn, what work the owner does (support, sales, dev)."""),
 "A2": ("Flippa verified listings $20k-$150k", 20, """Find CURRENT flippa.com listings (flippa.com/<id>-... pages) for SaaS, apps, browser extensions, WordPress/Shopify plugins, APIs with asking price $20k-$150k, monthly revenue >= $1k, profitable, and Flippa 'P&L verified' / 'Revenue verified' / 'Google Analytics verified' or Stripe-connected badges. Open each listing page. Any country. Record listing URL, price, monthly revenue/profit, verification badges, multiple, owner hours, age, listing date, the work the owner does. Skip content/affiliate/ecommerce/agency/service businesses."""),
 "A3": ("Empire Flippers / FE International / Quiet Light / Microns / Tiny / IndieMaker / SideProjectors $20k-$150k", 15, """Find current listings on empireflippers.com/marketplace (SaaS/app; they vet P&L), feinternational.com, quietlight.com/listings, microns.io (Stripe-verified badges), tinyacquisitions, indiemaker.co, sideprojectors.com, with price $20k-$150k, revenue >= $1k/month, profitable, and VERIFIED/vetted revenue. Any country. Record listing URL, price, revenue, profit, verification, multiple, owner hours, listing date, owner's work."""),
 "D1": ("Demand-first: verified-revenue small products", 15, """Find small software/digital products with VERIFIED revenue >= $1k/month, dated within the last 18 months (since Apr 2025): TrustMRR (trustmrr.com, Stripe-verified MRR leaderboard), Indie Hackers products with Stripe-verified revenue, OpenStartup/'open metrics' pages, Baremetrics open startups. Prefer niche B2B/B2C tools in narrow verticals (not generic AI wrappers), any country. Record product URL, verified MRR and date, whether it's for sale, the niche, and what defensible asset it relies on. These seed either buy leads (if for sale) or an ADJACENT build idea in the same paying niche (state it in 'what')."""),
 "G1": ("Build ideas meeting time-to-moat", 15, """Find build opportunities (any country) where AI agents could build a defensible asset within 3 months that a rival would need 3+ months to replicate, and NOBODY already owns it: e.g. a compiled dataset from many messy sources in a niche nobody covers yet, a maintained rules engine for a newly mandated regulation (2026-2028 commencements, any jurisdiction) in a segment incumbents ignore, a data network that compounds with each customer. Must have evidence of willingness to pay dated within 18 months (adjacent products' pricing, verified revenue, tenders). Check that nobody already sells the asset."""),
}

def _future(ra, today):
    try: return dt.date.fromisoformat(ra[:10]) > today
    except Exception:
        try: return dt.datetime.strptime(ra, "%d %b %Y").date() > today
        except Exception: return True

def harvest():
    sn = seen_names()
    def one(k):
        title, n, brief = HARVEST[k]
        p = f"""You are a research scout. Today is {TODAY}. Use live web search; open pages and cite them. Never invent numbers; mark anything you could not see as 'unverified'.
Task: harvest about {n} distinct business-opportunity LEADS for source {k} ({title}).
{brief}
{CONSTRAINTS}
Prefer leads that could fit these constraints (software/digital, self-serve online sales, a real moat). Leads are cheap: do NOT deeply validate, just record the facts you saw.
Skip anything already in this seen list (by meaning): {sn}
{LEAD_SCHEMA}"""
        d = ask(f"harvest_{k}", p, "high")
        return [dict(l, source=k, track=("buy" if k.startswith("A") else ("demand" if k == "D1" else "build"))) for l in (d or {}).get("leads", [])]
    with ThreadPoolExecutor(7) as ex: res = list(ex.map(one, HARVEST))
    leads = [l for r in res for l in r]
    # dedup against ledger + within run
    seen = seen_rows(); today = dt.date(2026, 10, 23); kept, dropped = [], []
    for l in leads:
        m = None
        for r in seen:
            if fuzz.token_set_ratio(l["name"].lower(), r["name"].lower()) >= 88:
                ra = (r.get("recheck_after") or "").strip()
                if not ra or _future(ra, today): m = r; break
        if not m:
            for k in kept:
                if fuzz.token_set_ratio(l["name"].lower(), k["name"].lower()) >= 88: m = k; break
        (dropped if m else kept).append(dict(l, dup_of=(m or {}).get("name")) if m else l)
    kept = kept[:100]
    for i, l in enumerate(kept): l["id"] = f"L{i+1:03d}"
    with open(V9 / "leads.jsonl", "w") as f:
        for l in kept: f.write(json.dumps(l, ensure_ascii=False) + "\n")
    with open(V9 / "leads_dropped_dupes.jsonl", "w") as f:
        for l in dropped: f.write(json.dumps(l, ensure_ascii=False) + "\n")
    by = {}
    for l in kept: by[l["source"]] = by.get(l["source"], 0) + 1
    log(f"harvest: raw {len(leads)}, dupes dropped {len(dropped)}, kept {len(kept)} {by}")

KC_SCHEMA = """Return ONLY JSON: {"results":[{"id":"L001","verdict":"survive|kill","kill_rule":"K0|K1|K2|K3|K4|K5|K6|B1|B2|B3|B4|B5|B6|none","defensible_asset":0,"moat_type":"data|rules|network|switching|none","time_to_moat":"build only: a) agents<=3mo yes/no why; b) rival>=3mo yes/no why; c) unowned yes/no who","handover_feasible":"buy only: can a 90-day plan reach <=5h/week? why",
"reason":"one sentence, specific","launches_last_6m":"names + launch dates of competing products found by a dated search since 23 Apr 2026, or 'none found'","buy_checklist":"buy track: B1-B6 findings, else null",
"platform_or_partner":"who, or 'none found'","incumbents":"main maintained incumbents with price, or 'none found'",
"claim_event_date":"YYYY-MM or 'unverified'","urls":["URLs supporting the verdict; every kill needs >=1"]}]}"""

def kc_prompt(batch, effort_note=""):
    return f"""You are running a CHEAP KILL-CHECK on business leads. Today is {TODAY}. Use live web search, targeted (2-4 searches per lead). Never invent facts; say 'unverified'.
{effort_note}
Apply these locked rules exactly:
{RULES}
For each lead decide survive or kill. FIRST apply K0 (build: time-to-moat a/b/c, any "no" = kill; buy: switching-cost moat >=4). Buy and for-sale demand leads: apply B1 (verified revenue, strict) and B3 (price band $20k-$150k) next, open the listing. Then RUN A DATED SEARCH for competitor launches since 23 Apr 2026 (K2). Buy leads use the B checklist instead of K4. Other kills need URL evidence; if missing, survive.
LEADS:
{json.dumps(batch, ensure_ascii=False, indent=1)}
{KC_SCHEMA}"""

def leads(): return [json.loads(l) for l in open(V9 / "leads.jsonl")]

def killcheck_x():
    """Safeguard re-run (RULES_LOCKED shadow rule): whole kill-check at xhigh; replaces the medium result."""
    killcheck(effort="xhigh", pre="kcx", fout="kc_x.json")

def kc_file():
    return W / ("kc_x.json" if (W / "kc_x.json").exists() else "kc.json")

def survivors():
    res = json.loads(kc_file().read_text())
    s = [r["id"] for r in res if r["verdict"] == "survive"]
    if kc_file().name == "kc.json":
        try: s += [o["id"] for o in json.loads((W / "shadow.json").read_text()) if o["shadow"].get("verdict") == "survive"]
        except Exception: pass
    return s

def killcheck(effort="xhigh", pre="kc", fout="kc.json"):
    L = leads(); B = [L[i:i+3] for i in range(0, len(L), 3)]
    def one(ib):
        i, b = ib
        slim = [{k: l.get(k) for k in ("id","name","source","track","sub_source","what","trigger","moat","listing","urls","evidence_of_payment","claim_event_date")} for l in b]
        d = ask(f"{pre}_{i:02d}", kc_prompt(slim, "Effort: thorough (up to 6 searches per lead)." if effort == "xhigh" else ""), effort)
        return (d or {}).get("results", [])
    with ThreadPoolExecutor(6) as ex: res = [r for rr in ex.map(one, enumerate(B)) for r in rr]
    (W / fout).write_text(json.dumps(res, indent=1)); log(f"killcheck {effort}: {len(res)} results, survive {sum(r['verdict']=='survive' for r in res)}")

def shadow():
    res = json.loads((W / "kc.json").read_text()); kills = [r for r in res if r["verdict"] == "kill"]
    random.seed(11); samp = random.sample(kills, min(10, len(kills))); byid = {l["id"]: l for l in leads()}
    def one(r):
        l = byid[r["id"]]
        p = kc_prompt([l], "SHADOW RE-JUDGE (independent model). Be thorough (up to 8 searches). Another pass killed this lead with: " + json.dumps(r) + "\nJudge independently; also set field \"agree_with_kill\": true/false in your result.")
        d = ask(f"shadow_{r['id']}", p, "high", order=["claude", "codex", "pi"]); x = ((d or {}).get("results") or [{}])[0]
        return {"id": r["id"], "name": l["name"], "cheap": r, "shadow": x}
    with ThreadPoolExecutor(5) as ex: out = list(ex.map(one, samp))
    wrong = [o for o in out if o["shadow"].get("verdict") == "survive"]
    (W / "shadow.json").write_text(json.dumps(out, indent=1)); log(f"shadow: {len(out)} re-judged, wrong kills {len(wrong)}")

def evidence():
    res = json.loads(kc_file().read_text()); byid = {l["id"]: l for l in leads()}
    try: sh = json.loads((W / "shadow.json").read_text())
    except Exception: sh = []
    surv = survivors()
    (V9 / "evidence").mkdir(exist_ok=True)
    def one(i):
        p = f"""DEEP EVIDENCE on one business lead that survived a cheap kill-check. Today is {TODAY}. Use live web search thoroughly; cite URLs for every fact. Never invent numbers; 'unverified' otherwise.
{CONSTRAINTS}
Lead: {json.dumps(byid[i], ensure_ascii=False)}
Kill-check notes: {json.dumps([r for r in res if r['id']==i] or [o['shadow'] for o in sh if o['id']==i], ensure_ascii=False)}
For buy-track leads, re-open the listing and assess it as an ACQUISITION (verified revenue, churn, price vs profit, transferability, seller dependence) and draft a 90-day handover-to-agents plan; owner hours <=5/week must hold AFTER the 90 days. For build leads assess time-to-moat a/b/c. Gather: demand size (searches, installs, users, regulated population with source), prices of current solutions, revenue proof WITH the date of the underlying event (claim_event_date; >18 months old = zero weight; self-described failures = zero weight),
copy-speed (competitors launched since Apr 2026 with dates), platform/partner risk, defensible asset (compiled data, rules engine, network effect, switching costs), build effort for an AI-agent-run solo operator, lawful acquisition channel, the cheapest <=1-day desk test.
Return ONLY JSON: {{"id":"{i}","name":"","demand":"","prices":"","revenue_proof":[{{"claim":"","claim_event_date":"","url":""}}],"copy_speed":"","platform_risk":"","defensible_asset":"","build_effort":"","channel":"","owner_hours_per_week":"","automation_share_pct":"INTEGER 0-100 you estimate (share of ALL work incl. sales/support/admin agents can do), or null if truly unknowable","automation_reason":"","track":"build|buy","listing_check":"buy: listing_url, price, verified revenue/profit and how verified, multiple, churn, current owner hours and tasks, transferability; else null","handover_plan":"buy: 90-day handover-to-agents plan in 3-6 steps and resulting steady-state owner h/week; else null","time_to_moat":"build: a/b/c assessment","moat_assessment":"","desk_test":"","red_flags":"","urls":[]}}"""
        d = ask(f"ev_{i}", p, "xhigh")
        if d: (V9 / "evidence" / f"{i}.json").write_text(json.dumps(d, indent=1, ensure_ascii=False))
    with ThreadPoolExecutor(5) as ex: list(ex.map(one, surv))
    log(f"evidence: {len(surv)} survivors processed")

def score():
    sv = set(survivors())
    ev = [json.loads(f.read_text()) for f in sorted((V9 / "evidence").glob("*.json")) if f.stem in sv]
    p = f"""Score each business lead (METHOD step 8) using ONLY the evidence given. Today is {TODAY}. No web needed.
{CONSTRAINTS}
Rules: {RULES}
Five separate scores per lead, each with a short reason: success_12m (0-10), agent_runnability (0-10), fit (0-10), automation_share_pct (an INTEGER you must estimate from the evidence and argue in automation_reason; never copy a placeholder; 0 only if argued), defensible_asset (0-10; build: time-to-moat; buy: switching-cost moat; <4 = hard_rule_fail "K0"). Automation and hours for buy are at STEADY STATE after the 90-day handover. Use hard_rule_fail null when nothing fails (never a string like "none"). Revenue claims whose event is >18 months old or self-described failures get ZERO weight.
Also: claim_event_date (newest dated revenue event or 'none'), copy_speed (launches since Apr 2026), defensible_asset (short), hard_rule_fail (null or which rule).
EVIDENCE: {json.dumps(ev, ensure_ascii=False)}
Return ONLY JSON: {{"scores":[{{"id":"","name":"","success_12m":0,"success_reason":"","agent_runnability":0,"runnability_reason":"","fit":0,"fit_reason":"","automation_share_pct":"integer you estimate","automation_reason":"","defensible_asset":0,"defensible_reason":"","track":"","listing_url":"","price":"","verified_revenue_profit":"","multiple":"","handover_plan":"","claim_event_date":"","copy_speed":"","defensible_asset":"","hard_rule_fail":null}}]}}"""
    d = ask("score", p, "xhigh", web=False)
    nf = lambda s: not s.get("hard_rule_fail") or str(s.get("hard_rule_fail")).strip().lower() in ("none", "null", "")
    S = sorted([s for s in d["scores"] if nf(s)], key=lambda s: (-s["success_12m"], -(s.get("defensible_asset") or 0), -s["fit"]))
    bad = [s for s in d["scores"] if not nf(s)]
    buy = [s for s in S if s.get("track") == "buy"][:4]; rest = [s for s in S if s not in buy]
    S = buy + rest; S = sorted(S[:8], key=lambda s: (-s["success_12m"], -(s.get("defensible_asset") or 0), -s["fit"])) + S[8:]
    (W / "scores.json").write_text(json.dumps({"ranked": S, "failed": bad}, indent=1))
    log(f"score: {len(d['scores'])} scored, {len(bad)} hard-rule fails, top8 {[s['id'] for s in S[:8]]}")

def validate():
    d_ = json.loads((W / "scores.json").read_text()); sc = d_["ranked"][:8]
    if not sc and os.environ.get("AUDIT_IDS"):  # scorer-audit: validate named hard-rule fails to check the scorer
        ids = os.environ["AUDIT_IDS"].split(","); sc = [s for s in d_["failed"] if s["id"] in ids]
    def one(s):
        i = s["id"]; ev = json.loads((V9 / "evidence" / f"{i}.json").read_text())
        p = f"""You are doing HIGH-EFFORT, WEB-CHECKED VALIDATION (METHOD step 10) of one business opportunity. Today is {TODAY}. Use WebSearch and WebFetch extensively; re-verify every decisive fact live. Cite a URL for every fact. Never invent numbers; mark unverifiable as 'unverified'.
{CONSTRAINTS}
Locked rules: {RULES}
Lead evidence (from a cheaper pass — re-check, don't trust): {json.dumps(ev, ensure_ascii=False)}
Scores: {json.dumps(s, ensure_ascii=False)}
For buy-track candidates, validate as an ACQUISITION: re-open the listing, verified revenue/profit (how verified), churn, current owner hours and tasks, price multiple, transferability, seller dependence, platform risk; write the 90-day handover-to-agents plan and the steady-state hours. For build candidates re-check time-to-moat a/b/c. Check: current competitors and prices (esp. any launched since Apr 2026), platform/partner ownership, demand signals dated <=18 months, legal position (UK), lawful acquisition channel, owner hours, defensible asset.
Verdict: pursue / maybe / kill, with confidence low/medium/high. 'pursue' at medium+ only if: live demand/revenue evidence dated <=18 months, reachable lawful channel, copy-speed passes on re-check, the moat is confirmed, and a <=1-day first test exists (buy track: VERIFIED revenue re-confirmed on the listing, price that makes sense vs verified profit, a credible 90-day handover-to-agents plan reaching <=5 h/week, and a defined due-diligence step).
If your verdict would be 'maybe' and the deciding test is desk-only and doable now with web research (<=1 day), RUN IT NOW and report its result, then give the final verdict.
Return ONLY JSON: {{"id":"{i}","name":"","verdict":"","confidence":"","one_line":"","why":["3-6 bullets each with URL"],"competitors":[{{"name":"","price":"","launched":"","url":""}}],"demand":"","legal":"","channel":"","owner_hours":"","listing_url":"","price":"","verified_revenue_profit":"","handover_plan":"","desk_test_run":"what you ran and result, or 'n/a'","first_test":"","unverified":[],"urls":[]}}"""
        return ask(f"val_{i}", p, "high", web=True, order=["claude", "codex", "pi"])
    with ThreadPoolExecutor(4) as ex: out = [o for o in ex.map(one, sc) if o]
    (W / "validation.json").write_text(json.dumps(out, indent=1)); log(f"validate: {len(out)} done " + str([(o.get('id'), o.get('verdict'), o.get('confidence')) for o in out]))

if __name__ == "__main__":
    (W / "pid").write_text(str(os.getpid()))
    t0 = time.time()
    for st in sys.argv[1:]: log(f"== stage {st} start"); globals()[st](); log(f"== stage {st} end ({time.time()-t0:.0f}s total)")
