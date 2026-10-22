#!/usr/bin/env python3
"""v7 extraction via Codex CLI (gpt-6-luna, xhigh) instead of Claude.

Reuses extract.py's build_prompt + SYSTEM (system text is prepended to the prompt, since
`codex exec` has no system flag). Writes /tmp/v7/raw/<id>.json in the shape finalize.py expects,
then finalizes it. Resumable: ids that already have a raw file are skipped.

Usage: python codex_extract.py [--ids a,b] [--limit N] [--workers 4]
Log: /tmp/v7/codex_extract.log
"""
import argparse, concurrent.futures as cf, datetime as dt, json, os, subprocess, sys, tempfile, threading, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import *
from extract import SYSTEM, build_prompt
import finalize as F

MODEL = "gpt-6-luna"
CODEX = os.path.expanduser("~/.local/bin/codex")
LOG = WORK / "codex_extract.log"
TIMEOUT = int(os.environ.get("CODEX_TIMEOUT_S", "2400"))
_loglock = threading.Lock()


class Busy(Exception):
    """Transient model capacity / rate-limit error: back off and retry without using an attempt."""

EXTRA = (
    "\n\nIMPORTANT FOR THIS RUN: you are running as a pure text extractor. Do not run any shell "
    "commands, do not read files, do not browse. Everything you need is in this message. "
    "Every quote 'text' MUST be copied character-for-character from inside <transcript>, "
    "including mis-heard words and odd grammar; never paraphrase, tidy, or merge sentences inside a quote. "
    "Every enum field must use one of the schema's listed values exactly; if none fits, use \"other\". "
    "Reply with the single JSON object only.\n"
)


def log(msg):
    line = f"{dt.datetime.now():%m-%d %H:%M:%S} {msg}"
    with _loglock:
        with open(LOG, "a") as f:
            f.write(line + "\n")
    print(line, flush=True)


def run_codex(prompt):
    """Run codex exec with the prompt on stdin; return (answer_text, usage, seconds)."""
    cwd = WORK / "codex_cwd"; cwd.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, dir=cwd) as out:
        out_path = out.name
    cmd = [CODEX, "exec", "--skip-git-repo-check", "--ephemeral", "-s", "read-only",
           "--disable", "hooks", "-m", MODEL, "-c", 'model_reasoning_effort="xhigh"',
           "--color", "never", "--json", "-o", out_path, "-C", str(cwd), "-"]
    t0 = time.time()
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         text=True, cwd=cwd, start_new_session=True)
    try:
        so, se = p.communicate(prompt, timeout=TIMEOUT)  # writes prompt then closes stdin
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, 9); p.communicate()
        raise TimeoutError(f"codex timed out after {TIMEOUT}s")
    secs = time.time() - t0
    answer, usage, errs = None, {}, []
    for line in (so or "").splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        it = ev.get("item") or {}
        if ev.get("type") == "item.completed" and it.get("type") in ("agent_message", "assistant_message"):
            answer = it.get("text") or answer
        if ev.get("type") == "turn.completed":
            usage = ev.get("usage") or {}
        if ev.get("type") in ("error", "turn.failed"):
            errs.append(json.dumps(ev)[:300])
    try:
        lm = Path(out_path).read_text()
        if lm.strip():
            answer = lm
        os.unlink(out_path)
    except Exception:
        pass
    if not answer and any(k in " ".join(errs).lower() for k in ("capacity", "rate limit", "429", "overloaded", "try again")):
        raise Busy("; ".join(errs)[:200])
    if not answer:
        raise ValueError(f"no agent message rc={p.returncode} errs={errs} stderr={(se or '')[-300:]}")
    return answer, usage, secs


def repair_enums(vid, rec):
    """Map out-of-vocabulary enum values (e.g. 'sales', 'events_experiences') to 'other' in the raw file
    and re-finalize. Only touches enum errors whose allowed list contains 'other'. Returns the new record."""
    rp = WORK / "raw" / f"{vid}.json"
    raw = json.loads(rp.read_text())
    fixed = 0
    for e in F.VALIDATOR.iter_errors(rec):
        path = list(e.absolute_path)
        if e.validator != "enum" or "other" not in (e.validator_value or []) or not path or path[0] in ("video", "extraction"):
            continue
        o = raw
        try:
            for k in path[:-1]:
                o = o[k]
            o[path[-1]] = "other"; fixed += 1
        except (KeyError, IndexError, TypeError):
            pass
    if not fixed:
        return rec
    raw.setdefault("_meta", {})["enum_repairs"] = fixed
    rp.write_text(json.dumps(raw, ensure_ascii=False, indent=1))
    return F.finalize(vid)


def extract_one(vid, meta):
    rp = WORK / "raw" / f"{vid}.json"
    if rp.exists():
        return vid, "cached"
    prompt = SYSTEM + EXTRA + "\n\n" + build_prompt(vid, meta, tx_text(vid))
    best = None  # (n_errors, -rate, data, attempt)
    last_err = ""
    for attempt in range(1, 4):  # first try + up to 2 retries
        try:
            for wait in range(40):  # transient capacity errors do not count as attempts
                try:
                    ans, usage, secs = run_codex(prompt)
                    break
                except Busy as b:
                    log(f"{vid} busy ({b}); backing off {min(60 * (wait + 1), 600)}s")
                    time.sleep(min(60 * (wait + 1), 600))
            else:
                raise ValueError("model busy for too long")
            data = parse_json_text(ans)
            if not isinstance(data, dict):
                raise ValueError("answer is not a JSON object")
            data["_meta"] = dict(model=MODEL, extracted_at=dt.datetime.now().isoformat(timespec="seconds"),
                                 cost_usd=0, attempt=attempt)
            rp.write_text(json.dumps(data, ensure_ascii=False, indent=1))
            rec = F.finalize(vid)
            if rec["extraction"]["schema_errors"]:
                rec = repair_enums(vid, rec)
                data = json.loads(rp.read_text())
            errs = rec["extraction"]["schema_errors"]
            qv = rec["extraction"]["quote_verification"]
            res = {"total_cost_usd": 0, "duration_ms": secs * 1000,
                   "usage": {"input_tokens": usage.get("input_tokens", 0),
                             "output_tokens": usage.get("output_tokens", 0),
                             "cache_read_input_tokens": usage.get("cached_input_tokens", 0)}}
            log_cost("extract", vid, MODEL, res, "ok" if not errs else f"schema_err:{len(errs)}")
            log(f"{vid} attempt={attempt} {secs:.0f}s schema_errors={len(errs)} quotes={qv['verified']}/{qv['quotes']}" + (f" first_err={errs[0][:200]}" if errs else ""))
            cand = (len(errs), -(qv["rate"] or 0), data, attempt)
            if best is None or cand[:2] < best[:2]:
                best = cand
            if not errs:
                break
            last_err = "; ".join(errs[:3])
            rp.unlink(missing_ok=True)
        except Exception as e:
            last_err = str(e)[:300]
            rp.unlink(missing_ok=True)
            log(f"{vid} attempt={attempt} FAIL {last_err}")
            log_cost("extract", vid, MODEL, {"total_cost_usd": 0}, "fail:" + last_err[:60].replace(",", ";").replace("\n", " "))
    if best is None:
        return vid, "fail " + last_err
    if best[0]:
        data = best[2]
        rp.write_text(json.dumps(data, ensure_ascii=False, indent=1))
        F.finalize(vid)
        return vid, f"ok_with_schema_errors({best[0]})"
    return vid, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", default="")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    (WORK / "raw").mkdir(parents=True, exist_ok=True)
    idx, _ = load_index()
    ids = args.ids.split(",") if args.ids else [l.strip() for l in (WORK / "ids.txt").read_text().split() if l.strip()]
    todo = [i for i in ids if not (WORK / "raw" / f"{i}.json").exists()]
    if args.limit:
        todo = todo[: args.limit]
    log(f"START {len(todo)} to extract with codex {MODEL} xhigh, workers={args.workers}")
    with cf.ThreadPoolExecutor(args.workers) as ex:
        futs = {ex.submit(extract_one, v, idx.get(v, {})): v for v in todo}
        for f in cf.as_completed(futs):
            try:
                vid, st = f.result()
            except Exception as e:
                vid, st = futs[f], f"crash {e}"
            log(f"DONE {vid} {st} raw_total={len(list((WORK / 'raw').glob('*.json')))}")
    log("END")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--repair"]:  # fix enum errors in already-extracted codex files
        for p in sorted(OUT.glob("*.json")):
            r = json.loads(p.read_text())
            if r["extraction"].get("model") == MODEL and r["extraction"].get("schema_errors") and (WORK / "raw" / f"{p.stem}.json").exists():
                r2 = repair_enums(p.stem, r)
                print(p.stem, len(r["extraction"]["schema_errors"]), "->", len(r2["extraction"]["schema_errors"]))
    else:
        main()
