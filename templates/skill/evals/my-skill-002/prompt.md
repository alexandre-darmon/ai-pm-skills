---
name: my-skill-002
description: 'Edge case, a mandatory input is missing (source - origin, year)'
tags: [my-skill, edge-case]  # first tag is the skill name
expected_outcome: 'Asks for the missing input before producing anything.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

<A scenario where a mandatory input is missing.>
