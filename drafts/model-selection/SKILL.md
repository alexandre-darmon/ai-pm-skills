---
name: model-selection
description: 'Choose a model for an AI use case on your own eval suite (cost per success, latency, hosting) and write the decision record. Use for "which model?", a new release or a cost review.'
stage: measure
version: 0.1.0
depends_on: [build-evals]
feeds: [release-to-production, model-card-ai-registry]
autonomy_relevant: false
sources: [own-model-selection]
eval_threshold: 0.80
status: draft
---

# model-selection

## When to use
- Someone asks which model to use for an AI feature, or proposes one.
- A new model ships, a cost review starts, or a sovereignty requirement appears.
- Do not use without an eval suite for the use case: build it first with `build-evals`.
- Do not use to explain how models work or to compare public leaderboards.

## Inputs
Mandatory: the use case and its eval suite (version, size, classes), the candidate models, the constraints (hosting, data residency, personal data, latency, structured output, context length).
Ask if missing: volume per month (for cost), the quality threshold from `build-evals`, the current model if any.

## Method
1. Apply the filters first. Hosting, data residency and personal-data constraints are filters, not criteria: a candidate that fails one is excluded and not scored. Say which candidate was filtered out and why.
2. Widen the candidate list. Include at least one small or EU-hosted model; for classification or extraction, include a small model, a fine-tuned classifier or a specialised decision model next to the frontier ones.
3. Run every remaining candidate on the same suite version. Never choose on public benchmarks or leaderboards: they test someone else's task.
4. Compute per candidate: score per class, cost per success (cost per call ÷ success rate), latency p95, structured-output error rate.
5. Choose on cost per success among candidates above the threshold. When a costlier model is better, quantify the gap in points and in cost, and state what the gap is worth with references/roi-model.md before paying for it.
6. Write the decision record: date, suite version, candidates, filters, scores, chosen model, reasons, re-evaluation date and trigger (new release, price change, drift on the suite).

## Output
`templates/decision-record.md`, one page, all headings present. The decision line reads `Chosen model: <name>`; it says `Chosen model: pending suite run` until the suite has run.

## Rules and red lines
- Never choose on public benchmarks.
- Cost per success is the primary economic metric.
- A candidate that fails a filter is never scored nor chosen.
- Every decision record has a date, a suite version and a re-evaluation date.

## Links
references/roi-model.md · build-evals · release-to-production · model-card-ai-registry

## Sources
- own-model-selection: filters before criteria, cost per success, the dated decision record.
