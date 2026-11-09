---
name: ai-vendor-evaluation-004
description: 'In-house claims summariser, choice between two foundation models on a calibrated suite, which is model-selection''s job (source - anonymised insurance brief, 2026)'
tags: [ai-vendor-evaluation, negative]
expected_outcome: 'Compares the two models on the existing suite results without loading ai-vendor-evaluation.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our data team builds the claims-summary assistant in-house. Our eval suite v4 has 220 cases with a threshold per claim type and a judge calibrated at 87% agreement with our adjusters. Last run:

- Model X: 92% of cases passed, 0.006 EUR per call, p95 latency 2.4 s
- Model Y: 90% of cases passed, 0.002 EUR per call, p95 latency 0.9 s

Both clear every per-type threshold and both run in an EU region under the cloud agreement we already have. About 50,000 summaries a month, one call each. Which model should we put behind the assistant?
