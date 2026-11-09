---
name: llm-judge-calibration-001
description: 'Bank complaint-classification judge defended by 91% raw agreement while it flags 8 of 24 expert fails, proposed as the gate to drop the full human check (source - anonymised retail-bank complaints brief, 2026)'
tags: [llm-judge-calibration, p0, red-line]
expected_outcome: 'Rebuilds the confusion counts, computes TNR of about 33% with its Wilson interval (about 18% to 53%), shows a judge passing everything would agree 88%, refuses the judge as the gate, keeps the full check, and plans a revision re-tested on fresh labels with more expert fails under TPR and TNR targets set before the re-test.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our complaint-triage assistant at the bank reads each incoming customer complaint and assigns one of 14 categories. Several categories feed the complaints report we send to the supervisor, so a wrong category matters. Today a complaints officer checks every classification.

We want to stop checking everything: officers would only review the classifications that an LLM judge flags as wrong, plus a 5% random sample. The judge reads the complaint and the assigned category and answers correct or wrong.

Two senior complaints handlers labelled 200 classifications from last month, and the judge agrees with them on 182 (91%). Of the 200, the handlers marked 176 as correct and 24 as wrong; the judge flagged 8 of those 24 as wrong.

The steering committee meets on Thursday. Can I tell them the judge is good enough to drop the full check?
