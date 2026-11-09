---
name: release-to-production-001
description: '1,800 weekly users, 3-point lift sought (source - anonymised bank brief, 2026)'
tags: [release-to-production, nominal, red-line]
expected_outcome: 'Sample size computed, A/B infeasible, plan falls back on shadow and canary.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

New prompt version passed the offline suite. The assistant has 1,800 weekly users, always the same people. We want an A/B test on task completion, currently 70%, to prove a 3-point lift. Plan the release.
