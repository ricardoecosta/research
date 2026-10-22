#!/usr/bin/env python3
"""Unattended v7 pipeline driver: runs every stage, waits out Claude usage-limit resets,
and commits + pushes to origin/main after each chunk. Log: /tmp/v7/driver.log"""
import datetime as dt, re, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).parent
PY = sys.executable
LIMIT = Path("/tmp/v7/limit.txt")
PATHS = ["koerner-office/analysis/v7", "koerner-office/scripts/v7"]


def log(*a):
    print(dt.datetime.now().strftime("%m-%d %H:%M:%S"), *a, flush=True)


def wait_reset():
    txt = LIMIT.read_text() if LIMIT.exists() else ""
    now = dt.datetime.now()
    m = re.search(r"resets\s+(?:([A-Z][a-z]{2})\s+(\d{1,2}),?\s+(?:at\s+)?)?(\d{1,2})(?::(\d{2}))?\s*(am|pm)", txt)
    target = now + dt.timedelta(minutes=20)
    if m:
        mon, day, h, mi, ap = m.groups()
        h = int(h) % 12 + (12 if ap == "pm" else 0); mi = int(mi or 0)
        if mon:
            t = dt.datetime.strptime(f"{mon} {day} {now.year} {h}:{mi}", "%b %d %Y %H:%M")
        else:
            t = now.replace(hour=h, minute=mi, second=0, microsecond=0)
            if t <= now:
                t += dt.timedelta(days=1)
        target = t + dt.timedelta(minutes=3)
    log("usage limit:", txt.strip()[:160], "-> sleeping until", target)
    while dt.datetime.now() < target:
        time.sleep(60)
    LIMIT.unlink(missing_ok=True)


def run(args):
    log("RUN", " ".join(args))
    return subprocess.run([PY] + args, cwd=HERE).returncode


def stage(args, max_fail=3):
    fails = 0
    while True:
        rc = run(args)
        if rc == 0:
            return True
        if rc == 75:
            wait_reset(); continue
        fails += 1
        log("stage failed rc", rc, "attempt", fails)
        if fails >= max_fail:
            return False
        time.sleep(60)


def push(msg):
    run(["finalize.py"]); run(["consolidate.py"])
    r = subprocess.run(["zsh", str(HERE / "push.sh"), msg, *PATHS], capture_output=True, text=True)
    log("push:", (r.stdout + r.stderr).strip()[-300:])


def remaining():
    raw = {p.stem for p in Path("/tmp/v7/raw").glob("*.json")}
    tx = {p.stem for p in (HERE.parents[1] / "transcripts" / "raw").glob("*.txt")}
    return len(tx - raw)


def main():
    while remaining() > 0:
        rc = run(["extract.py", "--workers", "5", "--order", "shuffle", "--limit", "50"])
        n = 435 - remaining()
        push(f"v7: mined {n} transcripts into structured learnings")
        if rc == 75:
            wait_reset()
        elif rc != 0:
            log("extract rc", rc); time.sleep(120)
        if Path("/tmp/v7/STOP").exists():
            log("STOP file found"); return
    steps = [("review.py --n 30", "v7: Opus quality review of 30 random extractions (corrections applied)"),
             ("cluster.py", "v7: deduplicated and clustered idea catalogue"),
             ("score.py", "v7: scored idea catalogue (success and automation rubric)"),
             ("synth.py", "v7: cross-transcript learnings synthesis parts")]
    for cmd, msg in steps:
        if Path("/tmp/v7/STOP").exists():
            log("STOP file found"); return
        ok = stage(cmd.split())
        if cmd == "cluster.py" and ok:
            run(["consolidate.py"])
        push(msg if ok else msg + " (partial)")
        if not ok:
            log("giving up at", cmd); return
    Path("/tmp/v7/PIPELINE_DONE").write_text(dt.datetime.now().isoformat())
    log("PIPELINE DONE")


if __name__ == "__main__":
    main()
