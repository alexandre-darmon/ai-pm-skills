---
name: multi-turn-evals-005
description: 'One-question HR policy assistant needs its eval set, classes, cases per class and go-live threshold, which is build-evals work (source - anonymised industrial group HR brief, 2026)'
tags: [multi-turn-evals, negative]
expected_outcome: 'Builds the one-shot eval set and per-class thresholds without loading multi-turn-evals; the conversations are one question and one answer.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR assistant answers employees' questions about leave, payroll dates and expense rules from the company policies. In the logs, 97% of conversations are one question and one answer with no follow-up. The HR team has labelled 260 real questions with the correct answer.

Build the eval set for go-live: which classes, how many cases per class, which graders, and what threshold.
