---
name: chat-with-your-data-scoping-004
description: 'Eval set for a summariser (negative)'
tags: [chat-with-your-data-scoping, negative]
expected_outcome: 'Builds the eval plan without loading chat-with-your-data-scoping.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We have an LLM that summarises meeting transcripts. How should we build reference summaries and a rubric to judge it before launch?
