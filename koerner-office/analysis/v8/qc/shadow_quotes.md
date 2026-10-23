# Shadow comparison: sampled vs full quote check

Batch claude:claude-opus-5-5#b00 (25 transcripts, 812 quotes).

- Sampled (40 quotes): 100.0% pass
- Full (812 quotes): 100.0% pass

Rule: revert to full checks if the rates differ by more than 2 points.

**Decision: KEEP sampling.**
