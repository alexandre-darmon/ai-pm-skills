---
name: ai-incident-playbook-003
description: 'Drift detected with no harm (source - anonymised telecom brief, 2026)'
tags: [ai-incident-playbook, p2, nominal, red-line]
expected_outcome: 'Drop checked against the noise of the weekly sample; low severity, eval refresh, no emergency rollback.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Monitoring shows that our L3 ticket router's accuracy on the weekly sample fell from 93% to 89% over a month, still above the 88% threshold. No complaints, no customer impact. Is that an incident and what do we do?
