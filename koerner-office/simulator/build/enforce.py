"""Deterministic overrides: make constraint values mirror the kill codes and structured scores in the reports
(LLM tags sometimes ignored them; spot-check found e.g. K0 kills tagged with a 3-month moat)."""
import csv, re
from pathlib import Path
A = Path(__file__).resolve().parents[2] / "analysis"
v8 = {r["cid"]: r for r in csv.DictReader(open(A/"v8/ideas_scored.csv"))}
v10s = {}
for m in re.finditer(r"^\| (L\d+) \|(.*)$", open(A/"v10/SCORES.md").read(), re.M):
    cols = [c.strip() for c in m.group(2).split("|")]
    v10s[m.group(1)] = {"automation": int(cols[4]), "moat": int(cols[5])}
def setc(r, k, s, v=None, why="", keepv=False):
    c = r["c"].setdefault(k, {})
    c["s"] = s
    if not keepv: c["v"] = v
    c["r"] = (why + " | " + c.get("r", "")).strip(" |")[:200]
def enforce(r, ledger):
    c = r["c"]; n = 0
    lv = (ledger.get("verdict") or ""); lr = ledger.get("reason") or ""
    vtxt = " ".join(" ".join(x.get("reasons") or []) for x in r.get("verdicts") or [])
    codes = set(re.findall(r"\b([KCB]\d)\b", lv)) | (set(re.findall(r"\b(K\d)\b", lr)) if "kill" in lv else set()) | set(re.findall(r"\b(K\d) kill", lr))
    if "K0" in codes:
        m = c.get("moat", {}); setc(r, "moat", "hard", min(m.get("v") or 2, 2), "Report K0: moat gate failed"); n += 1
    if codes & {"K2", "K4"}: setc(r, "crowded", "hard", c.get("crowded", {}).get("v"), f"Report {'/'.join(sorted(codes & {'K2','K4'}))}: crowded"); n += 1
    if "K3" in codes: setc(r, "platform", "hard", c.get("platform", {}).get("v") or "platform owner/partner", "Report K3: platform owner serves it"); n += 1
    if "K5" in codes: setc(r, "claim_age", "hard", c.get("claim_age", {}).get("v"), "Report K5: payment evidence >18 months old"); n += 1
    if "K6" in codes: setc(r, "dead_demand", "hard", True, "Report K6: demand gone"); n += 1
    if "K1" in codes:
        m = re.search(r"automation share is (\d+)%", lr)
        if m: setc(r, "automation", "hard" if int(m.group(1)) < 50 else "soft", int(m.group(1)), "Report K1: automation share"); n += 1
        if re.search(r"hours", lr, re.I) and not m: setc(r, "hours", "hard", max(c.get("hours", {}).get("v") or 8, 6), "Report K1: hours (est. if no figure)"); n += 1
        if re.search(r"local", lr, re.I): setc(r, "local", "hard", True, "Report K1: sells to local businesses"); n += 1
        if re.search(r"face|personal brand", lr, re.I): setc(r, "face", "hard", True, "Report K1: needs face/brand"); n += 1
        if re.search(r"cold|outreach|PECR", lr, re.I): setc(r, "outreach", "hard", "unlawful_cold", "Report K1: cold/unlawful outreach"); n += 1
    if "C9" in codes:
        h = c.get("hours", {}).get("v"); setc(r, "hours", "hard", h if (h and h > 5) else 8, "Checklist C9: no plausible <=5 h/wk handover (8 = est.)"); n += 1
    if codes & {"C7", "B5"}: setc(r, "face", "hard", True, "Checklist C7/B5: depends on seller face/brand"); n += 1
    if codes & {"C2", "C3", "B3", "B6"}: setc(r, "economics", "hard", "/".join(sorted(codes & {"C2","C3","B3","B6"})), "Listing economics: revenue/profit floor, price multiple or decline"); n += 1
    if "C1" in codes:
        e = c.get("evidence", {}); setc(r, "evidence", "hard" if (e.get("v") or 0) <= 1 else "soft", min(e.get("v") if e.get("v") is not None else 1, 1), "Checklist C1: revenue not verified"); c["evidence"]["count"] = e.get("count"); n += 1
    m = re.search(r"missing=(\d+)", lr)
    if "too many missing" in lv: setc(r, "diligence", "hard", f"{m.group(1) if m else '>3'} of 9 checklist rows missing", "v11 checklist: too many rows missing from the listing"); n += 1
    else: c.setdefault("diligence", {"s": "pass", "v": None, "r": "No missing-info kill"})
    c.setdefault("economics", {"s": "pass" if r.get("track") == "buy" else "unknown", "v": None, "r": "No listing-economics kill"})
    # structured scores
    if r["id"] in v8:
        x = v8[r["id"]]; f = x["fails"]
        setc(r, "automation", "hard" if int(x["automation_share"]) < 50 else ("soft" if int(x["automation_share"]) < 60 else "pass"), int(x["automation_share"]), "v8 scored automation share", )
        setc(r, "hours", "hard" if float(x["hours_per_week"]) > 5 else "pass", float(x["hours_per_week"]), "v8 scored hours/week")
        setc(r, "interest", "hard" if int(x["fit"]) < 4 else ("soft" if int(x["fit"]) < 6 else "pass"), int(x["fit"]), "v8 fit score")
        setc(r, "local", "hard" if x["local"] == "True" else "pass", x["local"] == "True", "v8 flag")
        setc(r, "face", "hard" if x["face"] == "True" else "pass", x["face"] == "True", "v8 flag")
        setc(r, "digital", "hard" if x["physical"] == "True" else "pass", x["physical"] != "True", "v8 physical-world flag")
        if x["uk_legal_risk"] == "True": setc(r, "legal", "hard", "UK legal risk (PECR etc.)", "v8 UK legal-risk flag")
        if x["stale"] == "True": setc(r, "claim_age", "hard", c.get("claim_age", {}).get("v"), "v8 stale-evidence flag")
        n += 1
    m = re.match(r"V10-(L\d+)", r["id"])
    if m and m.group(1) in v10s:
        s = v10s[m.group(1)]
        setc(r, "automation", "hard" if s["automation"] < 50 else ("soft" if s["automation"] < 60 else "pass"), s["automation"], "v10 SCORES automation %")
        c["moat"]["score"] = s["moat"]
        if s["moat"] < 4: setc(r, "moat", "hard", min(c["moat"].get("v") or 2, 2), f"v10 SCORES moat {s['moat']}/10 (<4 = K0)")
        n += 1
    return n
