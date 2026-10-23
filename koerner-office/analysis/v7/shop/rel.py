import json,re
d=json.load(open('search.json'))
K={'royal mail':r'royal ?mail|click (&|and) drop','evri':r'\bevri\b|hermes','dpd uk':r'\bdpd\b','parcelforce':r'parcelforce','yodel':r'\byodel\b',
'inpost uk lockers':r'\binpost\b','uk vat invoice':r'\bvat\b','hmrc mtd':r'\bhmrc\b|\bmtd\b|making tax digital','uk vat ioss':r'\bioss\b|\bvat\b',
'eori customs':r'\beori\b|customs','cn22 customs declaration':r'\bcn2[23]\b|customs','uk eu shipping brexit':r'brexit|customs|\bioss\b|\bddp\b',
'ddp duties uk':r'\bddp\b|dut(y|ies)','xero':r'\bxero\b','sage accounting':r'\bsage\b','freeagent':r'freeagent|free agent','quickbooks uk':r'quickbooks',
'b2b wholesale trade pricing':r'wholesale|\bb2b\b','trade account approval':r'\bb2b\b|wholesale|trade account','net 30 payment terms':r'net ?30|net terms|payment terms|b2b credit',
'companies house':r'companies house','business credit check':r'credit check|credit limit|b2b credit','vat number validation':r'vat (number|id)|vat validat|\bvies\b',
'gift aid':r'gift ?aid','charity donation uk':r'donat|charit','uk returns portal':r'\breturns?\b','royal mail returns label':r'royal ?mail|click (&|and) drop',
'uk postcode address lookup':r'postcode|address (lookup|valid|autocomplete)','ukca weee compliance':r'\bweee\b|\bukca\b','extended producer responsibility packaging':r'\bepr\b|producer responsibility|packaging',
'gpsr product safety':r'\bgpsr\b','age verification uk':r'age (verif|gate|check)','klarna clearpay uk':r'klarna|clearpay','gocardless direct debit':r'gocardless|direct debit',
'amazon uk sync':r'\bamazon\b','ebay uk sync':r'\bebay\b','onbuy marketplace':r'\bonbuy\b','tiktok shop uk':r'tiktok shop','subscription cancellation notice dmcc':r'subscription','trustpilot reviews uk':r'trustpilot'}
for t,v in d.items():
    for c in v['cards']: c['relevant']=bool(re.search(K[t],(c['name']+' '+c['desc']).lower()))
    rel=[c for c in v['cards'] if c['relevant']]
    v['pattern']=K[t]
    print(f"{t:45s} rel={len(rel):2d}/{len(v['cards'])}  ", '; '.join(f"{c['handle']} {c['rating']}/{c['reviews']}" for c in sorted(rel,key=lambda c:-c['reviews'])[:5]))
json.dump(d,open('search.json','w'),indent=1)
