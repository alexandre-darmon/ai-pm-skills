---
name: prd-to-claude-code-002
description: 'PRD with three modules (source - anonymised insurance brief, 2026)'
tags: [prd-to-claude-code, nominal, red-line]
expected_outcome: 'Three spec files, tasks ordered by risk, a do-not-build list.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

The approved PRD has three modules: (a) extract fields from claim emails with an LLM, (b) push them to the claims system through its API, (c) a review screen for adjusters. Non-goal: automatic settlement. Write the brief for our coding agent.
