---
name: synthetic-eval-data-001
description: Mortgage assistant six weeks before launch with only 12 real customer questions and a 150-case eval set to build (source - anonymised retail banking brief, 2026)
tags: [synthetic-eval-data, p0, nominal]
expected_outcome: Derives dimensions from the 12 questions, lists tuples before writing inputs in a separate step, has experts review and records the rejection rate, flags every synthetic case and states the share per class, and plans replacement by real cases with a date.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We launch a chat assistant for our mortgage customers in six weeks. It answers questions on early repayment, rate changes, payment holidays, loan insurance and the documents we need. Our eval set should have about 150 cases, but branch advisers only collected these 12 real questions:

1. "je veux rembourser 20k par anticipation, combien de frais ?"
2. Can I pause my payments for 3 months, I lost my job
3. "taux variable, il passe a combien en janvier"
4. Which documents do you need to change the bank account for my loan?
5. "assurance emprunteur je peux changer ? j'ai 52 ans"
6. "remboursement total du pret, le notaire demande un decompte"
7. Why did my monthly payment go up?
8. "modulation des echeances c'est possible ?"
9. My wife passed away, what happens to the loan
10. "attestation de pret pour les impots"
11. "on a vendu la maison, que faire du pret"
12. Is the early repayment penalty capped?

How do we get to a usable 150-case set before launch?
