# Eval plan: HR assistant release (Friday)

## Can we use the judge as the release gate? No.

The judge agrees with the HR experts on 31 of 50 answers (62%). The bar for a gate is 80% or more. At 62%, about 1 in 3 verdicts disagrees with the experts, so a "90%" score from it doesn't tell us the assistant is 90% correct.

- **Raw agreement may overstate the judge.** If most answers are correct, a judge that says "correct" almost every time still scores high. We need the confusion matrix from the 50 labels. The two numbers that matter are how often the judge passes an answer the experts marked wrong, and how often it fails one they marked right. Wrongly passing a bad leave or expense answer is the costly error.
- **A single global 90% is the wrong rule.** Leave and expenses, and any class with legal or financial effect (statutory leave, pay, reimbursement limits), need their own thresholds. A large easy class would otherwise hide a failing risky one.
- **The 50 labelled answers are enough to measure agreement, but not to tune on and then re-measure.** Revising the rubric against the same 50 overfits it. Hold some of them out, or label new ones.

## Plan

**1. Task and classes** (to confirm with the team)
- Task: an employee asks an HR question about leave or expenses, and the assistant answers.
- "Correct" means the answer matches current policy, contains no invented entitlements or limits, and routes edge cases to HR.
- Proposed classes, each with its own risk and check:
  - Leave entitlement, statutory or legal.
  - Leave process.
  - Expense limits and eligibility, which are financial.
  - Expense process.
  - Out-of-scope or ambiguous questions that should escalate.
- Still needed from you: the real traffic share per class.

**2. Golden set**
- Size: 50–80 cases, at least 20 real, sampled by traffic and by risk. Legal and financial classes get more than their traffic share.
- The 50 expert-labelled answers can seed it if they are real employee questions.
- Keep 20% as a private holdout, kept out of prompts, repos and docs.
- If we have fewer than 20 real questions, any synthetic cases must be flagged per case, and the set is provisional.

**3. Graders, cheapest first**
- **Exact checks:** the policy figure is right (days, amounts, limits), the escalation or link is present, and no forbidden claim appears. Many leave and expense answers hinge on a number, so most can be checked by matching, with no judge.
- **Checklist:** one check per mandatory item in the answer.
- **LLM judge:** only for what matching can't decide, such as faithfulness to policy wording and tone. It needs a written rubric with pass and fail examples.

**4. Judge calibration (currently failing)**
1. Pull the confusion matrix and read the 19 disagreements.
2. Group them: vague criteria, missing policy context, or numeric errors the judge misses.
3. Split vague criteria, add pass and fail examples, and give the judge the policy text.
4. Re-run on fresh labelled cases. The target is 80% or more agreement, with a low rate of wrongly passing bad answers.
5. Until it passes, the judge is not a gate. Experts review whatever the judge would have decided.

**5. Thresholds, one per class** (proposals to confirm with HR)

| Class | Threshold |
|---|---|
| Statutory leave and pay/expense limits | Strictest (for example ≥ 95%, no wrong figures) |
| Process questions | Lower (for example ≥ 90%) |
| Escalation and out-of-scope | Set with HR |

The score is reported per class, and any class failing blocks the release.

**6. Baseline**
- Run the current production version on the same set.
- Store the model name and version, the judge model, the date and the set version. Without these it isn't a baseline.
- Judge the new version by comparison to the baseline, not by an absolute 90%.

**7. Cost per correct outcome**
- This is total cost divided by (volume × quality). Add it once we have the volumes.

## What to do before Friday
1. **Today:** get the confusion matrix and the 19 disagreements, and confirm the classes.
2. **Next:**
   - Build the exact and checklist graders first. They need no calibration, and they cover the highest-risk checks.
   - Revise the rubric and re-test it on new expert labels.
3. **Release decision:**
   - If the judge reaches 80% or more by Friday, use it only for the subjective checks, alongside the exact graders and per-class thresholds.
   - If it doesn't, gate on the exact and checklist graders plus expert review of a sample, especially for the high-risk classes. Or move the date. Don't ship on the 62% judge.

## What I need from you
- The real question examples and the traffic share per class (HR or support).
- The judge's 50 verdicts next to the expert labels, so I can build the confusion matrix.
- The policy source of truth the answers should match.
- Who owns the thresholds for the legal and financial classes.

I haven't written any files. This plan is in the conversation only.