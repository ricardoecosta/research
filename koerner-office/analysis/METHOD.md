# Research method

This is the official method for turning video transcripts into ranked, validated business ideas. Part 1 covers the core pipeline, from ingest to validation. Part 2 (to follow) covers everything after that.

It records what the v7 run learned. Each step below is a rule, not a suggestion.

---

## Part 1: Core pipeline

### 1. Clean transcripts at ingest

Before any mining, strip the content that isn't about a business:

- filler and throat-clearing ("so yeah", "um", intros, outros, "smash that like button")
- sponsor reads and ad segments
- tangents unrelated to any business (personal stories, banter, off-topic chat)

Keep the cleaned text and the original side by side, and record which lines were removed and why. Quotes and line references in later steps always point at the original, so citations stay checkable.

### 2. Split multi-business videos at ingest

Many videos cover several businesses ("5 side hustles that…", interview round-ups). Split them into **one record per business** before mining. Each record keeps:

- the parent video ID and title
- the start and end time or line of its segment
- the business name or description as the speaker gives it

Never let one record mix two businesses, because that blurs problems, numbers and evidence across ideas.

### 3. Tag publish date, and flag specifics

- Tag every record with its video's **publish date**. Evidence ages: prices, platform rules, tool landscapes and "nobody is doing this" claims go stale fast.
- **Flag** any idea that names a specific tool, price, platform or marketplace (for example "Shopify app", "£49/month", "Fiverr gig", "uses Zapier"). These claims are the most time-sensitive and must be rechecked against the web at validation (step 10).

### 4. Mine with structured output

Mining must return structured records (JSON with a fixed schema), never free text. Each idea record includes:

| Field | Rule |
|---|---|
| `stated_problem` | The speaker's problem **in their own words**, quoted, captured **before** any interpretation or reframing. |
| `idea` | Our interpretation of the business, written after `stated_problem`. |
| `citation` | The exact minute (timestamp) or line number in the original transcript for every idea and every key claim. No citation, no idea. |
| `claims` | Revenue, price, customer and channel numbers as stated, each with its own citation. |
| `feature_request` | Negative tag: `true` when the "idea" is really a feature request for an existing tool (for example "I wish Notion did X"). These are kept for reference but don't count as standalone businesses. |
| `publish_date`, `specifics_flag` | Carried over from step 3. |

### 5. UK legal filter at mining

Apply UK law while mining, not at the end:

- Under PECR, unsolicited marketing by **cold text (SMS), WhatsApp or direct message to individuals or sole traders is banned**. Cold email is only allowed to limited companies, and only with an opt-out.
- Any idea whose acquisition channel **relies** on those banned channels is flagged `uk_legal_risk` straight away, with the reason. Flagged ideas are not quietly dropped; they're carried forward with the flag so the reason for the kill is visible.
- Note other obvious UK rules where relevant: TPS/CTPS for calls, UK GDPR, the DMCC Act subscription rules, and the 2003 Conduct of Employment Agencies Regulations.

### 6. Quote verification

Every quote a model produces is checked against the original transcript:

- Fuzzy-match each quote to the source text. A score of **90 out of 100 or better** passes.
- A quote that fails is marked **unverified**. Unverified quotes are kept for audit but **are not evidence**: they can't support a score, a cluster or a claim.
- Report the verification pass rate for every run.

### 7. Cluster by distinct videos

Group similar ideas into clusters, then measure support as the **number of distinct videos** backing each cluster, not the raw number of mentions. One enthusiastic video that repeats an idea ten times is one source. Record which clusters are single-video, because single-video ideas carry far less weight.

### 8. Score

Score every cluster on four separate dimensions, each with a short written reason:

| Score | Scale | Meaning |
|---|---|---|
| Success in 12 months | out of 10 | Realistic odds of meaningful revenue within a year. |
| Agent-runnability | out of 10 | How much of the day-to-day a team of AI agents can run. |
| Fit | out of 10 | Fit with the owner's interests, skills, hours and hard constraints. |
| Automation share | percentage | The realistic share of the total work that is automated, including sales, support and admin, not just the core product. |

Keep the four scores separate. Never collapse them into one number before reporting.

### 9. Report the automation distribution

Report how automation shares are distributed **across all ideas** (for example a histogram, or the count at 40% or more, 50%, 60% and 70%), not just how many passed a threshold. The shape of the distribution shows which constraint is doing the killing, and how much a looser bar would unlock.

### 10. Validation gate: high effort and web-checked

- The top slice of ideas goes through **high-effort, web-checked validation**: current competitors, prices, platform rules, demand signals and the legal position, each with a link.
- This is the **gate**: an idea is only "validated" once it passes this step.
- It is never a redo of a low-effort pass. A low-effort review can help triage, but it doesn't count as validation and its result can't be passed off as one.

### 11. Always validate the most-cited ideas

Whatever their rank, the **most-cited clusters** (the most distinct videos backing them) always go through step 10. Popular ideas that score badly still need a web-checked reason for being killed, so that a big signal is never dropped because of a scoring quirk.

---

*Part 2 (to follow) covers what happens after validation.*

---

## FALLBACKS

When we hit a wall, use this order.

- **Bulk mining and cheap passes:** Codex on Ricardo's Mac first, then pi, then Researcher (Grok Bot) if both are out.
- **Reviews and validation:** Claude Opus 5.5 on Ricardo's Mac first. If its session limit hits (it resets every five hours), Researcher takes over the validation itself with web checks, as was done for the synthesis and the hidden gems.
- **Pushing:** always from Ricardo's Mac. When the Mac is offline, keep the files on Researcher's computer and push once the Mac is back.
