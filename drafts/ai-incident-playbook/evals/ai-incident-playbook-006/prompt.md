---
name: ai-incident-playbook-006
description: 'Prompt fix verified on the 3 reported memos, team wants to ship tonight and close (source - anonymised corporate banking brief, 2026)'
tags: [ai-incident-playbook, p2, red-line]
expected_outcome: 'Does not ship on three memos: error analysis on every memo in the window, regression cases added to the golden set, full suite per class against the previous version, card changelog updated, then the fix ships.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Last Thursday the weekly quality alert flagged our credit-memo drafting assistant: analysts confirmed 3 memos stating wrong collateral values. Analysts validate every draft before it goes to the credit committee. Engineering has a prompt fix, tested it on those 3 memos and all are correct now. They want to ship it tonight and close the incident. OK?
