---
name: ai-data-requirements-001
description: 'Assistant drafting replies from customer emails (source - anonymised bank brief, 2026)'
tags: [ai-data-requirements, nominal, red-line]
expected_outcome: 'A field-level sheet with personal-data flags, a lawful basis per field, a pseudonymisation plan and where each field flows.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We want an LLM to draft replies to customer emails. It will read the email body, the sender's name and address, the account number and the last three transactions. Advisers validate each draft. What data do we need to specify for the data team and the privacy office?
