---
name: production-evals-monitoring
description: "Watch an AI feature's answer quality in production (samples, judges, alerts, drift). Use before go-live, for a post-market monitoring plan, or when a pass rate drops and someone wants to roll back."
stage: evaluate
version: 0.1.2
last_verified: 2026-11-09
legal: true
depends_on: [build-evals, llm-judge-calibration, conversation-analysis, ai-act-classification]
feeds: [error-analysis, build-evals, release-to-production, ai-incident-playbook, assistant-kpis-cost-per-outcome, model-card-ai-registry]
autonomy_relevant: true
sources: [otel-genai, montgomery-spc, google-sre, husain-shankar-evals, anthropic-evals, rogan-gladen, eu-ai-act, eu-digital-omnibus-ai, en-18286, gdpr, own-production-monitoring]
eval_threshold: 0.90
status: draft
---

# production-evals-monitoring

## When to use
- Go-live is near and nobody has written how answer quality will be watched once real traffic arrives.
- "Write our post-market monitoring plan", or a deployer must monitor a high-risk system (AI Act arts. 72 and 26(5)).
- A sampled pass rate drops and someone wants to roll back today, or to call it fine: is the drop real or noise? Or drift is suspected.
- The production dashboard shows usage, latency, cost and thumbs, and no measured quality.
- Do not use to build the offline eval set, graders and thresholds before launch: that is `build-evals`.
- Do not use to ship a change, including a provider model update: that is `release-to-production`; this skill watches what runs after it.
- Do not use for the sponsor's dashboard of adoption, cost per correct outcome or ROI: that is `assistant-kpis-cost-per-outcome`.

## Inputs
Mandatory: the offline eval plan (question classes, failure modes, graders, per-class thresholds, baseline) or what stands in for it; traffic per class per week; the fields the traces hold today; who can roll back or suspend, and the autonomy level of each step (references/autonomy-ladder.md).
Ask if missing: the judge's validation (TPR and TNR against expert labels, `llm-judge-calibration`), expert review hours per week, where the judge runs (in-house or an external API), what personal data the traces hold, retention rules, the AI Act role and category (`ai-act-classification`), the provider's instructions for use when you are a deployer.
No offline plan: fill the plan's slots, send the classes and thresholds to `build-evals`, and never invent a production threshold.

## Method
1. **Scope per class.** Take the classes, failure modes, graders and thresholds from the offline plan. Quality is watched per class, never as one global number: a large easy class hides a failing risky one. Name the costliest class. Usage, latency, cost and thumbs are operating and sentiment signals, not quality: thumbs are given on a small, self-selected share of answers. They stay on the dashboard; no correctness alert rests on them. Adoption and cost per correct outcome belong to `assistant-kpis-cost-per-outcome`, which reads the per-class quality rate from this plan.
2. **Instrument the traces** with the OpenTelemetry GenAI semantic conventions (references/otel-genai-fields.md): model asked and model that answered, provider, prompt name and version, retrieved document ids, tool calls and errors, tokens, conversation id; the question class from `conversation-analysis`; the outcome event from `assistant-kpis-cost-per-outcome`; each evaluator's result as a `gen_ai.evaluation.result` event attached to the span it judges. The convention has no field for the evaluator's version: add one (judge model, rubric version). The conventions are at Development status: pin the version you follow. Message content capture is opt-in: switch it on only where step 8 is in place.
3. **Tier the evaluators by cost.**
   - Deterministic checks on 100% of traffic: output format, personal data in the answer, refusal or hand-over where the policy requires it, tool errors, guardrail hits, forbidden actions, cited source exists. A forbidden action or a data leak acts on one occurrence.
   - A validated judge (`llm-judge-calibration`) on a random sample stratified by class. Report the level corrected by its TPR and TNR (references/eval-statistics.md §7).
   - Expert review on a smaller random slice of the judged sample: it finds what the judge misses and re-measures the judge's TPR and TNR every month. A judge whose TPR or TNR falls below its validation bar stops gating until revalidated.
   - Oversample low-confidence classifications, escalations, thumbs-down, unclassified and new requests to find new failure modes. Read them, but keep them out of the class rate: they would bias it.
4. **Size the sample per class and set control limits** (references/eval-statistics.md §3, §9; references/online-sampling.md). For each class, write δ, the drop that matters (from the margin above its threshold). Limits are p̄ ± 3√(p̄(1−p̄)/n). For limits within δ of the centre, n ≥ 9·p̄(1−p̄)/δ² per class per period: p̄ = 90%, δ = 5 points gives 324. A drop of exactly δ then crosses the limit about half the time in its first period; with n ≥ 16·p̄(1−p̄)/δ², about 84%. A class that cannot fill n in a week is charted over two or four weeks, and the plan states the detection delay. Worked band: p̄ = 94%, n = 150 gives σ = 1.94 points, ±5.8 points, limits 88.2% to 99.8%. The centre line comes from the first 8 to 12 production periods, not from the offline score; a new judge version restarts the chart. `scripts/control_limits.py` computes limits, run rule and n.
5. **Alert rules, owners, action ladder.** Alert when a period falls outside the limits, when 8 periods in a row sit on the same side of the centre line, or when a deterministic red-line check fires. Each alert names an owner (a role, not a team), a response time and the next rung: investigate (pull the failing traces, the per-class breakdown, the version diff of model, prompt, KB and judge) → roll back to the last pinned bundle (`release-to-production`) → suspend the step or move it down one level (references/autonomy-ladder.md). Moving down never needs approval; moving back up passes the gate again. A dip inside the limits is noise until a run rule or a larger sample says otherwise: it earns an investigation and a bigger sample, never a rollback on its own. Page only on what needs action now (google-sre); the rest goes to the weekly review.
6. **Watch for drift.** New question classes and the share of unclassified requests (`conversation-analysis` monthly check); input shift (class mix, language, length); output shift (refusal, hand-over and citation rates, answer length); knowledge-base staleness. Any provider model, embedding model or judge model change is a release, announced or silent: pin dated versions, alert when the model that answered (`gen_ai.response.model`) changes, re-run the offline gate on the golden set, follow `release-to-production`.
7. **Close the loop.** Every confirmed failure (judge fail confirmed by an expert, upheld complaint, red-line hit) gets an `error-analysis` note on its failure mode and, masked, becomes a regression case in the golden set (`build-evals`). A new failure mode gets a deterministic check or a grader. A serious incident goes to `ai-incident-playbook` (art. 73 clocks for high-risk systems). Count confirmed failures and cases added per month.
8. **Protect the data.** Mask personal data with typed placeholders before any trace reaches an external judge, an external tool or a reviewer who does not need raw text; check the residual leak rate by hand on a sample. If masking cannot be done, the judge runs in-house or under a processing contract. Set a retention period for traces, evaluation events and review notes, and who deletes them (GDPR art. 5(1)(c) and (e)); a high-risk deployer keeps the logs it controls at least six months unless other law says otherwise (art. 26(6)): reconcile the two with the DPO. Name who can read raw traces, and log that access.
9. **Map to the AI Act when the system is high-risk** (references/ai-act-monitoring.md). Role first (`ai-act-classification`). Provider: art. 72 rows (an active, systematic collection and analysis of performance data over the system's lifetime, including data from deployers, based on a plan kept in the technical documentation, Annex IV), with arts. 12(2), 17(1)(h), 43(4) and 73. Deployer: art. 26(5) rows (monitor per the instructions for use, inform the provider, suspend use on a risk), with art. 26(6). Each row gets the plan section that answers it, an evidence status (on file, draft, missing) and a question for counsel. Dates: Annex III duties under Chapter III apply from 2 December 2027 (Regulation (EU) 2026/1744); when arts. 72–73 bite is a question for counsel; the Commission's guidance with a template for the plan is due by 2 September 2027. A provider model change may be a substantial modification (art. 43(4)): question for counsel. Below high risk, mark the rows as good practice.
10. **Set the review cadence.** Weekly: per-class charts and alerts, by the owner. Monthly: judge re-check, drift, failures added. Quarterly, and after every release: re-estimate the centre lines, sample sizes and classes.

## Output
A monitoring plan following `templates/monitoring-plan.md`: scope and classes, instrumentation, evaluator tiers with sample sizes, metrics per class with control limits, alert rules and owners, action ladder, drift watch, feedback loop, privacy, AI Act mapping when relevant, review cadence, open questions. A section that cannot be filled says what is missing and who provides it. When the AI Act mapping is present, the plan ends with: "This plan is evidence for counsel, not a conformity assessment."

## Rules and red lines
- No monitoring plan without a quality signal per class from sampled traces scored by a validated judge or experts. Usage, latency, cost and thumbs are not quality.
- Never alert, roll back or declare a recovery on a sampled change without control limits. Inside the limits it is noise until a run rule or a larger sample shows a shift. Deterministic red-line hits are the exception: one occurrence acts.
- Never send unmasked personal data to an external judge or tool.
- A provider model, embedding model or judge model change is a release, never swapped in place.
- Never mix oversampled traces into a class rate, nor judge rates from two judge versions on one chart.
- Never state that the plan or the system "meets", "satisfies" or "complies with" art. 72 or art. 26(5): it is evidence and questions for counsel.
- Moving a step down never waits for approval.

## Links
references/eval-statistics.md · references/autonomy-ladder.md · references/evals-as-evidence.md · references/otel-genai-fields.md · references/online-sampling.md · references/ai-act-monitoring.md · build-evals · llm-judge-calibration · error-analysis · conversation-analysis · release-to-production · assistant-kpis-cost-per-outcome · ai-act-classification · ai-incident-playbook

## Sources
- otel-genai: trace attributes and the `gen_ai.evaluation.result` event, checked in the semantic-conventions-genai repository on 2026-11-09.
- montgomery-spc: control limits for a rate, run rules, sample size against the shift to detect.
- google-sre: alert on what users feel, page only on what needs action now, name the owner.
- husain-shankar-evals: production failures feed error analysis and the eval set; judges re-checked against expert labels.
- anthropic-evals: regression cases from production failures.
- rogan-gladen: the judge-corrected rate.
- eu-ai-act: arts. 12(2), 17(1), 26(5)-(6), 43(4), 72, 73, checked on the EUR-Lex consolidated text of 27 July 2026.
- eu-digital-omnibus-ai: the Annex III date and the amended art. 72(3).
- en-18286: monitoring as a test procedure during and after development inside the quality system.
- gdpr: minimisation and storage limitation (art. 5) behind masking and retention.
- own-production-monitoring: tiered evaluators, per-class sampling and the action ladder, from monitoring assistants in production (method only).
