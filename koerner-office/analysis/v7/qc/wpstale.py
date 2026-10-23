import json,urllib.request,urllib.parse,datetime
now=datetime.date(2026,10,23); out=[]
for page in range(1,26):
    q=urllib.parse.urlencode({"action":"query_plugins","request[browse]":"popular","request[per_page]":100,"request[page]":page,"request[fields][active_installs]":1,"request[fields][last_updated]":1,"request[fields][short_description]":0,"request[fields][description]":0,"request[fields][sections]":0})
    d=json.load(urllib.request.urlopen("https://api.wordpress.org/plugins/info/1.2/?"+q,timeout=60))
    for p in d["plugins"]:
        u=p.get("last_updated","")[:10]
        if not u: continue
        age=(now-datetime.date.fromisoformat(u)).days
        out.append(dict(slug=p["slug"],name=p["name"][:55],inst=p["active_installs"],rating=p["rating"],nrat=p["num_ratings"],upd=u,age=age,tested=p.get("tested"),support=p.get("support_threads"),resolved=p.get("support_threads_resolved")))
json.dump(out,open("wpstale.json","w"))
st=[r for r in out if r["age"]>730 and r["inst"]>=20000]
print(len(out),"scanned;",len(st),"stale>2y with >=20k installs")
for r in sorted(st,key=lambda r:-r["inst"])[:45]:
    print(f'{r["inst"]:>8} {r["rating"]:>3}({r["nrat"]}) upd={r["upd"]} tested={r["tested"]} sup={r["support"]}/{r["resolved"]} {r["slug"]}')
