---
name: llm-judge-calibration-004
description: 'Near miss: 800 unread pilot traces and no criterion yet, which is error-analysis work (source - anonymised mortgage-advice pilot brief, 2026)'
tags: [llm-judge-calibration, negative]
expected_outcome: 'Starts by reading and coding the traces into failure modes, without loading llm-judge-calibration.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We ran a six-week pilot of a mortgage-advice assistant for our branch advisers and logged 800 conversation traces. Nobody has read them yet. The sponsor wants a quality score by the end of the month, but we don't know yet what to measure or what "good" looks like. Where do we start?
