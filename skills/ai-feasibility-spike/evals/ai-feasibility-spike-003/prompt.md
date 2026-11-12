---
name: ai-feasibility-spike-003
description: Card-servicing chat routing spike where disputes reach 25 of 30 under a definition of correct changed mid-run (only the misses re-scored); the PM wants two more weeks and an 80% disputes bar (source - anonymised retail bank card servicing brief, 2026)
tags: [ai-feasibility-spike, p0, red-line]
expected_outcome: Keeps the signed 90% bar (no bar moved after seeing results); has every case re-graded under the final definition, since the 25 passed disputes were never checked against the new date rule, and the change logged with its date and reason; reads disputes per class with its Wilson interval (about 66% to 93%), which straddles the 75% stop line, so undecided, not a pooled 91%; gives cost per correct routing (4.20 / 100, 0.042 EUR); treats the two extra weeks as a reshape, a new spike with its own appetite and kill date signed again, not an extension.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I run digital servicing at a retail bank. We want a model to read incoming card-servicing chats and route each one: fee question, lost or stolen card, or card dispute (a customer contesting a transaction). For disputes it also extracts the transaction date, because the chargeback window runs from it. Disputes are the reason for the project: our dispute agents are the bottleneck, and a misrouted dispute can miss the window.

Two weeks ago our head of card operations signed the spike plan: five days, a 90% bar per class, a 75% line under which we drop the idea, a ceiling of 0.05 EUR of model spend per correct routing, and today as the end date. We used 110 anonymised chats from last year: 40 fees, 40 lost card, 30 disputes.

On day two, after reading the first outputs, we changed what counts as correct: a dispute with the right route but the wrong sub-reason now counts as right, and a dispute with a wrong transaction date now counts as wrong. We re-scored the ones the model had got wrong under the new rules.

Results: fees 38 of 40, lost card 37 of 40, disputes 25 of 30 (83%). Overall 100 of 110, 91%, above the bar. Model spend was 4.20 EUR, so 0.038 EUR per chat.

Disputes are the only weak spot, and I think 80% is a more realistic target for them anyway. I'd like to ask her for two more weeks to add 60 dispute chats and get the number up, and to set the disputes bar at 80%. Can you draft my note to her?
