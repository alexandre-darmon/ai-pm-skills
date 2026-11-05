---
name: semantic-layer-design-001
description: 'Two teams, two definitions of active customer (source - anonymised telecom brief, 2026)'
tags: [semantic-layer-design, nominal, red-line]
expected_outcome: 'A conflict register entry, both versions draft, a named decider.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Marketing counts a customer as active with a login in the last 90 days: 412,000. Finance counts one with an invoice paid in the last 12 months: 365,000. The comex sees both numbers. We want to feed this to our data assistant. Sort it out.
