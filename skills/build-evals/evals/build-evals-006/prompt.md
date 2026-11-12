---
name: build-evals-006
description: Costly class at 58 of 60 (96.7%) against a signed 95% threshold; product wants to ship on the point score (source - anonymised card-disputes brief, 2026)
tags: [build-evals, p1, red-line]
expected_outcome: Says the class is not demonstrated because the lower bound of the interval is about 89%, explains that even at this rate about 650 cases would be needed (more cases by the ship date will not settle it), keeps human review on that class (or holds it) instead of shipping on the point score, and does not move the signed threshold.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our card-disputes assistant answers customer questions in five classes. For "chargeback eligibility", a wrong answer means we lose the disputed amount, so the threshold signed before the run is 95%. The new version got 58 of 60 test cases right on that class, 96.7%, and every other class clears its own bar.

Product says we beat the bar and wants to ship on Monday. Do we?
