# Eval review: what to change before the next release

The current 88% doesn't show the release is safe. Warranty, the class with legal consequences, is barely tested. I haven't seen the cases, graders or outputs, only your description. Anything about graders, judges and baselines below is a question for you, not a finding.

## Main problems

**1. One global threshold hides the risky class.**
- A random sample of 120 cases gives about 72 order status, 30 returns, 12 warranty and 6 product advice.
- Suppose order status passes 95%, returns 90% and advice 100%. Warranty could then pass only about 4 of 12 (35%) and the overall score would still be 88%.
- The overall score is mostly an order-status score. That class is 60% of traffic and probably the easiest.

**2. Warranty has about 12 cases, which is too few to gate on.**
- Even 12/12 passes gives a 95% interval of roughly 76–100%. That cannot show 90% or better.
- 11/12 gives a lower bound near 65%.
- Reading a rate near 90% within ±10 points takes about 35 cases. Within ±5 points it takes about 140.
- A class with legal impact needs enough cases for its threshold, whatever its share of traffic. Oversample warranty instead of sampling by traffic.

**3. 88% against an 85% bar is inside the noise.**
- With 120 cases the 95% interval on 88% is about 81–93%.
- The 3-point margin is not a pass. Compare the new version to the last one on the same cases (paired) and treat small gaps as ties.

**4. Product advice has about 6 cases.** It is 5% of traffic, so the impact is low. Report it separately and don't gate on it.

## What to change

1. **Define "correct" per class and name the costliest error.** For warranty it is probably a wrong promise or denial of coverage. Set the thresholds from that error.
2. **Set one threshold per class, signed and dated before the run.**
   - Warranty gets the strictest bar, and the gate passes only if the *lower bound* of its interval clears the threshold.
   - Make one warranty check non-relaxable, for example "never states a legal or coverage commitment without the policy basis".
   - Name who signs thresholds and who may relax them.
3. **Rebuild the set by class.**
   - Aim for about 140 warranty cases (at least 35 as a floor), 50–60 returns and 40–50 order status. Add a small product-advice set for monitoring.
   - Use real cases wherever possible. If you add synthetic ones, flag them per case.
   - Keep 20% as a private holdout, kept out of prompts and repos.
4. **Read outputs before trusting graders.** Have a domain expert, not the build team, review 50–100 outputs, especially warranty ones. Group the failures into modes and write one grader per mode. Use exact or checklist graders where code can decide, for example the right policy cited, the right order data, or a required escalation.
5. **Validate any LLM judge before it gates.** Test it on held-out expert labels. TPR and TNR must each be at least 80%, and stricter for warranty. Until it qualifies, a human reviews the warranty cases.
6. **Freeze a baseline.** Store the last version's per-class scores with model name and version, judge model, date and set version. A baseline without those fields doesn't count.
7. **Report cost per correct answer.**
   - At 0.04 EUR per answer and 88% quality, cost is 0.04 ÷ 0.88 ≈ 0.045 EUR per correct answer.
   - Compare versions on that figure. For warranty, also weigh it against the cost of one wrong legal answer.
8. **Feed production failures back in as regression cases** after release.

## Questions for you

- How are cases graded today (exact, rubric, LLM judge, human)? Has the judge been checked against expert labels?
- Who labels the cases, and are they domain experts?
- What are the per-class scores for the 88%? If warranty is already visible, send me the numbers.
- Is there a stored baseline with model and judge versions?

Once I have those, I can write the full eval plan with the thresholds, set composition and case sizes filled in.