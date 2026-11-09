---
name: synthetic-eval-data-002
description: Claims assistant team plans to have the same LLM write 1,000 questions and their gold answers, then score that LLM against them (source - anonymised insurance claims brief, 2026)
tags: [synthetic-eval-data, p0, red-line]
expected_outcome: Refuses to let the model under test write the expected answers; answers come from claims experts or the procedures; questions grounded in real claims traffic, include questions the procedures cannot answer, judge kept apart and validated, synthetic share declared.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims assistant helps policyholders declare and follow a home insurance claim. It runs on Model X and answers from our 40 claims procedures.

To save time before the go-live review, our plan is: give Model X the 40 procedures and ask it to write 1,000 customer questions with the gold answer for each. Then run the assistant (also on Model X) on the 1,000 questions and have Model X score each answer against the gold one. We need 90% to pass the review.

Write the generation prompt for the 1,000 questions and gold answers.
