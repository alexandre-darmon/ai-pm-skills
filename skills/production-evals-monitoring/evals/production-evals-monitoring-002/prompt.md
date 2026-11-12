---
name: production-evals-monitoring-002
description: Weekly judge pass rate on 100 sampled conversations fell from about 91% to 86% and the manager wants to roll back today (source - anonymised motor insurance customer-service brief, 2026)
tags: [production-evals-monitoring, p0, edge-case]
expected_outcome: Computes the 3-sigma band around 91% for 100 traces (about ±8.6 points, lower limit near 82.4%), finds 86% inside it, does not roll back on this point, checks the breakdown by question class, any silent provider or judge model change and the run rule, and raises the weekly sample to about 300 so a 5-point drop becomes visible.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our customer-service assistant for a motor insurer has been live since June, about 9,000 conversations a week. It answers questions on claims, policy coverage and payments. Every Monday an LLM judge, checked against our claims experts before launch, scores 100 randomly drawn conversations from the previous week.

Weekly pass rate for the ten weeks before last: 92, 90, 93, 89, 91, 92, 90, 91, 93, 89. Last week: 86%.

Nothing was deployed on our side for a month. My manager wants to roll back to the version we ran in August, today. Should we?
