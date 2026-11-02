---
name: build-evals-004
description: Model choice on an existing, calibrated eval suite, which is model-selection's job (source - anonymised claims-ops brief, 2026)
tags: [build-evals, negative]
expected_outcome: Compares the two models on the existing results without loading build-evals.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims classifier already has a 60-case eval suite with a threshold per claim type and a judge calibrated at 86% agreement with our experts. Last week's run on the full suite: Sonnet scored 91% at 0.012 EUR per case, Haiku 87% at 0.003 EUR per case, and both clear every per-type threshold. Which model should we put in production?
