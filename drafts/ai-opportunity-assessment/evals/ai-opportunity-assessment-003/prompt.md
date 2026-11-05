---
name: ai-opportunity-assessment-003
description: 'Support-ticket triage with history and categories (source - anonymised telecom brief, 2026)'
tags: [ai-opportunity-assessment, nominal, red-line]
expected_outcome: 'Go, LLM triage at L2 to start, non-AI alternative named, data readiness scored.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our B2B support receives 12,000 tickets a month by email in French and English. Two people spend their days reading each ticket and assigning one of 14 categories and a priority, with a median delay of 5 hours before a ticket reaches the right team. We have 3 years of tickets with the category finally assigned by the resolving team. Keyword rules were tried in 2023 and got about half of tickets right. Hosting must be in the EU.

Is this worth doing with AI, and how?
