---
name: dpia-prescreen-005
description: 'Recruitment scoring with nominal human review (source - synthetic scenario, 2026)'
tags: [dpia-prescreen, edge-case, red-line]
expected_outcome: 'DPIA required or recommended; art. 22 raised as a question for the DPO, the review challenged as possibly nominal, no conclusion on art. 22.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We are adding an LLM to our recruitment tool. It scores each application and the lowest-scored ones get a rejection email unless a recruiter overrides. Two recruiters handle about 400 applications a day and have overridden fewer than 1% in the pilot. Do we need a DPIA before go-live?
