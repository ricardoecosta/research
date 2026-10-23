"""v9 loop iteration pipeline (LOOP.md §6). Stages: harvest, killcheck, shadow, evidence, score, validate.
Resumable: each LLM answer cached in /tmp/loop/v9/out/<tag>.json. Calls logged to calls.jsonl."""
import csv, json, os, random, sys, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from runner import call_llm, BoxPending
from rapidfuzz import fuzz

REPO = Path(__file__).resolve().parents[2]
AN = REPO / "analysis"; V9 = AN / "v9"; W = Path("/tmp/loop/v9"); OUT = W / "out"; OUT.mkdir(parents=True, exist_ok=True)
LOG = W / "run.log"; CALLS = W / "calls.jsonl"
TODAY = "23 Oct 2026"
RULES = (V9 / "RULES_LOCKED.md").read_text()
CONSTRAINTS = """Owner: Ricardo, Bromley UK. Hard constraints: fully/mostly run by AI agents (>=50% automation, <=5 h/week of his time);
software/digital/data product interesting to a technical founder; NOT selling to local businesses; NOT needing his face or personal brand;
NOT relying on cold outreach unlawful under UK PECR (cold SMS/WhatsApp/DM/email to individuals or sole traders)."""

def log(m):
    line = f"{dt.datetime.now():%H:%M:%S} {m}"; print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def ask(tag, prompt, effort, web=True, order=None):
    f = OUT / f"{tag}.json"
    if f.exists(): return json.loads(f.read_text())
    try:
        data, runner, secs = call_llm(prompt, effort=effort, logf=str(LOG), tag=f"v9_{tag}", web=web, order=order)
    except BoxPending:
        log(f"{tag} BOX PENDING"); return None
    f.write_text(json.dumps(data, indent=1))
    with open(CALLS, "a") as c: c.write(json.dumps({"tag": tag, "runner": runner, "effort": effort, "secs": round(secs), "t": f"{dt.datetime.now():%H:%M}"}) + "\n")
    log(f"{tag} done via {runner} in {secs:.0f}s"); return data

def seen_rows():
    return list(csv.DictReader(open(AN / "loop/SEEN.csv")))

def seen_names():
    return "; ".join(r["name"] for r in seen_rows())

LEAD_SCHEMA = """Return ONLY JSON: {"leads":[{"name":"short product/opportunity name","source":"S1|S2|S3|S4","sub_source":"e.g. WordPress.org / Flippa / HMRC",
"what":"one sentence: the product we would build/buy and who pays","trigger":"the regulation, decaying product, listing or complaint behind it",
"urls":["1-3 source URLs you actually opened"],"evidence_of_payment":"price/revenue/installs/users as stated, with numbers only if seen on the page",
"claim_event_date":"YYYY-MM or 'unverified'","notes":"anything unverified marked 'unverified'"}]}"""

HARVEST = {
 "S1": ("UK regulation-change calendar", 24, """Search GOV.UK, HMRC, Companies House, FCA, ICO, Ofgem, Ofcom, DESNZ, MHCLG, legislation.gov.uk for UK legal/regulatory changes COMMENCING between Nov 2026 and end of 2028
that force small businesses, landlords, charities, sole traders or consumers to buy or use software, a digital product or a data service (e.g. MTD for Income Tax threshold steps, Companies House ID verification and software-only filing,
DMCC Act subscription-contract rules, Renters' Rights Act duties, e-invoicing, pensions dashboards, Awaab's law, EPC/MEES, Building Safety, Making Tax Digital for corporation tax, Economic Crime Act, Procurement Act, etc. — verify each, do not assume).
One lead per concrete product opportunity (a regulation can give 1-2 leads). Give the commencement date with its GOV.UK/legislation URL."""),
 "S2a": ("Decaying WordPress / WooCommerce plugins", 12, """Find paid or freemium WordPress.org plugins (with a paid pro version) that are closed or not updated for 12+ months, still with >=10,000 active installs (or large paid user base), ideally with 2025-2026 complaints. Use wordpress.org plugin pages (show 'Last updated', 'Active installations')."""),
 "S2b": ("Decaying Atlassian / Shopify / Xero / QuickBooks / Zendesk / HubSpot apps", 10, """Find PAID marketplace apps (Atlassian Marketplace, Shopify App Store, Xero App Store, Intuit, Zendesk, HubSpot, Slack, Zoom, monday.com) whose last release/update is 12+ months ago, that still have a meaningful paying user base (installs/reviews) and recent (2025-2026) negative reviews about bugs or lack of updates."""),
 "S2c": ("Decaying Chrome extensions / iOS & Mac utilities / Figma & Notion plugins", 10, """Find paid Chrome Web Store extensions, iOS/macOS utility apps, Figma/Notion/Obsidian/Raycast plugins that are abandoned (no update 12+ months, or removed/MV2-deprecated) but still have many paying users and recent complaints. Prefer ones with a clear paid tier."""),
 "S1b": ("UK regulation-change calendar (non-MTD, non-waste)", 14, """Same as S1 but EXCLUDE Making Tax Digital and waste tracking (already covered). Look specifically at: DMCC Act subscription-contract regime (commencement date), Renters' Rights Act phases (PRS database, landlord ombudsman, periodic tenancies), Awaab's law extension to private rented sector, Pensions dashboards connection deadlines, UK e-invoicing roadmap, Economic Crime and Corporate Transparency Act (ID verification, failure-to-prevent-fraud offence), Procurement Act 2023, Data (Use and Access) Act 2025 commencements, Building Safety / Higher-risk building regime, EPC/MEES consultation outcomes, Simpler Recycling / EPR packaging data reporting, Employment Rights Act commencements (e.g. SSP, fire-and-rehire, flexible working), Online Safety Act duties for small platforms, Leasehold reforms, Biodiversity net gain small sites, Martyn's Law. Verify each commencement date between Nov 2026 and 2028 on GOV.UK/legislation.gov.uk."""),
 "S2d": ("Decaying WordPress plugins (retry)", 12, """Search wordpress.org/plugins for plugins showing 'This plugin hasn't been tested with the latest 3 major releases of WordPress' or 'Last updated: 1 year ago' (or closed) that still show 'Active installations: 10,000+' or more AND that have (or had) a paid Pro/Premium version sold on the author's site. Good search queries: site:wordpress.org/plugins "hasn't been tested with the latest 3 major releases" "10,000+"; also check WP Tavern / wpmudev / Reddit r/Wordpress posts from 2025-2026 about abandoned popular plugins. Report the plugin page URL, active installs, last updated, pro price."""),
 "S3a": ("Acquire.com listings", 10, """Find public Acquire.com (acquire.com) marketplace listings or listing summaries (and Acquire blog/newsletter 'startups for sale' roundups) from the last 6 months for small SaaS/digital products asking under ~£50k (~$65k) with stated revenue and low owner hours. Record asking price, stated revenue (verified or not), listing date."""),
 "S3b": ("Flippa / Microns / SideProjectors / Tiny Acquisitions listings", 10, """Find public listings from the last 6 months on Flippa, Microns.io, SideProjectors, Tiny Marketplace, IndieMaker, Empire Flippers, for small SaaS, plugins, browser extensions, apps, data/digital products asking under ~£50k with stated revenue and low owner hours. Record asking price, stated revenue and verification status, listing date. Skip content/affiliate sites and anything needing the owner's face."""),
 "S4": ("Paying-user complaints about UK tools", 14, """Mine Trustpilot, G2, Capterra, App Store / Google Play, Reddit (r/UKPersonalFinance, r/smallbusinessuk, r/ukaccounting, r/LandlordUK) and marketplace reviews from 2025-2026 where PAYING users of tools used by UK sole traders, landlords, charities or small businesses complain about a UK-specific gap
(VAT, MTD/HMRC, Companies House, UK open banking/bank feeds, Royal Mail/Evri, Gift Aid, CIS, payroll/RTI, Land Registry, council tax, DVLA). One lead per concrete gap; quote or paraphrase the complaint with its URL and date."""),
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
Task: harvest about {n} distinct business-opportunity LEADS for source {k[:2]} ({title}).
{brief}
{CONSTRAINTS}
Prefer leads that could fit these constraints (software/digital, self-serve online sales). Leads are cheap: do NOT deeply validate, just record the facts you saw.
Skip anything already in this seen list (by meaning): {sn}
{LEAD_SCHEMA}"""
        d = ask(f"harvest_{k}", p, "medium")
        return [dict(l, source=k[:2]) for l in (d or {}).get("leads", [])]
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

KC_SCHEMA = """Return ONLY JSON: {"results":[{"id":"L001","verdict":"survive|kill","kill_rule":"K1|K2|K3|K4|K5|K6|none",
"reason":"one sentence, specific","launches_last_6m":"names+dates of competing products launched since Apr 2026, or 'none found'",
"platform_or_partner":"who, or 'none found'","incumbents":"main maintained incumbents with price, or 'none found'",
"claim_event_date":"YYYY-MM or 'unverified'","urls":["URLs supporting the verdict; every kill needs >=1"]}]}"""

def kc_prompt(batch, effort_note=""):
    return f"""You are running a CHEAP KILL-CHECK on business leads. Today is {TODAY}. Use live web search, targeted (2-4 searches per lead). Never invent facts; say 'unverified'.
{effort_note}
Apply these locked rules exactly:
{RULES}
For each lead decide survive or kill. Kill only when a rule is evidenced with a URL. If evidence is missing, survive (the deep stage decides).
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

def killcheck(effort="medium", pre="kc", fout="kc.json"):
    L = leads(); B = [L[i:i+4] for i in range(0, len(L), 4)]
    def one(ib):
        i, b = ib
        slim = [{k: l.get(k) for k in ("id","name","source","sub_source","what","trigger","urls","evidence_of_payment","claim_event_date")} for l in b]
        d = ask(f"{pre}_{i:02d}", kc_prompt(slim, "Effort: thorough (up to 6 searches per lead)." if effort == "xhigh" else ""), effort)
        return (d or {}).get("results", [])
    with ThreadPoolExecutor(6) as ex: res = [r for rr in ex.map(one, enumerate(B)) for r in rr]
    (W / fout).write_text(json.dumps(res, indent=1)); log(f"killcheck {effort}: {len(res)} results, survive {sum(r['verdict']=='survive' for r in res)}")

def shadow():
    res = json.loads((W / "kc.json").read_text()); kills = [r for r in res if r["verdict"] == "kill"]
    random.seed(9); samp = random.sample(kills, min(10, len(kills))); byid = {l["id"]: l for l in leads()}
    def one(r):
        l = byid[r["id"]]
        p = kc_prompt([l], "SHADOW RE-JUDGE at high effort. Be thorough (up to 8 searches). A cheaper pass killed this lead with: " + json.dumps(r) + "\nJudge independently; also set field \"agree_with_kill\": true/false in your result.")
        d = ask(f"shadow_{r['id']}", p, "xhigh"); x = ((d or {}).get("results") or [{}])[0]
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
Gather: demand size (searches, installs, users, regulated population with source), prices of current solutions, revenue proof WITH the date of the underlying event (claim_event_date; >18 months old = zero weight; self-described failures = zero weight),
copy-speed (competitors launched since Apr 2026 with dates), platform/partner risk, defensible asset (UK data, rules engine, switching costs), build effort for an AI-agent-run solo operator, lawful acquisition channel, the cheapest <=1-day desk test.
Return ONLY JSON: {{"id":"{i}","name":"","demand":"","prices":"","revenue_proof":[{{"claim":"","claim_event_date":"","url":""}}],"copy_speed":"","platform_risk":"","defensible_asset":"","build_effort":"","channel":"","owner_hours_per_week":"","automation_share_pct":0,"desk_test":"","red_flags":"","urls":[]}}"""
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
Four separate scores per lead, each with a short reason: success_12m (0-10), agent_runnability (0-10), fit (0-10), automation_share_pct. Revenue claims whose event is >18 months old or self-described failures get ZERO weight.
Also: claim_event_date (newest dated revenue event or 'none'), copy_speed (launches since Apr 2026), defensible_asset (short), hard_rule_fail (null or which rule).
EVIDENCE: {json.dumps(ev, ensure_ascii=False)}
Return ONLY JSON: {{"scores":[{{"id":"","name":"","success_12m":0,"success_reason":"","agent_runnability":0,"runnability_reason":"","fit":0,"fit_reason":"","automation_share_pct":0,"claim_event_date":"","copy_speed":"","defensible_asset":"","hard_rule_fail":null}}]}}"""
    d = ask("score", p, "xhigh", web=False)
    S = sorted([s for s in d["scores"] if not s.get("hard_rule_fail")], key=lambda s: (-s["success_12m"], -s["fit"], -s["agent_runnability"]))
    bad = [s for s in d["scores"] if s.get("hard_rule_fail")]
    (W / "scores.json").write_text(json.dumps({"ranked": S, "failed": bad}, indent=1))
    log(f"score: {len(d['scores'])} scored, {len(bad)} hard-rule fails, top8 {[s['id'] for s in S[:8]]}")

def validate():
    sc = json.loads((W / "scores.json").read_text())["ranked"][:8]
    def one(s):
        i = s["id"]; ev = json.loads((V9 / "evidence" / f"{i}.json").read_text())
        p = f"""You are doing HIGH-EFFORT, WEB-CHECKED VALIDATION (METHOD step 10) of one business opportunity. Today is {TODAY}. Use WebSearch and WebFetch extensively; re-verify every decisive fact live. Cite a URL for every fact. Never invent numbers; mark unverifiable as 'unverified'.
{CONSTRAINTS}
Locked rules: {RULES}
Lead evidence (from a cheaper pass — re-check, don't trust): {json.dumps(ev, ensure_ascii=False)}
Scores: {json.dumps(s, ensure_ascii=False)}
Check: current competitors and prices (esp. any launched since Apr 2026), platform/partner ownership, demand signals dated <=18 months, legal position (UK), lawful acquisition channel, owner hours, defensible asset.
Verdict: pursue / maybe / kill, with confidence low/medium/high. 'pursue' at medium+ only if: live demand evidence dated <=18 months, reachable lawful channel, copy-speed passes on re-check, and a <=1-day first test exists.
If your verdict would be 'maybe' and the deciding test is desk-only and doable now with web research (<=1 day), RUN IT NOW and report its result, then give the final verdict.
Return ONLY JSON: {{"id":"{i}","name":"","verdict":"","confidence":"","one_line":"","why":["3-6 bullets each with URL"],"competitors":[{{"name":"","price":"","launched":"","url":""}}],"demand":"","legal":"","channel":"","owner_hours":"","desk_test_run":"what you ran and result, or 'n/a'","first_test":"","unverified":[],"urls":[]}}"""
        return ask(f"val_{i}", p, "high", web=True, order=["claude", "codex", "pi"])
    with ThreadPoolExecutor(4) as ex: out = [o for o in ex.map(one, sc) if o]
    (W / "validation.json").write_text(json.dumps(out, indent=1)); log(f"validate: {len(out)} done " + str([(o.get('id'), o.get('verdict'), o.get('confidence')) for o in out]))

if __name__ == "__main__":
    t0 = time.time()
    for st in sys.argv[1:]: log(f"== stage {st} start"); globals()[st](); log(f"== stage {st} end ({time.time()-t0:.0f}s total)")
