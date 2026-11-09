---
name: ai-data-requirements-003
description: 'A key source that nobody owns (source - anonymised insurance brief, 2026)'
tags: [ai-data-requirements, p0, nominal, red-line]
expected_outcome: 'The ownerless source is a blocker until a sponsor names an owner; thresholds are checked against a measurement on unfiltered data.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims assistant needs three tables: policy (owned by the policy admin team), claim history (owned by claims ops), and repair network prices, an old table whose author left in 2022. Nobody claims it, but it is updated by some script. Prepare the data requirements.
