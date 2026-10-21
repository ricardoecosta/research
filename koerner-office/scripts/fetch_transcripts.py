#!/usr/bin/env python3
"""Fetch English transcripts for The Koerner Office YouTube channel.

Usage: PYTHONPATH=/tmp/ytlib /usr/bin/python3 fetch_transcripts.py [limit]
Reads ../data/videos.csv, writes ../transcripts/raw/<id>.txt and ../data/transcripts.jsonl.
Skips existing files. Retries rate limits with backoff.
"""
import csv, json, os, re, sys, time, random
from concurrent.futures import ThreadPoolExecutor, as_completed
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(BASE, 'data', 'videos.csv')
OUTDIR = os.path.join(BASE, 'transcripts', 'raw')
JSONL = os.path.join(BASE, 'data', 'transcripts.jsonl')
os.makedirs(OUTDIR, exist_ok=True)

def safe_name(s):
    s = re.sub(r'[^\w\s.-]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:140]

def clean_text(t):
    return re.sub(r'\s+', ' ', t.replace('\xa0', ' ')).strip()

def fetch_one(row, attempt=1):
    vid = row['id']
    path = os.path.join(OUTDIR, f"{vid}.txt")
    if os.path.exists(path) and os.path.getsize(path) > 200:
        return {'id': vid, 'channel': row.get('channel',''), 'title': row['title'], 'duration': row['duration'], 'status': 'cached', 'path': path}
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(vid, languages=['en', 'en-US', 'en-GB'])
        text = clean_text(' '.join(s.text for s in fetched.snippets))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# {row['title']}\n\n")
            f.write(f"Channel: {row.get('channel','')}\n")
            f.write(f"Video: https://www.youtube.com/watch?v={vid}\n")
            f.write(f"Duration: {row['duration']} seconds\n\n")
            f.write(text + "\n")
        return {'id': vid, 'channel': row.get('channel',''), 'title': row['title'], 'duration': row['duration'], 'status': 'ok', 'path': path, 'chars': len(text)}
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        return {'id': vid, 'channel': row.get('channel',''), 'title': row['title'], 'duration': row['duration'], 'status': 'unavailable', 'error': type(e).__name__}
    except Exception as e:
        if attempt < 4 and ('429' in str(e) or 'Too Many Requests' in str(e) or 'timed out' in str(e).lower()):
            time.sleep((2 ** attempt) + random.random() * 2)
            return fetch_one(row, attempt + 1)
        return {'id': vid, 'channel': row.get('channel',''), 'title': row['title'], 'duration': row['duration'], 'status': 'error', 'error': str(e)[:300]}

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    rows = list(csv.DictReader(open(CSV, encoding='utf-8')))
    if limit:
        rows = rows[:limit]
    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(fetch_one, r): r for r in rows}
        for i, fut in enumerate(as_completed(futs), 1):
            res = fut.result()
            results.append(res)
            if i % 20 == 0:
                ok = sum(1 for x in results if x['status'] in ('ok', 'cached'))
                print(f"{i}/{len(rows)} processed, {ok} ok", flush=True)
    existing = {}
    if os.path.exists(JSONL):
        for line in open(JSONL, encoding='utf-8'):
            try:
                old = json.loads(line)
                existing[old['id']] = old
            except Exception:
                pass
    for r in results:
        existing[r['id']] = r
    results = sorted(existing.values(), key=lambda x: x['id'])
    with open(JSONL, 'w', encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    from collections import Counter
    print(Counter(r['status'] for r in results))
    print('wrote', JSONL)

if __name__ == '__main__':
    main()
