---
name: synthetic-eval-data-003
description: Consumer-credit assistant scoring 94% on 500 tidy English generated questions while pilot users write short French messages with typos (source - anonymised consumer finance brief, 2026)
tags: [synthetic-eval-data, p1, edge-case]
expected_outcome: Adds language and writing style as a dimension anchored on pilot messages, compares the set with pilot traffic on length, language and class mix, rejects and regenerates, reports the 94% as a score on synthetic cases only, and brings in masked pilot cases.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Last month we generated 500 test questions for our consumer-credit assistant with an LLM. They are clean, well-formed English, 22 words on average, spread evenly over our six topics. The assistant scores 94% on them.

The pilot started three weeks ago: 1,800 conversations so far. Customers write mostly in French, on their phones: short messages, typos, no accents, some English words mixed in, and two topics (repayment difficulties and early settlement) make up most of the traffic. Escalations to human agents are much higher than the 94% suggested.

What do we do with our test set?
