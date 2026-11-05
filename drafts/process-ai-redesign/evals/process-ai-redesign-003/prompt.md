---
name: process-ai-redesign-003
description: 'Claims process with 40% exceptions and handler tracking (source - anonymised insurance brief, 2026)'
tags: [process-ai-redesign, nominal, red-line]
expected_outcome: 'Exception redesign first, low target levels, and cse-consultation called because handlers are measured.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Motor claims: 4,000 a month, 40% of them need a manual exception (missing photos, disputed liability, garage quotes over limit). We want AI to speed up the process, and the new tool would also record each handler's processing time per claim so team leads can compare them. What should the target process look like?
