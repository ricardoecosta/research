#!/bin/zsh
# Commit the given paths and push to origin/main safely (pull --rebase first, never force).
set -e
cd ~/hustling/research
msg="$1"; shift
git add -- "$@"
if git diff --cached --quiet; then echo "nothing to commit"; else git commit -q -m "$msg"; fi
for i in 1 2 3; do
  git pull -q --rebase --autostash origin main && git push -q origin HEAD:main && { git log --oneline -1; exit 0; }
  sleep 5
done
echo "PUSH FAILED"; exit 1
