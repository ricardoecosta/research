"""Shared helpers for the v7 transcript-learnings pipeline."""
import csv, datetime as dt, json, os, re, subprocess, threading, time
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KO = REPO / "koerner-office"
V7 = KO / "analysis" / "v7"
RAW_TX = KO / "transcripts" / "raw"
OUT = V7 / "transcripts"
SCHEMA_PATH = V7 / "schema" / "transcript_learnings.schema.json"
COST_LOG = V7 / "cost_log.csv"
WORK = Path("/tmp/v7")
CLAUDE = os.path.expanduser("~/.local/bin/claude")
BUDGET_USD = float(os.environ.get("V7_BUDGET_USD", "100"))
_lock = threading.Lock()

COST_FIELDS = ["ts", "stage", "item", "model", "cost_usd", "input_tokens", "output_tokens",
               "cache_read", "cache_create", "duration_s", "status"]


def total_cost():
    if not COST_LOG.exists():
        return 0.0
    with open(COST_LOG) as f:
        return sum(float(r["cost_usd"] or 0) for r in csv.DictReader(f))


def log_cost(stage, item, model, res, status):
    u = (res or {}).get("usage", {}) or {}
    row = dict(ts=dt.datetime.now().isoformat(timespec="seconds"), stage=stage, item=item, model=model,
               cost_usd=round((res or {}).get("total_cost_usd", 0) or 0, 6),
               input_tokens=u.get("input_tokens", 0), output_tokens=u.get("output_tokens", 0),
               cache_read=u.get("cache_read_input_tokens", 0), cache_create=u.get("cache_creation_input_tokens", 0),
               duration_s=round(((res or {}).get("duration_ms", 0) or 0) / 1000, 1), status=status)
    with _lock:
        new = not COST_LOG.exists()
        with open(COST_LOG, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COST_FIELDS)
            if new:
                w.writeheader()
            w.writerow(row)


def run_claude(prompt, system, model="sonnet", effort=None, tools="", timeout=1800, extra=None):
    """Run claude -p and return the parsed --output-format json result dict."""
    cmd = [CLAUDE, "-p", prompt, "--model", model, "--output-format", "json",
           "--system-prompt", system, "--tools", tools, "--strict-mcp-config",
           "--no-session-persistence", "--setting-sources", ""]
    if effort:
        cmd += ["--effort", effort]
    if extra:
        cmd += extra
    cwd = WORK / "cwd"
    cwd.mkdir(parents=True, exist_ok=True)
    p = subprocess.run(cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, cwd=cwd, timeout=timeout)
    try:
        return json.loads(p.stdout)
    except Exception:
        return {"is_error": True, "result": (p.stdout or "")[-2000:] + (p.stderr or "")[-2000:], "total_cost_usd": 0}


def parse_json_text(txt):
    txt = txt.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", txt, re.S)
    if m:
        txt = m.group(1).strip()
    if not txt.startswith("{"):
        i = txt.find("{")
        txt = txt[i:] if i >= 0 else txt
    j = txt.rfind("}")
    return json.loads(txt[: j + 1])


def load_index():
    idx = {}
    with open(KO / "data" / "transcripts_v2.jsonl") as f:
        for line in f:
            r = json.loads(line)
            idx[r["id"]] = r
    dates = {}
    dpath = WORK / "dates.tsv"
    if dpath.exists():
        for line in dpath.read_text().splitlines():
            parts = line.split("\t")
            if len(parts) >= 5 and parts[1] not in ("NA", "NA\n"):
                dates[parts[0]] = dict(upload_date=parts[1], channel=parts[2], views=parts[3], duration=parts[4])
    return idx, dates


def tx_text(vid):
    return (RAW_TX / f"{vid}.txt").read_text(errors="replace")


def tx_body(text):
    """Strip the header block (title/channel/url/provider) from a raw transcript file."""
    lines = text.splitlines()
    i = 0
    hdr = re.compile(r"^(#|Channel:|Video:|Provider:|Source:|Title:|URL:|Status:|Language:)")
    while i < len(lines) and i < 10 and (hdr.match(lines[i]) or not lines[i].strip()):
        i += 1
    return "\n".join(lines[i:]).strip()
