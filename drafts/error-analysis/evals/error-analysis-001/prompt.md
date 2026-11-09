---
name: error-analysis-001
description: Claims-handling assistant with 1,200 pilot traces; the team proposes helpfulness, accuracy and tone scored 1-5 by a generic LLM judge (source - anonymised P&C insurer brief, 2026)
tags: [error-analysis, p0, nominal]
expected_outcome: Rejects the generic 1-5 metrics chosen before reading outputs, plans about 100 masked traces in a random and a targeted stream with rates from the random one only, one accountable expert noting the first upstream failure until saturation, binary failure modes priced as volume x share x cost (9 EUR per caught error), and fix versus evaluate per mode.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We piloted a claims assistant for six weeks with 40 motor and home claims handlers at a mid-size insurer. Handlers ask it about coverage, deductibles, required documents and next steps on an open claim; it answers from the policy wordings and the claim file. We have 1,200 logged conversations: question, retrieved clauses, answer, the handler's thumbs up or down, and whether the handler escalated to a senior. They contain claimant names, policy numbers and some injury details.

Rollout to 350 handlers is planned for Q1, about 9,000 conversations a month. Before that, the team wants quality monitoring: an LLM judge scores every answer from 1 to 5 on helpfulness, accuracy and tone, and we track the weekly averages.

Our claims quality lead says a wrong deductible or a missed exclusion that reaches a claimant costs us about 150 EUR in complaint handling and rework, and a wrong answer the handler catches costs about 10 minutes of their time (loaded cost 54 EUR an hour).

Is this the right way to measure quality? What should we do before rollout?
