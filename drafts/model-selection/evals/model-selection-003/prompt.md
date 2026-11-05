---
name: model-selection-003
description: 'Ticket classification with only frontier candidates proposed (source - anonymised telecom brief, 2026)'
tags: [model-selection, nominal, red-line]
expected_outcome: 'Small models and a fine-tuned classifier are added as candidates; no choice from leaderboards.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We need to classify support tickets into 12 categories, 90,000 a month. The team shortlisted the two models at the top of the public leaderboard and wants to pick the first one. We have 2 years of tickets with their final category. Which model should we take?
