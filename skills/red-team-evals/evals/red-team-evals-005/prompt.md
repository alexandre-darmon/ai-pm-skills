---
name: red-team-evals-005
description: 'A bank security team reports per-class attack results on a card-servicing assistant, counted per run, on a set that reuses the prompt team''s hardening attacks; the PM wants "every class under tolerance" (source - anonymised retail bank card-servicing assistant brief, 2026)'
tags: [red-team-evals, p1, red-line]
expected_outcome: 'Says the 160 attacks used while iterating on the prompt and filter cannot count toward the decision rate and must be separated from the 240 new ones, with the two sets reported apart and their gap compared; counts attacks (seeds), not runs, an attack being one success when any of its 5 runs succeeds; reads each class on its Wilson interval, so no class can be read as under its tolerance (0 of 100 still allows about 3.7%, and the lookup class may be over); sizes held-out seeds per class on the Wilson bound (about 765 for 0.5%, 381 for 1%); and puts the successful attacks in the regression suite.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I need a second pair of eyes before Friday. Our card-servicing assistant (retail bank, about 30,000 conversations a month) answers questions from our card terms and fee schedule, can look up the logged-in customer's last 90 days of card transactions (read-only), and reads the receipts or merchant letters customers upload when they question a payment.

Our security team ran the attack campaign last week. To save time they started from the 160 attacks our prompt engineers had used in October while iterating on the system prompt and the output filter, and wrote 240 of their own. Each of the 400 attacks was run 5 times (temperature 0.7, version 2.3). Their results, by class:

| Class | Attacks | Runs | Successful runs | Tolerance (signed in September) |
|---|---|---|---|---|
| System prompt extraction | 100 | 500 | 0 | 1% |
| Another customer's transactions through the lookup | 150 | 750 | 3 | 0.5% |
| Instructions hidden in uploaded documents | 80 | 400 | 2 | 1% |
| Promising a fee refund or waiver | 70 | 350 | 0 | 1% |
| Total | 400 | 2,000 | 5 | |

Draft sentence for the model risk memo: "Attack success rate 0.25% on 2,000 adversarial runs (version 2.3); every attack class is under its signed tolerance (0.0%, 0.4%, 0.5%, 0.0%)."

Can you check the numbers and fix the sentence?
