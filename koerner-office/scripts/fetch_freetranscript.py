#!/usr/bin/env python3
"""FreeTranscriptAPI fallback (no API key, 20 requests/hour/IP).

Reads videos_v2.csv + transcripts_v2.jsonl, fetches missing transcripts,
writes transcripts/raw/<id>.txt, updates transcripts_v2.jsonl.
Usage: python3 fetch_freetranscript.py [limit] [--include-unavailable]
"""
import csv, json, os, re, sys, time, urllib.parse, urllib.request, random
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV=os.path.join(BASE,'data','videos_v2.csv')
JSONL=os.path.join(BASE,'data','transcripts_v2.jsonl')
OUT=os.path.join(BASE,'transcripts','raw')
os.makedirs(OUT,exist_ok=True)
API='https://api.freetranscriptapi.com/v1/transcript'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36'
PRIORITY={'The Koerner Office':0,'Side Hustle Nation':1,'Starter Story':1,'UpFlip':1,'My First Million':1,'Niche Pursuits':1,'Nick Huber - Sweaty Startup':1,'Codie Sanchez':1,"Harry's Stealth Wealth":2,'David Heacock':2,'Johnny & Sergio':2,'Tim Richard':2,'Casper Capital':2,'Mikey No Code':2,'Dark Horse Entrepreneur':2,'George McConnell':2}
KW=['business','side hustle','hustle','ai','agency','client','money','profit','million','month','passive','income','rent','rental','boring','scale','sell','easy','automat','app','software','lead','local','niche']
def clean(s): return re.sub(r'\s+',' ',s.replace('\xa0',' ')).strip()
def score(title): return sum(1 for k in KW if k in title.lower())
def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 20
    include_unavail='--include-unavailable' in sys.argv
    vids={r['id']:r for r in csv.DictReader(open(CSV,encoding='utf-8'))}
    rows=[json.loads(l) for l in open(JSONL,encoding='utf-8')]
    byid={r['id']:r for r in rows}
    missing=[]
    for vid,v in vids.items():
        st=byid.get(vid,{}).get('status')
        if st in ('ok','cached','ok_freetranscriptapi'): continue
        if st=='unavailable' and not include_unavail: continue
        missing.append((PRIORITY.get(v['channel'],3), -score(v['title']), vid, v))
    missing.sort()
    todo=missing[:limit]
    print(f'{len(missing)} missing; fetching {len(todo)}')
    for n,(_,_,vid,v) in enumerate(todo,1):
        path=os.path.join(OUT,f'{vid}.txt')
        if os.path.exists(path) and os.path.getsize(path)>200:
            print('cached',vid); continue
        url=API+'?'+urllib.parse.urlencode({'video_url':vid,'format':'text','lang':'en'})
        req=urllib.request.Request(url,headers={'User-Agent':UA})
        try:
            with urllib.request.urlopen(req,timeout=90) as r:
                body=r.read().decode('utf-8','ignore')
            if not body.strip() or 'error' in body[:200].lower() and 'transcript' not in body[:200].lower():
                raise RuntimeError(body[:300])
            text=clean(body)
            with open(path,'w',encoding='utf-8') as f:
                f.write(f"# {v['title']}\n\nChannel: {v['channel']}\nVideo: https://www.youtube.com/watch?v={vid}\n\n{text}\n")
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'ok_freetranscriptapi','path':path,'chars':len(text)}
            print(f"{n}/{len(todo)} OK {v['channel']} | {v['title'][:70]} | {len(text)}")
        except Exception as e:
            msg=str(e)[:300]
            unavailable=('404' in msg or 'NOT_FOUND' in msg.upper() or 'No transcript' in msg)
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'unavailable' if unavailable else 'error_freetranscriptapi','error':msg}
            print(f"{n}/{len(todo)} {'UNAVAILABLE' if unavailable else 'ERR'} {vid} {msg[:160]}")
            if '429' in msg or 'rate' in msg.lower():
                print('Rate limited; stopping this run.'); break
        time.sleep(2.5+random.random())
    # merge and write
    allrows=list(byid.values())
    with open(JSONL,'w',encoding='utf-8') as f:
        for r in allrows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print('updated',JSONL)
if __name__=='__main__': main()
