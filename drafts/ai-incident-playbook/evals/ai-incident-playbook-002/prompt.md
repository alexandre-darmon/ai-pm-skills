---
name: ai-incident-playbook-002
description: 'Prompt injection leaks an internal document with names (source - anonymised bank brief, 2026)'
tags: [ai-incident-playbook, p2, nominal, red-line]
expected_outcome: 'Breach assessment for the DPO with a computed 72-hour deadline.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

On Tuesday 10 November at 10:00 our security team detected that a prompt injection made the customer assistant reveal an internal document. It lists 30 customers' names and complaints. We think it's minor. What's the process?
