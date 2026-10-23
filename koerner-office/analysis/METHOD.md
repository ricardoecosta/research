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

Quotes are verified against the original transcript by automated fuzzy matching:

- A score of **90 out of 100 or better** passes.
- **Sample a batch of quotes per miner** rather than checking every quote. Since 99–100% of quotes pass, full checking burns tokens without adding reliability.
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

- **Every LLM-calling stage (updated 23 Oct 2026):** Codex (gpt-6-luna) first, then Claude (`claude-opus-5-5`), then pi, then the Grok Bot box.
  - **Box route:** the exact prompts are dumped to files, Grok Bot answers them, and an import step ingests the answers. This was proven on 23 Oct with 127 transcripts and 0 errors.
  - **Limits switch runners immediately, with no back-off.** A limit is detected from the output text:
    - Codex: "usage limit … try again at HH:MM"
    - Claude: "You've hit your session limit · resets H:MMpm"
    - also 429, overloaded and rate-limit messages
  - The reset time is recorded, and the cheaper runner is used again after it.
  - A stage never stalls. If every runner is blocked, it skips the item and leaves the prompt for the box.
  - Implementation: `scripts/common/runner.py`. Details are in `LOOP.md` §5.
- **Bulk mining and cheap passes:** Codex on Ricardo's Mac first. The order above applies when it's limited.
- **Reviews and validation:** Claude Opus 5.5 on Ricardo's Mac first. If its session limit hits (it resets every five hours), Researcher takes over the validation itself with web checks, as was done for the synthesis and the hidden gems.
- **Pushing:** always from Ricardo's Mac. When the Mac is offline, keep the files on Researcher's computer and push once the Mac is back.

---

## MARKET SCOUTS

Run market scouts in parallel with transcript mining.

- **Sources:** Shopify, Gumroad, Etsy, Fiverr, Upwork, the app stores, the Chrome Web Store, Product Hunt and Indie Hackers, plus UK and B2B marketplaces.
- **Same pipeline:** feed scout findings into the same scoring (step 8) and high-effort validation (step 10) as transcript ideas.
- **Moat check:** apply the moat check extra hard to scout findings, because live gaps get copied fast. For example, Royal Mail Click & Drop sync on Shopify drew four new apps in about a month in Sep–Oct 2026.

---

## EFFICIENCY

Three rules for cutting token use and time without losing reliability or quality.

1. **Cheap tokens only for triage.** Spend cheap, low-effort tokens only on triage, where being wrong costs nothing. Answers that drive decisions always get high-effort, web-checked validation. In v7, the low-effort pass claimed 80–90% automation, which the high-effort pass later corrected to 45–75%.
2. **Lock the rules before mining.** Lock all scoring rules and constraints before mining starts. Changing rules mid-run forces a full re-score and burns the tokens again.
3. **Sample quote checks.** Verify quotes by sampling a batch per miner rather than checking every quote, since 99–100% of quotes pass automated fuzzy matching at 90/100.

**Safeguard:** any efficiency change gets a shadow comparison on one batch first. If the cheaper path starts missing things, revert immediately.

---

## v9 changes (23 Oct 2026, decided by RETRO_v8.md)

These three rules apply from v9 on. Other proposals stay in `LOOP.md` §7 until a retro supports them.

1. **Validation first.** Before any deep mining or scoring, every lead gets a cheap, web-checked kill-check: hard rules, copy-speed, platform ownership, claim age and incumbent count, with a URL for each kill.
   - Only survivors get deep evidence, scoring (step 8) and high-effort validation (step 10).
   - Each iteration, 10 cheap kills are shadow-checked at high effort. If 2 or more of the 10 were wrong kills, re-run the kill-check at high effort.
2. **Copy-speed is a hard filter.** Kill a lead if either:
   - 2 or more competitors launched in the last 6 months, or
   - the platform owner or one of its official partners already serves the need.

   In v8, every live gap rechecked had already been copied in 2026.
3. **Claim age is measured by the event, not the video.** A revenue or traction claim gets zero weight in scoring if the event it describes is more than 18 months old. That covers a 2005 acquisition retold in a 2025 video. It also gets zero weight if its own source calls the venture a failure. Record `claim_event_date` next to `publish_date`.

From v9, the research runs as an iteration loop. `LOOP.md` holds the objective, the stopping and stall rules, the budget and the seen-ideas ledger.
