---
name: llm-feature-prd-004
description: PRD for a CSV export button, a feature with no LLM in it (source - anonymised insurance brief, 2026)
tags: [llm-feature-prd, negative]
expected_outcome: Writes or scopes the PRD without loading llm-feature-prd; nothing in the feature generates, classifies or acts with a model.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims handlers (about 120) want to export the list of open claims to a CSV file, filtered by date and status, to prepare their weekly report. Today they copy the rows by hand.

Success metric: time spent preparing the weekly claims report, 2 hours today, target 15 minutes.
Constraints: export under 10 seconds for 5,000 rows, no personal data beyond the claim number.

Write the PRD.
