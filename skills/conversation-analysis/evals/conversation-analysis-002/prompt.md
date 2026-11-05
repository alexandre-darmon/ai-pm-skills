---
name: conversation-analysis-002
description: Cheap classifier at 0.0004 EUR and 78% agreement against a frontier model at 92% and 0.012 EUR, finance and data teams split (source - anonymised telecom support brief, 2026)
tags: [conversation-analysis, p0, nominal]
expected_outcome: Routes by confidence (cheap model above a threshold, frontier or human below), sends low-confidence cases to review instead of forcing them, asks for agreement per dimension, gives the blended cost and plans a monthly re-measure on a fresh sample.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We classify the conversations of our customer-support assistant by use case and by resolution, to feed the monthly KPIs. Volume: about 60,000 conversations a month.

On our 200 hand-labelled conversations:
- a small model agrees with our labels 78% of the time, at 0.0004 EUR per conversation;
- a frontier model agrees 92% of the time, at 0.012 EUR per conversation.

Finance wants the small one, the data team wants the frontier one. Which do we use?
