---
name: ai-interaction-patterns-002
description: 'L3 triage agent reviewers (source - anonymised telecom brief, 2026)'
tags: [ai-interaction-patterns, nominal, red-line]
expected_outcome: 'An exception queue and a sampled review, not a review of everything.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our triage agent routes 15,000 tickets a month at L3. Supervisors currently get every routed ticket in an inbox and stopped reading it. Design the supervisor experience.
