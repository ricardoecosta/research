"""Shared helpers for the v8 pipeline (METHOD.md @31dfcc4, RULES_LOCKED.md)."""
import csv, datetime as dt, json, os, re, subprocess, tempfile, threading, time
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KO = REPO / "koerner-office"
V8 = KO / "analysis" / "v8"
RAW_TX = KO / "transcripts" / "raw"
WORK = Path("/tmp/v8")
CODEX = os.path.expanduser("~/.local/bin/codex")
PI = "/opt/homebrew/bin/pi"
MODEL = "gpt-6-luna"
STALE_BEFORE = "20250423"  # 18 months before 23 Oct 2026
CATS = ['local_service', 'home_service', 'b2b_service', 'agency', 'saas_software', 'ai_automation', 'data_leads',
        'content_media', 'ecommerce_physical', 'digital_products', 'marketplace_directory', 'rental_asset',
        'vending_machines_kiosks', 'real_estate', 'acquisition_buy_business', 'events_experiences',
        'education_coaching', 'arbitrage_reselling', 'manufacturing', 'franchise', 'job_career', 'other']
_lk = threading.Lock()


def log(path, msg):
    line = f"{dt.datetime.now():%m-%d %H:%M:%S} {msg}"
    with _lk:
        with open(path, "a") as f:
            f.write(line + "\n")
    print(line, flush=True)


def load_dates():
    d = {}
    for line in (V8 / "ingest" / "dates.tsv").read_text().splitlines():
        p = line.split("\t")
        if len(p) >= 5:
            d[p[0]] = dict(date=p[1], channel=p[2], views=p[3], duration=p[4])
    return d


HDR = re.compile(r"^(#|Channel:|Video:|Provider:|Source:|Title:|URL:|Status:|Language:)")


def parse_raw(vid):
    raw = (RAW_TX / f"{vid}.txt").read_bytes()
    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()
    meta, i = {}, 0
    while i < len(lines) and i < 10 and (HDR.match(lines[i]) or not lines[i].strip()):
        l = lines[i]
        if l.startswith("# "): meta["title"] = l[2:].strip()
        elif ":" in l and l.strip():
            k, v = l.split(":", 1); meta[k.strip().lower()] = v.strip()
        i += 1
    return text, meta, "\n".join(lines[i:]).strip()


def number_lines(body):
    """Deterministic: split at sentence ends; chunk 30 words when unpunctuated. Returns [(text, char_offset)]."""
    out, pos = [], 0
    parts = re.split(r"(?<=[.?!])\s+|\s+(?=- [A-Z])", body)
    for p in parts:
        off = body.find(p, pos)
        if off < 0: off = pos
        pos = off + len(p)
        w = p.split()
        if not w: continue
        if len(w) <= 60:
            out.append((p.strip(), off))
        else:
            sub_off = off
            for k in range(0, len(w), 30):
                chunk = " ".join(w[k:k + 30])
                o = body.find(w[k], sub_off); o = o if o >= 0 else sub_off
                out.append((chunk, o)); sub_off = o + 1
    return out


def numbered(vid, dates=None):
    _, meta, body = parse_raw(vid)
    dur = float((dates or {}).get(vid, {}).get("duration") or 0)
    L = number_lines(body)
    n = max(len(body), 1)
    rows = []
    for k, (t, off) in enumerate(L, 1):
        sec = int(off / n * dur) if dur else None
        rows.append(dict(line=k, minute=(f"{sec // 60}:{sec % 60:02d}" if sec is not None else None), text=t))
    return meta, body, rows


def fmt_lines(rows, keep=None):
    return "\n".join(f"L{r['line']:04d} [{r['minute'] or '?'}] {r['text']}" for r in rows if keep is None or r["line"] in keep)


def parse_json_text(txt):
    txt = txt.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", txt, re.S)
    if m: txt = m.group(1).strip()
    i = txt.find("{"); j = txt.rfind("}")
    return json.loads(txt[i: j + 1])


class Busy(Exception):
    pass


def run_codex(prompt, effort="xhigh", timeout=2400):
    cwd = WORK / "codex_cwd"; cwd.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, dir=cwd) as out:
        out_path = out.name
    cmd = [CODEX, "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only", "--disable", "hooks",
           "-m", MODEL, "-c", f'model_reasoning_effort="{effort}"', "--color", "never", "--json",
           "-o", out_path, "-C", str(cwd), "-"]
    t0 = time.time()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, cwd=cwd, start_new_session=True)
    try:
        so, se = p.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, 9); p.communicate(); raise TimeoutError(f"codex timeout {timeout}s")
    answer, usage, errs = None, {}, []
    for line in (so or "").splitlines():
        try: ev = json.loads(line)
        except Exception: continue
        it = ev.get("item") or {}
        if ev.get("type") == "item.completed" and it.get("type") in ("agent_message", "assistant_message"):
            answer = it.get("text") or answer
        if ev.get("type") == "turn.completed": usage = ev.get("usage") or {}
        if ev.get("type") in ("error", "turn.failed"): errs.append(json.dumps(ev)[:300])
    try:
        lm = Path(out_path).read_text()
        if lm.strip(): answer = lm
        os.unlink(out_path)
    except Exception:
        pass
    if not answer and any(k in " ".join(errs).lower() for k in ("capacity", "rate limit", "429", "overloaded", "try again", "usage limit")):
        raise Busy("; ".join(errs)[:200])
    if not answer:
        raise ValueError(f"no answer rc={p.returncode} errs={errs[:2]} stderr={(se or '')[-200:]}")
    return answer, usage, time.time() - t0


def run_pi(prompt, timeout=2400):
    cwd = WORK / "pi_cwd"; cwd.mkdir(parents=True, exist_ok=True)
    pf = cwd / f"p_{os.getpid()}_{threading.get_ident()}.txt"; pf.write_text(prompt)
    t0 = time.time()
    p = subprocess.run([PI, "-p", "--no-tools", f"@{pf}", "Follow the instructions in the attached file. Reply with the JSON only."],
                       stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=cwd, timeout=timeout)
    pf.unlink(missing_ok=True)
    if not p.stdout.strip(): raise ValueError("pi empty: " + p.stderr[-200:])
    return p.stdout, {}, time.time() - t0


def call_llm(prompt, effort="xhigh", logf=None, tag=""):
    """FALLBACKS order: Codex (with busy back-off) -> pi. Returns (parsed_json, runner, secs)."""
    last = ""
    for attempt in range(3):
        try:
            for wait in range(30):
                try:
                    ans, usage, secs = run_codex(prompt, effort); break
                except Busy as b:
                    if logf: log(logf, f"{tag} codex busy {b}; backoff")
                    time.sleep(min(60 * (wait + 1), 600))
            else:
                raise ValueError("codex busy too long")
            return parse_json_text(ans), f"codex:{MODEL}:{effort}", secs
        except Exception as e:
            last = str(e)[:200]
            if logf: log(logf, f"{tag} codex attempt {attempt + 1} failed: {last}")
    try:
        ans, _, secs = run_pi(prompt)
        return parse_json_text(ans), "pi", secs
    except Exception as e:
        raise RuntimeError(f"all runners failed: codex={last} pi={str(e)[:200]}")


def norm(s):
    s = s.lower().replace("\u2019", "'")
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()
