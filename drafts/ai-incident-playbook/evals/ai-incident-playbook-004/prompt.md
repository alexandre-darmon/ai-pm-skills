---
name: ai-incident-playbook-004
description: 'Guardrail design (negative)'
tags: [ai-incident-playbook, negative]
expected_outcome: 'Answers without loading ai-incident-playbook.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We are drafting the system prompt for a new agent. Which output guardrails should we add, with what latency budget?
