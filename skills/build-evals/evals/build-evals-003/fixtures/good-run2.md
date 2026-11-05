# Eval review: what to change before the next release

The main problem is the single overall score. With random sampling, the class that matters most is barely tested, so the 88% tells you very little about it.

## What's wrong

**1. One global threshold (>85%) hides the risky class.**
- A random sample of 120 gives about 72 order-status, 30 returns, 12 warranty and 6 product-advice cases.
- If the assistant failed all 12 warranty cases and got every other case right, the overall score would still be 90%.
- Warranty claims have legal consequences, so they should have the strictest gate. At the moment they have none.

**2. Warranty has too few cases to measure anything.**
- With 12 cases, one or two failures move that class's score by 8–17 points.
- Even a clean 12/12 only shows the true pass rate is probably above about 75%. That isn't enough for a legal-risk class.
- The same applies to product advice with about 6 cases, though its risk is low.

**3. Sampling by traffic matches the wrong priorities.**
- Order status makes up 60% of the set and is likely the easiest class, so it dominates and inflates the score.
- Sample by traffic and by risk. Rare classes with legal or financial impact need more cases than their traffic share.

**4. The 88% can't be compared with a future score.**
- Nothing says it was a frozen baseline with model version, judge model, date and set version.
- With 120 cases, the noise is about ±6 points. A move from 88% to 86% or 90% may be noise.

**5. Three things I can't see and you need to confirm:**
- **Grader:** I don't know how cases are scored. If an LLM judge scores them, it needs calibration against domain experts, with at least 80% agreement on 20 or more cases. Until it passes, it isn't a valid gate.
- **Labels:** I don't know who labelled the expected answers. Warranty "correct" should be defined by legal or support experts, not the build team.
- **Holdout:** Check whether there is a private holdout. If the team iterates on all 120 cases, the score is optimistic.

## What to change

1. **Stratify the set.** Aim for about 80–100 cases, at least 20 of them real.

   | Class | Cases |
   |---|---|
   | Order status | 25 |
   | Returns | 25 |
   | Warranty | 30–40, including edge cases such as expired warranty, excluded damage and ambiguous claims |
   | Product advice | 10 |

   Hold out 20% privately, outside any repo or prompt. Keep the 120 real conversations as a separate traffic-weighted sample for the baseline.

2. **Set one threshold per class and report each separately.** These numbers are my suggestions, so adjust them to your risk tolerance.
   - Order status ≥ 90%.
   - Returns ≥ 90%.
   - Warranty ≥ 95%, with zero tolerance for wrong legal commitments such as promising coverage or refusing wrongly. Any such critical failure blocks the release.
   - Product advice ≥ 80%.
   - Ship only if every class passes.

3. **Use cheap exact graders where possible.** For order status, check that the tool was called and the status field matches. For returns, check the policy window and the steps. Use an LLM judge with a written rubric only for tone and faithfulness, and for warranty, add a mandatory-items checklist, such as the correct clause and a disclaimer or human handoff.

4. **Calibrate the judge** with 20 or more expert-labelled cases and at least 80% agreement. Until then, a human reviews warranty answers.

5. **Freeze a baseline** for the current version. Store the model name and version, judge model, date, set version and per-class scores. Compare future runs to it, and treat gaps smaller than the noise as ties.

6. **Report cost per correct outcome, not per answer.**
   - At 88%, it is 0.04 ÷ 0.88 ≈ 0.045 EUR.
   - Track it per class. A cheaper model that drops warranty accuracy is not a saving.

## What I need from you

- How the 88% is currently scored: exact checks, an LLM judge, or humans.
- Who labelled the expected answers.
- Whether you have per-class results from the last run. If you do, I can check whether warranty was already weak.
- Whether you have any real warranty conversations beyond the 12 in the suite, so I can build the larger warranty slice.

I haven't looked at any files in the repo. This review is based only on your description. If the eval cases are in the repo, point me to them and I can check them against the points above, and draft the cases in the `claude plugin eval` format.