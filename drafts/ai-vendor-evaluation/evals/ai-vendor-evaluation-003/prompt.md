---
name: ai-vendor-evaluation-003
description: 'Bake-off with a 5-point gap between two vendors on the same 60 cases, 9 of them split, the cheaper vendor 40% cheaper (source - anonymised retail bank brief, 2026)'
tags: [ai-vendor-evaluation, p1, edge-case]
expected_outcome: 'Shows the 5-point gap is inside the 10-point noise (2 x sqrt(9) / 60), calls it a tie, decides on cost per correct outcome with correction time (B about 7.76 EUR against 8.89 EUR), asks for the result per document class, and writes the decision with a re-evaluation date and triggers.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our mortgage team checks income documents (payslips and tax notices) for about 25,000 loan files a year. We ran a bake-off between two document-check vendors on the same 60 files from our own archive (40 with payslips, 20 with tax notices), scored by our analysts:

- Vendor A: 54 of 60 files fully right (90%). 150,000 EUR a year all-in.
- Vendor B: 51 of 60 files fully right (85%). 90,000 EUR a year, 40% cheaper.
- On 9 files exactly one of the two vendors was right (6 where only A was, 3 where only B was).

Each wrong file costs an analyst about 20 minutes to fix, at a loaded cost of 60 EUR an hour. Both vendors passed our data and contract checks (processing agreement signed, EU hosting, no training on our data, notice before any model change).

Our head of operations wants A because it is 5 points more accurate. Which vendor do we take? I need the decision for the committee.
