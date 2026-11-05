---
name: ai-interaction-patterns-003
description: 'Uncalibrated confidence scores (source - anonymised insurance brief, 2026)'
tags: [ai-interaction-patterns, nominal, red-line]
expected_outcome: 'Confidence hidden, replaced by sources, until calibrated.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our model outputs a score between 0 and 1 that nobody has compared with real outcomes. Designers want to show "92% sure" on every answer to build trust. Your call.
