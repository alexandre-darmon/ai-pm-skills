---
name: build-evals-005
description: Invoice pipeline at 84% end to end; the team wants to swap the extraction model without knowing which step fails (source - anonymised accounts-payable brief, 2026)
tags: [build-evals, p1, edge-case]
expected_outcome: Keeps the end-to-end score as the release gate, adds a labelled check per step, labels the first failing step on the failed cases, scores a step on frozen upstream outputs, and compares old and new extraction on the same cases before any swap.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our supplier-invoice pipeline has four steps: OCR on the PDF, an LLM that extracts supplier, amount, VAT and due date, business rules that validate the fields, and posting to the ERP. On our 120 test invoices, 84% end up posted correctly. The team thinks the LLM is the weak point and wants to switch to a newer model next sprint.

What should we measure before deciding?
