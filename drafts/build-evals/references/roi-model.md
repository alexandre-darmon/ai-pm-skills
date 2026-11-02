<!-- Synced copy of foundations/roi-model.md. Edit the original, then run: python3 scripts/validate_skills.py --sync -->
# ROI model

The single way any skill states a gain. A gain, ROI or productivity figure that does not trace to these five lines is not shown.

## The five lines

```
ROI (per use case, per period) =
    volume            # outcomes produced by the AI in the period
  × quality           # share of outcomes judged correct / accepted
  × unit value        # € value of one correct outcome (time saved × loaded cost, or error cost avoided)
  − run cost          # tokens + infra + licences
  − change cost       # training, support, review time
```

## Where each input comes from

| Line | Comes from | Never from |
| --- | --- | --- |
| Volume | traces or conversation classification (`conversation-analysis`) | declared usage |
| Quality | sampled evaluation (`build-evals`, `assistant-kpis-cost-per-outcome`) | thumbs-up alone |
| Unit value | the business: interviews, time studies; conservative, sourced, assumption written down | an assumed figure |
| Run cost | tokens + infra + licences | — |
| Change cost | training, support, review time | — |

## Rules

1. **Baseline first.** A baseline before deployment is mandatory. Without it the ROI is a **projection** and is labelled so.
2. **Five lines or nothing.** Any skill that outputs a gain shows the five lines with named inputs. Otherwise the output fails its grader.
3. **Conservative unit values.** Unit values are interviewed and sourced, never assumed, and the assumption is written down.
4. **Successes as denominator.** Cost per correct outcome divides a cost by the number of correct outcomes (volume × quality), never by all outputs. Each KPI spec states which costs it puts in the numerator.
5. **Negative is shown.** A use case with negative ROI is shown, not hidden.
6. **No free-floating percentages.** A percentage gain without volume, quality and unit value behind it is removed or rewritten as anchored.

## Assumptions

Any skill that states a gain writes down its unit-value assumption with its source. `ai-roi-quantification` goes further: an assumptions register (assumption, source, confidence) and a sensitivity analysis on the three weakest assumptions.

## Who reads this model

`ai-initiative-pitch`, `assistant-kpis-cost-per-outcome`, `ai-roi-quantification`, `process-ai-redesign`.
