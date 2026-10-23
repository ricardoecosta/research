"""Fail-over LLM runner for the research loop (LOOP.md "Inference fallbacks"; METHOD.md FALLBACKS).

Order: Codex (gpt-6-luna) -> Claude (claude-opus-5-5) -> pi -> Grok Bot box.
- A limit message switches to the next runner at once; there is no hours-long back-off.
- The reset time is parsed from the message and stored in STATE, so the cheaper runner is used again after its reset.
- If every runner is blocked, the prompt is written to BOX_DIR/<tag>.txt and BoxPending is raised. The caller
  skips that item; Grok Bot answers into BOX_ANS/<tag>.json, and import_box-style code ingests it.

Usage:  from runner import call_llm, BoxPending
        data, runner_name, secs = call_llm(prompt, effort="xhigh", tag="vid123", logf=path)
"""
import datetime as dt, json, os, re, subprocess, tempfile, threading, time
from pathlib import Path

WORK = Path(os.environ.get("LOOP_WORK", "/tmp/loop"))
STATE = WORK / "runner_state.json"
BOX_DIR = WORK / "box_prompts"
BOX_ANS = WORK / "box_answers"
CODEX = os.path.expanduser("~/.local/bin/codex")
CLAUDE = os.path.expanduser("~/.local/bin/claude")
PI = "/opt/homebrew/bin/pi"
CODEX_MODEL = "gpt-6-luna"
CLAUDE_MODEL = "claude-opus-5-5"
ORDER = os.environ.get("LOOP_RUNNERS", "codex,claude,pi").split(",")
DEFAULT_BLOCK_MIN = 60
_lk = threading.Lock()

# Phrases seen in real limit messages (23 Oct 2026):
#   Codex : "You've hit your usage limit. ... try again at 2:34 PM."
#   Claude: "You've hit your session limit · resets 5:20pm"
LIMIT_RE = re.compile(r"usage limit|session limit|hit your (?:usage|session|weekly)?\s*limit|limit reached|rate.?limit"
                      r"|\b429\b|overloaded|at capacity|resets? (?:at )?\d{1,2}(?::\d{2})?\s*[ap]m|try again (?:at|in)", re.I)
RESET_RE = re.compile(r"(?:try again at|resets?(?: at)?)\s*(\d{1,2})(?::(\d{2}))?\s*([ap]\.?m\.?)?", re.I)


class Busy(Exception):
    def __init__(self, msg, until=None):
        super().__init__(msg); self.until = until


class BoxPending(Exception):
    pass


def log(path, msg):
    line = f"{dt.datetime.now():%m-%d %H:%M:%S} {msg}"
    if path:
        with _lk, open(path, "a") as f: f.write(line + "\n")
    print(line, flush=True)


def parse_reset(text, now=None):
    """Return the local datetime the limit resets, or None. '2:34' without am/pm = next occurrence."""
    now = now or dt.datetime.now()
    m = RESET_RE.search(text or "")
    if not m: return None
    h, mi, ap = int(m.group(1)), int(m.group(2) or 0), (m.group(3) or "").lower().replace(".", "")
    if ap == "pm" and h < 12: h += 12
    if ap == "am" and h == 12: h = 0
    cands = [now.replace(hour=h % 24, minute=mi, second=0, microsecond=0)]
    if not ap and h < 12: cands.append(cands[0].replace(hour=h + 12))
    cands = [c if c > now else c + dt.timedelta(days=1) for c in cands]
    return min(cands)


def detect_limit(text, now=None):
    """(is_limited, reset_datetime). Unparseable resets block for DEFAULT_BLOCK_MIN."""
    if not text or not LIMIT_RE.search(text): return False, None
    return True, parse_reset(text, now) or (now or dt.datetime.now()) + dt.timedelta(minutes=DEFAULT_BLOCK_MIN)


def _state():
    try: return json.loads(STATE.read_text())
    except Exception: return {}


def blocked_until(name):
    s = _state().get(name)
    if s and dt.datetime.fromisoformat(s) > dt.datetime.now(): return dt.datetime.fromisoformat(s)
    return None


def mark_blocked(name, until):
    with _lk:
        WORK.mkdir(parents=True, exist_ok=True)
        s = _state(); s[name] = until.isoformat(timespec="minutes"); STATE.write_text(json.dumps(s, indent=1))


def _check(name, out, err, rc):
    lim, until = detect_limit(f"{out[-2000:] if out else ''} {err or ''}")
    if lim and (rc != 0 or len((out or "").strip()) < 400):
        raise Busy(f"{name} limited: {(err or out or '')[-160:]}", until)


def run_codex(prompt, effort="xhigh", timeout=2400, web=False):
    cwd = WORK / "codex_cwd"; cwd.mkdir(parents=True, exist_ok=True)
    fd, out_path = tempfile.mkstemp(suffix=".txt", dir=cwd); os.close(fd)
    cmd = [CODEX, "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "--disable", "hooks",
           "-m", CODEX_MODEL, "-c", f'model_reasoning_effort="{effort}"', *(["-c", 'web_search="live"'] if web else []), "--color", "never", "--json",
           "-o", out_path, "-C", str(cwd), "-"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, cwd=cwd, start_new_session=True)
    try: so, se = p.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, 9); p.communicate(); raise TimeoutError(f"codex timeout {timeout}s")
    answer, errs = None, []
    for line in (so or "").splitlines():
        try: ev = json.loads(line)
        except Exception: continue
        it = ev.get("item") or {}
        if ev.get("type") == "item.completed" and it.get("type") in ("agent_message", "assistant_message"):
            answer = it.get("text") or answer
        if ev.get("type") in ("error", "turn.failed"): errs.append(json.dumps(ev)[:400])
    try:
        lm = Path(out_path).read_text(); os.unlink(out_path)
        if lm.strip(): answer = lm
    except Exception: pass
    if not answer: _check("codex", "", " ".join(errs) + " " + (se or ""), 1)
    if not answer: raise ValueError(f"codex no answer rc={p.returncode} {errs[:1]}")
    return answer


def run_claude(prompt, effort=None, timeout=2400, web=False):
    p = subprocess.run([CLAUDE, "-p", "--model", CLAUDE_MODEL, "--output-format", "text",
                        *(["--allowedTools", "WebSearch", "WebFetch"] if web else [])],
                       input=prompt, capture_output=True, text=True, cwd=str(WORK), timeout=timeout)
    out = (p.stdout or "").strip()
    _check("claude", out, p.stderr, p.returncode)
    if not out: raise ValueError("claude empty: " + (p.stderr or "")[-200:])
    return out


def run_pi(prompt, effort=None, timeout=2400, web=False):
    cwd = WORK / "pi_cwd"; cwd.mkdir(parents=True, exist_ok=True)
    pf = cwd / f"p_{os.getpid()}_{threading.get_ident()}.txt"; pf.write_text(prompt)
    p = subprocess.run([PI, "-p", "--no-tools", f"@{pf}", "Follow the instructions in the attached file. Reply with the JSON only."],
                       stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=cwd, timeout=timeout)
    pf.unlink(missing_ok=True)
    _check("pi", p.stdout, p.stderr, p.returncode)
    if not p.stdout.strip(): raise ValueError("pi empty: " + p.stderr[-200:])
    return p.stdout


RUNNERS = {"codex": run_codex, "claude": run_claude, "pi": run_pi}


def parse_json_text(txt):
    txt = txt.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", txt, re.S)
    if m: txt = m.group(1).strip()
    i, j = txt.find("{"), txt.rfind("}")
    return json.loads(txt[i:j + 1])


def call_llm(prompt, effort="xhigh", logf=None, tag="item", parse=True, web=False, order=None):
    """Try runners in ORDER, skipping blocked ones. Two tries per runner on parse/other errors.
    On a limit: record the reset, switch to the next runner immediately. All blocked -> BoxPending."""
    ans_file = BOX_ANS / f"{tag}.json"
    if ans_file.exists():  # already answered on the box
        t = ans_file.read_text(); return (parse_json_text(t) if parse else t), "grokbot-box", 0.0
    for name in (order or ORDER):
        bu = blocked_until(name)
        if bu: continue
        for attempt in range(2):
            t0 = time.time()
            try:
                out = RUNNERS[name](prompt, effort, web=web) if name == "codex" else RUNNERS[name](prompt, web=web)
                return (parse_json_text(out) if parse else out), (f"codex:{CODEX_MODEL}:{effort}" if name == "codex" else name), time.time() - t0
            except Busy as b:
                mark_blocked(name, b.until); log(logf, f"{tag} {name} LIMIT until {b.until:%H:%M}; switching"); break
            except Exception as e:
                log(logf, f"{tag} {name} attempt {attempt + 1} failed: {str(e)[:160]}")
    BOX_DIR.mkdir(parents=True, exist_ok=True)
    (BOX_DIR / f"{tag}.txt").write_text(prompt)
    log(logf, f"{tag} all runners blocked/failed; prompt dumped to {BOX_DIR}/{tag}.txt for Grok Bot")
    raise BoxPending(tag)


if __name__ == "__main__":  # self-test of limit detection (no LLM calls)
    now = dt.datetime(2026, 10, 23, 12, 0)
    cases = {
        "You\u2019ve hit your usage limit. Upgrade to Pro ... or try again at 2:34 PM.": "14:34",
        "You've hit your usage limit ... try again at 2:34": "14:34",
        "You've hit your session limit \u00b7 resets 5:20pm": "17:20",
        "Claude AI usage limit reached|1761235200": "13:00",
        "Error: 429 Too Many Requests": "13:00",
        "Here is the JSON you asked for": None,
    }
    for txt, want in cases.items():
        lim, until = detect_limit(txt, now)
        got = until.strftime("%H:%M") if lim else None
        print("OK " if got == want else "BAD", repr(txt[:50]), "->", got)
        assert got == want
    print("all detection tests passed")
