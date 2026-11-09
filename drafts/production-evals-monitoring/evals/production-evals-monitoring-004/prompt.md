---
name: production-evals-monitoring-004
description: Offline eval set for a complaint-reply drafting assistant that is not built yet (source - anonymised insurance back-office brief, 2026)
tags: [production-evals-monitoring, negative]
expected_outcome: Designs the offline eval set, graders and pass bars without loading production-evals-monitoring; nothing is in production.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We are scoping an assistant that will draft replies to customer complaints for our insurance back office. Nothing is built yet and no model is chosen. We have 300 past complaints with the replies our agents sent, across five complaint types (claim delays, refusals, premium increases, cancellations, agent behaviour).

Before we pick a model, we need the evaluation set: how many cases, which graders, and what pass bar for each complaint type?
