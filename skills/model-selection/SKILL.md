---
name: model-selection
description: 'Choose a model for an AI use case on your own eval suite (cost per success, latency, hosting) and write the decision record. Use for "which model?", a new release or a cost review.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.3.5"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "false"
  depends_on: "build-evals"
  feeds: "release-to-production, model-card-ai-registry"
  sources: "own-model-selection, repo-chanmeng, repo-lenny"
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
1. Apply the filters first. Hosting, data residency and personal-data constraints are filters, not criteria: a candidate that fails one is excluded and not scored. Say which candidate was filtered out and why. The filters hold for the eval run too: suite data with personal data goes only to candidates that pass them. A region label does not settle a filter on its own: where the provider processes and logs the data, retention and training use, sub-processors and the processing agreement decide it, so list them as checks before go-live for the candidates that remain.
2. Widen the candidate list. Include at least one small or EU-hosted model; for classification or extraction, include a small model, a fine-tuned classifier or a specialised decision model next to the frontier ones. When a rule set, a retrieval lookup or another non-LLM option is plausible, it joins the run as the reference line and can win: `ai-opportunity-assessment` names that alternative, this step measures it. If nobody has scored it yet, say it is the next thing to score; that does not hold a decision between models already scored.
3. Run every remaining candidate on the same suite version. Never choose on public benchmarks or leaderboards: they test someone else's task. Repeat the finalists' runs a few times: LLM outputs change from one run to the next. When the suite or a trained candidate comes from historical records, test on a later period than the training data, and give every candidate only the fields known at decision time.
4. Compute per candidate: score per class, cost per success (cost per run ÷ success rate), monthly run cost at expected volume, latency p95, structured-output error rate. Cost per run is calls per run × cost per call, so an agent loop costs several calls, not one. Write the assumption next to the figure: calls per run, and the cache-hit rate or "no cache". This figure feeds the run cost line of references/roi-model.md, which adds what tokens do not show.
5. Choose on cost per success among candidates above the threshold. The threshold is the one set in `build-evals`; this step does not raise it. Flag a thin margin as a risk, not a gate: compare each candidate's margin over the threshold with about two standard errors of its score, 2√(p(1−p) ÷ n), worked once so the reader can check it. Where the margin is inside that band, the choice stands but is conditional on a larger suite and the per-class check below (repeat runs on the same cases do not shrink this noise); if the bar must hold with confidence, that belongs in the threshold's definition in `build-evals`. State the gap between finalists in points and in cases, then test it against noise:
   - Run noise: the spread across repeated runs.
   - Case noise, which repeats do not measure: on the same cases, with n cases and d cases where only one finalist is right, a gap under 2√d ÷ n can come from the case set. Without d, ask for it or the per-case results, and give the condition: a gap of g cases is real when d is under g² ÷ 4. Never guess d. Never read overlapping confidence intervals as a tie: intervals can overlap while the paired gap is real.
   - Until the gap is shown to exceed the noise, say it cannot be distinguished from noise on the data given, not that the models are equal. Treat it as a tie for the decision: the cheaper model wins, stated as a decision under uncertainty, with the d value or repeat result that would reverse it. Given a single run, decide this way and list the repeat runs and the d count as checks still to do.
   - When a costlier model scores higher, tie or not, or a model is compared with the reference line, price the gap: extra monthly cost ÷ extra successes a month, in currency per extra success. Cross-check it as cost difference per run ÷ score difference; the two must agree (a gap in cost per success is a different figure). This is the break-even. It decides only once the gap exceeds the noise: then compare it, and any new failure mode, with the value of a success or the cost of an error in references/roi-model.md. If that value is unknown, do not invent it: keep the cheaper model and name the error cost that would flip the choice.
   - Look past the headline score before signing off: per-class scores and the kinds of failures (a dropped or invented fact can matter more than a wording slip). Name the fallback for uncertain or costly cases (human review below a confidence level, or on the riskiest classes).
6. Write the decision record: date, suite version, candidates, filters, scores, chosen model, reasons, re-evaluation date and trigger (new release, price change, drift on the suite or in production: inputs, class mix or label definitions moving after launch). The record is also the audit trail of why this model runs.

Keep the answer proportionate. Every figure beyond the inputs is a claim: derive it from stated inputs and show the arithmetic, or leave it out. Name unknown rates (escalation share, error cost, volume) as missing inputs instead of assuming them, and drop table rows or columns you have no data for, listing the missing inputs once.

## Output
`templates/decision-record.md`, one page, all headings present. The decision line reads `Chosen model: <name>`; it says `Chosen model: pending suite run` until the suite has run.

## Rules and red lines
- Never choose on public benchmarks.
- Cost per success is the primary economic metric.
- A gap not shown to exceed the noise never justifies the costlier model, whatever the break-even: a deliberate burden of proof, since the extra successes it pays for may be zero. It is never called proof of equal quality either.
- A candidate that fails a filter is never scored nor chosen.
- Every decision record has a date, a suite version and a re-evaluation date.

## Links
references/roi-model.md · build-evals · ai-opportunity-assessment · release-to-production · model-card-ai-registry

## Sources
- own-model-selection: filters before criteria, cost per success, the dated decision record.
- repo-chanmeng: pricing extra accuracy against a rules baseline, modelling cost per run because loops multiply tokens.
- repo-lenny: LLM non-determinism as a source of false confidence in eval results (idea only). The tie rule on the gap is our inference from it, not a sourced method.
