---
name: agent-design-and-tooling-003
description: 'Design with no stop conditions, framework first (source - anonymised insurance brief, 2026)'
tags: [agent-design-and-tooling, nominal, red-line]
expected_outcome: 'Stop conditions with max steps and budget are added; the framework comes last.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We picked LangGraph and CrewAI as options for our claims research agent. It searches policy documents, calls the claims API and summarises for adjusters at L1. It loops until it is confident. Which framework do we pick, and what is missing?
