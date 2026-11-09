---
name: llm-judge-calibration-003
description: 'Production judge reports 85% against an 88% bar; its test split gives TPR 0.92 and TNR 0.80 (source - anonymised SME-lending credit-memo brief, 2026)'
tags: [llm-judge-calibration, p1, edge-case]
expected_outcome: 'Explains why the raw 85% is biased, corrects it to about 90% with an interval carrying the TPR and TNR uncertainty (about 82% to 99%), reads the 88% bar against the interval (not decided either way), points to the bootstrap script, and asks for fresh expert labels on production memos.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our SME-lending assistant drafts the credit memo for each loan request, and an LLM judge checks one failure mode on a weekly sample of production memos: a figure in the memo that is not in the client's financial statements. Last month the judge passed 340 of 400 sampled memos (85%). The risk committee's bar for keeping the assistant at its current level is 88% of memos free of unsupported figures, so the dashboard is red.

The judge was validated in September on a test split of 150 memos labelled by a credit analyst, none of them used to write its prompt: of the 100 memos she passed, the judge passed 92; of the 50 she failed, it failed 40.

The committee chair asks whether we are really below 88% before she orders a return to full human review of every memo. What should I tell her?
