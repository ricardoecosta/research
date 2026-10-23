import json,csv,datetime
S=json.load(open('search.json')); A={d['handle']:d for f in ['apps.json','apps2.json','apps3.json'] for d in json.load(open(f))}
L=json.load(open('lowrevs.json')); X=json.load(open('extra.json'))
cut=datetime.date(2026,4,23)
def ld(h):
    s=A.get(h,{}).get('launched'); return datetime.datetime.strptime(s,'%B %d, %Y').date() if s else None
V={ # term: (verdict, reason, extra relevant handles from other searches)
'royal mail':('FAIL (near miss)','Leader Click & Drop (official) 1.6/89 and 46 of 75 low reviews say orders stop syncing, but 4 new rivals launched 17 Sep-19 Oct 2026 (limit is 1) and Shopify sells Royal Mail labels natively since Aug 2025',['cleatly-click-and-drop-sync','postbag','makepost','shipping-king']),
'evri':('FAIL','Leader Evri (Parcel2Go) is 1.0 but has only 13 reviews (need 30); Shopify sells Evri labels natively',[]),
'dpd uk':('FAIL','Leader WebShopAssist 4.9/113',[]),
'parcelforce':('FAIL','One app, 0 reviews: no demand signal',[]),
'yodel':('FAIL','One app, 1 review: no demand signal',[]),
'inpost uk lockers':('FAIL','Official InPost UK app 1.0/1; Polish apps strong; Shopify sells InPost UK labels natively',[]),
'uk vat invoice':('FAIL','Leaders 4.9-5.0',[]),
'hmrc mtd':('FAIL','No relevant apps; MTD filing lives in accounting software, not Shopify',[]),
'uk vat ioss':('FAIL','13 relevant apps, leaders 4.9-5.0',[]),
'eori customs':('FAIL','No reviewed incumbent; 2 new apps with 0 reviews (EORI Checker Jan 2026, Origo Jun 2026): no paid demand shown',['eori-checker','origo-eu-uk-customs-invoice']),
'cn22 customs declaration':('FAIL','No relevant app on this term; CN22/CN23 is bundled in shipping apps',[]),
'uk eu shipping brexit':('FAIL','No relevant app on this term',[]),
'ddp duties uk':('FAIL','Leader iGlobal 4.4/159; the weak app (Crossborderit 1.4) has only 16 reviews',[]),
'xero':('FAIL','Crowded: 17 relevant apps; Bold Xero Sync 2.5/153 is weak but A2X 4.9/360 and Xero Bridge 4.9/309 lead',[]),
'sage accounting':('FAIL (watch)','Only 2 relevant apps; Combidesk Sage 4.2/10 with 6 x 1-star, but too few reviews to prove demand',[]),
'freeagent':('FAIL by rule (notable)','No incumbent with 30+ reviews. FreeAgent shut its own Shopify integration on 30 Apr 2025. The only app in the store is Equali (launched 3 Apr 2026, $23/mo, 1.0/1)',['equali']),
'quickbooks uk':('FAIL','Crowded: 16 relevant apps, leaders 4.6-4.9 with 500-3,349 reviews',[]),
'b2b wholesale trade pricing':('FAIL','Crowded: 24/24 relevant apps, leaders 4.7-4.9 with 700-1,300 reviews',[]),
'trade account approval':('FAIL','Few apps, but leaders 5.0 and no complaint volume',['b2b-portal-1','tradeaccount-checkout']),
'net 30 payment terms':('FAIL','2 apps with 0 reviews: no demand signal',[]),
'companies house':('FAIL','No relevant apps: unproven demand',[]),
'business credit check':('FAIL','Leader Monk Commerce 5.0/23',[]),
'vat number validation':('FAIL','Leader tax-exemption 4.9/47',[]),
'gift aid':('FAIL','No relevant apps: unproven demand',[]),
'charity donation uk':('FAIL','Leaders 4.2-5.0 with many reviews',[]),
'uk returns portal':('FAIL','Crowded: leaders 4.6-4.9 with 400-1,542 reviews',[]),
'royal mail returns label':('FAIL','No relevant app on this term',[]),
'uk postcode address lookup':('FAIL','Leaders 4.7-4.9 with 116-236 reviews',[]),
'ukca weee compliance':('FAIL','No reviewed incumbent; only new 0-review apps',[]),
'extended producer responsibility packaging':('FAIL','EAS 3.9/76 (above the 3.8 limit); at least 3 new EPR apps since Jun 2026',['eas-eu-compliance','epr-pack-report','packpilot-epr','packaging-epr','epr-insights']),
'gpsr product safety':('FAIL','10 relevant apps, mostly new with 0 reviews (EU rule, crowded fast)',[]),
'age verification uk':('FAIL','Crowded: 20 relevant apps, leaders 4.6-4.9',[]),
'klarna clearpay uk':('FAIL','Klarna official 2.4/113 (32 low reviews about support), but only Klarna can fix its own account flow; no paid third-party tier found',[]),
'gocardless direct debit':('FAIL','No relevant apps: unproven demand',[]),
'amazon uk sync':('FAIL','Crowded: leaders 4.6-4.9 with 350-1,167 reviews',[]),
'ebay uk sync':('FAIL','Crowded: leaders 4.7-4.9 with 270-1,275 reviews',[]),
'onbuy marketplace':('FAIL','CedCommerce 4.6/78; New craft OnBuy Sync launched Jun 2026',['onbuy-sync']),
'tiktok shop uk':('FAIL','Crowded: leaders 4.6-4.9',[]),
'subscription cancellation notice dmcc':('FAIL','Crowded subscription category, leaders 4.8-5.0 with thousands of reviews',[]),
'trustpilot reviews uk':('FAIL (near miss)','Official Trustpilot app 3.4/35, 3 relevant apps, 0 launches in 6 months, cheaper rivals at $8.99-9.99. Fails because there are only 13 low reviews (need 10 on one theme) and they are scattered',[]),
}
TH={'click-drop-app':'orders stop syncing or importing: 46/75; support slow or absent: 19/75; tracking not written back: 7/75',
'xero-sync':'price or billing: 46/91; support: 36/91; sync failures: 25/91','klarna-on-site-messaging':'support: 32/61; not working: 20/61',
'trustpilot':'13 low reviews, no theme reaches 10 (blank screen or install ~4, language ~3, price ~2)','evri':'13 low reviews: sync 5, price 4',
'duty-calculator':'price 11/15, tax wrong 6/15','sage-business-cloud-accounting':'6 low reviews: support 3, not working 3','onbuy-integration':'8 low reviews, mixed'}
rows=[]
for t,v in S.items():
    rel=[c for c in v['cards'] if c['relevant']]; hs=[c['handle'] for c in rel]+[h for h in V[t][2] if h not in [c['handle'] for c in rel]]
    top=sorted(rel,key=lambda c:-c['reviews'])[:4]
    lead=top[0] if top else None
    weak=[c for c in rel if c['rating'] and c['rating']<=3.8 and c['reviews']>=30]
    known=[h for h in hs if ld(h)]; l6=[h for h in known if ld(h)>=cut]
    paid=[A[h]['lowest_paid_usd_month'] for h in hs if h in A and A[h].get('lowest_paid_usd_month')]
    weakh=weak[0]['handle'] if weak else (lead['handle'] if lead else '')
    rows.append(dict(term=t,search_results_total=v['total'],relevant_apps_page1=len(rel),relevant_incl_other_searches=len(hs),
      top_apps='; '.join(f"{c['handle']} {c['rating']}/{c['reviews']}" for c in top),
      weak_incumbent_le3_8_ge30rev='; '.join(f"{c['handle']} {c['rating']}/{c['reviews']}" for c in weak) or 'none',
      launches_last_6mo=(f"{len(l6)} of {len(known)} dated ("+', '.join(f'{h} {A[h]["launched"]}' for h in l6)+')') if known else 'not checked (failed an earlier rule)',
      lowest_paid_usd_month=min(paid) if paid else ('n/a' if not known else 'none found'),
      low_review_themes=TH.get(weakh,'not clustered (no weak incumbent)'),
      last_update='not shown on the Shopify App Store; see the newest low-review date in the summary',
      verdict=V[t][0],reason=V[t][1]))
for q,v in X.items():
    if q in('windsor framework','freeagent sync'): continue
    rows.append(dict(term=q+' (extra)',search_results_total=v['total'],relevant_apps_page1=len(v['rel']),relevant_incl_other_searches=len(v['rel']),
      top_apps='; '.join(f"{a} {c}/{d}" for a,b,c,d in v['rel'][:5]),weak_incumbent_le3_8_ge30rev='see related term',launches_last_6mo='see related term',
      lowest_paid_usd_month='',low_review_themes='',last_update='not shown',verdict='supporting search',reason='Cross-check for related term'))
with open('/workspace/v7work/shopify_gap_scan.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows))
for r in rows[:3]: print(r)
