---
name: trace-review-tool-004
description: 'Motor claims settlement letters: a review tool sketch that loads thumbs-down letters first and pre-fills a GPT score, quality rate for the steering committee (source - anonymised insurer claims brief, 2026)'
tags: [trace-review-tool, p1, nominal]
expected_outcome: 'Moves sampling into a separate script with a random stream that alone gives the rate with its interval, says the thumbs-down fill over-counts failures, replaces the pre-filled score with an expert pass/fail read first, keeps a dev/test split for a later judge, computes 840 EUR of review and asks for cost per correct letter, not only per run.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our claims assistant drafts motor settlement letters for claims handlers, about 12,000 letters a month. 4% of letters get a thumbs-down from handlers.

Our data scientist has sketched a review tool and wants a coding agent to build it this week. To save the handlers' time, the tool first loads the letters that got a thumbs-down, then fills up with other recent letters until it reaches 240, and GPT pre-fills a quality score from 1 to 5 that the handler confirms or changes. Two senior handlers would do it, about 3 minutes per letter, at a loaded 70 EUR an hour. At the end we report the average score and the share of letters scored 4 or 5 to the steering committee as our quality rate.

The steering committee also asked what one run of the assistant costs. A letter uses about 9,000 tokens in total, and our contract prices tokens at 0.004 EUR per thousand.

Please turn this into the brief for the coding agent.
