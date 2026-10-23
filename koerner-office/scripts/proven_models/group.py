"""Deterministic grouping of v8 mined records by business MODEL (not gap).
Input: analysis/v8/ideas_flat.jsonl (no re-mining). Output: analysis/proven_models/models.json"""
import json, re, statistics, collections, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows = [json.loads(l) for l in open(ROOT/'analysis/v8/ideas_flat.jsonl')]
# ordered: first match wins
MODELS = [
 ("buy_small_online_business", r"\b(acquir\w*|acquisition|bought (a|an|the) \w+ (business|app|saas|site|website|newsletter|channel)|buy(ing)? (a|an|existing) (small )?(online |digital )?(business|app|saas|site|website)|flippa|acquire\.com|microacquire|empire flippers)"),
 ("kdp_low_content_books", r"\b(kdp|kindle direct|low[- ]content|colou?ring books?|activity books?|puzzle books?|amazon books?|self[- ]publish\w*|audiobook)"),
 ("print_on_demand", r"(print[- ]on[- ]demand|\bpod\b|printful|printify|merch by amazon|redbubble|teepublic|spring\b.*merch|gelato)"),
 ("etsy_digital_printables", r"(printables?|etsy digital|digital downloads?|svg|clip ?art|digital planners?|wall art download)"),
 ("faceless_video_channels", r"(faceless|youtube automation|cash ?cow|ai[- ]generated (video|channel)|ai video channel|shorts channel|tiktok (page|account|channel)|compilation channel|dub\w* (your|youtube)|ai music channel|slideshow)"),
 ("newsletter_media", r"(newsletter|substack|beehiiv|email list business)"),
 ("programmatic_seo_directory", r"(director(y|ies)|programmatic|listing site|aggregator site|database site|marketplace of listings)"),
 ("free_tool_calculator_sites", r"(calculator|converter|generator site|free (online )?tool|utility site|tool site)"),
 ("niche_content_affiliate_sites", r"(niche (site|website|content)|blog\b|blogging|affiliate (site|website|content|marketing)|content site|seo (site|content)|adsense|display ads|mediavine|raptive|ezoic|review site|authority site)"),
 ("digital_templates_info_products", r"(templates?|notion|canva|spreadsheet|prompt (pack|library)|presets?|e-?books?|digital products?|guide\b|swipe file|gpts?\b|skill stack|lightroom)"),
 ("mobile_apps_consumer", r"(ios|android|mobile app|app store|in-app|iphone app|\bgame\b|games\b)"),
 ("api_scraper_wrappers", r"(apify|actor\b|api wrapper|wrapper|scrap(er|ing))"),
 ("b2b_data_products", r"(data(set)?s?\b|lead lists?|leads database|intelligence|reports?\b|alerts?\b|tracker)"),
 ("chrome_ext_plugins_shopify_apps", r"(chrome extension|browser extension|plugin|shopify app|wordpress|add-on|integration)"),
 ("micro_saas", r"(saas|software|subscription app|web app|\bapp\b|platform|tool\b|ai tool|chatbot product)"),
 ("ecom_dropship_private_label", r"(dropship\w*|amazon fba|\bfba\b|private label|shopify store|e-?commerce brand|online store|tiktok shop)"),
 ("stock_media_ai_art", r"(stock (photo|footage|music|images)|midjourney|ai art|wallpapers?|music licensing)"),
 ("freelance_productised_service", r"(fiverr|upwork|freelanc\w*|productized|productised|virtual assistant|voiceover|copywriting|ghostwrit)"),
 ("ai_automation_agency", r"(agency|done[- ]for[- ]you|automation (service|consult)|ai consult|retainer|implementation)"),
 ("courses_coaching_community", r"(course|coaching|cohort|community|membership|mastermind|tutor|bootcamp|academy|workshop)"),
 ("podcast_youtube_personal_brand", r"(podcast|youtube channel|influencer|ugc|personal brand|creator)"),
 ("domain_website_flipping", r"(domain|flip(ping)? (websites|sites)|website flipping)"),
]
CAT_FALLBACK = {"arbitrage_reselling":"ecom_dtc_dropship_resale","home_service":"local_or_physical_service","local_service":"local_or_physical_service","events_experiences":"local_or_physical_service",
 "rental_asset":"rental_assets","real_estate":"real_estate","vending_machines_kiosks":"vending_kiosks","franchise":"franchise","manufacturing":"physical_products_manufacturing",
 "ecommerce_physical":"ecom_dtc_dropship_resale","job_career":"job_career","acquisition_buy_business":"buy_small_online_business"}
PHYS_CATS = {"home_service","local_service","events_experiences","rental_asset","real_estate","vending_machines_kiosks","franchise","manufacturing"}
def text(x):
    i = x['idea']; return " ".join(str(i.get(k) or '') for k in ('name','one_liner','offer','revenue_model')).lower()
LABELS = {}
_lp = ROOT/'analysis/proven_models/labels.json'
if _lp.exists() and '--regex' not in sys.argv: LABELS = json.load(open(_lp))
CODE = {"SAAS":"micro_saas","APP":"consumer_mobile_apps_games","PLUG":"plugins_extensions_marketplace_apps","API":"api_scraper_wrappers","DATA":"b2b_data_products",
 "SEO":"niche_content_affiliate_sites","DIR":"niche_programmatic_directories","TOOL":"free_tool_calculator_sites","NEWS":"newsletters","FACELESS":"faceless_social_video_pages",
 "DIGI":"digital_templates_info_products","KDP":"kdp_self_publishing","POD":"print_on_demand_personalised","ECOM":"ecom_dtc_dropship_resale","BUY":"buy_small_online_business",
 "MKT":"two_sided_marketplaces","LEADGEN":"rank_and_rent_local_leadgen","AGENCY":"ai_automation_agency_services","FREEL":"freelance_productised_service",
 "EDU":"courses_coaching_community","BRAND":"personal_brand_media","LOCAL":"local_or_physical_service","NONE":"not_a_business_model"}
RXMAP = {"print_on_demand":"print_on_demand_personalised","kdp_low_content_books":"kdp_self_publishing","faceless_video_channels":"faceless_social_video_pages",
 "newsletter_media":"newsletters","mobile_apps_consumer":"consumer_mobile_apps_games","ai_automation_agency":"ai_automation_agency_services",
 "podcast_youtube_personal_brand":"personal_brand_media","chrome_ext_plugins_shopify_apps":"plugins_extensions_marketplace_apps",
 "ecom_dropship_private_label":"ecom_dtc_dropship_resale","programmatic_seo_directory":"niche_programmatic_directories","etsy_digital_printables":"digital_templates_info_products"}
def model_of(x):
    if x['key'] in LABELS: return CODE[LABELS[x['key']]]
    m = model_of_rx(x); return RXMAP.get(m, m)
def model_of_rx(x):
    cat = x['idea']['category']
    if cat in PHYS_CATS or (x['physical_world'] and cat not in ('ecommerce_physical',)):
        return CAT_FALLBACK.get(cat, "physical_other")
    t = text(x)
    for m, rx in MODELS:
        if re.search(rx, t): return m
    return CAT_FALLBACK.get(cat, "unmatched_"+cat)
MONEY = re.compile(r"(?:\$|£|€|usd ?)\s?(\d[\d,]*(?:\.\d+)?)\s?(k|m|million|thousand|grand)?\b|(\d[\d,]*(?:\.\d+)?)\s?(k|million|thousand|grand)\b", re.I)
def amounts(s):
    out=[]
    for m in MONEY.finditer(s):
        n = m.group(1) or m.group(3); suf=(m.group(2) or m.group(4) or '').lower()
        try: v=float(n.replace(',',''))
        except: continue
        v*= {'k':1e3,'thousand':1e3,'grand':1e3,'m':1e6,'million':1e6}.get(suf,1)
        out.append(v)
    return out
REV = re.compile(r"(revenue|\bmrr\b|\barr\b|\bmade\b|making|earn|profit|sales|\bsold\b|income|brings? in|generat|run rate|payout)", re.I)
NOTREV = re.compile(r"(spen[dt]|\bcosts?\b|pric(e|ed|ing)|charg|budget|\bfees?\b|salary|valuation|raised|funding|visits|downloads|users|subscribers)", re.I)
def per_month(s):
    a = amounts(s); 
    if not a: return None
    v = max(a); s=s.lower()
    if re.search(r"(a|per|/) ?(month|mo)\b|mrr|monthly", s): return v
    if re.search(r"(a|per|/) ?(year|yr)\b|arr|annual|annually", s): return v/12
    if re.search(r"(a|per|/) ?(day)\b|daily", s): return v*30
    if re.search(r"(a|per|/) ?week|weekly", s): return v*4.3
    return None
COST = re.compile(r"(start(ed|ing)? (with|for|on)|startup cost|start-up|spent|invest(ed)?|cost (me|us|about|around|just)|upfront|initial|launch(ed)? (with|for)|budget|credit card)", re.I)
FIRST = re.compile(r"(first (sale|client|customer|dollar|month|paying|order|subscriber|payment)|within (a |the )?(\d+|first|few|couple|one|two|three|four|six) (days?|weeks?|months?)|after (\d+|a few|two|three|six) (days?|weeks?|months?))", re.I)
YEAR = re.compile(r"\b(20[12]\d)\b")
groups = collections.defaultdict(list)
for x in rows:
    groups[model_of(x)].append(x)
res = {}
for m, xs in groups.items():
    vids = {x['video_id'] for x in xs}; chans = {x['channel'] for x in xs}
    rev=[]; cost=[]; first=[]
    for x in xs:
        for c in x.get('claims') or []:
            s = (c.get('claim') or '')+' || '+(c.get('quote') or '')
            hyp = c.get('hypothetical'); fh = c.get('first_hand')
            base = dict(vid=x['video_id'], ch=x['channel'], pub=x['publish_date'], idea=x['idea']['name'], claim=c.get('claim'), quote=c.get('quote'), line=c.get('line'), years=sorted(set(YEAR.findall(s))))
            if not hyp and REV.search(s) and not NOTREV.search(c.get('claim') or '') and amounts(s):
                pm = per_month(s); rev.append({**base, 'per_month':pm, 'first_hand':bool(fh)})
            if not hyp and COST.search(s) and amounts(s): cost.append(base)
            if not hyp and FIRST.search(s): first.append(base)
    rev_vids = {r['vid'] for r in rev}; fh_vids = {r['vid'] for r in rev if r['first_hand']}
    pm_by_vid = {}
    for r in rev:
        if r['per_month']: pm_by_vid[r['vid']] = max(pm_by_vid.get(r['vid'],0), r['per_month'])
    med = lambda k: statistics.median([x[k] for x in xs if isinstance(x.get(k),(int,float))] or [0])
    frac = lambda f: round(sum(1 for x in xs if f(x))/len(xs),2)
    res[m] = dict(model=m, n_records=len(xs), n_deep=sum(1 for x in xs if x['depth']!='mention'), n_videos=len(vids), n_channels=len(chans),
        n_videos_revenue=len(rev_vids), n_videos_firsthand_revenue=len(fh_vids), n_deep_videos=len({x['video_id'] for x in xs if x['depth']!='mention'}), n_videos_monthly_figure=len(pm_by_vid),
        monthly_claims_sorted=sorted(pm_by_vid.values(), reverse=True)[:15],
        median_monthly_claim=statistics.median(pm_by_vid.values()) if pm_by_vid else None,
        pub_range=[min(x['publish_date'] for x in xs), max(x['publish_date'] for x in xs)],
        automation_med=med('automation_share_e'), hours_med=med('hours_per_week_e'),
        local=frac(lambda x:x['sells_to_local_businesses']), face=frac(lambda x:x['needs_face_or_personal_brand']),
        uk_legal=frac(lambda x:(x.get('uk_legal_risk') or {}).get('flag')), physical=frac(lambda x:x['physical_world']),
        channels=collections.Counter(x['channel'] for x in xs).most_common(8),
        top_ideas=collections.Counter(x['idea']['name'] for x in xs).most_common(12),
        rev_claims=sorted(rev, key=lambda r:-(r['per_month'] or 0))[:25], cost_claims=cost[:20], first_claims=first[:20],
        record_ids=[x['record_id'] for x in xs])
out = ROOT/'analysis/proven_models/models.json'
json.dump(res, open(out,'w'), indent=1)
for m,r in sorted(res.items(), key=lambda kv:-kv[1]['n_videos_firsthand_revenue']):
    print(f"{m:34} rec{r['n_records']:5} vid{r['n_videos']:4} deepV{r['n_deep_videos']:4} anyRevV{r['n_videos_revenue']:4} ch{r['n_channels']:3} revV{r['n_videos_firsthand_revenue']:4} pmV{r['n_videos_monthly_figure']:4} med${(r['median_monthly_claim'] or 0):>9.0f} auto{r['automation_med']:4} h{r['hours_med']:4} loc{r['local']:.2f} face{r['face']:.2f} uk{r['uk_legal']:.2f} phys{r['physical']:.2f}")
