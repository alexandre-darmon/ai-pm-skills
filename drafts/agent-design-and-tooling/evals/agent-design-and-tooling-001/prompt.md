---
name: agent-design-and-tooling-001
description: 'Linear three-step workflow pitched as multi-agent (source - anonymised telecom brief, 2026)'
tags: [agent-design-and-tooling, nominal, red-line]
expected_outcome: 'A single loop, no multi-agent, stop conditions and traces.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

The team wants three cooperating AI agents for our invoice-dispute flow: one reads the dispute, one looks up the invoice in the ERP, one drafts the answer for an agent to send. The steps always run in that order. Design it.
