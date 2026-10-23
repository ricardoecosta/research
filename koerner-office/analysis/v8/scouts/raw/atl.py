import json,urllib.request,sys
out=[];off=0
while True:
    u=f"https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&withVersion=true&limit=50&offset={off}"
    try: d=json.load(urllib.request.urlopen(u,timeout=30))
    except Exception as e: print("err",off,e); break
    a=d["_embedded"]["addons"]
    if not a: break
    for x in a:
        e=x.get("_embedded",{})
        out.append(dict(key=x.get("key"),name=x.get("name"),summary=x.get("summary") or x.get("tagLine"),
          url="https://marketplace.atlassian.com"+x["_links"]["alternate"]["href"],
          installs=e.get("distribution",{}).get("totalInstalls"),
          stars=e.get("reviews",{}).get("averageStars"),reviews=e.get("reviews",{}).get("count"),
          release=(e.get("version") or {}).get("release",{}).get("date"),
          cats=[c["name"] for c in e.get("categories",[])],vendor=x.get("vendor",{}) and None))
    off+=50
    if off%1000==0: print(off,flush=True)
json.dump(out,open("raw/atlassian_cloud.json","w"))
print("total",len(out))
