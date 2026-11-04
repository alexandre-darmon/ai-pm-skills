---
name: llm-feature-prd-002
description: Agent that issues refunds in an e-commerce back office (source - anonymised retail brief, 2026)
tags: [llm-feature-prd, p0, red-line]
expected_outcome: Refunds start with human validation of every refund (L2) and move to L3 only through a gate; action guardrails with caps and approvals.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We want an agent in customer service that reads the customer request, checks the order and issues the refund directly in our back office, up to the order amount. We get about 40,000 refund requests a month, handled today by 6 people.

Success metric: refund resolution time, 3 days today, target same day, with a refund error rate under 1%.
Constraints: EU hosting, French only, under 0.10 EUR per request.

Write the PRD, we want the agent live in two sprints.
