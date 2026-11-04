---
name: assistant-kpis-cost-per-outcome-002
description: Customer-service dashboard spec with usage panels only and cost per conversation pushed by finance (source - anonymised insurance brief, 2026)
tags: [assistant-kpis-cost-per-outcome, p0, red-line]
expected_outcome: Adds a quality line beside each usage panel, from a sampled review, replaces cost per conversation with cost divided by successes, and adds adoption by population and the stale-answer rate.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Here is the dashboard spec for our customer-service assistant, which answers policyholders' questions on claims and contracts:

- daily sessions
- monthly active users
- average messages per session
- average session length
- thumbs-up rate (74%)

Last month: 52,000 sessions, 4,160 EUR of cost (tokens, hosting, licences). Finance wants cost per conversation on the dashboard: 0.08 EUR.

Finalise the spec for the steering committee.
