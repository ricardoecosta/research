#!/bin/zsh
# Unattended v8 run: ingest (xhigh) and mining in parallel, then verify -> gate -> cluster -> score.
# Pushes each finished stage. Never touches analysis/v8/scouts. Log: /tmp/v8/run.log
REPO=~/hustling/research; S=$REPO/koerner-office/scripts/v8; PY=/tmp/v7venv/bin/python
log(){ echo "$(date '+%m-%d %H:%M:%S') $*" >> /tmp/v8/run.log; }
push(){
  until mkdir /tmp/v7/gitlock 2>/dev/null; do sleep 5; done
  cd $REPO && find koerner-office/scripts/v8 -name __pycache__ -prune -exec rm -rf {} + ;
  out=$(zsh koerner-office/scripts/v7/push.sh "$1" koerner-office/analysis/v8 ':(exclude)koerner-office/analysis/v8/scouts' koerner-office/scripts/v8 2>&1 | tail -1)
  rmdir /tmp/v7/gitlock; log "PUSH [$1] -> $out"; echo "$1 | $out" >> /tmp/v8/commits.txt
}
nmined(){ ls $REPO/koerner-office/analysis/v8/mined/*.json 2>/dev/null | wc -l | tr -d ' '; }
log "start pid=$$"
cd $S && $PY ingest.py --effort xhigh --workers ${INGEST_WORKERS:-4} >> /tmp/v8/ingest.stdout 2>&1 &
ING=$!
lastpush=0
for round in $(seq 1 400); do
  cd $S && $PY mine.py --workers ${MINE_WORKERS:-5} >> /tmp/v8/mine.stdout 2>&1
  n=$(nmined)
  if [ $((n - lastpush)) -ge 60 ]; then push "v8 mining: $n/435 transcripts mined"; lastpush=$n; fi
  if ! kill -0 $ING 2>/dev/null; then
    [ -f /tmp/v8/ingest_pushed ] || { push "v8 stage 1-3: ingest (clean, split, date) for all 435"; touch /tmp/v8/ingest_pushed; }
    cd $S && $PY gate.py > /tmp/v8/gate.out 2>&1 && break
    left=$(grep -c . /dev/null); pending=$(cd $S && $PY -c "
import json,sys;sys.path.insert(0,'.');from common8 import *
ids=[p.stem for p in RAW_TX.glob('*.txt')]
print(sum(1 for v in ids if not (V8/'mined'/f'{v}.json').exists() and not (V8/'mined'/'_failed'/f'{v}.txt').exists() and json.loads((V8/'ingest'/'records'/f'{v}.json').read_text())['status']=='ingested'))" 2>/dev/null)
    log "round $round mined=$n pending_after_ingest=$pending"
    [ "$pending" = "0" ] && break
  fi
  [ -f /tmp/v8/STOP ] && { log STOP; exit 0; }
  sleep 30
done
cd $S && $PY verify.py >> /tmp/v8/verify.out 2>&1; $PY gate.py > /tmp/v8/gate.out 2>&1; GATE=$?
push "v8 stage 4-6: mining + UK legal filter + sampled quote verification ($(nmined)/435 mined)"
[ $GATE -ne 0 ] && { log "GATE CLOSED after mining; stopping before clustering"; exit 1; }
log "gate open; clustering"
cd $S && $PY cluster.py >> /tmp/v8/cluster.out 2>&1 || { log "cluster failed"; exit 1; }
push "v8 stage 7: clusters by distinct videos"
log "scoring"
cd $S && $PY score.py >> /tmp/v8/score.out 2>&1 || { log "score failed"; exit 1; }
push "v8 stage 8-9: scores, automation distribution, top slice ready for validation"
log "DONE"; touch /tmp/v8/DONE
