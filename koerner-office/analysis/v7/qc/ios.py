import json,urllib.request,urllib.parse,time,datetime
terms=["bin collection","council tax","mot reminder","allotment","tide times uk","mileage hmrc","premium bonds","isa allowance","probate","lasting power of attorney","planning applications uk","ulez","dartford crossing","delay repay","boiler service reminder","hmo landlord","gas safety certificate","self assessment tax uk","tax free childcare","student loan repayment uk","narrowboat","canal","caravan club","parkrun","foraging uk","bird song uk","prescription reminder nhs","school term dates uk","council planning","electoral register","companies house","find a tender","cqc","ofsted","food hygiene rating","fishing licence","right to rent","pension tracker uk","inheritance tax","stamp duty","conveyancing","house move checklist","epc rating","solar panels uk","heat pump","energy bills uk","octopus agile","smart meter readings","water meter","car tax check","parking fine appeal","pcn appeal","small claims court","tenancy deposit","jury service"]
now=datetime.datetime(2026,10,23)
res={}
for t in terms:
    q=urllib.parse.urlencode({"term":t,"country":"gb","entity":"software","limit":25})
    try: d=json.load(urllib.request.urlopen("https://itunes.apple.com/search?"+q,timeout=30))
    except Exception as e: print(t,"ERR",e); time.sleep(3); continue
    rows=[]
    for a in d["results"]:
        rel=a.get("currentVersionReleaseDate","")[:10]
        age=(now-datetime.datetime.fromisoformat(rel)).days if rel else None
        rows.append(dict(n=a["trackName"][:45],r=round(a.get("averageUserRating",0),1),c=a.get("userRatingCount",0),upd=rel,age=age,p=a.get("formattedPrice"),id=a["trackId"]))
    res[t]=rows
    top=sorted(rows,key=lambda r:-r["c"])[:5]
    stale=sum(1 for r in rows if r["age"] and r["age"]>730)
    print(f"\n## {t}: n={len(rows)} stale>2y={stale} sumRatings={sum(r['c'] for r in rows)}")
    for r in top: print(f"  {r['c']:>6} {r['r']} upd={r['upd']} {r['p']} {r['n']}")
    time.sleep(1.5)
json.dump(res,open("ios.json","w"))
