# Post-go-live monitoring plan: HR assistant (go-live 1 December)

## Verdict

The dashboard isn't enough. Questions per day, active users, p95 latency, cost and thumbs-up rate show that the assistant is used and fast. They don't show whether it answers correctly. A wrong answer on parental leave or notice periods looks the same on that dashboard as a right one. Thumbs are given by a small, self-selected share of users, and an employee can't tell whether a policy answer is wrong. Keep the dashboard as an operating view, and add a measured quality signal per question class.

The 92% score has limits too. On 240 questions its 95% interval is about ±3.4 points. The sensitive class, at roughly 10% of questions, had only about 24 test questions, which is too few to say anything about that class. So the production centre lines come from the first 8–12 production periods, not from the 92%.

## 1. Scope: quality per class, never one number

| Class | Share | Questions/week (about) | Failure that matters |
|---|---|---|---|
| Leave and absence | 45% | 3,100 | Wrong entitlement, wrong rule, outdated rule |
| Pay and benefits | 30% | 2,075 | Wrong amount or eligibility, outdated grid |
| Mobility and training | 15% | 1,040 | Wrong procedure or conditions |
| **Sensitive** (sick leave, parental leave, manager conflict) | 10% | 690 | Policy wrong, or no hand-over to an HR advisor |

The sensitive class is the costliest, so it gets the strictest checks. Each class uses the thresholds the HR director signed. I don't have those bars, so I haven't invented production thresholds. Please send them, and I'll slot them in.

## 2. Instrumentation (before 1 December)

Log one trace per conversation, following the OpenTelemetry GenAI conventions and pinning the version:

- Model requested and model that answered, provider, prompt name and version.
- IDs of the retrieved knowledge-base documents and the KB version or date.
- Tokens, errors, conversation ID, question class and whether it was handed over.
- Each evaluator's result, with an added field for judge model and rubric version.
- Do not capture message text until section 8 is in place.

## 3. Evaluators, in three tiers

1. **Deterministic checks on 100% of traffic:**
   - Sensitive questions get the policy plus a hand-over to an HR advisor.
   - The answer cites a source that exists in the KB.
   - No personal data of another employee appears in the answer.
   - The answer makes no promise or decision, such as approving leave.
   - Format and tool errors are caught.

   One occurrence of a forbidden action or a data leak triggers action.
2. **LLM judge on a random sample stratified by class.** The judge must first be validated against HR-expert labels (sensitivity and specificity). Report rates corrected for the judge's error.
3. **HR expert review of a slice of the judged sample.** This catches what the judge misses and re-measures the judge every month. A judge that falls below its validation bar stops gating until it is revalidated.

Oversample thumbs-down, escalations, low-confidence and unclassified questions to find new failure modes. Read them, but keep them out of the class rates.

## 4. Sample sizes and control limits

Formula: n ≥ 9·p̄(1−p̄)/δ² per class per period, where δ is the drop that matters. Limits are p̄ ± 3√(p̄(1−p̄)/n). The p̄ and δ below are illustrative until the signed bars are in.

| Class | Illustrative p̄ / δ | Judged per week | Note |
|---|---|---|---|
| Leave | 90% / 5 pts | about 325 (576 for ~84% detection) | 3,100 available, easy |
| Pay | 90% / 5 pts | about 325 | Easy |
| Mobility | 90% / 5 pts | about 325 | About a third of the class |
| Sensitive | 95% / 5 pts | about 170, plus 100% of the hand-over check | About a quarter of the class |

- That is about 1,150 judged answers a week. Expert review of about 100–120 of them is roughly 10 hours a week at 5 minutes each. This is my assumption, so please confirm the reviewer hours you have.
- Centre lines come from the first 8–12 weeks. Until then, report rates but don't alert on the sampled score. Only red-line checks act from day one.
- A new judge version restarts the chart. Never plot two judge versions on one chart.

## 5. Alerts, owners and the action ladder

**Alert when:**
- A class's weekly rate falls outside its limits.
- 8 periods in a row sit on the same side of the centre line.
- A red-line check fires.

A dip inside the limits is noise. It earns an investigation and a bigger sample, never a rollback.

| Step | Action | Owner (role) | Response time |
|---|---|---|---|
| 1 | Investigate: failing traces, per-class breakdown, diff of model, prompt, KB and judge | Assistant product owner | 1 working day |
| 2 | Roll back to the last pinned bundle of model, prompt and KB | Assistant product owner, with IT release owner | Same day |
| 3 | Suspend the class, or route it entirely to HR advisors | HR director's delegate | Immediately; never waits for approval |

For the sensitive class, a red-line hit goes straight to step 3 for that class. Page only on what needs action now. Everything else goes to the weekly review.

## 6. Drift watch

- **Provider model change:** this is a release, announced or silent. Pin dated model versions, alert when the model that answered changes, and re-run the 240-question set (and the added regression cases) before accepting it.
- **KB staleness:** HR policies change, and a policy update without a KB refresh is the likeliest failure. Alert on KB age and on answers citing a superseded document. Re-test the affected class after each policy change.
- **Input shift:** class mix, languages, share of unclassified questions, and new topics such as a new collective agreement. Check monthly.
- **Output shift:** hand-over rate, refusal rate, citation rate and answer length.

## 7. Feedback loop

- Every confirmed failure (expert-confirmed judge fail, upheld complaint, red-line hit) gets an error-analysis note and, once masked, becomes a regression case in the test set.
- A new failure mode gets a deterministic check or a grader.
- Report the monthly count of confirmed failures and cases added.
- A serious incident, such as a leak of one employee's data to another, goes to the incident process.

## 8. Data protection

- Traces will contain sensitive employee data: sick leave is health data (GDPR art. 9), and manager conflicts are personal. The cloud provider and any external judge are processors.
- Mask personal data with typed placeholders before any trace reaches an external judge or a reviewer who doesn't need raw text. Check the residual leak rate by hand on a sample. If masking can't be done, run the judge in-house or under a processing contract.
- Set a retention period and a named deleter. Only a named few can read raw traces, and every access is logged.
- Agree with the DPO, and with the works council if one applies, that monitoring covers the assistant's answers and is not used to assess individual employees.

## 9. AI Act (good practice, pending counsel)

Employment and worker-management systems appear in Annex III. A Q&A assistant that doesn't decide anything about workers may not be high-risk, but the sensitive class makes that a question for counsel. Annex III duties apply from 2 December 2027. Until counsel confirms the classification, treat arts. 72 and 26(5) as good practice, and keep the logs and this plan as evidence.

*This plan is evidence for counsel, not a conformity assessment.*

## 10. Cadence

- **Weekly:** per-class charts and alerts, reviewed by the product owner.
- **Monthly:** judge re-check against expert labels, drift, failures added.
- **Quarterly and after every release:** re-estimate centre lines, sample sizes and classes.

## Operating dashboard (keep)

Questions per day, active users, p95 latency, cost per day and thumbs-up rate stay, split by class. Add the per-class corrected quality rate, hand-over rate on sensitive questions, and red-line counts. Cost per correct answer, rather than cost per question, can come later once the quality rate exists.

## Before 1 December (about 3 weeks)

1. Send me the signed pass bars per class.
2. Build the traces and the 100% deterministic checks.
3. Validate the judge against HR-expert labels. Find out whether you have the reviewer hours.
4. Settle masking, the processing contract, retention and DPO sign-off.
5. Name the owners in section 5.
6. Pin the model version and record the baseline bundle for rollback.

## Open questions

- What are the signed bars per class, and was the 240-question set stratified by class?
- How many expert-review hours per week are available?
- Where will the judge run, in-house or through the same cloud provider?
- Is there a works council, and who is the DPO contact?
- Does counsel consider the assistant high-risk?