#!/usr/bin/env python3
"""Build analysis/v7/HIDDEN_GEMS.md from the v7 transcript records.

The candidate list and analyst notes are deliberately explicit; evidence, quotes,
rank, cluster support, category, and automation scores are looked up in the data.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V7 = ROOT / "analysis" / "v7"
OUTPUT = V7 / "HIDDEN_GEMS.md"
ICO_PECR = (
    "https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-"
    "electronic-communications/guide-to-pecr/electronic-and-telephone-"
    "marketing/electronic-mail-marketing/"
)
ICO_LAWFUL_BASIS = "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/"
TOP10_CLUSTER_IDS = {
    "C0263", "C0116", "C0106", "C0266", "C1099", "C0482", "C0066", "C0084", "C0050",
    "C0114", "C0404", "C0063", "C0059", "C0111", "C0310", "C0691", "C0438", "C1119",
    "C0441", "C0681", "C0160", "C0188", "C0187", "C0186", "C0051", "C0265", "C0129",
    "C0431", "C0044", "C0122", "C0703", "C0108",
}


# These are the shortlist judgments. Every evidence selector below must resolve
# to a verified, first-hand, non-hypothetical quote in learnings.jsonl.
GEMS = [
    {
        "cid": "C1098",
        "evidence": [
            {"video": "22Jpzt683jw", "needle": "3 months we hit like 10k MR"},
            {"video": "22Jpzt683jw", "needle": "more than a million"},
        ],
        "automation_note": "Self-serve product ingestion, answer delivery, subscription billing and routine support are software-shaped. Acquisition is the weak point: the source used founder-led publicity and relationships, so Ricardo would need a repeatable inbound or B2B limited-company route.",
        "legal_note": "B2B SaaS can be sold in the UK. Keep outbound email to verified limited-company subscribers under Ricardo's rule; do not cold-message sole traders or individual support teams. Apply UK GDPR to any uploaded customer documents and make retention/security controls explicit.",
        "comparison": "Nearest to TOP10 #9 (UK-vertical micro-SaaS), but this is a documentation-grounded support-agent product, not a cheaper clone of a vertical incumbent. It is a distinct product wedge; the single-founder evidence is stronger than its frequency rank suggests.",
        "judgment": "Best software-shaped candidate in this set. The transcript gives an early MRR milestone and later ARR, but the product's growth channel and competitive position need independent validation.",
        "top5": True,
    },
    {
        "cid": "C1095",
        "evidence": [
            {"video": "LrLDsvbdPr0", "needle": "We're at 11K MRR"},
            {"video": "LrLDsvbdPr0", "needle": "usually our monthly plan is like $8.49"},
        ],
        "automation_note": "Speech capture, transcription, subscriptions and most onboarding can run in the product. The source rates acquisition through search, the Chrome marketplace and tutorial content; support and accessibility testing still need careful escalation.",
        "legal_note": "A UK launch should give clear audio-data and deletion information, minimize stored recordings, and avoid implying medical diagnosis. Use inbound search/marketplace/content. Do not contact disabled users or sole traders through unsolicited email, SMS or DMs.",
        "comparison": "Related to TOP10 #1 (ASO-first app portfolio) only at the app-store layer. This is a focused dictation product for older and disabled users, with a London-based operator and a documented SEO/Chrome distribution mix rather than a portfolio strategy.",
        "judgment": "Strongest UK-fit signal: the source describes a UK-run product, concrete recurring revenue and accessible software. Validate speech accuracy, privacy expectations and support load before choosing a user group.",
        "top5": True,
    },
    {
        "cid": "C0467",
        "evidence": [
            {"video": "s9aLA4IOSZE", "needle": "700,000 monthly active users"},
            {"video": "s9aLA4IOSZE", "needle": "30,000, $35,000 in programmatic"},
        ],
        "automation_note": "Daily game delivery, score sharing, billing and most support can be automated. The source's acquisition also relies on social posts and guest question-setters; replace any unsolicited creator DMs with opt-in partnerships and player-driven sharing.",
        "legal_note": "Use licensed or original questions, images and team references. If UK analytics or advertising cookies access/store information on devices, implement the relevant PECR consent controls and UK GDPR notices. Do not cold-DM individual players or creators.",
        "comparison": "Different from TOP10 #4 (utility/calculator sites) and #3 (SEO directories/content): this is an interactive daily game with a sharing loop and advertising/subscription revenue, not a static tool or directory.",
        "judgment": "The strongest media/software hybrid: one operator reports meaningful usage and ad income. The main caveat is that the creator had a large social audience and question-setter relationships, so the traffic result may not transfer to a new operator.",
        "top5": True,
    },
    {
        "cid": "C0450",
        "evidence": [
            {"video": "oaXnY1YExjE", "needle": "Wrestle AI the first month did 17K"},
            {"video": "oaXnY1YExjE", "needle": "10 bucks a month 60 for a year"},
        ],
        "automation_note": "Video analysis and recurring billing are automatable; the cluster's weighted automation score is 75/100. The source's growth depended on creator promotion, paid ads and sports-specific product judgment. Prefer inbound creator applications/opt-in affiliates and capped ads; do not automate cold DMs to athletes or sole traders.",
        "legal_note": "Obtain rights to uploaded footage, set retention/deletion rules, and take extra care if users are minors. Use clear subscription terms. For UK acquisition, rely on inbound and opt-in partners; any cold email must target a verified limited company.",
        "comparison": "Adjacent to TOP10 #1 (small apps), but the wedge is AI feedback for a specific sport and the revenue evidence comes from creator-led sports apps. This is a focused product, not an ASO portfolio play.",
        "judgment": "Good technical fit and unusually concrete first-month evidence for a one-video cluster. The result is creator- and ad-dependent, so validate one sport with a no-code demo and opt-in testers before building a broad platform.",
        "top5": True,
    },
    {
        "cid": "C1094",
        "evidence": [
            {"video": "NuYO7DWzlaM", "needle": "The first month, it made $66"},
            {"video": "NuYO7DWzlaM", "needle": "currently averaging around $2,000 to $3,000 a day"},
        ],
        "automation_note": "The product is on-device, with app-store discovery, software delivery and billing. The scored automation result is 85/100. Security incidents, store review and support for lost access still need a human escalation path.",
        "legal_note": "A UK app should make encryption and recovery claims precise, minimize telemetry, and explain what data stays on-device. Have UK privacy/security counsel review any cloud backup, account recovery or law-enforcement workflow. Acquisition can stay inbound through App Store search and SEO.",
        "comparison": "Related to TOP10 #1 only as a mobile app. Its differentiated idea is an encrypted, on-device file/photo vault, not an ASO portfolio; its reported later revenue makes this a high-variance security product worth examining separately.",
        "judgment": "High automation and strong technical fit, with a very large later claim from one source. The first-month-to-current jump is a single-source report, not a forecast.",
        "top5": True,
    },
    {
        "cid": "C1134",
        "evidence": [
            {"video": "SiRlIMtZygI", "needle": "I don't want to pay $100 at once"},
            {"video": "SiRlIMtZygI", "needle": "start with $9"},
        ],
        "automation_note": "A lightweight analytics SaaS can automate collection, dashboards, signup, billing and most support. The source's score is 80/100, but acquisition was not described and the tool's support/acquisition sub-scores are lower than delivery.",
        "legal_note": "Use privacy-preserving, cookieless analytics where possible. If the implementation stores or reads information on a user's device, handle PECR consent; explain UK GDPR roles, retention and processor terms. Acquire through inbound search or marketplaces, not unsolicited consumer messages.",
        "comparison": "Near TOP10 #4 (calculator/utility sites) only as a self-serve web tool. This is a paid site-analytics product with a reported pricing test, not an ad-supported utility page.",
        "judgment": "Interesting as an indie-maker product, but the evidence is price feedback rather than revenue or customers. Keep it behind the five stronger opportunities until distribution and privacy-light differentiation are clear.",
        "top5": False,
    },
    {
        "cid": "C1096",
        "evidence": [
            {"video": "LrLDsvbdPr0", "needle": "that one grew to 5K MRR"},
        ],
        "automation_note": "The extracted idea describes no-code community analytics with automated delivery and billing; the data-derived automation score is 71/100. The source says growth stalled for lack of marketing, and it gives no acquisition channel.",
        "legal_note": "Treat community member data as personal data: minimize collection, set retention limits and document controller/processor roles. Until a lawful inbound route is demonstrated, do not assume cold outreach is viable; do not cold-message community members or sole traders.",
        "comparison": "Not the public listing/lead directory in TOP10 #3. It is analytics software for private online communities, but the evidence is only a one-sentence mention and does not establish how customers were acquired.",
        "judgment": "Worth a discovery interview, not a build. The mention reports MRR but explicitly says marketing stalled; the idea has no described acquisition engine.",
        "top5": False,
    },
    {
        "cid": "C0711",
        "evidence": [
            {"video": "y_ON1Qbb274", "needle": "test, the official certification test, I think at the time, was 39 or 49"},
            {"video": "y_ON1Qbb274", "needle": "It's 59. That's actually become"},
        ],
        "automation_note": "An assessment, course checkout and lesson delivery are mostly self-serve; the source score is 75/100. The source also reports a broken checkout and no purchases from the initial funnel, so conversion and support readiness remain unproven.",
        "legal_note": "Do not describe a private test as an accredited or employer-recognized qualification unless that is true. Give clear course scope, refund/digital-content terms and marketing consent. Use paid ads or opt-in acquisition; no cold messages to individuals.",
        "comparison": "Related to TOP10 #7 (technical templates and AI skill packs), but this is a scored assessment funnel with courses/certification rather than downloadable developer assets. It is not yet validated as a UK credential.",
        "judgment": "The self-serve format fits, but this is a weak gem: the source documents pricing and a funnel failure, not proven sales. Only pursue after a UK buyer/employer test and checkout test.",
        "top5": False,
    },
    {
        "cid": "C0225",
        "evidence": [
            {"video": "MyNXdDskh6c", "needle": "within two hours, I had 18 people sign up"},
        ],
        "automation_note": "A narrow downloadable kit can be pre-sold, delivered and billed automatically; the scored automation result is 79/100. The evidence comes from a warm audience/community validation exercise, not an autonomous acquisition channel.",
        "legal_note": "Use an opt-in waitlist or a marketplace. Do not copy the transcript's suggested one-to-one cold messaging to individuals or sole traders. State delivery dates and refund terms for pre-sales, and handle digital VAT appropriately.",
        "comparison": "Adjacent to TOP10 #7 (technical templates), but the example is a specific workflow kit for solo bookkeepers, not developer templates or prompt packs. The presale result is a validation tactic more than proof of repeatable distribution.",
        "judgment": "The best evidence for a low-cost validation method, but the 18 sign-ups were for a podcasting course in a warm setting. The example bookkeeper kit itself did not have measured sales.",
        "top5": False,
    },
    {
        "cid": "C0060",
        "evidence": [
            {"video": "lG5U30gKCaY", "needle": "we sell these for 19 bucks"},
            {"video": "HOosrT6vj_Y", "needle": "pay five bucks a month"},
        ],
        "automation_note": "Agents can research, draft and update business-plan packs; checkout and file delivery are simple to automate. The score is 73/100. The observed acquisition route is the creator's existing YouTube/newsletter audience, which Ricardo would have to replace with inbound search or marketplace demand.",
        "legal_note": "Use inbound content or an opt-in audience. Make clear that plans are informational, not regulated legal/financial advice; show update dates and limitations. Do not cold-DM prospective buyers.",
        "comparison": "Related to TOP10 #7 only as a digital download. These are business-specific plans and idea books for aspiring operators, rather than technical templates/AI skill packs for builders.",
        "judgment": "The repeated $19 price points and $5 membership are concrete, but sales rely on creator distribution. A search-led catalog could be tested; the transcript does not show Ricardo can reproduce the audience.",
        "top5": False,
    },
    {
        "cid": "C0087",
        "evidence": [
            {"video": "QIX0lnr3qfo", "needle": "make $50 to $500 for a Facebook reel"},
            {"video": "QIX0lnr3qfo", "needle": "between 10 cents and 30 cents per thousand views"},
        ],
        "automation_note": "Character generation, video variants, scheduling and reporting can be agent-assisted; the scored automation result is 74/100. Human review is needed for originality, misleading scenes, platform eligibility and monetization changes.",
        "legal_note": "Use original or licensed likenesses and music, label commercial content clearly, and follow the platform's AI-content and monetization rules. Use platform-native organic publishing; no unsolicited DMs to individuals or creators.",
        "comparison": "Near TOP10 #3 (content/SEO) as a media business, but the revenue model here is social-platform payout/brand content rather than search ads or affiliate pages. Platform-policy risk is much higher.",
        "judgment": "Promising automation surface, weaker business durability. The firsthand reel figures are specific, but platform payouts and creator accounts can change or lose eligibility.",
        "top5": False,
    },
    {
        "cid": "C0344",
        "evidence": [
            {"video": "XBAR_cbfjPQ", "needle": "$8,000 extra dollars a month"},
            {"video": "XBAR_cbfjPQ", "needle": "13 different languages"},
        ],
        "automation_note": "Translation, dubbing, track production and publishing are automatable after a source video exists; the score is 83/100. It does not remove the need to create or license the original content or review translation quality.",
        "legal_note": "Use only content and voices you own or have licensed, and correct mistranslations before publishing. Monetization is inbound/platform-based; do not acquire creators through unsolicited DMs.",
        "comparison": "Related to TOP10 #3 (content/SEO) as an audience business, but the distinctive mechanism is multilingual dubbing that monetizes existing videos in new markets, not a search site or directory.",
        "judgment": "A compelling add-on for someone who already owns a large video library. For Ricardo starting from zero, the missing content/audience asset makes it a watchlist item rather than a first build.",
        "top5": False,
    },
    {
        "cid": "C0346",
        "evidence": [
            {"video": "T-lKmpCrICM", "needle": "it takes two credits"},
        ],
        "automation_note": "Product research, AI-video assembly, posting and affiliate link reporting can be partly automated; the score is 76/100. Product accuracy, platform eligibility and creative performance need human review. The cost quote is not evidence of sales.",
        "legal_note": "TikTok Shop eligibility and terms vary by market. Label affiliate advertising clearly under UK rules, do not imply a product was personally tested if it was not, and label AI-generated content when required. Use platform discovery, not cold DMs.",
        "comparison": "Not covered by the TOP10's app, directory or template picks. It is creator-commerce content with per-sale commissions, but is less durable and more platform-dependent than a standalone product.",
        "judgment": "The workflow is agent-friendly, but the data contains only a small production-cost detail and a US-centred pitch. It needs UK-specific proof before it merits a build.",
        "top5": False,
    },
    {
        "cid": "C1106",
        "evidence": [
            {"video": "a8qQzY3a1us", "needle": "set for $20 a month"},
        ],
        "automation_note": "Consumer onboarding, reminders and subscriptions can be automated; the scored automation result is 84/100. Trust, privacy complaints and relationship-sensitive support make the human escalation burden higher than the score implies.",
        "legal_note": "Message content can include personal data about both partners. Before any message ingestion, establish a lawful basis, minimize retention and provide clear privacy information; a user subscription is not blanket permission to process another person's data. Use paid/inbound acquisition, never unsolicited relationship DMs.",
        "comparison": "A consumer subscription app, unlike TOP10 #9's vertical B2B micro-SaaS. The only evidence is a stated price, so it is far behind the TOP10's evidence base.",
        "judgment": "A technically automatable idea with a serious privacy and trust burden. Do not build around reading private messages unless a UK privacy review supports the design.",
        "top5": False,
    },
    {
        "cid": "C1114",
        "evidence": [
            {"video": "QTEs5eBBl3c", "needle": "over eight million partners onto our database"},
        ],
        "automation_note": "Partner search, fit scoring and draft generation are software-shaped; the extraction-derived score is 77/100. The cold-start problem, data-rights work and customer acquisition are not answered by the one mention.",
        "legal_note": "Do not assume a large contact database may be reused. Verify source, lawful basis, transparency and suppression controls before processing UK personal data. Any electronic marketing to individual creators/sole traders needs consent; cold B2B email is limited to corporate subscribers under Ricardo's rule.",
        "comparison": "Adjacent to TOP10 #3 (directories) because both organize discoverable supply, but this is private partnership matching and fit scoring rather than a public SEO listing directory.",
        "judgment": "Scale signal only. The partner count is a promotional company claim, with no stated revenue, price or UK data provenance. Do not treat it as a replicable solo-business result.",
        "top5": False,
    },
]


def load_data():
    records = {}
    for line in (V7 / "learnings.jsonl").open(encoding="utf-8"):
        row = json.loads(line)
        records[row["video"]["id"]] = row
    scored = {row["cid"]: row for row in json.loads((V7 / "ideas_scored.json").read_text(encoding="utf-8"))}
    ranks = {}
    with (V7 / "ideas_scored.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ranks[row["cid"]] = int(row["rank"])
    return records, scored, ranks


def find_quote(records, scored_row, selector):
    for member in scored_row["members"]:
        video_id, local_id = member["key"].split(":", 1)
        if video_id != selector["video"]:
            continue
        record = records[video_id]
        for claim in record["metric_claims"]:
            quote = claim.get("quote") or {}
            text = quote.get("text") or ""
            if claim.get("idea_local_id") != local_id:
                continue
            if not claim.get("first_hand") or claim.get("hypothetical") is True:
                continue
            if quote.get("verified") is not True:
                continue
            if selector["needle"].casefold() not in text.casefold():
                continue
            return record, claim
    raise ValueError(f"No verified first-hand quote for {scored_row['cid']}: {selector}")


def pct_parts(row):
    judge = row.get("judge") or {}
    automation = judge.get("automation") or {}
    names = [("acquisition", "Acq"), ("onboarding", "Onb"), ("delivery", "Del"), ("billing", "Bill"), ("support", "Sup")]
    values = []
    for key, label in names:
        score = (automation.get(key) or {}).get("score")
        if score is not None:
            values.append(f"{label} {score}/5")
    return ", ".join(values) if values else "extractor-estimated parts"


def render():
    records, scored, ranks = load_data()
    if len(GEMS) < 15 or len(GEMS) > 25:
        raise ValueError("Keep the shortlist between 15 and 25 entries")
    cids = [gem["cid"] for gem in GEMS]
    if len(set(cids)) != len(cids):
        raise ValueError("The shortlist contains duplicate clusters")
    overlap = set(cids) & TOP10_CLUSTER_IDS
    if overlap:
        raise ValueError(f"Shortlist overlaps TOP10 clusters: {sorted(overlap)}")
    for cid in cids:
        row = scored[cid]
        if row["n_videos"] > 1 and not any(member["depth"] == "mention" for member in row["members"]):
            raise ValueError(f"{cid} is neither a single-video idea nor mention-depth supported")
    lines = [
        "# Hidden gems: low-frequency ideas with concrete evidence",
        "",
        "This is a 15-idea review of clusters that are either backed by one video or include an idea mentioned in passing. The frequency rank and source count come from `ideas_scored.csv` / `ideas_scored.json`; quotes below are fetched directly from `learnings.jsonl` and must be marked verified, first-hand and non-hypothetical. Podcast claims are not independently audited.",
        "",
        f"**UK marketing screen.** I treated Ricardo's stated rule as binding: no unsolicited marketing SMS, WhatsApp or social DMs to individuals or sole traders; use cold email only for limited companies. ICO guidance also treats email, text and social direct messages as electronic mail and distinguishes individual from corporate subscribers ([ICO guidance on electronic mail marketing]({ICO_PECR})). Personal-data processing needs a valid lawful basis and transparent privacy information ([ICO guide to lawful basis]({ICO_LAWFUL_BASIS})).",
        "",
        "**How to read this list.** Automation figures are the catalogue's weighted scores, not a promise of unattended operation. Some entries are conditional watchlist items: the evidence is interesting but their source channel, traction, UK fit or privacy controls do not yet pass the bar for a build. The final five are the ones I would investigate first.",
        "",
        "## Shortlist",
        "",
    ]
    for n, gem in enumerate(GEMS, 1):
        row = scored[gem["cid"]]
        rank = ranks[gem["cid"]]
        members = row["members"]
        depth_counts = Counter(m["depth"] for m in members)
        mention_n = depth_counts.get("mention", 0)
        if row["n_videos"] == 1:
            under = f"One video supports this cluster, so a frequency-weighted score has only one source to count (cluster {gem['cid']}, rank {rank}, n_videos {row['n_videos']})."
        else:
            under = f"{mention_n} of {len(members)} idea mentions are depth=mention across {row['n_videos']} videos; frequency weighting dilutes this specific signal (cluster {gem['cid']}, rank {rank}, n_videos {row['n_videos']})."
        category = row.get("category", "other").replace("_", " ").title()
        video_label = "video" if row["n_videos"] == 1 else "videos"
        evidence_grade = {5: "A", 4: "B", 2.5: "C", 1: "D"}.get(row.get("best_evidence"), "n/a")
        lines.extend([
            f"### {n}. {row['name']}",
            "",
            f"**What it is.** {row['description']}",
            "",
            f"**Why it was underrated.** {under}",
            "",
            "**First-hand evidence from the transcript:**",
        ])
        for selector in gem["evidence"]:
            record, claim = find_quote(records, row, selector)
            quote = claim["quote"]["text"]
            lines.append(f"- `{record['video']['id']}` ({record['video']['title']}): “{quote}”")
        lines.extend([
            "",
            f"**Automation potential.** Catalogue score {row['automation_pct']}/100 ({pct_parts(row)}). {gem['automation_note']}",
            "",
            f"**UK legal and acquisition notes.** {gem['legal_note']}",
            "",
            f"**Compared with TOP10.** {gem['comparison']}",
            "",
            f"**Judgment.** {gem['judgment']}",
            "",
            f"*Data: cluster {gem['cid']} · rank {rank} · {row['n_videos']} {video_label} · category {category} · best evidence grade {evidence_grade}.*",
            "",
        ])

    top5 = [g for g in GEMS if g.get("top5")]
    if len(top5) != 5:
        raise ValueError("Exactly five entries must be marked top5")
    lines.extend(["## Top five gems", ""])
    for rank, gem in enumerate(top5, 1):
        row = scored[gem["cid"]]
        lines.append(f"{rank}. **{row['name']}** (`{gem['cid']}`): {gem['judgment']}")
    lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(GEMS)} ideas; quotes resolved from learnings.jsonl).")


if __name__ == "__main__":
    render()
