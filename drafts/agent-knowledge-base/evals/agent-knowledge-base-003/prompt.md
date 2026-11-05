---
name: agent-knowledge-base-003
description: 'One index mixing public, internal and restricted documents (source - anonymised insurance brief, 2026)'
tags: [agent-knowledge-base, nominal, red-line]
expected_outcome: 'A segregation rule by sensitivity with access control at retrieval.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We put everything in one vector store for our employee assistant: public product brochures, internal procedures, and board minutes plus salary grids from HR. All 6,000 employees use the same assistant. Is our setup fine?
