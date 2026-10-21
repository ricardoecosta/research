#!/usr/bin/env python3
"""Scan local-business websites for chat widgets, support bots, booking tools,
WhatsApp buttons, call tracking and basic website gaps.

Input: a CSV with columns `name,url` (extra columns are kept), or a plain text
file with one URL per line.
Output: a CSV (one row per site) and, optionally, a Markdown table.

Two modes:
  static (default)  fetches the homepage (and one same-site "contact" page)
                    with requests and greps the HTML. Fast, but misses widgets
                    injected later by Google Tag Manager or a page builder.
  --render          loads each page in headless Chrome (Playwright), waits for
                    late scripts, and greps the final DOM plus every network
                    request URL. Slower, far fewer false negatives.

Usage:
  python3 chat_widget_scanner.py sites.csv -o results.csv --md results.md --render

What it cannot see: whether a business has missed-call text-back or an
answering service on its phone line. That is invisible from the website; test
it by calling (see the plan, probe P1b).

Only public homepages and contact pages are fetched, one request at a time per
site, with an honest User-Agent. Respect robots.txt and site terms when you
scale this up.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse

import requests

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36 widget-scanner/0.1 (+contact: ricardo)")

# category -> {label: [regex, ...]}. Patterns run case-insensitively over the
# page HTML plus (in --render mode) all network request URLs.
SIGNATURES: dict[str, dict[str, list[str]]] = {
    "chat": {
        "Intercom": [r"widget\.intercom\.io", r"js\.intercomcdn\.com", r"intercomSettings"],
        "Tidio": [r"code\.tidio\.co", r"tidioChatApi"],
        "Drift": [r"js\.driftt\.com", r"drift\.com/include"],
        "LiveChat": [r"cdn\.livechatinc\.com", r"__lc\.license", r"livechat\.com/tracking"],
        "Crisp": [r"client\.crisp\.chat", r"\$crisp\s*=", r"CRISP_WEBSITE_ID"],
        "tawk.to": [r"embed\.tawk\.to", r"Tawk_API"],
        "Facebook Messenger plugin": [r"xfbml\.customerchat", r"class=[\"']fb-customerchat"],
        "HubSpot chat": [r"js\.usemessages\.com", r"hubspot.*conversations-embed"],
        "GoHighLevel/LeadConnector chat": [r"widgets\.leadconnectorhq\.com", r"chat-widget/loader",
                                            r"leadconnectorhq\.com/loader", r"msgsndr\.com"],
        "Zendesk/Zopim": [r"static\.zdassets\.com/ekr", r"zopim"],
        "Freshchat": [r"wchat\.freshchat\.com", r"fw-cdn\.com/.*widget"],
        "Olark": [r"static\.olark\.com"],
        "Smartsupp": [r"smartsuppchat\.com", r"smartsupp\.com/loader"],
        "JivoChat": [r"code(-jvs)?\.jivosite\.com", r"code\.jivo\.ru", r"jivo_api"],
        "Chatra": [r"call\.chatra\.io"],
        "Podium": [r"connect\.podium\.com", r"podium-webchat"],
        "Birdeye": [r"birdeye\.com/embed", r"birdeye.*webchat"],
        "Trengo": [r"static\.widget\.trengo\.eu"],
        "Wix Chat": [r"wix-chat", r"chat\.wixapps\.net"],
        "Zoho SalesIQ": [r"salesiq\.zoho"],
        "Userlike": [r"userlike-cdn-widgets", r"userlike\.com/widget"],
        "Chaport": [r"app\.chaport\.com"],
        "Pure Chat": [r"purechat\.com"],
        "Tars/Landbot": [r"landbot\.io", r"hellotars\.com"],
    },
    "ai_bot": {
        "Chatbase": [r"chatbase\.co/embed", r"www\.chatbase\.co/"],
        "Voiceflow": [r"cdn\.voiceflow\.com", r"voiceflow\.com/widget"],
        "Botpress": [r"cdn\.botpress\.cloud", r"mediafiles\.botpress\.cloud"],
        "DocsBot": [r"docsbot\.ai/"],
        "ManyChat": [r"manychat\.com"],
        "Chatling": [r"chatling\.ai"],
        "Elfsight AI chatbot": [r"elfsight.*ai-chatbot"],
        "Zapier chatbot": [r"interfaces\.zapier\.com.*chatbot"],
        "Lindy/other embed": [r"lindy\.ai/embed"],
    },
    "whatsapp": {
        "WhatsApp link/button": [r"wa\.me/\d", r"api\.whatsapp\.com/send", r"whatsapp://send",
                                 r"web\.whatsapp\.com/send"],
        "WhatsApp chat plugin": [r"joinchat", r"click-to-chat", r"elfsight.*whatsapp", r"wa-chat-widget",
                                 r"getbutton\.io", r"whatshelp\.io"],
    },
    "booking": {
        "Calendly": [r"assets\.calendly\.com", r"calendly\.com/[a-z0-9_-]+"],
        "Acuity": [r"acuityscheduling\.com", r"as\.me/"],
        "SimplyBook.me": [r"simplybook\.(me|it)"],
        "Setmore": [r"setmore\.com"],
        "Square Appointments": [r"squareup\.com/appointments", r"book\.squareup\.com"],
        "Housecall Pro": [r"housecallpro\.com"],
        "Jobber": [r"getjobber\.com", r"clienthub\.getjobber"],
        "ServiceM8": [r"servicem8\.com"],
        "Tradify": [r"tradifyhq\.com"],
        "Fergus": [r"fergus\.com/.*(book|enquiry)"],
        "YouCanBook.me": [r"youcanbook\.me"],
        "Microsoft Bookings": [r"outlook\.office365\.com/(owa/calendar|book)", r"bookings\.office"],
        "Google appointment schedule": [r"calendar\.app\.google", r"calendar\.google\.com/calendar/appointments"],
        "LeadConnector booking": [r"/widget/booking/", r"leadconnectorhq\.com/widget/booking"],
        "HubSpot meetings": [r"meetings\.hubspot\.com"],
        "Zoho Bookings": [r"zohobookings"],
        "TidyCal": [r"tidycal\.com"],
        "Booksy/Fresha": [r"booksy\.com", r"fresha\.com"],
        "Bookly/Amelia (WP)": [r"wp-content/plugins/(bookly|ameliabooking)"],
    },
    "call_tracking": {
        "CallRail": [r"cdn\.callrail\.com"],
        "ResponseiQ/CallPage": [r"responseiq\.com", r"callpage\.io"],
        "Mediahawk/Infinity": [r"mediahawk", r"infinitycdn\.com", r"ictcdn"],
        "WhatConverts": [r"whatconverts\.com"],
    },
}

FORM_HINTS = [r"<form[^>]*>", r"wpcf7", r"wpforms", r"gform_", r"formspree\.io", r"jotform",
              r"typeform\.com", r"hsforms", r"elementor-form", r"ninja-forms", r"forminator",
              r"wixforms|wix-forms|\"form\"\s*:\s*\{", r"forms\.office\.com", r"docs\.google\.com/forms",
              r"leadconnectorhq\.com/widget/form", r"fluentform"]
TAG_MANAGER = [r"googletagmanager\.com/gtm\.js", r"GTM-[A-Z0-9]{4,}"]


@dataclass
class Result:
    name: str
    url: str
    final_url: str = ""
    status: str = ""
    https: bool = False
    mobile_viewport: bool = False
    tel_link: bool = False
    contact_form: bool = False
    tag_manager: bool = False
    copyright_year: str = ""
    found: dict[str, list[str]] = field(default_factory=dict)
    error: str = ""

    @property
    def has_live_chat_or_bot(self) -> bool:
        return bool(self.found.get("chat") or self.found.get("ai_bot"))

    @property
    def has_any_engagement(self) -> bool:
        return any(self.found.get(k) for k in ("chat", "ai_bot", "whatsapp", "booking"))

    def row(self) -> dict[str, str]:
        f = self.found
        return {
            "name": self.name, "url": self.url, "final_url": self.final_url, "status": self.status,
            "https": yn(self.https), "mobile_viewport": yn(self.mobile_viewport),
            "tel_link": yn(self.tel_link), "contact_form": yn(self.contact_form),
            "tag_manager": yn(self.tag_manager), "copyright_year": self.copyright_year,
            "chat": "; ".join(f.get("chat", [])), "ai_bot": "; ".join(f.get("ai_bot", [])),
            "whatsapp": "; ".join(f.get("whatsapp", [])), "booking": "; ".join(f.get("booking", [])),
            "call_tracking": "; ".join(f.get("call_tracking", [])),
            "has_chat_or_bot": yn(self.has_live_chat_or_bot),
            "has_chat_bot_whatsapp_or_booking": yn(self.has_any_engagement),
            "error": self.error,
        }


def yn(b: bool) -> str:
    return "yes" if b else "no"


def detect(blob: str, res: Result) -> None:
    for cat, tools in SIGNATURES.items():
        hits = [label for label, pats in tools.items() if any(re.search(p, blob, re.I) for p in pats)]
        if hits:
            res.found[cat] = sorted(set(res.found.get(cat, []) + hits))
    res.mobile_viewport |= bool(re.search(r"<meta[^>]+name=[\"']viewport", blob, re.I))
    res.tel_link |= bool(re.search(r"href=[\"']tel:", blob, re.I))
    res.contact_form |= any(re.search(p, blob, re.I) for p in FORM_HINTS)
    res.tag_manager |= any(re.search(p, blob) for p in TAG_MANAGER)
    years = re.findall(r"(?:©|&copy;|copyright)\s*(?:[^<]{0,40}?)((?:19|20)\d\d)", blob, re.I)
    if years:
        res.copyright_year = max(years)


def contact_link(html: str, base: str) -> str | None:
    for href in re.findall(r"href=[\"']([^\"'#]+)[\"']", html, re.I):
        if re.search(r"contact|get-in-touch|enquir|quote", href, re.I):
            u = urljoin(base, href)
            if urlparse(u).netloc == urlparse(base).netloc:
                return u
    return None


def scan_static(name: str, url: str, timeout: int = 20) -> Result:
    res = Result(name=name, url=url)
    s = requests.Session()
    s.headers["User-Agent"] = UA
    try:
        r = s.get(url, timeout=timeout, allow_redirects=True)
        res.final_url, res.status = r.url, str(r.status_code)
        res.https = r.url.startswith("https://")
        html = r.text
        detect(html, res)
        c = contact_link(html, r.url)
        if c:
            try:
                detect(s.get(c, timeout=timeout).text, res)
            except requests.RequestException:
                pass
    except requests.RequestException as e:
        res.status, res.error = "error", type(e).__name__
    return res


def scan_render(items: list[tuple[str, str]], wait_ms: int = 6000) -> list[Result]:
    from playwright.sync_api import sync_playwright

    out: list[Result] = []
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
        except Exception:
            browser = p.chromium.launch(headless=True, executable_path="/usr/bin/google-chrome")
        for name, url in items:
            res = Result(name=name, url=url)
            ctx = browser.new_context(user_agent=UA, viewport={"width": 390, "height": 844})
            page = ctx.new_page()
            reqs: list[str] = []
            page.on("request", lambda rq: reqs.append(rq.url))
            try:
                resp = page.goto(url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(wait_ms)
                res.final_url = page.url
                res.status = str(resp.status) if resp else "?"
                res.https = page.url.startswith("https://")
                html = page.content()
                detect(html + "\n" + "\n".join(reqs), res)
                c = contact_link(html, page.url)
                if c:
                    try:
                        reqs.clear()
                        page.goto(c, timeout=30000, wait_until="domcontentloaded")
                        page.wait_for_timeout(2500)
                        detect(page.content() + "\n" + "\n".join(reqs), res)
                    except Exception:
                        pass
            except Exception as e:  # noqa: BLE001 - report and continue
                res.status, res.error = "error", type(e).__name__
            finally:
                ctx.close()
            out.append(res)
            print(f"  scanned {name}: {res.status}", file=sys.stderr)
    return out


def load(path: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    with open(path, newline="") as f:
        first = f.readline()
        f.seek(0)
        if "," in first and "url" in first.lower():
            for row in csv.DictReader(f):
                items.append((row.get("name") or row["url"], row["url"].strip()))
        else:
            for line in f:
                if line.strip():
                    items.append((line.strip(), line.strip()))
    return [(n, u if u.startswith("http") else "https://" + u) for n, u in items]


def merge(a: Result, b: Result) -> Result:
    """Union of static and rendered findings (render wins on status)."""
    for cat, labels in a.found.items():
        b.found[cat] = sorted(set(b.found.get(cat, []) + labels))
    for attr in ("mobile_viewport", "tel_link", "contact_form", "tag_manager"):
        setattr(b, attr, getattr(a, attr) or getattr(b, attr))
    b.copyright_year = max(a.copyright_year, b.copyright_year)
    if b.status == "error" and a.status != "error":
        b.status, b.final_url, b.https, b.error = a.status, a.final_url, a.https, ""
    return b


def summarise(results: list[Result]) -> str:
    ok = [r for r in results if r.status not in ("error",) and not r.status.startswith(("4", "5"))]
    n = len(ok)
    if not n:
        return "No sites loaded."
    pct = lambda k: f"{sum(k(r) for r in ok)}/{n} ({100 * sum(k(r) for r in ok) / n:.0f}%)"
    lines = [
        f"Sites loaded: {n} of {len(results)}",
        f"No live chat or AI bot: {pct(lambda r: not r.has_live_chat_or_bot)}",
        f"No chat, bot, WhatsApp or online booking: {pct(lambda r: not r.has_any_engagement)}",
        f"No online booking: {pct(lambda r: not r.found.get('booking'))}",
        f"Has WhatsApp button: {pct(lambda r: bool(r.found.get('whatsapp')))}",
        f"No contact form found: {pct(lambda r: not r.contact_form)}",
        f"No mobile viewport tag: {pct(lambda r: not r.mobile_viewport)}",
        f"No tap-to-call link: {pct(lambda r: not r.tel_link)}",
        f"Not HTTPS: {pct(lambda r: not r.https)}",
    ]
    return "\n".join(lines)


def markdown(results: list[Result]) -> str:
    hdr = "| # | Business | Site | Chat / bot | WhatsApp | Booking | Form | Mobile | Tap-to-call |\n|---|---|---|---|---|---|---|---|---|\n"
    rows = []
    for i, r in enumerate(results, 1):
        f = r.found
        chat = "; ".join(f.get("chat", []) + f.get("ai_bot", [])) or "none"
        if r.status == "error" or r.status.startswith(("4", "5")):
            chat = f"(site failed: {r.error or r.status})"
        host = urlparse(r.url).netloc.replace("www.", "")
        rows.append(f"| {i} | {r.name} | {host} | {chat} | {'yes' if f.get('whatsapp') else '—'} | "
                    f"{'; '.join(f.get('booking', [])) or '—'} | {yn(r.contact_form)} | {yn(r.mobile_viewport)} | {yn(r.tel_link)} |")
    return hdr + "\n".join(rows) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("-o", "--out", default="widget_scan.csv")
    ap.add_argument("--md", help="also write a Markdown table here")
    ap.add_argument("--render", action="store_true", help="also load pages in headless Chrome")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()

    items = load(a.input)
    t0 = time.time()
    with ThreadPoolExecutor(a.workers) as ex:
        static = list(ex.map(lambda nu: scan_static(*nu), items))
    results = static
    if a.render:
        rendered = scan_render(items)
        results = [merge(s, r) for s, r in zip(static, rendered)]

    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].row().keys()))
        w.writeheader()
        for r in results:
            w.writerow(r.row())
    summary = summarise(results)
    if a.md:
        with open(a.md, "w") as f:
            f.write(markdown(results) + "\n```\n" + summary + "\n```\n")
    print(summary)
    print(f"({len(items)} sites in {time.time() - t0:.0f}s; wrote {a.out})")


if __name__ == "__main__":
    main()
