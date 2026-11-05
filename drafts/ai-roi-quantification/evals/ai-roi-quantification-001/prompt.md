---
name: ai-roi-quantification-001
description: 'Assistant with no baseline (source - anonymised bank brief, 2026)'
tags: [ai-roi-quantification, nominal, red-line]
expected_outcome: 'A labelled projection and a baseline plan, not an ROI claim.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Budget renewal for our HR assistant: 9,000 answers a month, 86% correct on sampled answers, HR estimates 8 minutes saved per answer at 40 EUR per hour, run cost 3,000 EUR a month, change cost 25,000 EUR. Nobody measured how long these questions took before launch. What's the ROI?
