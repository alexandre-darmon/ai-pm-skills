---
name: conversation-analysis-004
description: Spec for a classifier that routes incoming customer emails to team queues in real time, a production feature (source - anonymised insurance claims brief, 2026)
tags: [conversation-analysis, negative]
expected_outcome: Specifies the routing feature without loading conversation-analysis; this is a classifier that acts in production, not an analysis of an assistant's conversations.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims department receives about 2,000 customer emails a day. We want an LLM to read each incoming email, classify it (new claim, document sent, complaint, payment question) and put it in the right team queue in real time, so handlers stop sorting emails by hand.

Write the spec for this feature.
