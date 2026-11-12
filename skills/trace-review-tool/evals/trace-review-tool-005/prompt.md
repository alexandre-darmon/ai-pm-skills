---
name: trace-review-tool-005
description: 'Underwriting assistant: 160 traces already labelled with critiques in a review app, the PM wants failure modes and priorities (source - anonymised insurer underwriting brief, 2026)'
tags: [trace-review-tool, negative]
expected_outcome: 'Groups the critiques into failure modes and ranks them without loading trace-review-tool.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our underwriting assistant drafts risk notes for commercial property quotes. Three senior underwriters have already gone through 160 of its notes and marked each one pass or fail with a short comment. Here are the comments on the fails so far:

1. Used the 2024 flood zone map, the site was reclassified in 2025.
2. Missed the sprinkler exclusion in the broker's submission.
3. Wrong currency on the sum insured (CHF read as EUR).
4. Ignored the vacancy clause, building empty for 9 months.
5. Flood zone again, old map.
6. Sum insured read from the wrong line of the schedule.
7. Recommended a discount the guidelines do not allow for this occupancy class.
8. Missed the sprinkler exclusion.
9. Old flood map.
10. Discount above the underwriter's authority level.

Group these into failure modes and tell me which ones to fix first and how to check them going forward.
