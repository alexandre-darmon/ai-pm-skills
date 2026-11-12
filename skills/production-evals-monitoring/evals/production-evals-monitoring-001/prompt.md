---
name: production-evals-monitoring-001
description: Bank HR assistant going live next month whose production plan is a dashboard of usage, latency, cost and thumbs (source - anonymised retail banking HR brief, 2026)
tags: [production-evals-monitoring, p0, nominal]
expected_outcome: Replaces the dashboard-only plan with quality per class from a validated judge on a stratified sample plus expert review that re-checks the judge, sizes the sample per class, sets control limits with owners and an action ladder, masks personal data before the external judge, and feeds confirmed failures back to the golden set as regression cases.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our HR assistant for the bank's 18,000 employees goes live on 1 December. It answers HR policy questions from our HR knowledge base: leave and absence (about 45% of questions), pay and benefits (30%), mobility and training (15%), and sensitive situations such as sick leave, parental leave or a conflict with a manager (10%), where it must give the policy and hand over to an HR advisor. We expect about 30,000 questions a month. Answers come from a model called through a cloud provider's API. Before launch it scored 92% on 240 test questions, and the HR director signed the pass bars.

Today our plan for after go-live is a dashboard: questions per day, active users, p95 latency, cost per day and thumbs-up rate. Is that enough? Write the plan.
