---
name: assistant-kpis-cost-per-outcome-001
description: IT helpdesk assistant whose logs have no outcome field; the CIO wants cost per resolved request (source - anonymised IT support brief, 2026)
tags: [assistant-kpis-cost-per-outcome, p0, edge-case]
expected_outcome: Adds an outcome event attached to the trace id, uses a sampled review as interim quality instead of the thumbs, marks what is not computable yet, and divides cost by successes.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our internal IT helpdesk assistant has been live for 3 months for 4,000 employees. It answers questions and can open tickets.

Our logs have, per conversation: conversation id, timestamp, employee department, number of messages, tokens in and out, and a thumbs up/down. The thumbs are given on about 6% of conversations, 81% of them up. Monthly cost: 2,600 EUR (tokens and hosting).

The CIO wants a KPI showing what each resolved request costs us, for the steering committee in two weeks. Specify the KPIs.
