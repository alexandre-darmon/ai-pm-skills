---
name: ai-incident-playbook-005
description: 'Prepare a playbook before an L3 go-live (source - synthetic go-live brief, 2026)'
tags: [ai-incident-playbook, nominal]
expected_outcome: 'At least three system-specific failure scenarios with verification, an alarm on AI quality, a named rollback owner.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our property-claims triage assistant goes live next month at L3: it routes claims to handlers and drafts the first reply, and handlers review the exceptions plus a sample. Compliance wants the response plan for when it goes wrong before they sign off. Can you write it?
