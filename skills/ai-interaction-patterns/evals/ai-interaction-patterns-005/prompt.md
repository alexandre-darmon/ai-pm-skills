---
name: ai-interaction-patterns-005
description: 'Customer assistant with a "95% sure" label and a reliability table from labelled conversations (source - anonymised retail bank brief, 2026)'
tags: [ai-interaction-patterns, p0, nominal]
expected_outcome: 'Computes each bucket from the table (92% with an interval of about 89% to 95% on top, 74%, 48%), drops the "95% sure" label and the raw scores, words any figure as a measured frequency no higher than the lower bound, keeps the lowest bucket from answering and hands it to a person, and puts the AI Act art. 50(1) disclosure on the first screen.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our customer assistant goes live in the banking app next month. It answers questions about fees, card limits and transfers. Product wants a green "95% sure" label on answers where the model's confidence score is 0.9 or more, and the raw score shown as a percentage on the others, so customers know when to double-check.

The data team scored 600 past conversations that our experts labelled right or wrong:
- score 0.9 or more: 310 answers, 286 right
- score 0.7 to 0.9: 190 answers, 141 right
- score below 0.7: 100 answers, 48 right

What should customers see?
