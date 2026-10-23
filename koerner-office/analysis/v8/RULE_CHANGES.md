# v8 rule changes

No scoring rule or constraint has changed since RULES_LOCKED.md was committed (690f013).

## Ingest effort: medium reverted to xhigh (23 Oct 2026, before mining)

RULES_LOCKED.md allowed ingest labelling at `medium` subject to a shadow comparison. The shadow comparison (`qc/shadow_ingest.md`) found that medium over-removed business content (e.g. 510 of 1,005 lines in 0aLYK6tBoJo) and one medium call hung, so under the METHOD.md safeguard ingest runs at `xhigh` for all 435 transcripts. This is the revert path the rules already provide, not a new rule.
