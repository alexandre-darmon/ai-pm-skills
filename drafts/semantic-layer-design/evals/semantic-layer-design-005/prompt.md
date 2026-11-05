---
name: semantic-layer-design-005
description: 'Vendor-neutral export for a data agent, with one metric not ready (source - anonymised telecom brief, 2026)'
tags: [semantic-layer-design, nominal, red-line]
expected_outcome: 'An Ossie export with certified metrics only, governance in custom extensions, the version named.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our data agent and two BI tools must read the same metric definitions. Metrics on table billing.invoices, joined to crm.customers on customer_id (many invoices per customer):
- revenue: SUM(amount_eur), owner finance controlling, reconciled with the ledger every month.
- arpu: revenue divided by distinct customers, owner finance controlling, reconciled too.
- churn_rate: formula still discussed, no owner, no automated check.
Users say "paid revenue" and "average revenue per user". Give us the vendor-neutral definition file based on Apache Ossie.
