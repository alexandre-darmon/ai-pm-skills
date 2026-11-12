---
name: red-team-evals-001
description: 'Claims assistant with RAG, a customer-scoped claim lookup and uploads; model risk wants attack evidence before release in six weeks (source - anonymised insurance claims assistant brief, 2026)'
tags: [red-team-evals, p0, nominal]
expected_outcome: 'Plans the campaign from the feature''s own harms (another customer''s claim, an instruction hidden in an upload that makes it disclose claim data, promised coverage, prompt leak), writes a binary success criterion and a tolerable rate per class before testing, sizes the costly classes on the Wilson bound the reading uses, about 4/r in held-out seeds (about 765 to 800 for the cross-customer and upload-injection classes at 0.5%), says the 30 developer jailbreaks are not evidence, seals a held-out set kept by testers outside the build team, maps coverage and lists what stays untested, and turns every success into a regression case.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm the PM for our claims assistant at a mid-size insurer. Policyholders ask about their open claims in the app. How it works:

- answers from our policy wording and claims FAQ (about 1,200 documents in a vector store);
- a tool `get_claim(claim_id)` that returns the claim file (status, amounts, adjuster notes, medical details for injury claims). The app passes the logged-in customer's id, but the model chooses the claim_id;
- customers can upload photos and PDFs (invoices, police reports) that the assistant reads.

About 40,000 conversations a month expected. Go-live is planned in six weeks. Our model risk team says they won't sign without "evidence that the assistant resists attacks", and the CISO's team has offered two people for a week. My developers have already tried around 30 jailbreaks from the internet and nothing got through.

What should the attack testing look like, and what do I bring back to model risk?
