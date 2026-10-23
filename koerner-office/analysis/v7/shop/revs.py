import re,html,subprocess,json,sys
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/128 Safari/537.36"
def get(u): return subprocess.run(["curl","-s","-L","-A",UA,"--max-time","25",u],capture_output=True,text=True).stdout
def T(s): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',s,flags=re.S))))
out={}
for arg in sys.argv[1:]:
    h,pages=arg.split(':'); rs=[]
    for p in range(1,int(pages)+1):
        r=get(f"https://apps.shopify.com/{h}/reviews?ratings%5B%5D=1&ratings%5B%5D=2&sort_by=newest&page={p}")
        blks=r.split('data-review-content-id="')[1:]
        if not blks: break
        for blk in blks:
            st=re.search(r'aria-label="(\d) out of 5 stars"',blk); bt=T(re.sub(r'<svg.*?</svg>','','<x a="'+blk,flags=re.S)[:8000])
            dt=re.search(r'([A-Z][a-z]+ \d{1,2}, \d{4})',bt)
            body=re.sub(r'^.*?\d{4}\s*','',bt,count=1)
            body=re.split(r' Show more | replied ',body)[0][:600]
            rs.append(dict(stars=int(st.group(1)) if st else None,date=dt.group(1) if dt else None,text=body))
    out[h]=rs; print(h,len(rs),file=sys.stderr)
json.dump(out,open('lowrevs.json','w'),indent=1)
