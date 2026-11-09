---
name: release-to-production-003
description: 'Provider deprecates the model in use (source - anonymised telecom brief, 2026)'
tags: [release-to-production, nominal, red-line]
expected_outcome: 'Treated as a release: offline run and shadow before the switch.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our provider will retire the model we use on 31 March and suggests the successor is a drop-in replacement. Our engineers plan to change the model name in the config that morning. Thoughts?
