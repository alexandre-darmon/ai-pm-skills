**No, the dashboard isn't enough.** Questions per day, active users, p95 latency, cost and thumbs-up rate tell you the assistant is being used and is fast and cheap. None of them tells you whether answers are correct. Thumbs come from a small, self-selected share of users. An employee who gets a wrong leave-entitlement answer usually doesn't know it is wrong, so they don't click thumbs-down. Keep the dashboard as an operating view and add the quality monitoring below.

I don't have your offline eval plan, so the per-class thresholds are placeholders. I haven't invented any.

# Post-go-live monitoring plan (go-live 1 December)

## 1. Scope: quality per class, never one global number

| Class | Share | Questions/week (about) | Main failure to catch |
|---|---|---|---|
| Leave and absence | 45% | 3,100 | Wrong entitlement, notice period or calculation. This is the biggest class and the easiest to get wrong at volume. |
| Pay and benefits | 30% | 2,070 | Wrong amount, eligibility or date. Financial impact on the employee. |
| Mobility and training | 15% | 1,040 | Outdated procedure, wrong eligibility. |
| Sensitive situations | 10% | 690 | Policy not given, or no hand-over to an HR advisor. **This is the costliest class.** |

A large easy class can hide a failing risky one. The sensitive class is only 10% of traffic, so a global score could stay above 90% while it fails.

The 92% offline score was global over 240 questions. That is roughly 24 questions for the sensitive class, which is too few to be a reliable baseline. The signed pass bars should be restated per class. If they only exist as a global figure, ask the HR director for per-class bars before launch. Production centre lines will come from the first weeks of real traffic, not from the 92%.

## 2. Instrumentation (before 1 December)
Each trace records:
- model requested and model that answered, provider, and prompt name and version
- retrieved HR knowledge-base document IDs and the KB version
- tokens, latency, guardrail hits and errors, and conversation ID
- question class, and whether the answer was a hand-over
- each evaluator's result as an event on the span it judges, with the judge model and rubric version

Follow the OpenTelemetry GenAI conventions and pin the version, since they are still at Development status. Turn on message-content capture only once section 8 is in place.

## 3. Three evaluator tiers

**Tier 1: deterministic checks on 100% of traffic.** One occurrence triggers action.
- Sensitive situation with no hand-over to an HR advisor, or no policy given. Classify with a rule or classifier, and review misclassifications.
- Personal data of another employee in an answer.
- Cited HR document doesn't exist, or the answer has no citation where one is required.
- Answer or advice outside HR policy, such as legal or disciplinary conclusions.
- Tool or retrieval errors, and guardrail hits.

**Tier 2: validated LLM judge on a random sample, stratified by class.**
- The judge must first be validated against HR expert labels (true positive and true negative rates). Report the judge-corrected rate.
- If the judge's rates fall below the validation bar, it stops gating until it is revalidated.

**Tier 3: HR expert review.**
- Review a random slice of the judged sample, about 10% (roughly 100 per week), to find what the judge misses.
- Re-measure the judge's rates monthly.
- Open question: how many expert hours per week can the HR team give? This sets the slice size.

**Oversampled traces** (thumbs-down, escalations, low-confidence or unclassified requests) are read to find new failure modes. They are kept out of the class rates because they would bias them.

## 4. Sample sizes and control limits
Limits are p̄ ± 3√(p̄(1−p̄)/n). The sample needed per class per week is n ≥ 9·p̄(1−p̄)/δ², where δ is the drop that matters. At 16 instead of 9 you detect a drop of exactly δ about 84% of the time in its first period, rather than about half.

| Class | δ (to confirm) | Judged per week | Coverage of weekly traffic |
|---|---|---|---|
| Leave and absence | 5 pts | about 265 | about 9% |
| Pay and benefits | 5 pts (3 if the HR director wants it) | about 265–470 | 13–23% |
| Mobility and training | 5 pts | about 265 | about 25% |
| Sensitive | 3 pts | about 475, so judge nearly all | about 70–100% |

- These figures assume p̄ ≈ 92%. Recompute with `scripts/control_limits.py` once the real centre line is known.
- That is about 1,000–1,500 judged answers a week, which is affordable for an automated judge.
- The centre line comes from the first 8–12 production weeks. Until then, report rates but don't alert on them, except for the Tier 1 red lines, which are active from day one.
- Restart the chart whenever the judge version changes. Never plot two judge versions on one chart.

## 5. Alerts, owners and actions

| Trigger | Owner (role) | Response time | Action |
|---|---|---|---|
| Tier 1 red line (missing hand-over, personal-data leak) | HR assistant product owner, with the HR advisor lead for sensitive cases | Same business day. A leak is immediate. | Investigate. If it recurs or is systematic, suspend that class's automatic answer and route to an advisor. |
| Weekly class rate outside control limits | Product owner | 2 business days | Investigate: pull failing traces, compare the versions of model, prompt, KB and judge. |
| 8 consecutive weeks on one side of the centre line | Product owner | Next weekly review | Investigate. Increase the sample. |
| `gen_ai.response.model` changes | Technical owner | Immediate | Treat as a release: re-run the offline gate before the change stays. |
| Judge TPR or TNR below its bar | Evaluation lead | 1 week | Suspend the judge as a gate and revalidate it. |

- **Action ladder:** investigate, then roll back to the last pinned bundle (model, prompt, KB), then suspend the step or move it down one autonomy level. Moving down never needs approval.
- A dip inside the limits is noise. It earns a bigger sample, not a rollback.
- Name a person with authority to roll back or suspend. That person is currently missing from your plan.
- Only page for what needs action now. Everything else goes to the weekly review.

## 6. Drift watch (monthly)
- **Question mix and new topics:** class shares, share of unclassified requests, and language and length. Expect shifts around payroll cycles, annual leave booking, bonus season and year-end.
- **Output shift:** hand-over rate, refusal rate, citation rate and answer length.
- **KB staleness:** every HR policy change must be reflected in the knowledge base, with a named KB owner and a re-test of affected questions. This is the likeliest cause of quality decline for an HR assistant.
- **Provider model changes:** pin dated model versions. A silent provider update is a release, so re-run the golden set (the offline test set).

## 7. Feedback loop
- Every confirmed failure (expert-confirmed judge fail, upheld complaint or red-line hit) gets a short root-cause note.
- Masked, it becomes a regression case in the golden set.
- New failure modes get a new deterministic check.
- Track confirmed failures and cases added per month.
- Define an employee route to report a wrong answer, and log HR-advisor corrections after hand-overs as a free source of labels.

## 8. Data protection
These traces contain HR questions about sick leave, parental leave and manager conflicts, which are sensitive.
- Mask personal data with typed placeholders before any trace goes to the judge or to reviewers who don't need raw text. Check the residual leak rate by hand on a sample.
- If you can't mask reliably, run the judge in-house or under a processing contract with your cloud provider. This needs sign-off from the DPO and information security.
- Set a retention period for traces, evaluation events and review notes, and name who deletes them.
- Name who can read raw traces, and log that access.
- Check with the works council or employee representatives whether monitoring employee questions needs consultation.

## 9. Review cadence
- **Weekly:** per-class charts and alerts, with the product owner.
- **Monthly:** judge re-check, drift, and failures added.
- **Quarterly, and after every release:** re-estimate centre lines, sample sizes and classes.
- **Operating dashboard:** keep your five metrics, and add the per-class quality rate, the hand-over rate in the sensitive class, and the number of open alerts.

## 10. AI Act (good practice pending counsel)
Employment-related AI can fall under Annex III (high-risk). A policy Q&A assistant probably doesn't, unless its answers feed decisions on promotion, task allocation or evaluation, which the mobility and training class could come close to. Ask counsel to classify it. If it is high-risk, the Annex III duties apply from 2 December 2027, and the provider and deployer monitoring duties (arts. 72 and 26(5)) would need mapping to this plan. Until then, treat this plan as good practice. It is not a compliance statement.

## Open questions and what's missing
1. Per-class pass bars and baselines from the signed offline plan (HR director).
2. Judge validation against HR expert labels (evaluation lead).
3. Expert review hours per week (HR).
4. Named owners, including who can roll back or suspend (steering group).
5. Where the judge runs, and masking and retention decisions (DPO and information security).
6. AI Act classification (counsel).
7. Trace fields already available today (engineering).

If you want, I can turn this into the full plan document, or set up the control-limit calculations once you have the first few weeks of data.