#!/usr/bin/env python3
import csv,json,os,re,time,random,sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from youtube_transcript_api import YouTubeTranscriptApi
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV=os.path.join(BASE,'data','videos_v2.csv'); JSONL=os.path.join(BASE,'data','transcripts_v2.jsonl'); OUT=os.path.join(BASE,'transcripts','raw')
os.makedirs(OUT,exist_ok=True)
def clean(s): return re.sub(r'\s+',' ',s.replace('\xa0',' ')).strip()
rows=list(csv.DictReader(open(CSV,encoding='utf-8')))
byid={r['id']:r for r in map(json.loads,open(JSONL,encoding='utf-8'))}
missing=[]
for v in rows:
    st=byid.get(v['id'],{}).get('status')
    if st in ('ok','cached','ok_freetranscriptapi','ok_multiprovider','ok_whisper','unavailable'): continue
    missing.append(v)
limit=int(sys.argv[1]) if len(sys.argv)>1 else len(missing)
missing=missing[:limit]
print('fetching',len(missing))
def fetch(v):
    vid=v['id']; path=os.path.join(OUT,f'{vid}.txt')
    if os.path.exists(path) and os.path.getsize(path)>200:
        return {'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'cached','path':path,'chars':os.path.getsize(path)}
    for attempt in range(3):
        try:
            t=YouTubeTranscriptApi().fetch(vid,languages=['en','en-US','en-GB'])
            text=clean(' '.join(s.text for s in t.snippets))
            with open(path,'w',encoding='utf-8') as f:
                f.write(f"# {v['title']}\n\nChannel: {v['channel']}\nVideo: https://www.youtube.com/watch?v={vid}\nProvider: youtube-transcript-api\n\n{text}\n")
            return {'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'ok','path':path,'chars':len(text)}
        except Exception as e:
            msg=str(e)
            if 'members-only' in msg.lower() or 'no transcript' in msg.lower() or 'unavailable' in msg.lower():
                return {'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'unavailable','error':msg[:300]}
            if attempt<2: time.sleep(3*(attempt+1)); continue
            return {'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'error','error':msg[:300]}
with ThreadPoolExecutor(max_workers=2) as ex:
    futs={ex.submit(fetch,v):v for v in missing}
    for i,f in enumerate(as_completed(futs),1):
        r=f.result(); byid[r['id']]=r
        print(i,'/',len(missing),r['status'],r['id'],r['title'][:60])
        time.sleep(0.4)
with open(JSONL,'w',encoding='utf-8') as f:
    for r in sorted(byid.values(),key=lambda x:x['id']): f.write(json.dumps(r,ensure_ascii=False)+'\n')
print('updated')
