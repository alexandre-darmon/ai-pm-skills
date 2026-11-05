**No, we can't confirm the judge as a release gate.** It agrees with the experts on 31 of 50 answers (62%), and the bar for gating is 80% or more. With 50 labels, the 95% interval on 62% is roughly 48–75%, so even the best case is under the bar. A ">90%" score from this judge wouldn't tell us the answers are 90% correct. For leave and expenses, a wrong answer has financial and legal effects, so the judge shouldn't decide Friday's release.

## Eval plan: HR assistant release

**1. Task and classes**
- The task: an employee asks about leave or expenses, and the assistant gives an answer that matches policy.
- "Correct" means the answer matches current policy on entitlement, amounts, deadlines and eligibility, and it doesn't invent rules. Please have HR confirm this definition.
- Proposed classes, to be confirmed with traffic shares:
  - Leave entitlement and calculation (financial)
  - Leave process and approvals
  - Expense limits and eligibility (financial)
  - Expense process and forms
  - Out-of-scope or edge cases, where the right answer is to escalate to HR
- **Missing, from the team:** real traffic shares per class.

**2. Golden set**
- Start with 50–80 cases, at least 20 of them real employee questions. Over-sample the financial and legal classes.
- Keep 20% as a private holdout that stays out of prompts and repos.
- Label synthetic cases and state their share. The set is provisional until real cases replace them.
- **Missing, from the team:** how many real logged questions exist.

**3. Graders, cheapest first**
- Use exact checks for amounts, day counts, deadlines and escalation. These can be regexes or field matches against the policy table.
- Use a checklist for mandatory items, such as the right policy cited and the right next step.
- Use the LLM judge only for what text matching can't decide, such as faithfulness and tone. It never decides alone.

**4. Judge calibration (currently failing: 62%, needs ≥80%)**
- Pull the confusion matrix first. Check whether the judge errs toward passing wrong answers, which is the dangerous direction for a gate, or toward failing right ones.
- Read the 19 disagreements and group them by cause. Split vague rubric criteria and add pass and fail examples.
- Re-check on at least 20 fresh expert-labelled cases, not the original 50 that we tuned on. Also measure agreement per class.
- Until it passes, HR experts review everything the judge would have decided.

**5. Thresholds, one per class**
- The threshold applies to each class, not to a single global score. A global 90% would let the large easy classes hide a failing risky one.
- Proposed starting point, for HR to confirm:

| Class | Threshold |
|---|---|
| Financial or legal classes (entitlement, expense limits) | ≥95%, zero tolerated invented policy |
| Process classes | ≥90% |
| Escalation class | ≥90% |

**6. Baseline**
- Run the current production version on the same set.
- Store the model and version, judge model, date and set version. Without these it isn't a baseline.

**7. Cost per correct outcome**
- Cost per correct outcome = total cost ÷ (volume × quality). Report it alongside the quality score.

**8. What this gates**
- It gates the release of the new version, which is a change to what employees will rely on.
- **Missing, from the team:** the autonomy level, meaning whether the assistant answers directly or HR reviews first.

## What to do before Friday
1. **Today:** get the confusion matrix and the 19 disagreements, and revise the rubric.
2. **Mon–Wed:** have HR experts label 20–30 new cases, ideally from the financial classes, and re-measure agreement.
3. **Thu:** run the new version and the baseline on the set. Experts review the financial classes in full, plus a sample of the rest.
4. **Friday decision:**
   - If the judge now reaches 80% or more, it can gate the process classes. Experts still review the financial classes.
   - If it doesn't, the experts' review is the gate. The judge only sorts which answers to look at first.
   - If the financial classes miss their thresholds, we don't ship, or we ship with those topics routed to HR.

I can draft the rubric revision once you share the disagreements, or write the cases in the harness format.