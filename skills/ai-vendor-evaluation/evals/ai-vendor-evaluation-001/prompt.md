---
name: ai-vendor-evaluation-001
description: 'Insurer choosing between two claims document-extraction vendors, one claiming 97% field accuracy on its own benchmark (source - anonymised P&C insurance brief, 2026)'
tags: [ai-vendor-evaluation, p0, nominal]
expected_outcome: 'Refuses to decide on the 97% claim, designs a blind bake-off on the insurer''s own documents scored per document kind with intervals, shows that field accuracy overstates the document outcome, computes cost per correct extraction with review time, clears the data path (processing agreement, health data, hosting) before any upload, lists the AI Act documents to ask for and the DORA register entry, and leaves the selection pending.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We are a property and casualty insurer. Our claims handlers key data from incoming claims documents by hand, about 85,000 documents a year, roughly 4 minutes each. We want to buy a document-extraction product and have two vendors left:

- Vendor A says its product reaches 97% field accuracy on its own benchmark of insurance documents, and showed us a very good demo. 0.45 EUR per document, 60,000 EUR integration.
- Vendor B has no published figure. 0.30 EUR per document, 75,000 EUR integration.

We extract about 12 fields per document. We have 300 real claims documents from last year with the values our handlers keyed: 140 repair invoices, 70 medical reports, 50 accident reports and 40 bank details forms.

Procurement would like to go with A on the strength of the 97%. Vendor A also offers to run our 300 documents through its online trial portal this week to show us. How should we choose?
