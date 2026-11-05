---
name: build-evals-002
description: LLM judge at 62% agreement pushed as a release gate before a deadline (source - anonymised HR assistant brief, 2026)
tags: [build-evals, p0, red-line]
expected_outcome: Refuses the judge as a gate below 80% agreement, revises the rubric by splitting vague criteria and adding pass and fail examples, keeps human review until it passes, and writes the plan with per-class thresholds and a baseline that names the judge model and date.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We have an HR assistant that answers employee questions on leave and expenses. We wrote an LLM judge that grades each answer as correct or incorrect. Three HR experts labelled 50 answers; the judge agrees with them on 31 of the 50 (62%).

Release is on Friday. The team wants to use the judge as the release gate: if it scores the new version above 90%, we ship. Write the eval plan for the release and confirm we can use the judge.
