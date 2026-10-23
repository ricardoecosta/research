"""v10 loop iteration pipeline (LOOP.md §6). Stages: harvest, killcheck, shadow, evidence, score, validate.
Resumable: each LLM answer cached in /tmp/loop/v9/out/<tag>.json. Calls logged to calls.jsonl."""
import csv, json, os, random, sys, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from runner import call_llm, BoxPending
from rapidfuzz import fuzz

REPO = Path(__file__).resolve().parents[2]
AN = REPO / "analysis"; V9 = AN / "v10"; W = Path("/tmp/loop/v10"); OUT = W / "out"; OUT.mkdir(parents=True, exist_ok=True)
LOG = W / "run.log"; CALLS = W / "calls.jsonl"
TODAY = "23 Oct 2026"
RULES = (V9 / "RULES_LOCKED.md").read_text()
CONSTRAINTS = """Owner: Ricardo, a UK-based (Bromley) technical founder. MARKET SCOPE: ANY COUNTRY (US, EU, UK, global customers all fine).
Hard constraints: mostly run by AI agents (>=50% of all work automated, <=5 h/week of his time, also for a bought business);
software/digital/data product; NOT selling to local businesses; NOT needing his face or personal brand;
NO cold outreach (no cold email/SMS/DM/calls) - channels must be lawful in UK and recipient's country: SEO, app stores, marketplaces, integrations, paid ads, partnerships.
MOAT REQUIRED: compiled/proprietary data, a maintained rules engine (tax/regulation/compliance, any jurisdiction), a network effect, or real switching costs."""

def log(m):
    line = f"{dt.datetime.now():%H:%M:%S} {m}"; print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def ask(tag, prompt, effort, web=True, order=None):
    f = OUT / f"{tag}.json"
    if f.exists(): return json.loads(f.read_text())
    try:
        data, runner, secs = call_llm(prompt, effort=effort, logf=str(LOG), tag=f"v10_{tag}", web=web, order=order)
    except BoxPending:
        log(f"{tag} BOX PENDING"); return None
    f.write_text(json.dumps(data, indent=1))
    with open(CALLS, "a") as c: c.write(json.dumps({"tag": tag, "runner": runner, "effort": effort, "secs": round(secs), "t": f"{dt.datetime.now():%H:%M}"}) + "\n")
    log(f"{tag} done via {runner} in {secs:.0f}s"); return data

def seen_rows():
    return list(csv.DictReader(open(AN / "loop/SEEN.csv")))

def seen_names():
    return "; ".join(r["name"] for r in seen_rows())

LEAD_SCHEMA = """Return ONLY JSON: {"leads":[{"name":"short product/opportunity name","source":"G1|G2|G3|G4|A1|A2","track":"build|buy",
"moat":"the specific defensible asset (data/rules engine/network/switching cost) and why it takes months to copy",
"listing":"buy track only: asking price, TTM revenue, TTM profit, verified?, owner hours, listing date, else null","sub_source":"e.g. WordPress.org / Flippa / HMRC",
"what":"one sentence: the product we would build/buy and who pays","trigger":"the regulation, decaying product, listing or complaint behind it",
"urls":["1-3 source URLs you actually opened"],"evidence_of_payment":"price/revenue/installs/users as stated, with numbers only if seen on the page",
"claim_event_date":"YYYY-MM or 'unverified'","notes":"anything unverified marked 'unverified'"}]}"""

HARVEST = {
 "G1": ("Compiled-data products (any country)", 15, """Find paid products/businesses (or clear demand for them) whose core value is a COMPILED DATASET assembled from many scattered public/semi-public sources and kept fresh by automation: e.g. government contract/tender feeds for a niche, permit/licence/planning data, regulatory filings, product recall/safety databases, grant databases, price indices, company/registry enrichment, court/docket data, real-estate or zoning data, sanctions/PEP lists, supplier/certification registries, app/plugin market intelligence.
Any country (US/EU/UK/AU/global). Evidence of payment: pricing pages, revenue disclosures dated within 18 months, Indie Hackers/Starter Story revenue pages, or listings. Prefer niches where a solo operator with agents could build and maintain it."""),
 "G2": ("Maintained rules engines (any jurisdiction)", 15, """Find paid products (or proven demand) whose moat is a MAINTAINED RULES ENGINE for tax, regulation or compliance in some jurisdiction: e.g. US state sales-tax/nexus niches, EU VAT OSS edge cases, payroll/benefit calculators by state, e-invoicing format mandates (EU ViDA, Poland KSeF, Belgium 2026, Germany 2025-28, France 2026-27), accessibility/EAA compliance checkers, cookie/privacy rules by country, customs/HS-code and duty calculators, labelling/allergen rules, export-control screening, insurance/licensing requirement lookups by state.
Any country. Include mandate commencement dates (Nov 2026-2028) with official URLs where relevant, current solution prices, and whether incumbents are expensive enterprise tools leaving SMB/self-serve gaps."""),
 "G3": ("Network-effect / two-sided products runnable by agents", 12, """Find niche online marketplaces, directories with two-sided participation, review/benchmark networks, data co-ops or communities where value compounds with each participant, that are small, online-only, self-serve, and could be run mostly by AI agents (moderation, matching, billing). Any country. Prefer existing evidence of payment (listing fees, take rate, subscriptions) dated within 18 months. Exclude local-services marketplaces and anything needing the founder's personal brand."""),
 "G4": ("Switching-cost B2B tools in decaying niches", 12, """Find B2B SaaS niches (any country) where customers store data/workflows/integrations (high switching cost), and the incumbent is decaying: acquired-and-neglected, price-hiked, sunset announced, or end-of-life (e.g. products sunset in 2026-2027 with migration deadlines, legacy desktop tools, abandoned SaaS with active paying users). Record the sunset/EOL date and URL, the user base size, and current alternatives. Exclude cases where the platform owner provides the migration."""),
 "A3": ("Flippa SaaS/app/plugin listings (buy track, retry)", 15, """Search flippa.com for CURRENT listings (flippa.com/<number>-... pages, and Flippa search results for 'SaaS', 'Chrome extension', 'WordPress plugin', 'Shopify app', 'mobile app') with monthly profit >= $500. Open each listing page and record asking price, monthly revenue/profit, 'verified' badges (P&L verified, traffic verified), owner hours, age, listing date. Also search Google: site:flippa.com SaaS "net profit" 2026. Any country."""),
 "A4": ("Empire Flippers / FE International / Quiet Light / Microns / Acquire roundups (buy track, retry)", 15, """Search empireflippers.com/marketplace (SaaS listings show monthly net profit and multiple), feinternational.com/buy-a-website, quietlight.com/listings, microns.io/startup-listings, tinyacquisitions.com, acquire.com blog 'startups for sale this week' and newsletters (e.g. 'Acquire Weekly', 'Microns newsletter', 'Tiny Acquisitions roundups') from Jun-Oct 2026, for SaaS/plugin/extension/app/data businesses with profit >= $500/month and asking price <= ~$300k. Record listing URL, asking price, profit, multiple, verification, owner hours, listing date."""),
 "A1": ("Acquire.com listings (buy track)", 20, """Find public Acquire.com listings (app.acquire.com/startup/... or /public/...) from the last ~6 months for small SaaS, plugins, extensions, apps or data products with stated TTM PROFIT >= $6k (>= $500/month) or MRR >= $1k, asking price ideally <= 4x annual profit, low owner hours, any country. Record asking price, TTM revenue, TTM profit, verified status, owner hours, listing date, churn if shown, and the moat (customer base + switching cost, data, integrations). Skip content/affiliate/ecommerce/agency businesses."""),
 "A2": ("Flippa / Microns / SideProjectors / Tiny / Empire Flippers / FE International / Motion Invest (buy track)", 20, """Find public listings from the last ~6 months on Flippa, Microns.io, SideProjectors, Tiny Acquisitions/Marketplace, Empire Flippers, FE International, Quiet Light, Motion Invest, IndieMaker for small SaaS/plugin/extension/app/data businesses with stated profit >= $500/month or MRR >= $1k, asking price ideally <= 4x annual profit, low owner hours, any country. Record asking price, revenue, profit, verified status, owner hours, listing date, churn, moat. Skip content/affiliate/ecommerce/agency/service businesses and anything reliant on the seller's face."""),
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
        d = ask(f"harvest_{k}", p, "high" if k in ("A3", "A4") else "medium")
        return [dict(l, source=k, track=("buy" if k.startswith("A") else "build")) for l in (d or {}).get("leads", [])]
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

KC_SCHEMA = """Return ONLY JSON: {"results":[{"id":"L001","verdict":"survive|kill","kill_rule":"K0|K1|K2|K3|K4|K5|K6|B2|B3|B5|B6|none","defensible_asset":0,"moat_type":"data|rules|network|switching|none",
"reason":"one sentence, specific","launches_last_6m":"names + launch dates of competing products found by a dated search since 23 Apr 2026, or 'none found'","buy_checklist":"buy track: B1-B6 findings, else null",
"platform_or_partner":"who, or 'none found'","incumbents":"main maintained incumbents with price, or 'none found'",
"claim_event_date":"YYYY-MM or 'unverified'","urls":["URLs supporting the verdict; every kill needs >=1"]}]}"""

def kc_prompt(batch, effort_note=""):
    return f"""You are running a CHEAP KILL-CHECK on business leads. Today is {TODAY}. Use live web search, targeted (2-4 searches per lead). Never invent facts; say 'unverified'.
{effort_note}
Apply these locked rules exactly:
{RULES}
For each lead decide survive or kill. FIRST apply K0 (moat gate, strict: unclear moat = kill). Then RUN A DATED SEARCH for competitor launches since 23 Apr 2026 (K2). Buy-track leads use the B checklist instead of K2/K4. Other kills need URL evidence; if missing, survive.
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
    random.seed(10); samp = random.sample(kills, min(10, len(kills))); byid = {l["id"]: l for l in leads()}
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
For buy-track leads, re-open the listing and assess it as an ACQUISITION (verified revenue, churn, owner hours <=5h, price vs profit, account transferability, seller dependence). Gather: demand size (searches, installs, users, regulated population with source), prices of current solutions, revenue proof WITH the date of the underlying event (claim_event_date; >18 months old = zero weight; self-described failures = zero weight),
copy-speed (competitors launched since Apr 2026 with dates), platform/partner risk, defensible asset (compiled data, rules engine, network effect, switching costs), build effort for an AI-agent-run solo operator, lawful acquisition channel, the cheapest <=1-day desk test.
Return ONLY JSON: {{"id":"{i}","name":"","demand":"","prices":"","revenue_proof":[{{"claim":"","claim_event_date":"","url":""}}],"copy_speed":"","platform_risk":"","defensible_asset":"","build_effort":"","channel":"","owner_hours_per_week":"","automation_share_pct":"INTEGER 0-100 you estimate (share of ALL work incl. sales/support/admin agents can do), or null if truly unknowable","automation_reason":"","track":"build|buy","listing_check":"buy track: verified revenue, churn, owner hours, price/profit multiple, transferability; else null","moat_assessment":"","desk_test":"","red_flags":"","urls":[]}}"""
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
Five separate scores per lead, each with a short reason: success_12m (0-10), agent_runnability (0-10), fit (0-10), automation_share_pct (an INTEGER you must estimate from the evidence and argue in automation_reason; never copy a placeholder; 0 only if argued), defensible_asset (0-10; <4 = hard_rule_fail "K0"). Revenue claims whose event is >18 months old or self-described failures get ZERO weight.
Also: claim_event_date (newest dated revenue event or 'none'), copy_speed (launches since Apr 2026), defensible_asset (short), hard_rule_fail (null or which rule).
EVIDENCE: {json.dumps(ev, ensure_ascii=False)}
Return ONLY JSON: {{"scores":[{{"id":"","name":"","success_12m":0,"success_reason":"","agent_runnability":0,"runnability_reason":"","fit":0,"fit_reason":"","automation_share_pct":"integer you estimate","automation_reason":"","defensible_asset":0,"defensible_reason":"","track":"","claim_event_date":"","copy_speed":"","defensible_asset":"","hard_rule_fail":null}}]}}"""
    d = ask("score", p, "xhigh", web=False)
    S = sorted([s for s in d["scores"] if not s.get("hard_rule_fail")], key=lambda s: (-s["success_12m"], -(s.get("defensible_asset") or 0), -s["fit"]))
    bad = [s for s in d["scores"] if s.get("hard_rule_fail")]
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
For buy-track candidates, validate as an ACQUISITION: re-open the listing, verified revenue/profit, churn, owner hours, price multiple, transferability, seller dependence, platform risk. Check: current competitors and prices (esp. any launched since Apr 2026), platform/partner ownership, demand signals dated <=18 months, legal position (UK), lawful acquisition channel, owner hours, defensible asset.
Verdict: pursue / maybe / kill, with confidence low/medium/high. 'pursue' at medium+ only if: live demand/revenue evidence dated <=18 months, reachable lawful channel, copy-speed passes on re-check, the moat is confirmed, and a <=1-day first test exists (buy track: a defined due-diligence step and a price that makes sense vs verified profit).
If your verdict would be 'maybe' and the deciding test is desk-only and doable now with web research (<=1 day), RUN IT NOW and report its result, then give the final verdict.
Return ONLY JSON: {{"id":"{i}","name":"","verdict":"","confidence":"","one_line":"","why":["3-6 bullets each with URL"],"competitors":[{{"name":"","price":"","launched":"","url":""}}],"demand":"","legal":"","channel":"","owner_hours":"","desk_test_run":"what you ran and result, or 'n/a'","first_test":"","unverified":[],"urls":[]}}"""
        return ask(f"val_{i}", p, "high", web=True, order=["claude", "codex", "pi"])
    with ThreadPoolExecutor(4) as ex: out = [o for o in ex.map(one, sc) if o]
    (W / "validation.json").write_text(json.dumps(out, indent=1)); log(f"validate: {len(out)} done " + str([(o.get('id'), o.get('verdict'), o.get('confidence')) for o in out]))

if __name__ == "__main__":
    (W / "pid").write_text(str(os.getpid()))
    t0 = time.time()
    for st in sys.argv[1:]: log(f"== stage {st} start"); globals()[st](); log(f"== stage {st} end ({time.time()-t0:.0f}s total)")
