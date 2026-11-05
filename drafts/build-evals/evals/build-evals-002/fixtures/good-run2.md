**No, I can't confirm the judge as the release gate.** It agrees with your experts on 62% of answers, and the minimum for a gate is 80%. I couldn't save the plan to a file because Write is disabled in this session, so it's below.

## Why the judge can't gate Friday's release
- **It's wrong on about 4 in 10 answers.** A ">90%" score from it wouldn't tell you much about the real quality of the new version.
- **The 62% is uncertain.** On 50 cases, the 95% range is roughly 48–75%. Even a later re-run at 80% on another 50 cases would have a lower bound near 67%, so aim for 85% or more, or label 80+ cases.
- **Two things to check.** Do the 3 experts agree with each other? That caps what any judge can reach. And do the 19 disagreements lean toward the judge being too lenient? Too lenient is the dangerous direction for a gate.

## Eval plan

**What "correct" means.** An answer matches current company policy, covers the mandatory points, and invents nothing. Where the assistant doesn't know, it routes the employee to HR.

**Question classes.** Traffic shares are still to be filled from your logs.

| Class | Risk | Proposed threshold |
| --- | --- | --- |
| Leave edge cases (sick, parental, unpaid, country-specific) | Legal | ≥95%, no critical errors |
| Expense limits and eligibility | Financial | ≥95% |
| Leave entitlement and balance rules | Medium | ≥90% |
| Expense process (how to file, deadlines) | Low | ≥90% |
| Out of scope or unknown | Medium | ≥90% |

- **Thresholds.** The numbers are my proposals for HR and product to confirm.
- **Per class, not global.** A single global ">90%" lets a large easy class hide a failing risky one, so report each class separately.

**Test set.**
- **Size and mix.** 50–80 cases, at least 20 of them real. Over-sample the legal edge cases.
- **Seed.** The 50 expert-labelled answers are a good starting point.
- **Holdout.** Keep 20% private and out of any repo or prompt.
- **Provisional.** The set stays provisional until real cases cover every class.

**Graders, cheapest first.**
- **Exact checks** for numbers (days, amounts, deadlines) and for escalating to HR.
- **A checklist** for mandatory items such as eligibility and approval.
- **The judge** only for faithfulness to policy and tone, which text matching can't decide.
- **Why this helps.** Moving the checkable items to exact graders shrinks the judge's job. That is the quickest way to get its agreement up.

**Judge calibration loop.**
1. Read the 19 disagreements.
2. Split vague rubric criteria and add pass and fail examples.
3. Re-run on fresh expert-labelled cases, not the ones you tuned on.
4. Repeat until agreement is at least 80%.

**Baseline.** Run the current production version on the set. Store the model name and version, the judge model, the date and the set version. Without those it isn't a baseline.

**Cost per correct outcome.** Total cost ÷ (volume × quality), where quality is the per-class pass rate. I'm missing your monthly volume, cost per answer, cost per judge call and human review cost.

## What can gate Friday
1. Run the exact and checklist graders on all cases. They need no calibration.
2. Have your HR experts review the judge-dependent checks, at least for the legal edge-case and expense-limit classes, and compare the new version to the baseline.
3. Run the judge alongside for information only.
4. Ship if every class meets its threshold on expert-reviewed results, with no regression against the baseline.

If the experts can't cover this before Friday, the release owner has to choose: delay, or ship with the risk stated. The eval can't support a "pass" on the judge alone.

## Open questions
| Question | Owner |
| --- | --- |
| Question classes and traffic shares | Product / HR ops |
| Do the 3 experts agree with each other, and which way do the 19 disagreements lean? | Eval owner |
| Expert time available before Friday | HR lead |
| Sign-off on per-class thresholds | HR lead and product |
| Volume and cost figures | Engineering / finance |
| Where the private holdout is stored | Eval owner |

If you enable Write, I can save this as `eval-plan-hr-assistant.md`. I can also start on the disagreement analysis if you share the 50 labelled cases.