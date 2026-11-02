---
name: build-evals-003
description: Support assistant suite with one global threshold over 4 question classes of different risk (source - anonymised e-commerce support brief, 2026)
tags: [build-evals, p0, red-line]
expected_outcome: Splits the threshold per class, stricter on the legal warranty class, re-samples the rare classes, and scores cost per correct answer.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our customer support assistant answers four kinds of questions: order status (60% of traffic), returns (25%), warranty claims, which have legal consequences (10%), and product advice (5%).

Our eval suite has 120 cases drawn at random from last month's conversations, and we ship when the overall score is above 85%. The last version scored 88%. Cost is 0.04 EUR per answer.

Review our eval setup and tell us what to change before the next release.
