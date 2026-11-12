---
name: trace-review-tool-001
description: 'Complaints-reply drafts, 300 to review by three senior officers in two weeks, the PM wants a coding agent to build the app this afternoon (source - anonymised retail bank complaints brief, 2026)'
tags: [trace-review-tool, p0, nominal]
expected_outcome: 'Writes the brief: masking in the export step, a residual-leak check sized by 3/n (all 300, about 1%), a separate sampling script whose random stream alone gives the rate with its interval, pass/fail plus critique with reviewer id and timestamp on every label, approved storage, and the officers'' edits captured as overrides.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We piloted an assistant that drafts replies to customer complaints for our complaints team. It has been live for six weeks, about 1,800 drafts a month, and an officer edits every draft before it goes out to the customer.

The head of complaints wants three of her senior officers to go through 300 drafts over the next two weeks, so we know what goes wrong before we extend it to the card disputes team. Right now they would copy the drafts into Excel one by one. I would rather have Claude Code build a small web app this afternoon. Our logging platform can export the conversations as JSON lines (complaint text, customer details, the draft, the final letter sent).

Officers cost about 85 EUR an hour loaded, and reading one complaint with its draft takes them about 2 minutes.

Write the brief I hand to the coding agent, plus anything I need to settle before the officers start.
