---
name: my-skill-004
description: 'Negative case, a near-miss request that belongs to another skill (source - origin, year)'
tags: [my-skill, negative]  # first tag is the skill name; negative = the skill must not fire
expected_outcome: 'Handles the request without loading my-skill.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

<A request close to this skill's job but covered by one of its "Do not use" bullets.>
