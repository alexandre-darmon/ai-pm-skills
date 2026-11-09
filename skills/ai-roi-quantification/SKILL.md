---
name: ai-roi-quantification
description: 'Compute a deployed AI product''s ROI with the five-line model, a baseline and sourced unit values. Use for a budget renewal, a CFO or comex review, "what did it return?" or a scaling decision.'
stage: prove
version: 0.2.2
depends_on: [assistant-kpis-cost-per-outcome, conversation-analysis]
feeds: [ai-opportunity-assessment, process-ai-redesign]
autonomy_relevant: false
sources: [own-roi-work, repo-yoseph, repo-chanmeng]
eval_threshold: 0.80
status: tested
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
1. Fill the five lines per use case from references/roi-model.md: volume × quality × unit value − run cost − change cost. Check each quoted cost against the model's run and change lines. If it does not say whether build cost or hidden recurring cost is in it, ask, and mark the net incomplete until answered. State the period over which any one-off cost is spread.
2. Check the baseline. No measured baseline: the figure is labelled a projection, not an ROI, and the plan to measure the baseline comes with it.
3. Source each unit value in the assumptions register: source, date, confidence. A figure with no source is flagged, and the interview template is proposed (who, which task, timed on real cases). Keep the conservative value. For a unit value based on time saved, report cash and capacity apart (references/roi-model.md): ask which cost went away or which named work took the freed hours, which P&L line it lands on and who confirms it. If nobody confirms, it stays capacity.
4. Run sensitivity on the three weakest assumptions, low and high, and show the result. For each, give the measured value at which the use case no longer pays for itself: the renewal decision needs that number, not only a range.
5. Show each use case on its own and the total. A negative use case stays visible, with a stop-or-fix recommendation. End each use case with a continue, shrink or stop call. Check it against the stop conditions already written in the assessment or PRD (`ai-opportunity-assessment`, `llm-feature-prd`), copied as written, never rewritten at decision time. If none exist, say so and propose them, each with the number it is measured against and the action it triggers. When inference cost alone breaks the case, cut scope before tuning the model.
6. Write the do-not-claim list: gains without baseline, capacity reported as cash. Write one paragraph the sponsor can reuse in the go / stop decision (`ai-opportunity-assessment`).

## Output
`templates/roi-sheet.md`, all headings present.

## Rules and red lines
- No baseline, no ROI claim: projection, labelled.
- Unit values are interviewed and sourced, never assumed.
- Every number traces to a line.
- Sensitivity is mandatory. Negative use cases are shown.
- Freed hours count as cash only when a named owner confirms the P&L line.
- A decision call has a stated threshold, not only a recommendation.

## Links
references/roi-model.md · assistant-kpis-cost-per-outcome · conversation-analysis · ai-opportunity-assessment · llm-feature-prd

## Sources
- own-roi-work: assumptions register and do-not-claim list.
- repo-yoseph: cost coverage, a threshold that invalidates the case, a P&L owner per number (ideas, own words).
- repo-chanmeng: continue, shrink or stop against conditions written beforehand (ideas, own words).
