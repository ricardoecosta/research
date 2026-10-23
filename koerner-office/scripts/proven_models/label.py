"""One cheap LLM labelling pass: assign each non-physical v8 record to a business MODEL code.
Runner order: Codex low -> Claude -> pi (box fallback is manual). Writes analysis/proven_models/labels.json + calls.json"""
import json, sys, concurrent.futures as cf
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/v8'))
import common8 as C
MODELS = {
 "SAAS":"micro-SaaS / web software sold to businesses or prosumers (subscription)",
 "APP":"consumer mobile app or game (App Store / Play, in-app purchases, paywall)",
 "PLUG":"plugin / browser extension / Shopify-WordPress-marketplace app",
 "API":"API or scraper wrapper / Apify actor / pay-per-use AI utility",
 "DATA":"B2B data product, lead database, reports, alerts, research packs",
 "SEO":"niche content / affiliate / SEO blog site monetised by ads or affiliates",
 "DIR":"niche or programmatic SEO directory / listings site (ads, featured listings)",
 "TOOL":"free tool / calculator / converter website monetised by ads or upsell",
 "NEWS":"newsletter (ads, sponsors, paid tier)",
 "FACELESS":"faceless social/video content pages or channels (YouTube, FB, IG, TikTok) monetised by ad share/creator payouts/affiliates",
 "DIGI":"digital products: templates, ebooks, printables, prompt packs, GPTs, Etsy/Gumroad downloads",
 "KDP":"self-published books / KDP / low-content books / audiobooks",
 "POD":"print-on-demand or personalised custom products made by a fulfilment partner",
 "ECOM":"e-commerce / DTC brand / dropshipping / Amazon FBA / reselling physical goods online",
 "BUY":"buying an existing (online) business to improve or flip",
 "MKT":"two-sided marketplace / platform / community app connecting buyers and sellers",
 "LEADGEN":"rank-and-rent or lead-generation sites that sell leads to local businesses",
 "AGENCY":"agency / done-for-you / AI automation or consulting service sold to businesses",
 "FREEL":"freelance or productised service done per gig (writing, design, VA, voiceover)",
 "EDU":"course / coaching / cohort / paid community / education",
 "BRAND":"personal-brand media where the founder is the face (podcast, own YouTube, influencer, UGC)",
 "LOCAL":"local or physical in-person service / physical asset business",
 "NONE":"not a business model (job, investing, a big company mentioned in passing, platform name)",
}
rows = [json.loads(l) for l in open(ROOT/'analysis/v8/ideas_flat.jsonl')]
PHYS = {"home_service","local_service","events_experiences","rental_asset","real_estate","vending_machines_kiosks","franchise","manufacturing"}
todo = [x for x in rows if x['idea']['category'] not in PHYS and not x['physical_world']]
print(len(todo), "to label")
def line(i,x):
    d=x['idea']; return f"{i}\t{d['name'][:70]}\t{(d.get('one_liner') or '')[:150]}\t{(d.get('revenue_model') or '')[:80]}"
HEAD = ("Classify each business record by its BUSINESS MODEL (how it makes money and is run), not its niche.\n"
        "Codes:\n" + "\n".join(f"{k}: {v}" for k,v in MODELS.items()) +
        "\nInput lines: idx<TAB>name<TAB>one-liner<TAB>revenue model.\n"
        "Reply with JSON only: {\"l\": [[idx, \"CODE\"], ...]} covering every idx.\n\n")
calls = {"codex:low":0, "claude":0, "pi":0, "failed":0}
def ask(prompt):
    try:
        for w in range(3):
            try:
                ans,_,s = C.run_codex(prompt, "low", timeout=900); calls["codex:low"]+=1; return C.parse_json_text(ans)
            except C.Busy: break
            except Exception as e: calls["codex:low"]+=1; print("codex err", str(e)[:150])
    except Exception as e: print(e)
    try:
        ans,_,s = C.run_claude(prompt, timeout=900); calls["claude"]+=1; return C.parse_json_text(ans)
    except Exception as e: calls["claude"]+=1; print("claude err", str(e)[:150])
    try:
        ans,_,s = C.run_pi(prompt, timeout=900); calls["pi"]+=1; return C.parse_json_text(ans)
    except Exception as e: calls["pi"]+=1; calls["failed"]+=1; print("pi err", str(e)[:150]); return {"l":[]}
B = 300
batches = [list(enumerate(todo))[i:i+B] for i in range(0, len(todo), B)]
labels = {}
def work(b):
    j = ask(HEAD + "\n".join(line(i,x) for i,x in b))
    return {todo[int(i)]['key']: c for i,c in j.get("l",[]) if c in MODELS and 0<=int(i)<len(todo)}
with cf.ThreadPoolExecutor(3) as ex:
    for r in ex.map(work, batches): labels.update(r)
missing = [x for x in todo if x['key'] not in labels]
print("missing", len(missing))
if missing:
    idx = {x['key']:i for i,x in enumerate(todo)}
    labels.update(work([(idx[x['key']], x) for x in missing]))
out = ROOT/'analysis/proven_models'
json.dump(labels, open(out/'labels.json','w'), indent=0)
json.dump(calls, open(out/'calls.json','w'))
print(calls, len(labels))
