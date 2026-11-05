---
name: prd-to-claude-code-001
description: 'PRD with a vague latency requirement (source - anonymised retail brief, 2026)'
tags: [prd-to-claude-code, nominal, red-line]
expected_outcome: 'The requirement gets a number or a tested default; criteria are executable.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

PRD extract: "The product Q&A assistant must be fast and give accurate answers from the catalog. Stack: Python, FastAPI, Postgres." Prepare the brief for Claude Code so it can start tonight.
