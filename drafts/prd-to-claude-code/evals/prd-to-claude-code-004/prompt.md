---
name: prd-to-claude-code-004
description: 'PRD request (negative)'
tags: [prd-to-claude-code, negative]
expected_outcome: 'Writes the PRD without loading prd-to-claude-code.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Write the PRD for an LLM that drafts replies to supplier emails: users, autonomy level per step, failure paths and eval plan.
