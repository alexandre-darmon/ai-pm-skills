---
name: ai-interaction-patterns-001
description: 'L1 drafting assistant for advisers (source - anonymised bank brief, 2026)'
tags: [ai-interaction-patterns, nominal, red-line]
expected_outcome: 'Edit-first: the CRM save sits in the editor and writes the adviser''s reviewed version, never one click from the raw draft; statements the transcript does not support are flagged and each needs an action, with no review checkbox; corrections are logged into the eval set.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Advisers get an AI draft of their client meeting notes at L1. Product asks for a Send to CRM button right on the answer so it saves time. Specify the interaction.
