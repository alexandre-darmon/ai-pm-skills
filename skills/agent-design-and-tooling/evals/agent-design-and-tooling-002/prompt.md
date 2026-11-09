---
name: agent-design-and-tooling-002
description: 'L4 step with a payment tool (source - anonymised bank brief, 2026)'
tags: [agent-design-and-tooling, nominal, red-line]
expected_outcome: 'A cap and an approval rule in the permission matrix for the payment tool.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our goodwill agent will pay small gestures to customers with a tool pay_goodwill(customer_id, amount). The redesign targets L4 for that step. Other tools: read_account and create_note. Write the agent design.
