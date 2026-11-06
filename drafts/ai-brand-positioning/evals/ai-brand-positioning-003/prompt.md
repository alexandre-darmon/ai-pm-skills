---
name: ai-brand-positioning-003
description: 'Me-too assistant over public documents asking for a category of one (source - invented brief, 2026)'
tags: [ai-brand-positioning, edge-case, red-line]
expected_outcome: 'Says what is not ownable yet and what would have to be true, and writes only copy that is true today.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We built an assistant for risk teams at European banks. It answers questions on regulators' published guidance, using a commercial LLM and a retrieval index we built over those documents. Three vendors sell something very close. We have good prompts and a nice chat interface.

Our board wants us out of the comparison tables. Give us a category of one: the category name, the point of view and a tagline for the website.
