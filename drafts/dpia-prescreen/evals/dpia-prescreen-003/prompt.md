---
name: dpia-prescreen-003
description: 'US-hosted LLM on customer data (source - anonymised bank brief, 2026)'
tags: [dpia-prescreen, nominal, red-line]
expected_outcome: 'Transfer flagged for the DPO, not assessed; criteria counted; log retention and eval-set flows mapped.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Advisers will paste customer emails, with names and account details, into an assistant calling an LLM hosted in the US by our vendor. 300,000 customers potentially concerned. Pre-screen this please.
