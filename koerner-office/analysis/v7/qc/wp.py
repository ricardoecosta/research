import json,urllib.request,urllib.parse,sys
terms=["gift aid","royal mail","click and drop","companies house","hmrc","uk postcode","uk vat","parcelforce","evri","uk bank holidays","charity commission","cqc rating","fca register","just giving","gocardless","direct debit uk","sage pay","opayo","worldpay","paypoint","land registry","council tax","epc certificate","rightmove","zoopla","school term dates","church","parish council","nhs","dvla"]
out=[]
for t in terms:
    q=urllib.parse.urlencode({"action":"query_plugins","request[search]":t,"request[per_page]":30,"request[fields][active_installs]":1,"request[fields][last_updated]":1})
    try:
        d=json.load(urllib.request.urlopen("https://api.wordpress.org/plugins/info/1.2/?"+q,timeout=30))
    except Exception as e:
        print(t,"ERR",e);continue
    ps=d.get("plugins",[])
    tot=d.get("info",{}).get("results")
    for p in ps:
        out.append(dict(term=t,total=tot,slug=p["slug"],name=p["name"][:60],inst=p.get("active_installs"),rating=p.get("rating"),nrat=p.get("num_ratings"),upd=p.get("last_updated","")[:10],tested=p.get("tested")))
json.dump(out,open("wp.json","w"))
import collections
for t in terms:
    rows=[r for r in out if r["term"]==t]
    if not rows: continue
    print(f"\n## {t} total={rows[0]['total']}")
    for r in sorted(rows,key=lambda r:-(r['inst'] or 0))[:6]:
        print(f"  {r['inst']:>7} {r['rating']:>3} ({r['nrat']}) upd={r['upd']} tested={r['tested']} {r['slug']}")
