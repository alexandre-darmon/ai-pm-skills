# Release eval plan: HR assistant (leave and expenses)

## Can we use the judge as the release gate? No.

- **The judge is not validated.** The skill's rule is that a judge gates a release only if its TPR and TNR on held-out expert labels each reach the bar set beforehand (80% by default). Raw agreement doesn't qualify it. You've given me only agreement, 31/50 (62%), with a 95% Wilson interval of about 48–74%. It is also well short of the 90% you want to gate on.
- **Agreement hides the failure that matters.** I can't tell from 62% whether the judge passes wrong answers (a false pass, which ships bad leave or expense advice) or fails right ones. If most answers are correct, a lenient judge agrees often and catches little. Please send the confusion matrix: judge pass/fail against the expert majority label.
- **A score above 90% wouldn't mean 90% of answers are correct.** With this agreement level, the judge's score is only loosely tied to real quality.
- **Check whether the 50 labels were also used to write the judge prompt.** If they were, even the 62% is optimistic.

Friday doesn't change this rule.

## Plan

### 1. Task and classes
- **Task:** an employee asks about leave or expenses, and the assistant answers.
- **Costliest error:** a confident wrong answer, such as a wrong entitlement, deadline or reimbursement rule. The employee acts on it, and HR or legal consequences follow. False passes are therefore worse than false fails.
- **Classes (to confirm with HR):** leave entitlement and eligibility, leave process, expense policy and limits, expense process, and out-of-scope or escalation questions. Each needs its traffic share, which I don't have.

### 2. Golden set
- Start from the 50 labelled answers, and say how many were real employee questions. At least 20 must be real.
- Size each gated class for its threshold. Reading a rate near 90% within ±10 points takes about 35 cases per class, and ±5 points takes about 140. Fifty cases total can't gate several classes.
- Keep 20% as a private holdout, never put in a prompt or a repo.

### 3. Graders
- Read 50–100 real outputs first (error analysis). HR experts write free notes, and I group them into failure modes.
- Use exact or checklist graders wherever code can decide: policy numbers, day counts, limits and required escalation.
- Use an LLM judge only for what code can't decide, such as faithfulness to the policy text. It gets one binary verdict per failure mode, not one global "correct".

### 4. Judge validation (the blocker)
- Have experts label 100 or more fresh answers, separate from any used to write the judge prompt. Aim for at least 50 expert-labelled fails, so TNR is measurable.
- Compute TPR and TNR with intervals. Both need to be at least 80%, and stricter (for example 90%) for the legal or financial classes.
- If the judge fails the bar, read the disagreements, split vague criteria, add pass and fail examples, and re-test on fresh labels.

### 5. Thresholds
I'll write each threshold down with the date and a named signer, before the run. The numbers below are proposals for the signers to confirm.

| Class | Proposed threshold | Gate rule | Relaxable? |
|---|---|---|---|
| Entitlement and expense limits | 95% | Lower bound of the 95% interval clears the threshold | No |
| Process questions | 90% | Lower bound clears the threshold | Named signer only |
| Out-of-scope and escalation | 90% | Lower bound clears the threshold | Named signer only |

Twelve passes out of twelve can't demonstrate 95%, so I'll add cases until each class can clear its bar.

### 6. Baseline
- Run the current production version on the same cases. Record the model name and version, judge model, date and set version.
- Compare the new version to the baseline on the same cases, paired. A gap inside the noise counts as a tie.

### 7. Cost
Cost per correct answer = total cost ÷ (volume × quality), not total cost ÷ all outputs.

### 8. What this gates
Release of the new version, per class, as in section 5.

## What to do before Friday

1. **Today:** send me the confusion matrix and say whether the 50 labels were used to write the judge prompt.
2. **Today:** HR experts do error analysis on real outputs, and I draft the classes and thresholds for sign-off.
3. **Next 1–2 days:** label 100 or more fresh answers and revalidate the judge.
4. **If the judge clears 80% TPR and TNR by Friday:** use it with the per-class gates above.
5. **If it doesn't:** the release decision rests on human review. HR experts grade a per-class sample of new-version answers against the same thresholds. The judge can prioritise what they read, but it doesn't decide. If the human sample is too small for a class's lower bound to clear its threshold, slip the release or ship with that class held back. Don't lower the bar.

## Missing inputs
- Confusion matrix for the 50 labels.
- Class list and traffic shares.
- How many of the 50 were real questions.
- Who signs the thresholds.
- The judge-call budget.

I can turn this into the `templates/eval-plan.md` format once I have those.