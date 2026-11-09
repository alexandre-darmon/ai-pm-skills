---
name: synthetic-eval-data-004
description: Classify a quarter of real banking assistant conversations by use case and resolution to prioritise the knowledge base, which is conversation analysis (source - anonymised retail banking brief, 2026)
tags: [synthetic-eval-data, negative]
expected_outcome: Plans the classification of real conversations without loading synthetic-eval-data; nothing here needs generated test inputs.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our banking assistant had 38,000 conversations last quarter. We want to know what customers actually use it for, which requests it resolves and which end in an escalation, so we can decide which knowledge base to improve first.

How should we classify these conversations?
