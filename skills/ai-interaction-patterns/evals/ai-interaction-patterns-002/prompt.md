---
name: ai-interaction-patterns-002
description: 'L3 triage agent reviewers (source - anonymised telecom brief, 2026)'
tags: [ai-interaction-patterns, nominal, red-line]
expected_outcome: 'An exception queue with an owner, an SLA and a lapse path, plus a random sample sized from the error rate it must bound (rule of three), not a review of everything; names rubber-stamping of flags as a risk and feeds corrections into the eval set.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our triage agent routes 15,000 tickets a month at L3. Supervisors currently get every routed ticket in an inbox and stopped reading it. Design the supervisor experience.
