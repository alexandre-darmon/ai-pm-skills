No. Questions per day, users, latency, cost and thumbs say the assistant is used and fast, not that its answers are right. Thumbs come from a small, self-selected share of employees. They stay on the dashboard, but no quality alert rests on them.

## Scope and classes
Quality is measured per class from sampled traces scored by a validated judge, never as one global number: leave and absence, pay and benefits, mobility and training, sensitive situations. The sensitive class is the costliest: a missed hand-over to an HR advisor.

## Instrumentation
OpenTelemetry GenAI fields: `gen_ai.response.model`, `gen_ai.prompt.version`, retrieved document ids, tokens, plus custom fields for the class and the judge version. Each judge verdict is a `gen_ai.evaluation.result` event on the span it scores.

## Evaluator tiers and sample sizes
- Deterministic checks on 100% of traffic: hand-over present on sensitive questions, personal data in answers, cited policy exists.
- Validated judge on a random sample stratified by class: 324 traces per class per week (p̄ = 90%, drop that matters 5 points, n ≥ 9 × 0.9 × 0.1 / 0.05²). The sensitive class has about 700 questions a week, so it is fully affordable.
- HR experts review 50 judged traces per class per month and re-measure the judge's TPR and TNR; if either falls below its validation bar, the judge stops gating.
- Oversampled thumbs-down and escalations are read for new failure modes but never mixed into the class rate.

## Control limits and alerts
Limits per class: p̄ ± 3√(p̄(1−p̄)/n), centre line from the first 8 production weeks. Alert on a week outside the limits or 8 weeks in a row below the centre. Owner: HR digital product owner, response within 2 working days; a missed hand-over on a sensitive question pages within 4 hours.

## Action ladder
Investigate → roll back to the last pinned bundle → suspend the step or move it down one level (answers drafted for an HR advisor). Moving down needs no approval.

## Drift
A provider model update is a release: pinned model version, offline gate re-run on the golden set before the switch, alert when `gen_ai.response.model` changes.

## Feedback loop
Every confirmed failure gets an error-analysis note and is added to the golden set as a regression case, masked.

## Privacy
Sick leave and parental leave questions carry health and family data. Mask names, employee ids and health details with typed placeholders before any trace reaches the external judge; check the leak rate on 100 traces. Retention: 6 months for traces and judge events, then deletion by the platform team.
