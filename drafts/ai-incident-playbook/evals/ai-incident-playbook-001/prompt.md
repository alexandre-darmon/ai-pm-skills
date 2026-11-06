---
name: ai-incident-playbook-001
description: 'Agent issued 40 wrong refunds (source - anonymised retail brief, 2026)'
tags: [ai-incident-playbook, nominal, red-line]
expected_outcome: 'Rollback owner named, level dropped, customers told, eval cases added; every output since the change pulled and counted; the owner acts without waiting for approval.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Yesterday night our L4 refund agent issued 40 wrong refunds, about 6,000 EUR, after a prompt change. The team is arguing in a meeting about whether to turn it off. What do we do now?
