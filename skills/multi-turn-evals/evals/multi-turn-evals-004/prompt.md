---
name: multi-turn-evals-004
description: 'Savings assistant moving from L2 to L3; the gate plan is 50 conversations of 8 exchanges run once, pass if the mean reply score is 90% or more (source - anonymised retail bank brief, 2026)'
tags: [multi-turn-evals, p1, red-line]
expected_outcome: 'Says the 400 reply scores are not independent cases and the conversation is the unit, sizes about 113 scenarios for ±5 points at 92%, sees that a gate on the lower bound at 90% cannot pass at that size when the true rate is 92% (about 830 needed, or a lower bar with a reason, a narrower class, or stay at L2), runs each 3 times and reports the observed pass^k with 0.92^3 ≈ 0.78 as a projection only, and prices the run or the exposure.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We want to move our savings-product assistant from L2 (an adviser approves every reply before it is sent) to L3 (replies go straight to the customer, advisers see a sample and the escalations). It handles about 25,000 conversations a month, with 8 customer messages on average. In the pilot, advisers judged about 92% of conversations fine.

Our plan for the gate: 50 test conversations of 8 exchanges each, so 400 scored replies; each conversation is run once; we pass if the mean reply score is at least 90%, and we want to know that rate within plus or minus 5 points.

Is the plan right? How many conversations, how many runs, and what pass rule?
