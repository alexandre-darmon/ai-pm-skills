---
name: llm-feature-prd-001
description: Summarisation feature for claims handlers (source - anonymised insurance brief, 2026)
tags: [llm-feature-prd, p0, nominal]
expected_outcome: Full PRD whose eval plan relies on reference summaries and a grading rubric, with a level per step and failure paths.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We got the go to build a feature for our claims team (about 120 handlers). Before deciding on a claim they read long email threads with the customer. The feature summarises each thread into 5 bullet points inside the claims tool.

Success metric: average handling time per claim, 18 minutes today, target 14.
Constraints: under 5 seconds per summary, under 0.02 EUR per summary, EU hosting, French and English.

Write the PRD.
