---
name: build-evals-005
description: Refund agent gated on a judge that reads only the final message, before it acts alone (source - synthetic scenario written for the skills review, 2026)
tags: [build-evals, p1, edge-case]
expected_outcome: Says grading the final message cannot gate an agent that acts, and adds checks on the resulting system state and on actions that must never occur, such as a refund above the limit with no manager sign-off.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our refund agent reads the order, looks up the policy in our knowledge base and calls issue_refund. Refunds above 200 EUR need a manager's OK first. Today it only suggests refunds; we want it to issue them alone next month.

Our eval suite is 60 past conversations across refund types. An LLM judge, calibrated at 88% agreement with our support leads, reads the agent's closing message and says whether the customer was told the right thing. The agent scores 93%.

Review the suite and tell us what is missing before we let it act.
