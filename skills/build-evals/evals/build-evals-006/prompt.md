---
name: build-evals-006
description: Release sign-off on a legal class tested on 12 cases, all passed, against a 95% threshold (source - anonymised HR assistant brief, 2026)
tags: [build-evals, p1, edge-case]
expected_outcome: Says 12 passes out of 12 cannot demonstrate 95% because the interval's lower bound is far below it, sizes the class (about 60 clean cases at least), and signs off the other classes on their own results.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR assistant answers employee questions in five classes. The new version passed every class threshold in yesterday's run. The class we worry about is contract termination, where a wrong answer can cost us at the labour court: its threshold is 95% and the new version answered all 12 of its test cases correctly. The four other classes are each tested on more than a hundred cases and clear their thresholds comfortably.

Legal wants a yes or no by tonight. Can we sign off the release?
