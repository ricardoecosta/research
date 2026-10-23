import re,json,urllib.request,urllib.parse,concurrent.futures as cf
terms=["premium bonds","octopus agile","octopus energy tracker","bin collection","tide times uk","food hygiene rating","mot check","council tax","delay repay","heat pump","ev charging uk","parking ticket appeal","national rail","uk tax calculator","self assessment","vat calculator uk","companies house","receipt scanner uk","mileage tracker hmrc","landlord","nhs prescription","dvla","solar panel monitoring","smart meter","isa tracker","cash isa","savings rates uk","fuel prices uk","tv licence","postcode lookup"]
H={'User-Agent':'Mozilla/5.0'}
def fetch(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read().decode('utf8','ignore')
def det(i):
    try: h=fetch(f"https://play.google.com/store/apps/details?id={i}&gl=GB&hl=en_GB")
    except Exception as e: return dict(id=i,err=str(e))
    f=lambda p:(re.search(p,h) or [None,None])[1]
    return dict(id=i,title=f(r'og:title" content="([^"]*?) – Apps'),rating=f(r'Rated ([0-9.]+) stars'),reviews=f(r'>([0-9.,KM]+) reviews<'),
      downloads=f(r'<div class="ClM7O">([^<]*)</div><div class="g1rdde">Downloads'),updated=f(r'Updated on</div><div class="xg1aie">([^<]*)'),url=f"https://play.google.com/store/apps/details?id={i}")
out={}
for t in terms:
    h=fetch(f"https://play.google.com/store/search?q={urllib.parse.quote(t)}&c=apps&gl=GB&hl=en_GB")
    ids=list(dict.fromkeys(re.findall(r'details\?id=([a-zA-Z0-9._]+)',h)))[:10]
    with cf.ThreadPoolExecutor(8) as ex: out[t]=list(ex.map(det,ids))
    print(t,len(ids),flush=True)
json.dump(out,open('raw/gplay.json','w'),indent=0)
