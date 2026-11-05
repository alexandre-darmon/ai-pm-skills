---
name: build-evals-001
description: Invoice classification eval with only 8 labelled examples (source - anonymised finance-ops brief, 2026)
tags: [build-evals, p0, edge-case]
expected_outcome: Says 8 examples are not enough, asks for more real cases, and if synthetic cases are generated states their share and flags them; the set is provisional.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our accounts payable team wants an LLM to route incoming supplier invoices into 5 categories (goods, services, utilities, rent, other). We have 8 invoices labelled by the team, below. We pick a model next week, so build the eval set we will use to compare them.

1. Office chairs x12, 2,340 EUR: goods
2. Monthly cleaning contract, October: services
3. Electricity bill, site Lyon, Q3: utilities
4. Office lease, November: rent
5. Laptop repair, labour only: services
6. Printer toner x30: goods
7. Water bill, site Lille: utilities
8. Conference sponsorship: other
