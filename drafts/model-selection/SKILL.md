---
name: model-selection
description: 'Choose a model for an AI use case on your own eval suite (cost per success, latency, hosting) and write the decision record. Use for "which model?", a new release or a cost review.'
stage: measure
version: 0.2.0
depends_on: [build-evals]
feeds: [release-to-production, model-card-ai-registry]
autonomy_relevant: false
sources: [own-model-selection, repo-chanmeng, repo-lenny]
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
Ask if missing: volume per month and calls per run (for cost), the quality threshold from `build-evals`, the current model if any.

## Method
1. Apply the filters first. Hosting, data residency and personal-data constraints are filters, not criteria: a candidate that fails one is excluded and not scored. Say which candidate was filtered out and why.
2. Widen the candidate list. Include at least one small or EU-hosted model; for classification or extraction, include a small model, a fine-tuned classifier or a specialised decision model next to the frontier ones. When a rule set, a retrieval lookup or another non-LLM option is plausible, it joins the run as the reference line and can win: `ai-opportunity-assessment` names that alternative, this step measures it. If nobody has scored it yet, say it is the next thing to score; that does not hold a decision between models already scored.
3. Run every remaining candidate on the same suite version. Never choose on public benchmarks or leaderboards: they test someone else's task. Repeat the finalists' runs a few times: LLM outputs change from one run to the next.
4. Compute per candidate: score per class, cost per success (cost per run ÷ success rate), monthly run cost at expected volume, latency p95, structured-output error rate. Cost per run is calls per run × cost per call, so an agent loop costs several calls, not one. Write the assumption next to the figure: calls per run, and the cache-hit rate or "no cache". This figure feeds the run cost line of references/roi-model.md, which adds what tokens do not show.
5. Choose on cost per success among candidates above the threshold. State the gap between finalists in points, then test it against noise:
   - Run noise: the spread across repeated runs.
   - Case noise, which repeats do not measure: with n cases and d cases where only one finalist is right, a gap under 2√d ÷ n can come from the case set. Without those counts, compare the two scores' confidence intervals.
   - A gap inside the noise is a tie, and a tie goes to the cheaper model. Given a single run, apply the case test, decide, and list the repeat runs as a check still to do.
   - When a costlier model scores higher, tie or not, or a model is compared with the reference line, price the gap: extra monthly cost ÷ extra successes a month, in currency per extra success. Recompute it as cost difference per run ÷ score difference; the two must agree. Weigh it, and any new failure mode, against the unit value in references/roi-model.md before paying for it.
6. Write the decision record: date, suite version, candidates, filters, scores, chosen model, reasons, re-evaluation date and trigger (new release, price change, drift on the suite).

## Output
`templates/decision-record.md`, one page, all headings present. The decision line reads `Chosen model: <name>`; it says `Chosen model: pending suite run` until the suite has run.

## Rules and red lines
- Never choose on public benchmarks.
- Cost per success is the primary economic metric.
- A gap between finalists inside the noise never justifies the costlier model.
- A candidate that fails a filter is never scored nor chosen.
- Every decision record has a date, a suite version and a re-evaluation date.

## Links
references/roi-model.md · build-evals · ai-opportunity-assessment · release-to-production · model-card-ai-registry

## Sources
- own-model-selection: filters before criteria, cost per success, the dated decision record.
- repo-chanmeng: pricing extra accuracy against a rules baseline, modelling cost per run because loops multiply tokens.
- repo-lenny: LLM non-determinism as a source of false confidence in eval results (idea only). The tie rule on the gap is our inference from it, not a sourced method.
