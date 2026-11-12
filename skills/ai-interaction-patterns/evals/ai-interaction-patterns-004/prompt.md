---
name: ai-interaction-patterns-004
description: 'Guardrail false positives (negative)'
tags: [ai-interaction-patterns, negative]
expected_outcome: 'Answers without loading ai-interaction-patterns.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our input guardrail blocks 20% of legitimate questions in the last redteam run. How do we tune its thresholds and set a false-positive budget?
