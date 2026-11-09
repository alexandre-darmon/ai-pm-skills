---
name: ai-data-requirements-005
description: 'HR policies revised yearly and product specs changing weekly (source - anonymised industry brief, 2026)'
tags: [ai-data-requirements, p1, nominal, red-line]
expected_outcome: 'Distinct expiry per source type, stated in days or months; stale-answer KPI defined.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our assistant answers two kinds of questions: HR policies (leave, travel), revised once a year in January, and technical product specifications, which engineering updates almost every week. Last month it quoted a spec that had changed three weeks earlier. How should we keep the knowledge fresh?
