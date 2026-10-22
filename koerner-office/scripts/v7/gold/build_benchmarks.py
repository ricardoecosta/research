#!/usr/bin/env python3
"""Extract numeric business claims and generate benchmarks.csv / BENCHMARKS.md."""
from __future__ import annotations

import csv
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V7 = ROOT / "analysis" / "v7"
CSV_OUT = V7 / "benchmarks.csv"
MD_OUT = V7 / "BENCHMARKS.md"

NUM = r"\d[\d,]*(?:\.\d+)?"
SCALE = r"(?:(?:\s*(?:k|m|b)(?![a-z])|\s*(?:thousand|million|billion)\b))?"
CURRENCY = r"(?:USD|US\$|CAD|AUD|GBP|EUR|[$£€])"
NUMBER_RE = re.compile(
    rf"(?P<currency>{CURRENCY})?\s*(?P<value>{NUM})(?P<scale>{SCALE})"
    rf"(?:\s*(?:-|–|—|to)\s*(?P<currency2>{CURRENCY})?\s*(?P<value2>{NUM})(?P<scale2>{SCALE}))?",
    re.IGNORECASE,
)
TIME_RE = re.compile(r"\b(days?|weeks?|months?|years?|hours?|minutes?|quarters?)\b", re.IGNORECASE)
MONEY_TAIL_RE = re.compile(r"\b(dollars?|USD|GBP|pounds?|euros?)\b", re.IGNORECASE)


FIELDS = [
    "metric", "value", "value_max", "unit", "currency", "category", "idea_name",
    "first_hand_or_hearsay", "hypothetical", "video_id", "idea_local_id", "source_type",
    "claim", "source_text", "source_quote", "quote_verified", "claimant",
]
KNOWN_CURRENCIES = {"USD", "GBP", "EUR", "CAD", "AUD", "NZD", "JPY", "CNY", "CHF", "INR", "SGD", "ZAR", "BRL", "MXN", "KRW", "AED", "unknown"}


def nfloat(value):
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def multiplier(scale):
    s = (scale or "").strip().casefold()
    return {"k": 1_000, "thousand": 1_000, "m": 1_000_000, "million": 1_000_000,
            "b": 1_000_000_000, "billion": 1_000_000_000}.get(s, 1)


def currency_name(raw):
    if not raw:
        return None
    return {"$": "USD", "US$": "USD", "£": "GBP", "€": "EUR"}.get(raw, raw.upper())


def text_currency(text, match_start):
    around = text[max(0, match_start - 18):match_start + 55]
    if re.search(r"\bUSD\b|\bUS dollars?\b", around, re.I):
        return "USD"
    if re.search(r"\bGBP\b|\bpounds?\b", around, re.I):
        return "GBP"
    if re.search(r"\bAUD\b|\bAustralian dollars?\b", around, re.I):
        return "AUD"
    if re.search(r"\bCAD\b|\bCanadian dollars?\b", around, re.I):
        return "CAD"
    if re.search(r"\bEUR\b|\beuros?\b", around, re.I):
        return "EUR"
    return None


def infer_unit(text, end, metric):
    tail = text[end:end + 36].lstrip()
    tests = [
        (r"^(?:%|percent\b)", "percent"),
        (r"^(?:per\s+|/)month\b|^monthly\b|^months?\b", "per month"),
        (r"^(?:per\s+|/)year\b|^annual(?:ly)?\b|^yearly\b|^years?\b", "per year"),
        (r"^(?:per\s+|/)week\b|^weekly\b|^weeks?\b", "per week"),
        (r"^(?:per\s+|/)day\b|^daily\b|^days?\b", "per day"),
        (r"^(?:per\s+|/)hour\b|^hours?\b", "hours"),
        (r"^minutes?\b", "minutes"), (r"^(?:paying\s+)?views?\b", "views"),
        (r"^(?:paying\s+)?users?\b", "users"), (r"^customers?\b", "customers"),
        (r"^subscribers?\b", "subscribers"), (r"^sign.?ups?\b", "sign-ups"),
        (r"^downloads?\b", "downloads"), (r"^employees?\b", "employees"),
        (r"^(?:per\s+)?leads?\b", "leads"), (r"^(?:per\s+)?clicks?\b", "clicks"),
    ]
    for pattern, unit in tests:
        if re.search(pattern, tail, re.I):
            return unit
    return "as stated"


def text_numbers(text, metric, currency_only=False, time_only=False):
    """Return literal numeric observations without interpreting prose numbers."""
    if not text:
        return []
    out = []
    for match in NUMBER_RE.finditer(text):
        raw_cur = match.group("currency") or match.group("currency2")
        end = match.end()
        after = text[end:end + 24]
        if currency_only and not raw_cur and not MONEY_TAIL_RE.search(after):
            continue
        if time_only:
            before = text[max(0, match.start() - 18):match.start()]
            after = text[end:end + 18]
            before_match = re.search(r"\b(days?|weeks?|months?|years?|hours?|minutes?|quarters?)\s+(?:about\s+|~\s*)?$", before, re.I)
            after_match = re.match(r"\s*(?:about\s+|~\s*)?(days?|weeks?|months?|years?|hours?|minutes?|quarters?)\b", after, re.I)
            time_match = before_match or after_match
            if time_match is None:
                continue
            unit = time_match.group(1).lower()
        else:
            unit = infer_unit(text, end, metric)
        low = float(match.group("value").replace(",", "")) * multiplier(match.group("scale"))
        hi_raw = match.group("value2")
        scale1, scale2 = match.group("scale"), match.group("scale2")
        if hi_raw and not (scale1 or "").strip() and (scale2 or "").strip():
            low *= multiplier(scale2)
        hi = float(hi_raw.replace(",", "")) * multiplier(scale2) if hi_raw else None
        cur = currency_name(raw_cur) or text_currency(text, match.start())
        literal = match.group(0).strip()
        out.append({"value": low, "value_max": hi, "currency": cur, "unit": unit, "literal": literal})
    return out


def guess_metric(text, default="other"):
    t = text.casefold()
    checks = [
        (r"\bmrr\b", "mrr"), (r"\barr\b", "arr"), (r"revenue|sales\b", "revenue"),
        (r"\bprofit\b|net income", "profit"), (r"conversion|convert(?:ed|s)?", "conversion_rate"),
        (r"\bchurn\b|cancellations?", "churn"),
        (r"\bexit multiple\b|\bsale multiple\b|\bvaluation multiple\b", "exit_multiple"),
        (r"\bcac\b|customer acquisition cost|cost per acquisition|cost per lead", "cac"),
        (r"ad spend|advertising cost|paid ads? cost", "ad_cost"),
        (r"\bmargin\b", "margin"), (r"customers?|users?|members?|subscribers?|sign.?ups?", "customers"),
        (r"valuation|multiple|\b\d+(?:\.\d+)?x\b", "valuation"),
        (r"sale price|sold for|exit", "sale_price"), (r"\bprice\b|priced|costs?\s+\$|\$\s*\d", "price"),
        (r"\bcost\b|spend|ad spend|startup", "cost"),
        (r"traffic|views?|downloads?|visits?", "traffic"),
        (r"hours?|minutes?|days?|weeks?|months?|years?", "hours"),
    ]
    for pattern, metric in checks:
        if re.search(pattern, t):
            return metric
    return default


def normalized_claim_metric(claim):
    raw = claim.get("metric") or "other"
    text = claim.get("claim") or ""
    lowered = text.casefold()
    if re.search(r"\bexit multiple\b|\bsale multiple\b|\bvaluation multiple\b|\b\d+(?:\.\d+)?x\s*(?:revenue|profit|ebitda|arr)\b", lowered):
        return "exit_multiple"
    if re.search(r"\bcac\b|customer acquisition cost|cost per acquisition|cost per lead", lowered):
        return "cac"
    if re.search(r"ad spend|advertising cost|paid ads? cost", lowered) and raw in {"other", "cost", "price"}:
        return "ad_cost"
    return guess_metric(text, raw) if raw == "other" else raw


def evidence_label(first_hand):
    if first_hand is True:
        return "first-hand"
    if first_hand is False:
        return "hearsay"
    return "unknown"


def row_base(video_id, idea_id, idea, record, metric, value, value_max, unit, currency,
             evidence="unknown", hypothetical=None, source_type="", claim="", source_text="",
             source_quote="", quote_verified=None, claimant=""):
    if currency and str(currency).upper() not in KNOWN_CURRENCIES:
        non_currency = str(currency).strip()
        currency = None
        if non_currency.casefold() in {"%", "percent", "pct"}:
            unit = "percent"
        elif non_currency and non_currency.casefold() not in str(unit or "").casefold():
            unit = f"{non_currency} {unit or ''}".strip()
    if unit and str(unit).strip() == "%":
        unit = "percent"
    return {
        "metric": metric or "other",
        "value": value,
        "value_max": value_max,
        "unit": unit or "unknown",
        "currency": currency or "unknown",
        "category": (idea or {}).get("category") or "unknown",
        "idea_name": (idea or {}).get("name") or "unspecified / transcript-level",
        "first_hand_or_hearsay": evidence,
        "hypothetical": "yes" if hypothetical is True else ("no" if hypothetical is False else "unknown"),
        "video_id": video_id,
        "idea_local_id": idea_id or "unknown",
        "source_type": source_type,
        "claim": claim,
        "source_text": source_text,
        "source_quote": source_quote,
        "quote_verified": "yes" if quote_verified is True else ("no" if quote_verified is False else "unknown"),
        "claimant": claimant or "unknown",
    }


def merge_source(row, source_type, source_text):
    types = set((row["source_type"] or "").split("|"))
    types.add(source_type)
    row["source_type"] = "|".join(sorted(x for x in types if x))
    if source_text and source_text not in row["source_text"]:
        row["source_text"] = (row["source_text"] + " | " + source_text).strip(" |")


def extract_rows():
    rows = []
    records = [json.loads(line) for line in (V7 / "learnings.jsonl").open(encoding="utf-8")]
    for record in records:
        video_id = record["video"]["id"]
        ideas = {idea["local_id"]: idea for idea in record.get("ideas", [])}
        index = defaultdict(list)

        # Structured metric claims are the primary source. Preserve their own
        # first-hand/hypothetical labels and verbatim quote field exactly.
        for claim in record.get("metric_claims", []):
            idea_id = claim.get("idea_local_id")
            idea = ideas.get(idea_id)
            val = claim.get("value") or {}
            metric = normalized_claim_metric(claim)
            quote_obj = claim.get("quote") or {}
            quote = quote_obj.get("text") or ""
            values = []
            if val.get("amount") is not None:
                values = [{"value": val["amount"], "value_max": val.get("amount_max"),
                           "currency": val.get("currency"), "unit": val.get("unit")}]
            else:
                # Some extractors leave amount null even when a numeric figure
                # is present in the claim/quote. Recover only literal digits.
                values = text_numbers(quote or claim.get("claim", ""), metric)
            for value in values:
                row = row_base(
                    video_id, idea_id, idea, record, metric, value["value"], value.get("value_max"),
                    value.get("unit") or val.get("unit"), value.get("currency") or val.get("currency"),
                    evidence_label(claim.get("first_hand")), claim.get("hypothetical"), "metric_claim",
                    claim.get("claim", ""), quote if quote else "",
                    quote, quote_obj.get("verified"), claim.get("claimant", ""),
                )
                rows.append(row)
                key = (idea_id, metric, row["value"], row["value_max"], row["currency"], row["unit"])
                index[key].append(row)

        # Price points are kept even when there is no linked metric claim. When
        # a structured price claim already records the same point, combine the
        # provenance to avoid counting the same observation twice.
        for idea_id, idea in ideas.items():
            for point in (idea.get("pricing") or {}).get("price_points", []):
                if point.get("amount") is None:
                    label = point.get("label") or ""
                    for value in text_numbers(label, "price"):
                        rows.append(row_base(
                            video_id, idea_id, idea, record, "price", value["value"],
                            value.get("value_max"), point.get("unit") or value["unit"],
                            point.get("currency") or value.get("currency"), "unknown", None,
                            "price_point_text", "", label,
                        ))
                    continue
                amount, amount_max = point.get("amount"), point.get("amount_max")
                currency = point.get("currency")
                unit = point.get("unit") or "unknown"
                key = (idea_id, "price", amount, amount_max, currency or "unknown", unit)
                candidates = index.get(key, [])
                # Some structured records use a slightly different unit label;
                # value/currency still identify a useful source match.
                if not candidates:
                    candidates = [r for (iid, metric, value, vmax, cur, _u), found in index.items()
                                  if iid == idea_id and metric == "price" and value == amount
                                  and vmax == amount_max and cur == (currency or "unknown") for r in found]
                label = point.get("label") or ""
                if candidates:
                    merge_source(candidates[0], "price_point", label)
                    continue
                rows.append(row_base(
                    video_id, idea_id, idea, record, "price", amount, amount_max, unit, currency,
                    "unknown", None, "price_point", "", label, "", None, "",
                ))

            # Free-text startup/timing fields carry useful numbers not always
            # repeated in metric_claims. Parse only explicit currency figures
            # for costs and explicit digit-plus-time-unit figures for timing.
            for field, metric, money_only, time_only in [
                ("startup_cost", "startup_cost", True, False),
                ("time_to_first_revenue", "time_to_first_revenue", False, True),
            ]:
                text = idea.get(field) or ""
                for value in text_numbers(text, metric, currency_only=money_only, time_only=time_only):
                    rows.append(row_base(video_id, idea_id, idea, record, metric, value["value"],
                                         value.get("value_max"), value["unit"], value.get("currency"),
                                         "unknown", None, field, "", text))

        # Tool costs are transcript-level because the schema does not bind each
        # tool to an idea. Keep them instead of guessing an idea association.
        for tool in record.get("tools_mentioned", []):
            cost_text = tool.get("cost_stated") or ""
            for value in text_numbers(cost_text, "cost", currency_only=True):
                rows.append(row_base(video_id, None, None, record, "cost", value["value"],
                                     value.get("value_max"), value["unit"], value.get("currency"),
                                     "unknown", None, "tool_cost", "", f"{tool.get('name', 'tool')}: {cost_text}"))

    return rows


def number_text(value):
    if value is None:
        return ""
    n = float(value)
    return f"{int(n):,}" if n.is_integer() else f"{n:,.2f}".rstrip("0").rstrip(".")


def write_csv(rows):
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def summary_rows(rows, keys):
    # De-duplicate repeated representations of the same number in a transcript
    # for summary statistics only. The CSV retains each structured claim row.
    unique = {}
    for row in rows:
        if nfloat(row["value"]) is None:
            continue
        if row["hypothetical"] == "yes":
            continue
        identity = (row["video_id"], row["idea_local_id"], row["metric"], row["value"],
                    row["value_max"], row["currency"], row["unit"])
        unique.setdefault(identity, row)
    grouped = defaultdict(list)
    for row in unique.values():
        grouped[tuple(row.get(k, "unknown") or "unknown" for k in keys)].append(row)
    result = []
    for key, observations in sorted(grouped.items(), key=lambda x: tuple(str(z).casefold() for z in x[0])):
        by_unit = defaultdict(list)
        for row in observations:
            by_unit[(row["currency"], row["unit"])].append(row)
        unit_stats = []
        for (currency, unit), group in sorted(by_unit.items(), key=lambda x: tuple(str(z).casefold() for z in x[0])):
            unit_stats.append({"currency": currency, "unit": unit, **summarize_group(group)})
        result.append({"group": key, "units": unit_stats})
    return result


def summarize_group(group):
    lows = [float(r["value"]) for r in group]
    highs = [float(r["value_max"]) if nfloat(r["value_max"]) is not None else float(r["value"]) for r in group]
    point_lows = [float(r["value"]) for r in group
                  if nfloat(r["value_max"]) is None or nfloat(r["value_max"]) == float(r["value"])]
    first = sum(r["first_hand_or_hearsay"] == "first-hand" for r in group)
    hearsay = sum(r["first_hand_or_hearsay"] == "hearsay" for r in group)
    unknown = len(group) - first - hearsay
    n = len(group)
    flag = "small sample" if n < 5 else ("limited sample" if n < 10 else "")
    return {
        "n": n, "low": min(lows), "high": max(highs),
        "median_low": statistics.median(point_lows) if point_lows else None,
        "n_points": len(point_lows), "n_ranges": n - len(point_lows),
        "first_hand": first, "hearsay": hearsay, "unknown": unknown, "flag": flag,
    }


def md_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ") if value is not None else "—"


def make_summary_table(items, grouped_keys):
    headings = list(grouped_keys) + ["Currency / unit subgroups (n; range; median lower figure; FH / hearsay / unknown; sample)"]
    lines = ["| " + " | ".join(headings) + " |", "|" + "|".join(["---"] * len(headings)) + "|"]
    for item in items:
        group = item["group"]
        label_values = [str(v) for v in group]
        pieces = []
        for stats in item["units"]:
            median = number_text(stats["median_low"]) if stats["median_low"] is not None else "no point values"
            evidence = f"{stats['first_hand']}/{stats['hearsay']}/{stats['unknown']}"
            sample = f"; {stats['flag']}" if stats["flag"] else ""
            pieces.append(
                f"{stats['currency']} / {stats['unit']}: n={stats['n']}; "
                f"{number_text(stats['low'])}–{number_text(stats['high'])}; median {median}; "
                f"FH/hearsay/unknown {evidence}{sample}"
            )
        cells = label_values + ["<br>".join(pieces)]
        lines.append("| " + " | ".join(md_cell(x) for x in cells) + " |")
    return "\n".join(lines)


def write_markdown(rows):
    overall = summary_rows(rows, ["metric"])
    by_category = summary_rows(rows, ["category", "metric"])
    lines = [
        "# Benchmarks extracted from v7 transcripts",
        "",
        "The full row-level extraction is in [`benchmarks.csv`](benchmarks.csv). Each row is tied to a video ID and an idea/category when the source schema provides one. Metric claims preserve the claim text, source quote, extractor's first-hand/hypothetical labels and quote-verification flag. Price points, startup-cost/timing fields and stated tool costs are also included when they contain explicit numeric figures; unit-economics summaries are represented by their structured metric claims to avoid counting the same restatement twice.",
        "",
        f"**Rows:** {len(rows):,}. These are transcript claims and structured extractions, not independently verified business accounts. `unknown` means the record did not mark a claim first-hand or hearsay. For free-text cost/time fields and price labels with a missing structured amount, only literal digits and explicit units/currencies were extracted; phrases such as ‘a few hundred dollars’ remain in source text but were not converted into a guessed value.",
        "",
        "**Summary method.** Each row groups by metric (and category in the second table); the cell keeps separate currency/unit subgroups so unlike amounts are not mixed. Ranges remain in the CSV; each displayed range spans the smallest lower figure to the largest upper figure in that subgroup. Median uses point observations only and is the median lower figure. Hypothetical claims are excluded from summary statistics but remain in the CSV. Rows are deduplicated by video, idea, metric, value, currency and unit for summaries only. Samples under five are flagged.",
        "",
        "## Across all categories",
        "",
        make_summary_table(overall, ["metric"]),
        "",
        "## By category",
        "",
        make_summary_table(by_category, ["category", "metric"]),
        "",
        "## Field notes",
        "",
        "- `first_hand_or_hearsay` comes from the transcript-learning record's `first_hand` flag. It describes who the speaker says the number belongs to; it does not validate the number.",
        "- Rows with no linked idea use `unspecified / transcript-level` and category `unknown`; the schema does not identify a specific business for those tool-cost claims. Startup-cost and time-to-first-revenue text fields are separate rows from similarly sized metric claims because they carry a distinct source field and metric label.",
        "- `metric` retains the source's metric label, including `other`, `traffic` and `hours`. Explicit churn, CAC or exit-multiple claims are not normalized into a new category unless the source claim labels them that way; the original claim and quote stay in the CSV.",
        "- Currency is preserved as stated. No currency conversion, inflation adjustment, or annualization is applied.",
        "",
    ]
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")


def main():
    rows = extract_rows()
    write_csv(rows)
    write_markdown(rows)
    print(f"Wrote {CSV_OUT} ({len(rows):,} rows) and {MD_OUT}.")


if __name__ == "__main__":
    main()
