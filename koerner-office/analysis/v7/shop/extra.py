import re,html,subprocess,urllib.parse,json,sys
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
Q={'windsor framework':r'windsor|northern ireland|\bni\b','northern ireland shipping':r'northern ireland|windsor','click & drop sync':r'click (&|and) drop|royal ?mail','royal mail international customs':r'royal ?mail|click (&|and) drop','freeagent sync':r'freeagent','making tax digital':r'making tax digital|\bmtd\b|hmrc','uk pepr packaging':r'\bepr\b|packaging (data|report|waste)|producer resp'}
out={}
for q,p in Q.items():
    h=subprocess.run(["curl","-s","-A",UA,"-H","Turbo-Frame: search_page","https://apps.shopify.com/search?q="+urllib.parse.quote_plus(q)],capture_output=True,text=True).stdout
    tot=re.search(r'([0-9,]+) apps',h); res=[]
    for part in h.split('data-controller="app-card"')[1:]:
        hd=re.search(r'handle-value="([^"]+)"',part).group(1); link=re.search(r'app-link-value="([^"]+)"',part).group(1)
        if 'search_ad' in link or hd.startswith('bif:'): continue
        nm=html.unescape(re.search(r'name-value="([^"]*)"',part).group(1))
        tx=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',part[:6000])))
        r=re.search(r'([0-9.]+) out of 5',tx); n=re.search(r'([0-9,]+) total reviews',tx)
        if re.search(p,(nm+' '+tx).lower()): res.append((hd,nm,r.group(1) if r else None,n.group(1) if n else '0'))
    res=list(dict.fromkeys(res)); out[q]=dict(total=tot.group(1) if tot else None,rel=res)
    print(q,tot.group(1) if tot else None,len(res),'|','; '.join(f"{a} {c}/{d}" for a,b,c,d in res[:10]))
json.dump(out,open('extra.json','w'),indent=1)
