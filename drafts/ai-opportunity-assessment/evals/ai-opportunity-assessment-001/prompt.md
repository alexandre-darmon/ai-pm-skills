---
name: ai-opportunity-assessment-001
description: 'Overdue-invoice prioritisation that a query covers (source - anonymised finance brief, 2026)'
tags: [ai-opportunity-assessment, p1, nominal, red-line]
expected_outcome: 'No-go on AI: a deterministic query on due date and amount does the job, named as the recommendation.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our collections team wants "an AI" that tells them each morning which unpaid invoices to call first. Today they sort an Excel export by hand, about 45 minutes a day. The criteria they use: invoices more than 60 days past due, amount above 5,000 EUR, and customers who already missed a payment this year. All three fields are in the ERP. A vendor offered us an AI collections assistant at 30k EUR a year.

Should we do this with AI?
