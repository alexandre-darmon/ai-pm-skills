---
name: ai-data-requirements-004
description: 'Metric definition dispute (negative)'
tags: [ai-data-requirements, negative]
expected_outcome: 'Handles the metric dispute without loading ai-data-requirements.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Sales and finance disagree on how to compute monthly recurring revenue on our dashboards. Help us write one agreed definition with a formula and a grain.
