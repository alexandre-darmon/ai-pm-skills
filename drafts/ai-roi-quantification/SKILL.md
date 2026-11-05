---
name: ai-roi-quantification
description: 'Compute a deployed AI product''s ROI with the five-line model, a baseline and sourced unit values. Use for a budget renewal, a CFO review, "what did it return?" or a scaling decision.'
stage: measure
version: 0.1.0
depends_on: [assistant-kpis-cost-per-outcome, conversation-analysis]
feeds: [ai-initiative-pitch, process-ai-redesign]
autonomy_relevant: false
sources: [own-roi-work]
eval_threshold: 0.80
status: draft
---

# ai-roi-quantification

## When to use
- A budget renewal, a CFO review or a scaling decision needs the return of a deployed AI product.
- Someone quotes a gain and asks to check it.
- Do not use to define KPIs: use `assistant-kpis-cost-per-outcome`.
- Do not use before any deployment for a business case with no data: label it a projection or use `ai-opportunity-assessment`.

## Inputs
Mandatory: volumes per use case, quality per use case, run and change costs.
Ask if missing: the baseline measurement, unit values and their source.

## Method
1. Fill the five lines per use case from references/roi-model.md: volume × quality × unit value − run cost − change cost.
2. Check the baseline. No measured baseline: the figure is labelled a projection, not an ROI, and the plan to measure the baseline comes with it.
3. Source each unit value in the assumptions register: source, date, confidence. A figure with no source is flagged, and the interview template is proposed (who, which task, timed on real cases). Keep the conservative value.
4. Run sensitivity on the three weakest assumptions, low and high, and show the result.
5. Show each use case on its own and the total. A negative use case stays visible, with a stop-or-fix recommendation.
6. Write the do-not-claim list: gains without baseline. Write one paragraph for `ai-initiative-pitch`.

## Output
`templates/roi-sheet.md`, all headings present.

## Rules and red lines
- No baseline, no ROI claim: projection, labelled.
- Unit values are interviewed and sourced, never assumed.
- Every number traces to a line.
- Sensitivity is mandatory. Negative use cases are shown.

## Links
references/roi-model.md · assistant-kpis-cost-per-outcome · conversation-analysis · ai-initiative-pitch

## Sources
- own-roi-work: assumptions register and do-not-claim list.
