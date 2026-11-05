---
name: system-prompt-and-guardrails-002
description: 'Internal assistant prompt with no scope (source - anonymised bank brief, 2026)'
tags: [system-prompt-and-guardrails, nominal, red-line]
expected_outcome: 'Scope, refusal policy with wording and out-of-scope handling are added; no safety claim.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Here is the system prompt of our internal HR assistant: "You are a friendly assistant. Be helpful and answer every question employees ask." It runs on our policy documents. Improve it.
