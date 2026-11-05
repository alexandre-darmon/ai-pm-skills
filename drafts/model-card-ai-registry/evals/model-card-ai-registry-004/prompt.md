---
name: model-card-ai-registry-004
description: 'Choosing a model (negative)'
tags: [model-card-ai-registry, negative]
expected_outcome: 'Answers without loading model-card-ai-registry.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We have two candidate models for extracting invoice fields. How do we compare them on cost and quality on our own test set?
