---
name: dpia-prescreen-001
description: 'Employee chat logs analysed for sentiment (source - anonymised industry brief, 2026)'
tags: [dpia-prescreen, nominal, red-line]
expected_outcome: 'DPIA recommended, criteria named and counted, controller decides on the DPO's advice.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

HR wants to analyse the internal assistant's chat logs to detect low morale per team: 4,000 employees, messages linked to user IDs, weekly report to managers. Do we need an impact assessment?
