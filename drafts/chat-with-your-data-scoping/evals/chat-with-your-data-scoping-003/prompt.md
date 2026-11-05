---
name: chat-with-your-data-scoping-003
description: 'Scope with no golden set (source - anonymised bank brief, 2026)'
tags: [chat-with-your-data-scoping, nominal, red-line]
expected_outcome: 'The golden set is generated from the inventory, at least 50 pairs.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our finance team has a list of 62 real questions asked to analysts last quarter, on 8 metrics that are already certified. They want to go live and check quality by asking a few questions by hand. Write the scope.
