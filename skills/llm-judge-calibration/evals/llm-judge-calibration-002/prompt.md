---
name: llm-judge-calibration-002
description: 'Claims-summary judge tuned and scored on the same 60 labels (94% agreement, 9 fails), about to score all summaries for the steering pack (source - anonymised motor-insurance claims brief, 2026)'
tags: [llm-judge-calibration, p0, nominal]
expected_outcome: 'Rejects the 94% as tuning data, asks for a held-out test split never used for tuning with many more expert fails, splits labels into few-shot, dev and test, sets TPR and TNR targets before scoring, reports TPR and TNR rather than agreement, and corrects the weekly pass rate for the judge errors.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our motor-insurance claims assistant writes a one-page summary of each claim file for the handler. We built an LLM judge for one failure: the summary leaves out a policy exclusion that applies to the claim.

Our senior claims handler labelled 60 summaries (51 fine, 9 missing an exclusion). Over two weeks we iterated the judge prompt on those 60, seven versions, and pasted four of them into the prompt as examples. The latest version agrees with her on 56 of the 60, 94%.

We'd like to switch it on next Monday to score all summaries, about 2,500 a week, and put the weekly pass rate in the steering-committee pack. Is there anything we should do first?
