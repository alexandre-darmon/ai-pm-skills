I found no eval files in the repo, so this review rests on what you described. I haven't seen your graders, labels or rubric. Some of the points below are therefore questions to check, not findings.

## Main problems

**1. One global score hides the class that matters.**
- Warranty is 10% of traffic but has legal consequences. At 12 of 120 cases, it counts for little in the overall score.
- The 88% is consistent with warranty answers being mostly wrong. If every warranty case failed and the other 108 were nearly perfect (about 106 correct), you would still score about 88%.
- Order status (60%) is probably the easiest class, and it dominates the average.
- **Change:** set one threshold per class and report the score for each. Make warranty strict, for example no critical errors and at least 95%. Any single class below its bar blocks the release.

**2. The set is too small for the threshold to mean anything.**
- Random sampling gives roughly 72 order, 30 returns, 12 warranty and 6 product cases.
- At 88% on 120 cases, the 95% confidence interval is about 82–94%. Your 85% bar sits inside the noise, so the gap between 88% and 85% doesn't show the version is good.
- Warranty at 12 cases is worse. Scoring 11 of 12 is consistent with a true rate anywhere from about 62% to 98%.
- Product advice has 6 cases, which is too few to say anything. That's acceptable only because it is 5% of traffic and low risk.
- **Change:** sample by risk as well as by traffic. Aim for about 50 warranty cases, 40 returns, 40 order status and 20 product, and include the hard variants of each. Weight the overall number back to traffic share if you still want one.

**3. Random cases from last month under-test the hard cases.**
- Rare failures show up only in a few conversations. These include edge-case warranty terms, expired warranties, cross-border rules, angry customers, requests to promise a refund, and prompt injection.
- Last month's traffic also won't cover new products or policy changes.
- **Change:** add a targeted adversarial and edge-case slice, labelled separately from the random slice. Refresh the set each release, and keep a private holdout of about 20% that never goes into prompts or tuning.

**4. "Correct" needs a definition per class.**
- Order status can be graded by exact checks: the right order, the right status field, the right tool call, and no invented dates.
- Returns can use a checklist: eligibility, window, and steps.
- Warranty needs an expert-written rubric and legal or compliance sign-off. It also needs a separate critical-error category. Examples are promising coverage that doesn't exist, denying valid coverage, and giving legal advice. One critical error should fail the class, however good the average is.
- **Change:** use exact or checklist graders wherever possible. Use an LLM judge only for tone and faithfulness.

**5. Check the judge, if you use one.**
- The judge must agree with domain experts, not the build team, on at least 20 cases, at 80% or higher agreement. Until it does, it can't gate a release.
- This matters most for warranty, where the judge may be lenient on confident but wrong answers.
- Have a human review all warranty failures and a sample of passes.

**6. No baseline.**
- Record the 88% with its model and version, the judge model, the date and the set version. Without these, you can't tell whether the next score is a real change or noise.
- Re-run the previous version on the new set so you compare like with like. Don't compare against 88% from a different set.

## Cost
- 0.04 EUR per answer is the cost per output. The cost per correct outcome is 0.04 ÷ 0.88 ≈ **0.045 EUR**.
- Track it per class. A wrong warranty answer costs far more than 0.045 EUR in legal exposure and escalations.
- Budget for the judge calls too. They are not in the 0.04 EUR.

## Before the next release
1. Split the existing 120 cases by class and report the per-class scores now. This takes no new data and may show a problem already.
2. Have legal or support experts label warranty cases and define the critical errors.
3. Add 40 or more warranty cases, plus the edge-case slice and a private holdout.
4. Set per-class thresholds and drop the single 85% gate.
5. Calibrate any judge, then freeze a baseline with full metadata.

If you share the cases and graders, I can compute the per-class scores and check the judge's agreement. I can also draft the eval plan using the build-evals template.