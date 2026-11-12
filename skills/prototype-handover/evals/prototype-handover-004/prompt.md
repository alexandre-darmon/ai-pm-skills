---
name: prototype-handover-004
description: 'Personal competitor-summary prompt app that 15 colleagues want to use, manager asks if IT must rebuild it (source - anonymised insurance group strategy brief, 2026)'
tags: [prototype-handover, p1, edge-case]
expected_outcome: 'Places it at tier 1 today and tier 2 once shared, with its autonomy level, proposes registering it at tier 2 instead of a rebuild, with a named owner, an inventory entry, prompts and model version under change control, a small eval set before sharing and a review date, and never says approved.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I work in group strategy at an insurer. Six weeks ago I built myself a small prompt app with a coding agent: I paste public annual reports and analyst notes on our competitors, and it drafts a two-page summary in our house format. Only I use it, and I rewrite every summary before it goes anywhere. It calls the model through our approved enterprise AI platform with my own login, and no client data goes in.

Fifteen colleagues in strategy and finance have asked for it, for their quarterly market reviews. My manager asks whether we need to hand it to IT to rebuild properly, which would take months.

What do you recommend?
