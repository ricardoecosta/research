import re,html,subprocess,urllib.parse,json
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
Q={'hmrc':r'hmrc|mtd|making tax','eori':r'eori','cn23':r'cn2[23]|customs','customs declaration':r'customs','companies house':r'companies house','gift aid':r'gift ?aid','gocardless':r'gocardless|direct debit','freeagent':r'freeagent','weee':r'weee','epr packaging':r'\bepr\b|producer resp|packaging (fee|data|report)','vies vat':r'\bvies\b|vat (number|id)|vat valid','click and drop':r'click (&|and) drop|royal ?mail','postcode lookup':r'postcode','b2b trade account':r'trade account|b2b','net terms':r'net ?terms|net ?30|payment terms','vat reverse charge':r'reverse charge|vat (number|id)|vat exempt','royal mail tracking':r'royal ?mail','dpd':r'\bdpd\b','evri':r'evri'}
out={}
for q,p in Q.items():
    h=subprocess.run(["curl","-s","-A",UA,"-H","Turbo-Frame: search_page","https://apps.shopify.com/search?q="+urllib.parse.quote_plus(q)],capture_output=True,text=True).stdout
    res=[]
    for part in h.split('data-controller="app-card"')[1:]:
        hd=re.search(r'handle-value="([^"]+)"',part).group(1); link=re.search(r'app-link-value="([^"]+)"',part).group(1)
        if 'search_ad' in link or hd.startswith('bif:'): continue
        nm=html.unescape(re.search(r'name-value="([^"]*)"',part).group(1))
        tx=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',part[:6000])))
        r=re.search(r'([0-9.]+) out of 5',tx); n=re.search(r'([0-9,]+) total reviews',tx)
        if re.search(p,(nm+' '+tx).lower()): res.append((hd,nm,r.group(1) if r else None,n.group(1) if n else '0'))
    res=list(dict.fromkeys(res)); out[q]=res
    print(q,len(res),'|','; '.join(f"{a} {c}/{d}" for a,b,c,d in res[:8]))
json.dump(out,open('alt.json','w'),indent=1)
