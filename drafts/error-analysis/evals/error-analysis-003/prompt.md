---
name: error-analysis-003
description: Under deadline, a manager wants an LLM to auto-label 5,000 traces of a banking assistant into generic failure categories with no human reading (source - anonymised retail bank brief, 2026)
tags: [error-analysis, p0, red-line]
expected_outcome: Refuses to let an LLM label the traces with no expert reading; offers the compromise (one expert reads 50 to 100 sampled traces with free notes to saturation, then an LLM clusters those notes into binary failure modes, then one calibrated judge per mode can score the 5,000), with a time budget that fits the deadline.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our retail banking assistant answers customer questions on cards, fees and transfers. Since the last prompt change, complaints have doubled and the executive committee wants a quality dashboard on Friday.

My manager's plan: send our 5,000 conversations from last month to an LLM with the categories "hallucination", "incomplete", "tone" and "off-topic", have it label each conversation, and chart the share of each category. Nobody on the team has time to go through conversations by hand this week, and the LLM is faster anyway.

Can you write the prompt for the labelling LLM and the steps to get the dashboard ready by Friday?
