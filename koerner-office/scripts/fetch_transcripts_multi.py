#!/usr/bin/env python3
"""Multi-provider transcript fetcher for missing videos.

Providers:
1. transcribeyoutube.com (free, keyless: 5/min, 30/hour, 100/day)
2. FreeTranscriptAPI (free, keyless: 20/hour)
3. youtube-transcript-api direct (often IP-blocked)

Usage: python3 fetch_transcripts_multi.py [limit]
"""
import csv, json, os, re, sys, time, urllib.parse, urllib.request, random
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV=os.path.join(BASE,'data','videos_v2.csv')
JSONL=os.path.join(BASE,'data','transcripts_v2.jsonl')
OUT=os.path.join(BASE,'transcripts','raw')
os.makedirs(OUT,exist_ok=True)
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36'
PRIORITY={'The Koerner Office':0,'Side Hustle Nation':1,'Starter Story':1,'UpFlip':1,'My First Million':1,'Niche Pursuits':1,'Nick Huber - Sweaty Startup':1,'Codie Sanchez':1,"Harry's Stealth Wealth":2,'David Heacock':2,'Johnny & Sergio':2,'Tim Richard':2,'Casper Capital':2,'Mikey No Code':2,'Dark Horse Entrepreneur':2,'George McConnell':2}
KW=['business','side hustle','hustle','ai','agency','client','money','profit','million','month','passive','income','rent','rental','boring','scale','sell','easy','automat','app','software','lead','local','niche']
def clean(s): return re.sub(r'\s+',' ',s.replace('\xa0',' ')).strip()
def score(t): return sum(1 for k in KW if k in t.lower())

def transcribeyoutube(vid):
    data=json.dumps({'url':f'https://www.youtube.com/watch?v={vid}','lang':'en'}).encode()
    req=urllib.request.Request('https://transcribeyoutube.com/api/transcript',data=data,headers={'Content-Type':'application/json','User-Agent':UA})
    with urllib.request.urlopen(req,timeout=90) as r:
        d=json.loads(r.read().decode('utf-8','ignore'))
    if not d.get('ok'): raise RuntimeError(f"{d.get('error')}: {d.get('message')}")
    return clean(' '.join(x.get('text','') for x in d.get('transcript',[]))), d.get('title','')

def freetranscriptapi(vid):
    url='https://api.freetranscriptapi.com/v1/transcript?'+urllib.parse.urlencode({'video_url':vid,'format':'text','lang':'en'})
    req=urllib.request.Request(url,headers={'User-Agent':UA})
    with urllib.request.urlopen(req,timeout=90) as r: return clean(r.read().decode('utf-8','ignore')), ''

def direct(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    t=YouTubeTranscriptApi().fetch(vid,languages=['en','en-US','en-GB'])
    return clean(' '.join(s.text for s in t.snippets)), ''

PROVIDERS=[('transcribeyoutube',transcribeyoutube),('freetranscriptapi',freetranscriptapi)]

def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 30
    vids={r['id']:r for r in csv.DictReader(open(CSV,encoding='utf-8'))}
    rows=[json.loads(l) for l in open(JSONL,encoding='utf-8')]
    byid={r['id']:r for r in rows}
    missing=[]
    for vid,v in vids.items():
        st=byid.get(vid,{}).get('status')
        if st in ('ok','cached','ok_freetranscriptapi','ok_multiprovider'): continue
        missing.append((PRIORITY.get(v['channel'],3),-score(v['title']),vid,v))
    missing.sort(); todo=missing[:limit]
    print(f'{len(missing)} missing; fetching {len(todo)}')
    for n,(_,_,vid,v) in enumerate(todo,1):
        path=os.path.join(OUT,f'{vid}.txt')
        if os.path.exists(path) and os.path.getsize(path)>200:
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'cached','path':path,'chars':os.path.getsize(path)}
            print('cached',vid); continue
        text=None; used=None; errs=[]
        primary_rate_limited=False
        for name,fn in PROVIDERS:
            try:
                text,_=fn(vid); used=name; break
            except Exception as e:
                errs.append(f'{name}: {str(e)[:120]}')
                if name=='transcribeyoutube' and ('429' in str(e) or 'RATE' in str(e).upper()):
                    primary_rate_limited=True
                    break
        if text and len(text)>200:
            with open(path,'w',encoding='utf-8') as f:
                f.write(f"# {v['title']}\n\nChannel: {v['channel']}\nVideo: https://www.youtube.com/watch?v={vid}\nProvider: {used}\n\n{text}\n")
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'ok_multiprovider','provider':used,'path':path,'chars':len(text)}
            print(f"{n}/{len(todo)} OK [{used}] {v['channel']} | {v['title'][:65]} | {len(text)}")
        else:
            joined=' | '.join(errs)
            unavailable=any(x in joined for x in ['404', 'NO_CAPTIONS', 'No captions', 'VideoUnavailable'])
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'unavailable' if unavailable else 'error_multiprovider','error':joined[:500]}
            print(f"{n}/{len(todo)} {'UNAVAILABLE' if unavailable else 'ERR'} {vid} {joined[:220]}")
            if primary_rate_limited:
                print('transcribeyoutube rate limited; stopping this run.'); break
        time.sleep(13+random.random()*3)
    with open(JSONL,'w',encoding='utf-8') as f:
        for r in sorted(byid.values(),key=lambda x:x['id']): f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print('updated',JSONL)
if __name__=='__main__': main()
