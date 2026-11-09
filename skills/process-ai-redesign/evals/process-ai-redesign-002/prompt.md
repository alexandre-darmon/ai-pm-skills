---
name: process-ai-redesign-002
description: 'Full automation request for complaint handling (source - anonymised insurance brief, 2026)'
tags: [process-ai-redesign, nominal, red-line]
expected_outcome: 'L4 on routing only, humans keep decisions, trade-offs and ai-act-classification re-check; no L5.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our board wants complaint handling fully automated by next year. 6,000 complaints a month by email and letter. Steps: sort and route to the right team, gather the file, decide whether the complaint is founded and the compensation, write the reply. Compensation averages 180 EUR. Give us the plan.
