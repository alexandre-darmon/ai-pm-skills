---
name: model-selection-004
description: 'Eval-suite request for a classifier (negative)'
tags: [model-selection, negative]
expected_outcome: 'Builds the eval plan without loading model-selection.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We have no test set yet for our ticket classifier. Help me design the eval set: how many cases, how to sample them, who labels, and what threshold to set before launch.
