#!/usr/bin/env python3
"""Playbook scoring for SMB AI-gap scan rows. Implements every externally observable variable from
ai-support-agency-manual.md (10-factor /50, ICP, signals, disqualifiers), niche-ranking-uk-portugal.md
(12-factor /60) and clarityrelay-operating-brief.md (ICP/disqualifiers). See analysis/smb_ai_gap/SIGNALS.md.
Booleans only for contact-ish signals; nothing personal is stored.
Usage (rescore an existing scan CSV without re-crawling): smb_playbook_score.py scan.csv -o rescored.csv"""
import csv, re, sys, argparse
from collections import Counter

def _txt(html):
    t = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", html[:600_000])
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).lower()

KW = {  # signal -> regex over homepage text + link/sitemap URLs (EN/PT/ES)
    "compat_kw": r"compatib|dimming|dimmable|regula[cç]|ip ?6[5-8]|photometr|fotom[eé]tr|ldt|ies file",
    "warranty_kw": r"warrant|guarantee|garantia|garant[ií]a",
    "install_kw": r"install|instala[cç]|montaje|montagem|fitting guide",
    "new_products_kw": r"new[- ]products|new[- ]range|launch|novidades|lan[cç]amento|novedades|lanzamiento|what'?s new",
    "export_kw": r"export|worldwide|international|distributors?|distribuidor|exporta|global",
    "contact_form": r"<form[^>]*>(?:(?!</form>).){0,4000}<textarea",
    "leadership_page": r"/(our-)?team|/management|/leadership|/about(-us)?/(people|team)|/equipa|/equipo|/quem-somos|/quienes-somos",
    "manufacturer_kw": r"manufactur|fabricant|fabricamos|fabrico|f[aá]brica|produ[cç][aã]o pr[oó]pria|made in|designed and made",
    "receptionist_type": r"book (an )?appointment|dental|dentist|clinic|cl[ií]nica|salon|sal[aã]o|beauty|spa\b|restaurant|restaurante|cita previa|marcar consulta",
    "local_trade": r"\b(plumb|electrician|roofer|locksmith|handyman|canalizador|eletricista|electricista|fontanero|serving (the )?local|areas we cover|free quote|or[cç]amento gr[aá]tis|presupuesto gratis)",
    "regulated_data": r"patient|medical records|financial advice|solicitor|law firm|insurance broker|advogad|abogad|seguros",
}
KW = {k: re.compile(v, re.I | re.S) for k, v in KW.items()}

def page_signals(html, links, urls):
    """Extra observable signals from the homepage HTML + homepage links + sitemap URLs (booleans/counts)."""
    t = _txt(html); blob = t + "\n" + "\n".join(list(links)[:3000]) + "\n" + "\n".join(urls[:20000])
    s = {k: ("yes" if rx.search(html if k == "contact_form" else blob) else "no") for k, rx in KW.items()}
    for k in ("receptionist_type", "local_trade", "regulated_data", "manufacturer_kw"):  # business type: visible text only
        s[k] = "yes" if KW[k].search(t) else "no"
    langs = set(re.findall(r'hreflang=["\']([a-z]{2})', html, re.I)) | set(re.findall(r'/(en|pt|es|fr|de|it)(?:-[a-z]{2})?/', " ".join(urls[:5000]) + " ".join(links)))
    s["languages"] = len({l.lower() for l in langs}) or 1
    s["named_contact_present"] = "yes" if re.search(r"\b(director|manager|head of|diretor|gerente|responsable|jefe)\b", t) else "no"
    return s

def _b(r, k): return r.get(k) == "yes"
def _i(r, k):
    try: return int(float(r.get(k) or 0))
    except ValueError: return 0

def density_scores(rows):
    c = Counter((r["country"], r["sector"]) for r in rows)
    return {k: (5 if n >= 100 else 4 if n >= 50 else 3 if n >= 20 else 2 if n >= 10 else 1) for k, n in c.items()}

def score(r, density=None):
    """Returns dict of factor scores (None = not observable -> ask in discovery) + totals + disqualifiers."""
    if r.get("status") != "ok": return {}
    docs = _i(r, "sitemap_doc_urls") + _i(r, "homepage_doc_links") + _i(r, "homepage_pdf_links")
    ds, pdf, prod, urls_n = _i(r, "datasheet_links"), _i(r, "pdf_links"), _i(r, "sitemap_product_urls"), _i(r, "sitemap_urls")
    ct = r.get("chat_type", "none")
    # 2 knowledge complexity
    k = 1 + (docs >= 5) + (docs >= 25 or pdf >= 10 or ds >= 5) + (docs >= 100 or ds >= 25) + (sum(_b(r, x) for x in ("compat_kw", "warranty_kw", "install_kw")) >= 2)
    # 3 existing support team (public evidence only; absence = weak, not proof)
    sup = sum([_b(r, "tech_support_page"), _b(r, "support_email_present"), _b(r, "help_centre"), bool(r.get("chat") or r.get("helpdesk"))])
    team = 5 if _b(r, "support_hiring") and sup >= 2 else 4 if (_b(r, "support_hiring") or sup >= 3) else 3 if sup >= 1 else 2
    # 5 tech signal: public docs/help + old widget, no modern AI agent
    tech = 1 if ct == "ai_agent" else min(5, 2 + (_b(r, "help_centre") or _b(r, "faq_or_support_page")) + (docs >= 25 or pdf >= 10 or ds >= 5)
                                           + (ct in ("live_chat_non_ai", "ticket_helpdesk_only")) - (ct.startswith(("ai_capable", "custom"))))
    # 7 recurring need: catalogue breadth + launches + docs
    rec = 1 + (prod >= 20 or urls_n >= 200) + (prod >= 200) + _b(r, "new_products_kw") + (docs >= 25)
    # 9 low DIY risk (not solo/indie)
    solo = urls_n < 15 and not _b(r, "careers_page") and sup == 0 and r.get("source") == "OSM"
    diy = 1 if solo else 2 + (_b(r, "careers_page")) + (urls_n >= 100 or r.get("source") not in ("", "OSM")) + (sup >= 2)
    # 10 competitive whitespace (not a commodity receptionist market)
    ws = 1 if _b(r, "receptionist_type") and not _b(r, "manufacturer_kw") else 2 if _b(r, "local_trade") else 3 + _b(r, "manufacturer_kw") + (k >= 4)
    # 6 reachability (manual: association/chamber/warm intro) ; 12 ease of list building
    assoc = r.get("source") not in ("", "OSM")
    reach = 4 if assoc else 3
    lists = 5 if assoc else 3
    # 11 founder advantage (Ricardo: Portuguese, UK-based; Spanish adjacent)
    founder = {"PT": 5, "UK": 4, "ES": 3}.get(r.get("country"), 2)
    dens = (density or {}).get((r.get("country"), r.get("sector")))
    f = {"m1_ticket_volume": None, "m2_knowledge_complexity": min(5, k), "m3_existing_support_team": team,
         "m4_ability_to_pay": None, "m5_tech_signal": max(1, tech), "m6_reachability": reach, "m7_recurring_need": min(5, rec),
         "m8_prospect_density": dens, "m9_low_diy_risk": min(5, diy), "m10_competitive_whitespace": min(5, ws),
         "n6_async_reachability": None, "n11_founder_advantage": founder, "n12_ease_of_list_building": lists}
    m = [f[x] for x in f if x.startswith("m")]
    n = m[:5] + [f["n6_async_reachability"]] + m[6:] + [founder, lists]
    out = dict(f)
    for tag, vals, mx in (("manual50", m, 50), ("niche60", n, 60)):
        known = [v for v in vals if v is not None]
        out[f"{tag}_known"] = sum(known); out[f"{tag}_unknowns"] = len(vals) - len(known)
        out[f"{tag}_est"] = sum(known) + 3 * (len(vals) - len(known))   # unknowns filled at neutral 3
    dq = []
    if docs < 3 and pdf == 0 and ds == 0: dq.append("no_public_docs")
    if sup == 0 and not _b(r, "careers_page") and urls_n < 30: dq.append("no_visible_support_function")
    if solo: dq.append("solo_or_micro")
    if _b(r, "receptionist_type") and not _b(r, "manufacturer_kw"): dq.append("receptionist_type_business")
    if _b(r, "local_trade") and not _b(r, "manufacturer_kw"): dq.append("local_trade")
    if _b(r, "regulated_data"): dq.append("regulated_data")
    if ct == "ai_agent": dq.append("already_has_ai_agent")
    out["disqualifiers"] = ";".join(dq)
    out["likely_enterprise"] = "yes" if urls_n >= 15000 or _i(r, "sitemap_doc_urls") >= 1000 else "no"  # size proxy; m4/size still unknown
    hard1 = any(f[x] == 1 for x in ("m2_knowledge_complexity", "m3_existing_support_team", "m9_low_diy_risk"))
    out["manual_pass_est"] = "yes" if out["manual50_est"] >= 35 and not hard1 and not dq else "no"
    out["manual_strong_est"] = "yes" if out["manual50_est"] >= 40 and out["manual_pass_est"] == "yes" else "no"
    return out

def rescore(rows):
    d = density_scores(rows)
    for r in rows: r.update({k: ("unknown" if v is None else v) for k, v in score(r, d).items()})
    return rows

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("inp"); ap.add_argument("-o", required=True); a = ap.parse_args()
    rows = rescore(list(csv.DictReader(open(a.inp))))
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(a.o, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} rescored -> {a.o}")
