---
name: chat-with-your-data-scoping-001
description: '50 questions, 10 on ambiguous metrics (source - anonymised telecom brief, 2026)'
tags: [chat-with-your-data-scoping, nominal, red-line]
expected_outcome: 'The ambiguous questions are blocked until defined; accuracy is set per class.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We collected 50 questions our sales managers ask. 10 of them use terms that mean different things across teams, such as active customer and margin. We have no shared metric layer yet. The vendor says its text-to-SQL reaches 90% and we can launch next month. Scope the product.
