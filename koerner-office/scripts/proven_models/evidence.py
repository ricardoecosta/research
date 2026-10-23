"""Per-model evidence summary (1 Codex medium call per model; fallback Claude -> pi). No re-mining: reads v8 mined claims only."""
import json, sys, concurrent.futures as cf, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/v8')); sys.path.insert(0, str(ROOT/'scripts/proven_models'))
import common8 as C
sys.argv = [sys.argv[0]]
OUT = ROOT/'analysis/proven_models'
models = json.load(open(OUT/'models.json'))
rows = {json.loads(l)['key']: json.loads(l) for l in open(ROOT/'analysis/v8/ideas_flat.jsonl')}
from group import model_of  # re-uses labels
SEL = ["consumer_mobile_apps_games","micro_saas","niche_programmatic_directories","niche_content_affiliate_sites","digital_templates_info_products",
       "faceless_social_video_pages","plugins_extensions_marketplace_apps","newsletters","buy_small_online_business","api_scraper_wrappers",
       "ecom_dtc_dropship_resale","print_on_demand_personalised","kdp_self_publishing","b2b_data_products","free_tool_calculator_sites"]
def packet(m):
    xs = [x for x in rows.values() if model_of(x)==m]
    xs.sort(key=lambda x: (x['depth']=='mention', -len(x.get('claims') or [])))
    lines=[]
    for x in xs[:45]:
        cl = [c for c in (x.get('claims') or []) if not c.get('hypothetical')][:10]
        lines.append(f"## {x['video_id']} | pub {x['publish_date']} | ch {x['channel']} | {x['idea']['name']} | depth {x['depth']} | local_b2b={x['sells_to_local_businesses']} face={x['needs_face_or_personal_brand']} phys={x['physical_world']} auto%={x['automation_share_e']} h/wk={x['hours_per_week_e']}\n"
                     f"   {x['idea']['one_liner'][:200]} | rev model: {(x['idea'].get('revenue_model') or '')[:120]}\n" +
                     "\n".join(f"   - [{'1st' if c.get('first_hand') else '2nd'} L{c.get('line')}] {c.get('claim')}" for c in cl))
    others = sorted({x['idea']['name'] for x in xs[45:]})[:80]
    return "\n".join(lines) + "\n\nOther (mention-only) records: " + "; ".join(others), len(xs)
HEAD = """You summarise evidence for ONE business model from YouTube-interview mining records (claims are speakers' claims, unaudited). Use ONLY the records below; cite video ids.
Lens: is this a PROVEN, REPEATABLE business model that an AI-agent team could copy and run? Many independent people succeeding = GOOD (do not penalise crowding).
Owner constraints: no selling to local businesses, no face/personal brand, no unlawful cold outreach (UK PECR: no cold email/SMS to individuals/sole traders), <=5 h/week owner time, any country market.
Return JSON only:
{"model":str,"label":str (short human name),
 "independent_operators": int (distinct videos where a real operator of THIS model reports their own revenue/sales, non-hypothetical),
 "revenue_examples":[{"video":id,"operator_or_product":str,"claim":str (with figure and period),"when":str (event date/year if stated, else 'as of <pub date>'),"first_hand":bool}] (max 8, strongest first),
 "startup_cost":str (range with cited video ids, or 'not stated'),
 "time_to_first_revenue":str (with cited ids, or 'not stated'),
 "repeatability":str (1-2 sentences: how many distinct people do it, how templated it is),
 "agent_automatable_pct":int (0-100, your estimate of ongoing work agents can do),
 "agent_runbook":str (1-2 sentences: what agents do; what the human must do),
 "constraint_fit":{"local_b2b":"ok|risk|fail","face":"ok|risk|fail","cold_outreach":"ok|risk|fail","hours_5":"ok|risk|fail","note":str},
 "main_risk":str,
 "proven_score":int (1-5: 5 = many independent operators with dated revenue),
 "fit_score":int (1-5 vs constraints and agent-runnability)}
"""
calls = {"codex:medium":0,"claude":0,"pi":0,"failed":0}
def ask(prompt):
    try:
        ans,_,_ = C.run_codex(prompt,"medium",timeout=1200); calls["codex:medium"]+=1; return C.parse_json_text(ans)
    except Exception as e: calls["codex:medium"]+=1; print("codex", str(e)[:150], flush=True)
    try:
        ans,_,_ = C.run_claude(prompt,timeout=1200); calls["claude"]+=1; return C.parse_json_text(ans)
    except Exception as e: calls["claude"]+=1; print("claude", str(e)[:150], flush=True)
    try:
        ans,_,_ = C.run_pi(prompt,timeout=1200); calls["pi"]+=1; return C.parse_json_text(ans)
    except Exception as e: calls["pi"]+=1; calls["failed"]+=1; print("pi", str(e)[:150], flush=True); return None
def work(m):
    p, n = packet(m); r = ask(HEAD + f"\nMODEL CODE: {m} ({n} records)\n\n" + p)
    if r: r["code"]=m; r["n_records"]=n
    print("done", m, flush=True); return m, r
import os
if os.environ.get("DRY"):
    p,n=packet(SEL[2]); print(n,len(p)); print(p[:1200]); sys.exit()
res = {}
with cf.ThreadPoolExecutor(4) as ex:
    for m, r in ex.map(work, SEL): res[m]=r
json.dump(res, open(OUT/'evidence.json','w'), indent=1)
c = json.load(open(OUT/'calls.json'))
for k,v in calls.items(): c[k]=c.get(k,0)+v
json.dump(c, open(OUT/'calls.json','w')); print(c)
