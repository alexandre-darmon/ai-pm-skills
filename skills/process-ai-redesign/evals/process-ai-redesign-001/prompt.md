---
name: process-ai-redesign-001
description: 'KYC document review in retail banking (source - anonymised bank brief, 2026)'
tags: [process-ai-redesign, nominal, red-line]
expected_outcome: 'Extraction L2, verification L3, onboarding decision L1; a gate per step; three scenarios.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our KYC team reviews 9,000 new-customer files a month. Steps: (1) read ID, proof of address and income documents and type the data into the core system, 12 minutes; (2) check the data against sanctions lists and internal rules, 6 minutes; (3) decide to open the account or ask for more documents, 3 minutes. About 8% of files have an issue. 25 people do this today. The COO wants a plan to use AI on this process.
