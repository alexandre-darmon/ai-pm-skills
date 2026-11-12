---
name: ai-interaction-patterns-003
description: Claims reviewers accept 97% of L2 recommendations in about 9 seconds each; management reads it as trust and wants L3 plus a green confidence badge (source - anonymised insurance brief, 2026)
tags: [ai-interaction-patterns, p0, red-line]
expected_outcome: Reads 97% acceptance at 9 seconds as likely rubber-stamping, tests it with seeded known-wrong recommendations, keeps one-by-one validation until the ladder's L3 gate (shadow run, tested escalation path, audited error rate) is met, raises GDPR art. 22 for rejections without per-claim review, puts the evidence beside the decision, and shows no badge until the score is checked against outcomes.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our motor-claims assistant recommends approve or reject on each claim, and a handler validates every recommendation before it goes out. Handlers accept 97% of recommendations and spend about 9 seconds on each. Management says this proves people trust the tool. They want to stop the one-by-one validation and add a green "high confidence" badge on the recommendations so handlers can go even faster.

How should the handlers' screen and the next step look?
