import re,html,subprocess,json,sys,time
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
def get(u): return subprocess.run(["curl","-s","-L","-A",UA,"-H","Accept-Language: en-GB","--max-time","25",u],capture_output=True,text=True).stdout
def t(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S).replace('<',' <')).replace(' <',' ')) 
def T(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',s,flags=re.S))))
def app(h):
    a=get(f"https://apps.shopify.com/{h}"); A=T(a)
    d={'handle':h}
    m=re.search(r'Launched ([A-Z][a-z]+ \d{1,2}, \d{4})',A); d['launched']=m.group(1) if m else None
    m=re.search(r'Rating ([0-9.]+) \(([0-9,]+)\)',A); d['rating']=m.group(1) if m else None; d['reviews']=m.group(2) if m else '0'
    m=re.search(r'Developer (.{1,60}?) (?:Install|Log in)',A); d['developer']=m.group(1) if m else None
    pi=A.find('Choose the plan that best fits'); P=A[pi:pi+3000] if pi>0 else ''
    prices=[float(x.replace(',','')) for x in re.findall(r'\$\s?([0-9][0-9,]*(?:\.[0-9]+)?)\s*/\s*month',P)]
    d['lowest_paid_usd_month']=min([p for p in prices if p>0],default=None)
    d['plans_snip']=P[:400]
    # rating breakdown e.g. "1 star 70" patterns
    r=get(f"https://apps.shopify.com/{h}/reviews?ratings%5B%5D=1&ratings%5B%5D=2&sort_by=newest")
    R=T(r)
    m=re.search(r'Showing \d+[-–]\d+ of ([0-9,]+)|([0-9,]+) reviews',R)
    revs=[]
    for blk in r.split('data-review-content-id="')[1:]:
        st=re.search(r'aria-label="(\d) out of 5 stars"',blk); bt=T(re.sub(r'<svg.*?</svg>','','<x a="'+blk,flags=re.S)[:6000])
        dt=re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})',bt)
        body=re.sub(r'^.*?\d{4}\s*','',bt,count=1)[:400]
        revs.append(dict(stars=int(st.group(1)) if st else None,date=dt.group(1) if dt else None,text=body))
    d['low_reviews']=revs
    # count 1-2 star from breakdown on main reviews page
    rb=re.findall(r'of ratings are (\d) stars? ([0-9,]+)',A)
    d['breakdown']=rb[:5]
    return d
if __name__=='__main__':
    res=[]
    for h in sys.argv[1:]:
        try: res.append(app(h))
        except Exception as e: res.append({'handle':h,'error':str(e)})
        time.sleep(0.7)
    print(json.dumps(res,indent=1))
