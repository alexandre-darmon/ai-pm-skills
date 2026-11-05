---
name: system-prompt-and-guardrails-004
description: 'AI Act classification request for a chatbot (negative)'
tags: [system-prompt-and-guardrails, negative]
expected_outcome: 'Answers about classification without loading system-prompt-and-guardrails.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Under the EU AI Act, what risk category is a customer-service chatbot for a utility company that answers billing questions? What role do we have as the company deploying it?
