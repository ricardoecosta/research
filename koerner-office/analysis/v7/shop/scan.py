import re,html,json,subprocess,urllib.parse,time,os
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
def get(url,frame=True):
    cmd=["curl","-s","-L","-A",UA,"-H","Accept-Language: en-GB","--max-time","25"]
    if frame: cmd+=["-H","Turbo-Frame: search_page"]
    return subprocess.run(cmd+[url],capture_output=True,text=True).stdout
def txt(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s))).strip()
out={}
for line in open('terms.txt'):
    term,kw=line.strip().split('|'); kws=kw.split(',')
    h=get("https://apps.shopify.com/search?q="+urllib.parse.quote_plus(term))
    total=re.search(r'([0-9,]+) apps',h); total=total.group(1) if total else None
    cards=[]; seen=set()
    parts=re.split(r'data-controller="app-card"',h)[1:]
    for p in parts:
        hd=re.search(r'data-app-card-handle-value="([^"]+)"',p).group(1)
        link=re.search(r'data-app-card-app-link-value="([^"]+)"',p).group(1)
        if 'search_ad' in link or hd.startswith('bif:') or hd in seen: continue
        seen.add(hd)
        name=html.unescape(re.search(r'data-app-card-name-value="([^"]*)"',p).group(1))
        body=p[:6000]
        r=re.search(r'([0-9.]+)\s*<span[^>]*>\s*out of 5',body)
        n=re.search(r'([0-9,]+) total reviews',body)
        t=txt(body)
        pr=re.search(r'total reviews\s*•\s*([^•]{0,60}?)\s{2,}|total reviews • (.{0,40})',t)
        price=None
        m=re.search(r'(Free to install|Free plan available|Free trial available|Free|\$[0-9.,]+/month|[^ ]*\d[^ ]*/month)',t)
        if m: price=m.group(1)
        desc=t
        cards.append(dict(handle=hd,name=name,rating=float(r.group(1)) if r else None,reviews=int(n.group(1).replace(',','')) if n else 0,price_card=price,desc=t[:300]))
    for c in cards:
        s=(c['name']+' '+c['desc']).lower()
        c['relevant']=any(k in s for k in kws)
    out[term]=dict(total=total,kws=kws,cards=cards)
    print(term,total,len(cards),sum(c['relevant'] for c in cards),flush=True)
    time.sleep(1)
json.dump(out,open('search.json','w'),indent=1)
