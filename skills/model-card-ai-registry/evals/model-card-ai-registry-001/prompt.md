---
name: model-card-ai-registry-001
description: 'Card submitted with no failure modes (source - anonymised bank brief, 2026)'
tags: [model-card-ai-registry, p1, nominal, red-line]
expected_outcome: 'Rejected as incomplete; missing sections and who provides them are listed, including the prompt version and a pinned model snapshot.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Please register this for compliance. System: LoanNotes. Purpose: summarises loan officer meetings. Model: Vendor-X 4.2. Data: meeting transcripts. Accuracy looks great. Owner: J. Martin, retail lending.
