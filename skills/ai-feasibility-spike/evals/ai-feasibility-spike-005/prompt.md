---
name: ai-feasibility-spike-005
description: Invoice-coding agent spike at 41 of 50 correct and 31 EUR of API spend, against a 0.25 EUR cost ceiling; the PM compares 0.62 EUR per invoice with the accountants' 0.90 and wants the PRD (source - anonymised industrial group finance brief, 2026)
tags: [ai-feasibility-spike, p1, edge-case]
expected_outcome: Computes cost per correct coding as 31 / 41, about 0.76 EUR, three times the 0.25 ceiling fixed before the run, and adds the rework of the 9 wrong codings (about 8 EUR of accountant time); rejects the per-invoice comparison and the "cheaper models later" argument as unmeasured; decides reshape (a fixed workflow where code does the vendor and PO lookups and one model call picks the account, re-run under a new appetite and kill date) or stop, not a go to PRD.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm the finance systems PM at an industrial group. Our shared service centre codes about 22,000 supplier invoices a month (general ledger account plus cost centre); an accountant costs us about 0.90 EUR per invoice for that step.

Before starting, the CFO and I agreed on a five-day time box and a cost ceiling of 0.25 EUR. In three days I built an agent with Claude Code: it reads the invoice text, searches the vendor master and the purchase order tables through tools, and proposes the account and cost centre. It makes about 14 tool calls per invoice.

On 50 anonymised invoices it coded 41 correctly. The API bill for the run was 31 EUR, so 0.62 EUR per invoice, already cheaper than the accountants' 0.90. Prices will drop with the next model generation anyway.

I'd like to tell the CFO we go to the PRD. Can you write my summary?
