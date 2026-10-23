"""How v8 clustering scattered each business model across gap-level clusters, and which hard rules killed them."""
import json, csv, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT/'scripts/proven_models'))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()): from group import model_of
rows = {json.loads(l)['key']: json.loads(l) for l in open(ROOT/'analysis/v8/ideas_flat.jsonl')}
mem = json.load(open(ROOT/'analysis/v8/clusters/membership.json'))
sc = {r['name']: r for r in csv.DictReader(open(ROOT/'analysis/v8/ideas_scored.csv'))}
out = collections.defaultdict(lambda: {"clusters":set(), "single_video":0, "fails":collections.Counter(), "passed":0})
for c in mem:
    r = sc.get(c['name']);
    if not r: continue
    ms = collections.Counter(model_of(rows[k]) for k in c['member_keys'] if k in rows)
    if not ms: continue
    m = ms.most_common(1)[0][0]; o = out[m]
    if r['cid'] in o['clusters']: continue
    o['clusters'].add(r['cid']); o['single_video'] += r['single_video']=='True'
    f = [x.strip() for x in r['fails'].split(';') if x.strip()]
    if not f: o['passed'] += 1
    for x in f: o['fails'][x] += 1
    if f == ['hours>5']: o['fails']['ONLY hours>5'] += 1
res = {m: dict(n_clusters=len(o['clusters']), single_video=o['single_video'], passed=o['passed'], fails=dict(o['fails'])) for m,o in out.items()}
json.dump(res, open(ROOT/'analysis/proven_models/v8_fragmentation.json','w'), indent=1)
for m,o in sorted(res.items(), key=lambda kv:-kv[1]['n_clusters']): print(m, o)
