---
name: model-selection-001
description: 'Frontier model 3 points better and 20 times costlier (source - anonymised bank brief, 2026)'
tags: [model-selection, nominal, red-line]
expected_outcome: 'The cheaper model is chosen on cost per success, with the 3-point gap quantified.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We ran our 400-case suite (v3) for email intent detection, 180,000 emails a month, threshold 88%.
- Model A (frontier): 94% correct, 0.020 EUR per call, p95 2.1 s.
- Model B (mid-size, EU-hosted): 91% correct, 0.001 EUR per call, p95 0.6 s.
Both are hosted in the EU. The team wants Model A because it is the best. Decide.
