"""v11 (rebuilt) pipeline. LLM only labels/clusters (E) and tabulates checklists (B); counting and pass rules are code.
Stages: label cluster count kc shadow checklist select validate. Cache: /tmp/loop/v11/out/<tag>.json"""
import csv, json, os, random, re, sys, time, datetime as dt, collections
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from runner import call_llm, BoxPending
from rapidfuzz import fuzz
REPO = Path(__file__).resolve().parents[2]; AN = REPO / "analysis"; V = AN / "v11"
W = Path("/tmp/loop/v11"); OUT = W / "out"; OUT.mkdir(parents=True, exist_ok=True); LOG = W / "run.log"; CALLS = W / "calls.jsonl"
TODAY = "23 Oct 2026"; RULES = (V / "RULES_LOCKED.md").read_text()
CONSTRAINTS = """Owner: Ricardo, UK-based (Bromley) technical founder. Market: ANY country. Hard constraints: >=50% of all work by AI agents and <=5 h/week of his time
(for a bought business: after a 90-day handover); software/digital/data product; NOT selling to local businesses; NO face/personal brand; NO cold or unlawful outreach
(UK PECR + recipient's law). Channels: SEO, app stores, marketplaces, integrations, paid ads, partnerships, existing customers."""
def log(m):
    line = f"{dt.datetime.now():%H:%M:%S} {m}"; print(line, flush=True); open(LOG, "a").write(line + "\n")
def ask(tag, prompt, effort, web=False, order=None):
    f = OUT / f"{tag}.json"
    if f.exists(): return json.loads(f.read_text())
    try: data, runner, secs = call_llm(prompt, effort=effort, logf=str(LOG), tag=f"v11_{tag}", web=web, order=order)
    except BoxPending: log(f"{tag} BOX PENDING"); return None
    f.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    open(CALLS, "a").write(json.dumps({"tag": tag, "runner": runner, "effort": effort, "secs": round(secs), "t": f"{dt.datetime.now():%H:%M}"}) + "\n")
    log(f"{tag} done via {runner} in {secs:.0f}s"); return data
def jl(p): return [json.loads(l) for l in open(p)]
def wjl(p, rows):
    with open(p, "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
SEEN = list(csv.DictReader(open(AN / "loop/SEEN.csv")))
def seen_match(name): return next((r["name"] for r in SEEN if fuzz.token_set_ratio(name.lower(), r["name"].lower()) >= 88), None)

# ---------- Track E ----------
def label():
    ev = jl(V / "evidence_raw.jsonl"); B = [ev[i:i+60] for i in range(0, len(ev), 60)]
    def one(ib):
        i, b = ib
        items = [{"i": k, "src": r["src"], "tool": r.get("tool"), "text": r["text"][:500]} for k, r in enumerate(b)]
        p = f"""Label each snippet. Do NOT invent ideas or judge business value. For each item return:
is_pain (true if the author describes a real problem, unmet need, or complaint about a tool/workflow; false for jokes, promotion, off-topic, generic praise),
pain (<=12 words, GENERIC and product-agnostic, e.g. "invoice data entry from PDFs into accounting software"; reuse wording consistently; null if not pain),
pays (true if the author pays or says they'd pay, names a paid tool they use/left, hired someone, or it's a 1-2 star review of a paid tool/app).
Items: {json.dumps(items, ensure_ascii=False)}
Return ONLY JSON: {{"labels":[{{"i":0,"is_pain":true,"pain":"...","pays":false}}]}}"""
        d = ask(f"label_{i:03d}", p, "low")
        out = []
        for l in (d or {}).get("labels", []):
            try: r = dict(b[int(l["i"])]); r.update(is_pain=bool(l.get("is_pain")), pain=l.get("pain"), pays=bool(l.get("pays"))); out.append(r)
            except Exception: pass
        return out
    with ThreadPoolExecutor(6) as ex: res = [r for rr in ex.map(one, enumerate(B)) for r in rr]
    wjl(W / "labelled.jsonl", res); log(f"label: {len(ev)} snippets, {len(B)} batches, {sum(r['is_pain'] for r in res)} pains")

def cluster():
    res = jl(W / "labelled.jsonl"); pains = collections.Counter(r["pain"].strip().lower() for r in res if r["is_pain"] and r.get("pain"))
    labels = sorted(pains); maps = {}
    chunks = [labels[i:i+450] for i in range(0, len(labels), 450)]
    canon = []
    for ci, ch in enumerate(chunks):
        p = f"""Group these pain labels into clusters of the SAME underlying problem (same job-to-be-done). Do not judge value. Reuse existing cluster names when they fit.
Existing clusters: {json.dumps(canon)}
Labels: {json.dumps(ch, ensure_ascii=False)}
Return ONLY JSON: {{"map":{{"<label>":"<cluster name, <=10 words>"}}}}  (every label must appear once)"""
        d = ask(f"cluster_{ci:02d}", p, "medium")
        for k, v in (d or {}).get("map", {}).items(): maps[k.strip().lower()] = v
        canon = sorted(set(maps.values()))
    for r in res: r["cluster"] = maps.get((r.get("pain") or "").strip().lower()) if r["is_pain"] else None
    wjl(W / "clustered.jsonl", res); log(f"cluster: {len(labels)} labels -> {len(set(maps.values()))} clusters")

def count():
    res = [r for r in jl(W / "clustered.jsonl") if r.get("cluster")]
    by = collections.defaultdict(list)
    for r in res: by[r["cluster"]].append(r)
    rows = []
    for c, rs in by.items():
        auth = {r["author"] for r in rs}; pay = [r for r in rs if r["pays"]]
        srcs = collections.Counter(r["src"].split(":")[0] for r in rs)
        rows.append({"cluster": c, "complainers": len(auth), "snippets": len(rs), "paying_proof": len(pay), "sources": dict(srcs),
                     "examples": [{"url": r["url"], "date": r["date"], "text": r["text"][:240]} for r in sorted(rs, key=lambda r: -r["pays"])[:6]],
                     "seen_dup": seen_match(c)})
    rows.sort(key=lambda r: (-r["complainers"], -r["paying_proof"]))
    n30 = [r for r in rows if r["complainers"] >= 30 and r["paying_proof"] >= 1 and not r["seen_dup"]]
    bar = 30 if len(n30) >= 5 else 10
    passed = [r for r in rows if r["complainers"] >= bar and r["paying_proof"] >= 1 and not r["seen_dup"]][:40]
    json.dump({"bar": bar, "n_at_30": len(n30), "clusters": rows, "passed": [r["cluster"] for r in passed]}, open(W / "counts.json", "w"), indent=1, ensure_ascii=False)
    log(f"count: {len(rows)} clusters; >=30 with pay: {len(n30)}; bar used {bar}; passed {len(passed)}")

def kc():
    C = json.load(open(W / "counts.json")); byc = {r["cluster"]: r for r in C["clusters"]}; P = [byc[c] for c in C["passed"]]
    B = [P[i:i+3] for i in range(0, len(P), 3)]
    def one(ib):
        i, b = ib
        p = f"""KILL-CHECK (single high-effort pass) for demand clusters harvested from real complaints. Today is {TODAY}. Use live web search; cite URLs. Never invent facts ('unverified').
{CONSTRAINTS}
Locked rules: {RULES}
For each cluster: name the most plausible agent-runnable software/data product (or curated paid-listing directory/data site) that fixes it; then apply K0 time-to-moat (a) agents can build the asset in <=3 months (b) rival needs >=3 months to copy (c) nobody owns it - any 'no' = kill; K1; K2 dated search for competing launches since 23 Apr 2026 (>=2 = kill, list names+dates); K3; K4; K6.
Clusters (with real complaint counts and examples): {json.dumps(b, ensure_ascii=False)}
Return ONLY JSON: {{"results":[{{"cluster":"","product":"","verdict":"survive|kill","kill_rule":"K0|K1|K2|K3|K4|K6|none","time_to_moat":{{"a":"yes/no why","b":"yes/no why","c":"yes/no who owns"}},"launches_last_6m":"","incumbents":"","reason":"","urls":[]}}]}}"""
        return (ask(f"kc_{i:02d}", p, "xhigh", web=True) or {}).get("results", [])
    with ThreadPoolExecutor(5) as ex: res = [r for rr in ex.map(one, enumerate(B)) for r in rr]
    for r in res: r.update({k: byc.get(r["cluster"], {}).get(k) for k in ("complainers", "paying_proof", "examples")})
    json.dump(res, open(W / "kc.json", "w"), indent=1, ensure_ascii=False); log(f"kc: {len(res)} clusters, survive {sum(r['verdict']=='survive' for r in res)}")

def shadow():
    res = json.load(open(W / "kc.json")); kills = [r for r in res if r["verdict"] == "kill"]
    random.seed(11); samp = random.sample(kills, min(10, len(kills)))
    def one(r):
        p = f"""SHADOW RE-JUDGE of a kill decision. Today is {TODAY}. Use live web; cite URLs. Rules: {RULES}
{CONSTRAINTS}
A previous pass killed this cluster/product: {json.dumps(r, ensure_ascii=False)}
Judge independently. Return ONLY JSON: {{"verdict":"survive|kill","kill_rule":"","agree_with_kill":true,"reason":"","urls":[]}}"""
        return {"cluster": r["cluster"], "cheap": r, "shadow": ask(f"shadow_{abs(hash(r['cluster']))%10**8}", p, "high", web=True, order=["claude", "codex", "pi"]) or {}}
    with ThreadPoolExecutor(5) as ex: out = list(ex.map(one, samp))
    json.dump(out, open(W / "shadow.json", "w"), indent=1, ensure_ascii=False); log(f"shadow: {len(out)}, wrong kills {sum(o['shadow'].get('verdict')=='survive' for o in out)}")

# ---------- Track B ----------
BAD = re.compile(r"affiliate|blog|content site|newsletter|ecommerce store|dropship|agency|amazon fba|youtube channel|casino|betting", re.I)
def money(s):
    m = re.search(r"(?:USD|US\$|\$)\s?([\d,.]+)\s?([kKmM])?", s or "")
    if not m: return None
    v = float(m.group(1).replace(",", "")); return v * (1000 if (m.group(2) or "").lower() == "k" else 1e6 if (m.group(2) or "").lower() == "m" else 1)
def checklist():
    L = jl(V / "listings_raw.jsonl"); keep = []
    for l in L:
        txt = (l.get("card") or "") + " " + (l.get("page") or "")[:600]
        if BAD.search(l["url"]) or not l.get("page"): continue
        m = re.search(r"Asking Price[^$]*?USD \$([\d,]+)", l["page"]) or re.search(r"USD \$([\d,]+)\s", l["page"][l["page"].find("Asking Price"):] if "Asking Price" in l["page"] else "")
        price = float(m.group(1).replace(",", "")) if m else None
        l["asking_usd_parsed"] = price
        if price is not None and not (20000 <= price <= 150000): continue
        keep.append(l)
    keep = keep[:100]
    def one(l):
        p = f"""Turn this business-for-sale listing into a DUE-DILIGENCE CHECKLIST TABLE. Use ONLY the listing text. Do NOT judge whether it is a good buy, do not rank.
For each row give status = stated | missing | looks off, plus the evidence (quote/number from the text) and a note.
Rows: C1 verified revenue (Flippa verification badge / Stripe or P&L verified); C2 revenue >= $1k/month and profit > 0; C3 asking price $20k-$150k and <= 5x annual profit (compute multiple if possible);
C4 traffic/acquisition mostly organic/app-store/marketplace (not owner outreach/sales); C5 owner's current hours and tasks; C6 no customer concentration (>20% of revenue from one customer);
C7 transferable, no seller face/brand dependence; C8 durability (no >30% decline, no platform-ban risk); C9 plausible 90-day handover to AI agents ending <=5 h/week (state the plan in 3-5 steps; 'looks off' if the work is inherently human: enterprise sales, account management, bespoke dev, regulated advice).
Also extract: name, category, asking_price_usd, monthly_revenue_usd, monthly_profit_usd, verification text, listing_date if any; and 5 follow-up questions for the seller.
Context on owner constraints: {CONSTRAINTS}
LISTING URL: {l['url']}
CARD: {l.get('card','')[:1200]}
PAGE: {l.get('page','')[:7000]}
Return ONLY JSON: {{"url":"{l['url']}","name":"","category":"","asking_price_usd":null,"monthly_revenue_usd":null,"monthly_profit_usd":null,"verification":"","listing_date":"",
"rows":[{{"id":"C1","status":"stated|missing|looks off","evidence":"","note":""}}],"handover_plan":["..."],"steady_state_hours":"","questions":["..."]}}"""
        d = ask(f"cl_{l['id']}", p, "medium")
        return d
    with ThreadPoolExecutor(6) as ex: res = [r for r in ex.map(one, keep) if r]
    for r in res:
        st = {x["id"]: x["status"].lower() for x in r.get("rows", [])}
        hard = [c for c in ("C1", "C2", "C3", "C7", "C9") if st.get(c) == "looks off"] + [c for c in ("C1", "C2") if st.get(c) == "missing"]
        miss = sum(v == "missing" for v in st.values())
        r["pass"] = not hard and miss <= 3; r["hard_fails"] = hard; r["missing"] = miss; r["seen_dup"] = seen_match(r.get("name") or "")
        if r["seen_dup"]: r["pass"] = False
    json.dump(res, open(W / "checklists.json", "w"), indent=1, ensure_ascii=False)
    log(f"checklist: {len(L)} listings, {len(keep)} in scope, {len(res)} tabulated, pass {sum(r['pass'] for r in res)}")

# ---------- Validation ----------
def validate():
    E = [r for r in json.load(open(W / "kc.json")) if r["verdict"] == "survive"] if (W / "kc.json").exists() else []
    try: E += [o["cheap"] for o in json.load(open(W / "shadow.json")) if o["shadow"].get("verdict") == "survive"]
    except Exception: pass
    Bs = [r for r in json.load(open(W / "checklists.json")) if r["pass"]] if (W / "checklists.json").exists() else []
    Bs.sort(key=lambda r: (r["missing"], -(r.get("monthly_profit_usd") or 0)))  # mechanical: fewest gaps, then profit
    E.sort(key=lambda r: -(r.get("complainers") or 0))
    nb = min(len(Bs), max(4, 8 - len(E))); sel = [("B", b) for b in Bs[:nb]] + [("E", e) for e in E[:8 - nb]]
    json.dump(sel, open(W / "selected.json", "w"), indent=1, ensure_ascii=False)
    def one(te):
        t, x = te; key = x.get("url") or x.get("cluster"); tag = "val_" + re.sub(r"\W+", "_", key)[-60:]
        what = ("BUY-TRACK acquisition. Re-open the listing URL; confirm verified revenue/profit and how verified; churn; owner hours; price multiple; transferability; platform risk; "
                "write the 90-day handover-to-agents plan and steady-state hours; define the first due-diligence step.") if t == "B" else \
               ("EVIDENCE-FIRST build. Re-check the complaint evidence (examples), paying proof, time-to-moat a/b/c, and copy-speed (dated launches since 23 Apr 2026). "
                "Favour compounding assets (e.g. agent-run curated directory/data site where vendors pay to be listed).")
        p = f"""HIGH-EFFORT WEB-CHECKED VALIDATION (METHOD step 10). Today is {TODAY}. Use WebSearch/WebFetch; cite a URL for every decisive fact; never invent numbers ('unverified').
{CONSTRAINTS}
Locked rules: {RULES}
Candidate ({what}): {json.dumps(x, ensure_ascii=False)[:9000]}
Verdict pursue/maybe/kill + confidence low/medium/high, per the locked pursue criteria.
If verdict is pursue or maybe, write a concrete REAL-MONEY TEST PLAN costing <= GBP 50 (pre-sale page, small ad test, or paid-listing page; for buy: first due-diligence step + low-cost verification). Include channel, spend, duration, success threshold, kill threshold. Plan only: nothing is to be spent and nobody contacted now.
Return ONLY JSON: {{"key":"{key}","track":"{t}","name":"","verdict":"","confidence":"","one_line":"","why":["bullets with URL"],"evidence_counts":"complainers / paying proof (E) or null","listing_url":"","price":"","verified_revenue_profit":"","handover_plan":"","competitors":[{{"name":"","price":"","launched":"","url":""}}],"test_plan":{{"what":"","channel":"","spend_gbp":0,"duration":"","success":"","kill":""}},"unverified":[],"urls":[]}}"""
        return ask(tag, p, "high", web=True, order=["claude", "codex", "pi"])
    with ThreadPoolExecutor(4) as ex: out = [o for o in ex.map(one, sel) if o]
    json.dump(out, open(W / "validation.json", "w"), indent=1, ensure_ascii=False)
    log("validate: " + str([(o.get("track"), o.get("name"), o.get("verdict"), o.get("confidence")) for o in out]))

if __name__ == "__main__":
    (W / "pid").write_text(str(os.getpid())); t0 = time.time()
    for st in sys.argv[1:]: log(f"== {st} start"); globals()[st](); log(f"== {st} end ({time.time()-t0:.0f}s)")
