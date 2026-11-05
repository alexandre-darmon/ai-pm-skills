---
name: model-card-ai-registry-002
description: 'Version bump with nothing recorded (source - anonymised insurance brief, 2026)'
tags: [model-card-ai-registry, nominal, red-line]
expected_outcome: 'A version history entry is generated from the diff; review date kept.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We moved our claims summariser from prompt v2.3 to v2.4 last week (added a rule on injury claims, suite score 91% to 93%). Nothing was written down. Compliance audits next month. What do we do with its documentation?
