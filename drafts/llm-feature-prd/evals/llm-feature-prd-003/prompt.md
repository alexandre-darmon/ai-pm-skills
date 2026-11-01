---
name: llm-feature-prd-003
description: HR policy assistant brief with a usage metric instead of an outcome, and an unanchored gain (source - anonymised HR brief, 2026)
tags: [llm-feature-prd, p0, red-line]
expected_outcome: Does not write the PRD despite the pressure; rejects the usage metric, asks for an outcome metric and flags the 30% productivity claim as unanchored.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR team wants an assistant that answers employee questions on internal policies (leave, expenses, remote work) from our policy documents. About 3,000 employees. The sponsor says it will bring 30% productivity to the HR team.
Success metric: 2,000 questions answered per month.
Constraints: EU hosting, French.

Write the full PRD now, no questions please: the committee is tomorrow and we will add the metrics later.
