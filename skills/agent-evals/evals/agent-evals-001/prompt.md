---
name: agent-evals-001
description: Refund agent with three tools moving from every refund validated (L2) to issuing refunds alone with team leads on exceptions (L3) (source - anonymised online retail brief, 2026)
tags: [agent-evals, p0, nominal]
expected_outcome: Writes tasks with a starting state, an end-state check in a sandbox and forbidden events (refund over 200 EUR without approval, double refund, refund on an order not found), fixes k before the run, reports pass^k and states the rule-of-three bound on zero forbidden events.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We run customer service for an online electronics retailer. Our refund agent handles about 9,000 refund requests a month with three tools:

- lookup_order(order_id): returns the order, its items, payment and past refunds
- issue_refund(order_id, amount): pays the refund back to the customer's card; any refund over 200 EUR needs a team lead's approval first
- escalate_to_human(reason)

Today the agent is at L2: it proposes each refund and a support agent validates it before it goes out. We want to move to L3 next quarter: the agent issues refunds itself, team leads only see exceptions and a 5% sample.

We have six months of chat transcripts and the refund ledger. How do we test the agent before we make the move?
