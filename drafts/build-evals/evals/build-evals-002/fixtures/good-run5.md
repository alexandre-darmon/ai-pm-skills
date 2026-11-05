**No, we can't use the judge as the release gate.** It agrees with the experts on 31 of 50 answers (62%), and the bar for gating is at least 80%. The 50-case sample is small, so the true agreement could plausibly be anywhere from about 48% to 75%. It is unlikely to be above 80%.

A judge that is wrong on roughly 4 in 10 answers makes "above 90%" meaningless. It could pass a bad release or fail a good one. For leave and expenses, a wrong answer has policy and money consequences. I don't know which way the judge errs, and that decides how risky it is: if it passes wrong answers, a bad version ships.

# Eval plan: HR assistant release (Friday)

## 1. Task and classes
- **Task:** answer employee questions on leave and expenses. Correct means the answer matches current HR policy, with the right numbers, eligibility and process.
- **Classes (to confirm with HR):**
  - Leave entitlement and calculations
  - Leave process and approvals
  - Expense limits and eligibility
  - Expense process
  - Edge cases and out-of-scope questions, where the right behaviour is to escalate to HR
- **Missing:** the traffic share per class, from you or from the logs.

## 2. Set composition
- Use 50–80 cases, at least 20 of them real employee questions, sampled by traffic and by risk.
- Give money and entitlement classes more cases than their traffic share.
- Hold out 20% privately. Don't put it in prompts, repos or docs.
- You already have 50 expert-labelled answers. Reuse them as the calibration set and as the base of the golden set.
- **Missing:** whether those 50 are real traffic, and their class breakdown.

## 3. Graders, cheapest first
- **Exact or checklist checks** cover most of this domain:
  - the number of days, the amount or the limit matches the policy value
  - the right policy is cited
  - the escalation happened when required
- **LLM judge** only for what text matching can't decide, such as completeness and tone. Give it a written rubric.

## 4. Judge calibration (currently failing)
- Status: 62% agreement, so **not a gate**.
- By Wednesday:
  1. Read the 19 disagreements and split them into judge too lenient, too strict, or the experts disagreeing with each other.
  2. Revise the rubric: split vague criteria and add pass and fail examples.
  3. Re-run on at least 20 new expert-labelled cases, not the ones used to tune the rubric, to avoid overfitting.
  4. Accept the judge only at 80% or higher, and also check that it doesn't pass wrong answers on the risky classes.
- Check inter-expert agreement. If the three experts disagree with each other, the labels are the ceiling.

## 5. Thresholds
- Set one threshold per class, not a single global "90%".
- Money and entitlement classes should be stricter, for example 95% or higher and no wrong numbers.
- Report scores per class.
- **Missing:** the thresholds themselves. HR and the product owner decide them.

## 6. Baseline
- Run the current production version on the same set.
- Record the model name and version, the judge model, the date and the set version.
- The release criterion is no regression against the baseline, and meeting the per-class thresholds.

## 7. Economics
- Cost per correct outcome = total cost ÷ (volume × quality). Report it alongside the score.

## 8. What the eval gates, until the judge passes
- **Release gate:** the exact and checklist graders, plus human review by an HR expert of every case the judge would have decided. Sample the risky classes in full.
- The judge's score is informational only until it clears 80%.

## Friday timeline
- **Today:** analyse the disagreements and build the exact checks. Get the class breakdown and traffic shares.
- **Tuesday–Wednesday:** revise the rubric, re-calibrate on fresh labels, and run the baseline.
- **Thursday:** run the new version and review the cases flagged for human review.
- **Friday:** ship if per-class thresholds are met with no regression against the baseline. If the judge still isn't calibrated, ship on the exact checks and human review, or delay.

I can start on the disagreement analysis if you share the 50 labelled cases.