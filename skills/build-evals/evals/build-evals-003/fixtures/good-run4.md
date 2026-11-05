**Main finding: the 88% doesn't tell you whether the assistant is safe to ship, because it can hide a failing warranty class.**

## Problems

1. **One global threshold.** The overall score is weighted by traffic, so order status carries 60% of it. Say order status scores 95%, returns 90% and advice 80%. That gives 83.5% from those three classes before warranty is counted. Warranty could then score around 15% and the overall score would still clear 85%. Warranty is the class with legal consequences, and it has the least influence on the gate.

2. **Too few warranty cases.** A random sample of 120 contains about 12 warranty cases (10%) and about 6 advice cases. With 12 cases, one error moves the class score by 8 points, and the 95% interval is roughly ±25 points. You can't tell a 95% warranty class from a 70% one.

3. **The gate sits inside the noise.** At n=120 the overall 88% has a 95% interval of about 82–94%. The 85% line falls inside it, so "above 85%" is close to a coin flip. Small changes in the score between versions aren't real signal.

4. **The sample is random, not stratified by risk.** Sample size should follow risk as well as traffic. The set is also a single month of data, so it has no seasonal or edge cases. It may also overlap with data used to tune prompts. There is no private holdout.

5. **Unknown grading.** You didn't say how answers are graded. If an LLM judge scores them, it needs calibration against domain-expert labels, with at least 20 cases and at least 80% agreement. Without that, the 88% isn't a trustworthy number. Order status can mostly be graded exactly (the right status or tool call, matching the order data), which is cheaper and more reliable than a judge.

6. **No baseline and no cost per correct answer.** I don't see a frozen run with the model, judge, date and set version. The cost figure of 0.04 EUR per answer divides by all outputs. Divided by successes, it is 0.04 / 0.88 ≈ **0.045 EUR per correct answer**. For warranty, the cost of a wrong answer is legal, not 0.04 EUR.

## What to change before the next release

1. **Split the set into four classes and gate each one separately.** Report the score per class. Suggested starting thresholds, to be set with your legal and support leads:
   - Order status: ≥95%, graded exactly
   - Returns: ≥90%
   - Warranty: ≥98%, or any legal-critical error blocks the release regardless of the score
   - Product advice: ≥80%

2. **Rebalance the set by risk.** Aim for 50–80 cases to start, and more if you can label them. For example: ~20 order status, ~15 returns, **~25 warranty**, ~10 advice. Include adversarial warranty cases such as expired warranty, a claim outside coverage, a request for a promise, and a user threatening legal action. Warranty cases should be labelled by someone from legal or the warranty team, not the build team.

3. **Pick graders per check, cheapest first.**
   - Exact checks for order status and for return eligibility and policy facts.
   - A checklist for warranty (correct terms cited, no promise of coverage, escalation to a human when required).
   - A judge only for tone and coherence. Calibrate it on at least 20 expert-labelled cases and require agreement of at least 80%.

4. **Keep 20% of the cases as a private holdout.** Don't put them in prompts, repos or tuning loops.

5. **Freeze a baseline.** Run the current version on the new set and record the model and version, the judge model, the date and the set version. Compare every release to that run. Don't compare it to the old 88%, because it was measured on a different set.

6. **Report cost per correct outcome by class.** Use total cost ÷ (volume × quality), not cost ÷ all answers.

7. **Treat the old 88% as unproven.** Rescore the last version on the new set before you decide whether the next one is better.

If you send me the current cases and grader (or judge prompt), I can check the class split, label quality and judge agreement directly. I haven't seen any of those yet. This review is based only on the numbers you gave me.