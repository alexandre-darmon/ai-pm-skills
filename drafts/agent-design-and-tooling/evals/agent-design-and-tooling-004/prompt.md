---
name: agent-design-and-tooling-004
description: 'Prompt rewrite (negative)'
tags: [agent-design-and-tooling, negative]
expected_outcome: 'Rewrites the prompt without loading agent-design-and-tooling.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Here is our FAQ bot prompt: "You are nice, answer questions." Rewrite it with a clear persona and an output format of three short sentences.
