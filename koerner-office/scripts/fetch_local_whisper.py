#!/usr/bin/env python3
"""Local Whisper fallback: download audio with yt-dlp cookies, transcribe with whisper.cpp tiny.en.

Usage: python3 fetch_local_whisper.py [limit]
"""
import csv, json, os, re, sys, subprocess, tempfile, shutil
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV=os.path.join(BASE,'data','videos_v2.csv')
JSONL=os.path.join(BASE,'data','transcripts_v2.jsonl')
OUT=os.path.join(BASE,'transcripts','raw')
MODEL=os.path.expanduser('~/.cache/whisper.cpp/ggml-tiny.en.bin')
os.makedirs(OUT,exist_ok=True)
PRIORITY={'The Koerner Office':0,'Side Hustle Nation':1,'Starter Story':1,'UpFlip':1,'My First Million':1,'Niche Pursuits':1,'Nick Huber - Sweaty Startup':1,'Codie Sanchez':1,"Harry's Stealth Wealth":2,'David Heacock':2,'Johnny & Sergio':2,'Tim Richard':2,'Casper Capital':2,'Mikey No Code':2,'Dark Horse Entrepreneur':2,'George McConnell':2}
KW=['business','side hustle','hustle','ai','agency','client','money','profit','million','month','passive','income','rent','rental','boring','scale','sell','easy','automat','app','software','lead','local','niche']
def score(t): return sum(1 for k in KW if k in t.lower())
def clean(s): return re.sub(r'\s+',' ',s.replace('\xa0',' ')).strip()
def main():
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 10
    vids={r['id']:r for r in csv.DictReader(open(CSV,encoding='utf-8'))}
    rows=[json.loads(l) for l in open(JSONL,encoding='utf-8')]
    byid={r['id']:r for r in rows}
    missing=[]
    for vid,v in vids.items():
        st=byid.get(vid,{}).get('status')
        if st in ('ok','cached','ok_freetranscriptapi','ok_multiprovider','ok_whisper','unavailable'): continue
        # skip likely members-only full episodes
        if '[NO ADS' in v['title'] or 'FULL EPISODE' in v['title']: continue
        missing.append((PRIORITY.get(v['channel'],3),-score(v['title']),vid,v))
    missing.sort(); todo=missing[:limit]
    print(f'{len(missing)} candidate missing; transcribing {len(todo)}')
    for n,(_,_,vid,v) in enumerate(todo,1):
        path=os.path.join(OUT,f'{vid}.txt')
        if os.path.exists(path) and os.path.getsize(path)>200:
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'cached','path':path,'chars':os.path.getsize(path)}
            print('cached',vid); continue
        tmp=tempfile.mkdtemp(prefix='whisper_')
        audio=os.path.join(tmp,'audio.%(ext)s')
        try:
            dl=subprocess.run(['yt-dlp','--no-update','--cookies-from-browser','chrome','-f','bestaudio','--max-filesize','150M','-o',audio,f'https://www.youtube.com/watch?v={vid}'],capture_output=True,text=True,timeout=300)
            if dl.returncode!=0:
                msg=(dl.stderr or dl.stdout)[-500:]
                unavailable=('members-only' in msg.lower() or 'join this channel' in msg.lower() or 'video unavailable' in msg.lower())
                byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'unavailable' if unavailable else 'error_whisper','error':msg}
                print(f"{n}/{len(todo)} {'UNAVAILABLE' if unavailable else 'DL_ERR'} {vid} {msg[:180]}")
                continue
            files=[f for f in os.listdir(tmp) if f.startswith('audio.')]
            if not files: raise RuntimeError('no audio file')
            src=os.path.join(tmp,files[0]); wav=os.path.join(tmp,'audio.wav')
            subprocess.run(['ffmpeg','-y','-i',src,'-ar','16000','-ac','1','-c:a','pcm_s16le',wav],capture_output=True,timeout=300,check=True)
            outbase=os.path.join(tmp,'out')
            tr=subprocess.run(['whisper-cli','-m',MODEL,'-f',wav,'-otxt','-of',outbase],capture_output=True,text=True,timeout=900)
            if tr.returncode!=0: raise RuntimeError((tr.stderr or tr.stdout)[-400:])
            text=clean(open(outbase+'.txt',encoding='utf-8').read())
            if len(text)<200: raise RuntimeError('transcript too short')
            with open(path,'w',encoding='utf-8') as f:
                f.write(f"# {v['title']}\n\nChannel: {v['channel']}\nVideo: https://www.youtube.com/watch?v={vid}\nProvider: local_whisper_tiny\n\n{text}\n")
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'ok_whisper','provider':'local_whisper_tiny','path':path,'chars':len(text)}
            print(f"{n}/{len(todo)} OK {v['channel']} | {v['title'][:70]} | {len(text)}")
        except Exception as e:
            byid[vid]={'id':vid,'channel':v['channel'],'title':v['title'],'duration':v['duration'],'status':'error_whisper','error':str(e)[:500]}
            print(f"{n}/{len(todo)} ERR {vid} {str(e)[:200]}")
        finally:
            shutil.rmtree(tmp,ignore_errors=True)
    with open(JSONL,'w',encoding='utf-8') as f:
        for r in sorted(byid.values(),key=lambda x:x['id']): f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print('updated',JSONL)
if __name__=='__main__': main()
