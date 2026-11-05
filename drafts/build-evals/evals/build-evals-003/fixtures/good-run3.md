# Eval review: what to change before the next release

I haven't seen your graders, judge or baseline, only the setup you described. Questions about those are at the end.

## Main problem: one global score hides the risky class

The 88% is a traffic-weighted average. Warranty claims carry the legal risk but are only 10% of traffic, so they barely move the score. This per-class result is plausible and still passes:

| Class | Weight | Pass rate |
|---|---|---|
| Order status | 60% | 97% |
| Returns | 25% | 90% |
| Warranty | 10% | **50%** |
| Product advice | 5% | 80% |
| **Overall** | | **≈ 89.7%** |

Half of the legally consequential answers could be wrong and you would still ship. Random sampling makes it worse. A random sample of 120 gives you about 72 order, 30 returns, 12 warranty and 6 advice cases. Twelve warranty cases can't tell 95% from 75%. Six advice cases tell you almost nothing.

## Changes

1. **Replace the single threshold with one per class.**
   - Order status and returns: roughly 90–95%. You choose the exact numbers.
   - Warranty: strictest. Set a high bar on correctness and treat any wrong legal commitment as a blocker, not a point deducted from an average.
   - Product advice: lower is acceptable.
   - Report the score for every class on every run.

2. **Sample by risk, not only by traffic.**
   - Use about 50 warranty cases, even though that class is 10% of traffic.
   - Use about 30 cases each for order status and returns, and about 20 for advice.
   - Include hard cases: edge-of-warranty dates, ambiguous defects, customers pushing for a commitment, and cases where the correct answer is to escalate to a human.
   - At least 20 cases must be real conversations. Say so explicitly for any synthetic cases.

3. **Account for noise.**
   - At 88% on 120 cases, the 95% confidence interval is about ±6 points, so 82–94%.
   - The 85% bar sits inside that interval, so the gate can't separate "ready" from "not ready."
   - Compare new versus baseline on the same cases, and gate on the per-class lower bound for warranty.

4. **Use exact graders where you can.**
   - Order status is mostly checkable by exact match: the right order, the right status, and the right tool called.
   - Returns can use a checklist: window, conditions, and the correct next step.
   - Use an LLM judge only for tone and faithfulness. For warranty, use a rubric written with legal or support experts, and have those experts do the labelling.

5. **Calibrate any judge before it gates anything.**
   - Have domain experts label at least 20 cases.
   - Require at least 80% agreement with them.
   - Until a judge passes, a human reviews warranty outputs. An uncalibrated judge shouldn't gate a release, whatever the deadline.

6. **Keep a private holdout.**
   - Hold out 20% of cases and never put them in prompts, repos or documents.
   - Tune against the rest. Otherwise the score will rise through overfitting rather than real improvement.

7. **Freeze a proper baseline.**
   - Record the system version, model name, judge model, date and set version, with per-class scores.
   - Re-score last version's 88% on the new set. It isn't comparable to anything new, because the set changed.

8. **Report cost per correct outcome, not cost per answer.**
   - Total cost ÷ (volume × quality) at 88% is 0.04 / 0.88 ≈ **0.045 EUR per correct answer**.
   - Track it per class. A cheaper model that drops warranty accuracy is not a saving.

9. **Refresh the set from fresh traffic each month.** Add new failure types as they appear, such as new products, policy changes and new complaint patterns.

## What I need from you to finish the plan
- How each class is graded today: exact match, rubric, LLM judge or human.
- If you use a judge: which model, and whether anyone has measured its agreement with human labels.
- Per-class results from the last run, if they exist. This is the quickest way to see whether warranty is already failing.
- Who can label warranty cases, and what counts as correct for each: a legal reviewer or senior support agent.
- What this eval gates: a release only, or also giving the assistant more autonomy, such as answering warranty claims without human review.

I can write this up as a full eval plan using the template once you have these.