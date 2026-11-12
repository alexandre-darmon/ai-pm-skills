---
name: multi-turn-evals-003
description: 'Private-banking adviser copilot scores 188 of 200 on one-message questions while 31 of 140 advisers say it forgets what they said or changes its recommendation (source - anonymised private bank advisory brief, 2026)'
tags: [multi-turn-evals, p1, nominal]
expected_outcome: 'Explains the one-message suite cannot see the problem, measures the drop on the same tasks given over several turns with the spread across runs, defines conversation outcomes such as constraints kept, builds scripted cases with decisive turns and simulated advisers with hidden facts.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our private-banking advisers use a copilot to prepare client meetings: they type the client's situation, ask for product ideas, then refine over several messages ("now without equities", "she also wants to keep 50k available at all times"). Our eval suite has 200 questions, each written as one complete message with its expected answer, and the latest version scores 188/200.

Yet in the adviser survey, 31 of 140 advisers say the copilot "forgets what I told it", and several say it changes its recommendation between two messages for no reason. The team's view is that the eval is fine and that advisers phrase things badly.

How should we evaluate this, and what do we report to the head of advisory?
