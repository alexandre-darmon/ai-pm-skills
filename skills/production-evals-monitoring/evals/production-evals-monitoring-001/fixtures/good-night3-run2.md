# Post-go-live monitoring plan: HR assistant (go-live 1 December)

**Short answer: no, the dashboard isn't enough.** Questions per day, active users, p95 latency, cost and thumbs-up rate show usage, speed, spend and sentiment. None of them shows whether answers are correct. If the model, the knowledge base (KB) or the prompt drifts and the assistant starts giving wrong leave entitlements, the dashboard will look normal. Thumbs are given by a small, self-selected share of users. They stay on the dashboard, but no correctness alert should rest on them.

I wrote this from your message and didn't open any project files. Figures marked *illustrative* need your real per-class thresholds and margins.

## 1. Scope: quality is watched per class

| Class | Share | Questions/month | ≈ per week |
|---|---|---|---|
| Leave and absence | 45% | 13,500 | 3,100 |
| Pay and benefits | 30% | 9,000 | 2,075 |
| Mobility and training | 15% | 4,500 | 1,040 |
| Sensitive situations | 10% | 3,000 | 690 |

- **Costliest class: sensitive situations.** A missed hand-over, or a wrong statement about sick or parental leave, harms a person and exposes the bank. It is only 10% of traffic, so a global score would hide it completely.
- **Pay and benefits** is the second risk, because a wrong figure gets acted on.
- **The 92% on 240 questions is a weak baseline.** It is a global number with a confidence interval of roughly ±3.5 points. A class like sensitive has about 24 questions, so its offline score says almost nothing. Use the HR director's signed pass bars as provisional floors per class. Don't invent new production thresholds. The real centre lines come from production data (section 4).

## 2. Instrumentation (before 1 December)

Log each trace using the OpenTelemetry GenAI conventions. Pin the convention version, because it is still at Development status.
- The model asked for and the model that answered, the provider, and the prompt name and version.
- The retrieved KB document ids and their KB version or date, tool calls and errors, tokens, and the conversation id.
- The question class. The classifier needs its own confidence score and an "unclassified" bucket.
- Each evaluator's result as a `gen_ai.evaluation.result` event on the span it judges, plus a field the convention lacks: the judge model and rubric version.
- Whether the user was handed over to an HR advisor, and the thumbs.

## 3. Evaluators in three tiers

1. **Deterministic checks on 100% of traffic.**
   - Sensitive class: the policy is given and the hand-over to an HR advisor is present.
   - No personal data about another employee in the answer.
   - A cited KB source exists and was actually retrieved.
   - The answer contains no legal or medical advice beyond the policy text.
   - Format is correct and there are no tool errors.
   - **One occurrence of a red-line hit triggers action.** No control limits apply to these.
2. **LLM judge on a random sample, stratified by class.** The judge must be validated first against expert-labelled HR answers (TPR and TNR). Report rates corrected for the judge's error. Judges from two different versions never share a chart.
3. **HR expert review of a smaller random slice of the judged sample.** This finds what the judge misses and re-measures the judge every month. If the judge falls below its validation bar, it stops gating until it is revalidated.

**Oversample, but keep out of the class rates:** thumbs-down, escalations, unclassified and low-confidence questions, and new topics. Read them to find new failure modes.

## 4. Sample sizes and control limits

Control limits are p̄ ± 3√(p̄(1−p̄)/n). The sample size for detecting a drop of δ is n ≥ 16·p̄(1−p̄)/δ², which gives about 84% chance of catching a drop of exactly δ in its first week.

| Class | p̄ (*illustrative*) | δ | n/week | Fillable? |
|---|---|---|---|---|
| Leave | 92% | 5 pts | ~470 | Yes (3,100/wk) |
| Pay and benefits | 92% | 5 pts | ~470 | Yes |
| Mobility and training | 92% | 5 pts | ~470 | Yes, about 45% of the week's traffic |
| Sensitive | 97% | 3 pts | ~520 | Barely (690/wk), so chart over 2 weeks and accept the delay |

- That is about 1,900 judged answers a week out of roughly 6,900 questions. If that is too much, use the lower n ≥ 9·p̄(1−p̄)/δ² (about 265 and 290). You then catch a drop of exactly δ only about half the time in its first week.
- **Expert review slice:** about 100 a week, at least 30 from the sensitive class. This is the real bottleneck. I need to know how many HR expert hours a week you can have.
- **Burn-in:** for the first 8 to 12 weeks, the signed pass bars act as floors. From the data of those weeks, set each class's centre line and limits. A new judge version restarts the chart.

## 5. Alerts, owners and action ladder

**Alert when:**
- a class's weekly rate falls outside its limits,
- 8 weeks in a row fall on the same side of the centre line, or
- a deterministic red-line check fires.

Inside the limits, a dip is noise. It earns an investigation and a larger sample, not a rollback.

| Step | Action |
|---|---|
| 1 | **Investigate** (the same working day for a red line, within 2 working days otherwise): pull the failing traces and diff the model, prompt, KB and judge versions. |
| 2 | **Roll back** to the last pinned bundle of model, prompt and KB. |
| 3 | **Suspend or step down:** for example, sensitive-class questions go straight to an advisor with the policy text only. Stepping down never needs approval. |

The owners are roles, to be named by you: an AI product owner, an HR policy owner (for KB errors), and someone with the authority to suspend. **I need those names and who has rollback rights.** Page only for red lines and for sensitive or pay failures. Everything else goes to the weekly review.

## 6. Drift watch

- **Provider model change.** Calling a model through a cloud API means aliases can silently move to a new version. Pin dated model versions. Alert whenever the model that answered differs from the pinned one. Treat any change, including the embedding model or the judge, as a release: re-run the golden set before it goes live.
- **KB changes.** HR policies change (leave rules, pay scales, annual cycles). Track KB version per answer, the age of the documents cited, and re-sample the affected class right after each KB update. Add a seasonal check around year-end leave carry-over and pay reviews.
- **Input shift.** Class mix, languages, question length, and the share of unclassified questions each month.
- **Output shift.** Refusal rate, hand-over rate, citation rate and answer length.

## 7. Close the loop

Every confirmed failure (judge fail confirmed by an expert, upheld complaint, red-line hit) gets an error-analysis note. After masking, it becomes a regression case in the golden set. Each new failure mode gets a deterministic check or a judge criterion. Report confirmed failures and cases added per month. Agree an incident path with HR, the DPO and compliance for serious cases, such as a wrongly denied leave that led to harm.

## 8. Privacy (a major risk here)

- Sensitive questions will contain **health data** (GDPR art. 9) and details about named colleagues and managers.
- Mask personal data with typed placeholders before any trace reaches an external judge or reviewer. Check the residual leak rate by hand on a sample. If masking can't be made reliable, run the judge in-house or under a processing contract.
- Capture message content only where this is in place. Set a retention period for traces, evaluation events and review notes, and name who deletes them.
- Restrict raw-trace access to named people and log every access.
- Consult the DPO, and the works council or employee representatives if your jurisdiction requires it. Employees should be told that conversations are sampled for quality.

## 9. Regulatory mapping

An HR policy Q&A assistant is probably not a high-risk system under the AI Act's Annex III, unless it feeds decisions about evaluating or managing employees. **This is a question for counsel**, together with the bank's own model-risk and operational-resilience requirements. Until then, treat the AI Act monitoring duties (arts. 72 and 26(5)) as good practice. If it turns out to be high-risk, the Annex III duties apply from 2 December 2027, and a provider model change may count as a substantial modification. This plan is evidence for counsel, not a conformity assessment.

## 10. Review cadence

- **Weekly:** per-class charts and alerts, reviewed by the AI product owner with an HR policy owner.
- **Monthly:** judge re-check against expert labels, the drift report, and failures added to the golden set.
- **Quarterly and after every release:** re-estimate centre lines, sample sizes and classes.

## Keep on the dashboard (operating signals)

Questions per day, active users, p95 latency, cost per day and thumbs-up rate all stay. Add:
- the per-class quality rate with control limits,
- red-line counts,
- hand-over rate,
- the share of unclassified questions, and
- the model version that answered.

## What I need from you

1. The per-class pass bars the HR director signed.
2. How many HR expert hours per week are available for review.
3. Whether the judge is validated yet (TPR and TNR against expert labels).
4. Where the judge runs (in-house or an external API), and what the traces will hold.
5. Named owners, and who can roll back or suspend.
6. Whether any output feeds decisions about individual employees.

Three weeks remain before go-live. The most urgent items are the trace fields (section 2), the judge validation, and the pinned model version, since they can't be added retroactively.