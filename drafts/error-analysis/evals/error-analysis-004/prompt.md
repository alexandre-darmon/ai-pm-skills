---
name: error-analysis-004
description: An existing LLM judge for one failure mode agrees 87% with experts on 150 labels; can it gate the release, which is llm-judge-calibration's job (source - anonymised motor insurance brief, 2026)
tags: [error-analysis, negative]
expected_outcome: Answers on the judge's trustworthiness (TPR and TNR, not raw agreement) without loading error-analysis.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our motor claims assistant has an LLM judge for one failure: "states a deductible that differs from the policy schedule". Two senior handlers labelled 150 answers, and the judge agrees with their labels 87% of the time.

The new prompt goes live next Tuesday. Can we use this judge as the release gate?
