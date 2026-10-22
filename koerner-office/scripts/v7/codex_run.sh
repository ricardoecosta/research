#!/bin/zsh
# Unattended: run codex_extract.py over all remaining ids, push every ~20 new raw files,
# then (only when exactly 435 raw files exist) start driver.py for the later stages.
# Log: /tmp/v7/codex_run.log
REPO=~/hustling/research
V7=$REPO/koerner-office/scripts/v7
PY=/tmp/v7venv/bin/python
TOTAL=435
log(){ echo "$(date '+%m-%d %H:%M:%S') $*"; }
nraw(){ ls /tmp/v7/raw/*.json 2>/dev/null | wc -l | tr -d ' '; }
push(){
  cd $V7 && $PY consolidate.py >/dev/null 2>&1
  cd $REPO
  until mkdir /tmp/v7/gitlock 2>/dev/null; do sleep 5; done
  git add koerner-office/analysis/v7 koerner-office/scripts/v7/codex_extract.py koerner-office/scripts/v7/codex_run.sh
  if git diff --cached --quiet; then log "push: nothing to commit"; else
    git commit -q -m "$1"
    for i in 1 2 3; do
      git pull -q --rebase --autostash origin main && git push -q origin HEAD:main && break
      sleep 10
    done
    log "push: $(git log --oneline -1) $(git status -sb | head -1)"
  fi
  rmdir /tmp/v7/gitlock
}
log "wrapper start pid=$$ raw=$(nraw)"
for round in 1 2 3 4 5; do
  [ "$(nraw)" -ge $TOTAL ] && break
  cd $V7 && $PY codex_extract.py --workers ${CODEX_WORKERS:-4} >> /tmp/v7/codex_extract.stdout 2>&1 &
  EX=$!
  last=$(nraw)
  while kill -0 $EX 2>/dev/null; do
    sleep 60
    n=$(nraw)
    if [ $((n - last)) -ge 20 ]; then push "v7: extracted $((n - last)) more (codex gpt-6-luna), $n/$TOTAL"; last=$n; fi
    [ -f /tmp/v7/STOP ] && { log "STOP file found"; kill $EX; exit 0; }
  done
  n=$(nraw); [ $n -gt $last ] && push "v7: extracted $((n - last)) more (codex gpt-6-luna), $n/$TOTAL"
  log "extract round $round ended raw=$n"
done
cd $V7 && $PY codex_extract.py --repair >> /tmp/v7/codex_extract.log 2>&1
n=$(nraw)
if [ "$n" -eq $TOTAL ]; then
  log "435 raw files: starting driver.py"
  cd $V7 && rm -f /tmp/v7/limit.txt && nohup $PY driver.py >> /tmp/v7/driver.log 2>&1 &
  log "driver pid=$!"
else
  log "NOT starting driver: raw=$n != $TOTAL (failed ids need attention)"
fi
