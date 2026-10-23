import re,json,urllib.request,concurrent.futures as cf
slugs=sorted(set(l.strip().split('/app/')[1] for l in open('raw/xero_urls.txt') if '/app/' in l))
def get(s):
    try:
        h=urllib.request.urlopen(urllib.request.Request(f"https://apps.xero.com/uk/app/{s}",headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf8','ignore')
    except Exception as e: return dict(slug=s,err=str(e))
    def f(p):
        m=re.search(p,h); return m.group(1) if m else None
    rc=f(r'"ratingCounts":(\[[^\]]*\])')
    revdates=re.findall(r'"createdAt":"(\d{4}-\d\d-\d\d)',h)
    return dict(slug=s,name=f(r'<title>([^<]*)</title>'),rating=f(r'"rating":([\d.]+),"reviewCount"'),reviews=f(r'"reviewCount":(\d+)'),
       ratingCounts=json.loads(rc) if rc else None,listed=f(r'"listedDate":"(\d{4}-\d\d-\d\d)'),newest_review=max(revdates) if revdates else None,
       summary=f(r'"description":"([^"]{0,200})'),url=f"https://apps.xero.com/uk/app/{s}")
with cf.ThreadPoolExecutor(8) as ex: out=list(ex.map(get,slugs))
json.dump(out,open('raw/xero_apps.json','w'),indent=0)
print(len(out),sum(1 for o in out if 'err' in o))
