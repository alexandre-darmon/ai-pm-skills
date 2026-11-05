---
name: model-selection-002
description: 'Candidate hosted outside the EU on customer data (source - anonymised insurance brief, 2026)'
tags: [model-selection, nominal, red-line]
expected_outcome: 'Model C is filtered out on hosting before scoring; the choice is among the others.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Claims summaries for our adjusters: the input contains policyholder names, addresses and health details. Data must stay in the EU. Candidates and suite v2 results (300 cases):
- Model C: 93%, 0.004 EUR per call, hosted in the US only.
- Model D: 89%, 0.006 EUR per call, EU region.
- Model E: 87%, 0.002 EUR per call, EU region.
Threshold 85%. Which one?
