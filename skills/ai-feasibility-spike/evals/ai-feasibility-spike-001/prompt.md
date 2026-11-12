---
name: ai-feasibility-spike-001
description: Insurer wants an agent built over a few weeks to triage claims emails, before the COO commits budget (source - anonymised insurance claims operations brief, 2026)
tags: [ai-feasibility-spike, p0, nominal]
expected_outcome: Sets one question, fixes a time box in days (or one week), a maximum cost per correct answer derived from the handler minutes it replaces, a target and stop line per class (stricter on bodily injury, which gets more cases, sized for its stop line) and a kill date before building; starts with a fixed workflow, not an agent; anonymised or synthetic cases only; removes forwarding in code (the lethal-trifecta check); ends on go to PRD, reshape or stop.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I'm a product manager at a mid-size insurer. Our claims inbox receives about 6,000 emails a month. Handlers spend around 4 minutes on each one: they sort it into motor, home, liability or bodily injury, key in the policy number, and forward it to the right team. A bodily injury email sent to the wrong team delays a statutory acknowledgement letter.

The COO wants to know whether AI could take this over before she commits budget to a real project. I have Claude Code and access to the model our group already approved, through the group's API gateway.

My idea is to build an AI agent over the next few weeks that reads the inbox, classifies and routes each email, and then show her the result. How should I set this up so she can decide?
