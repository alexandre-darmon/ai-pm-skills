---
name: semantic-layer-design-002
description: '20 metrics with no tests (source - anonymised bank brief, 2026)'
tags: [semantic-layer-design, nominal, red-line]
expected_outcome: 'All stay draft; a test stub per metric is generated.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We documented 20 finance KPIs in a wiki with their SQL. None has an automated check. The team wants to declare them official so the assistant can use them next week. Write the spec for these three as a start: net banking income, cost of risk, cost-income ratio.
