# Online sampling and control limits

Working detail for steps 3–5. The formulas come from references/eval-statistics.md (§3, §7, §9, §10); this page applies them to production traffic.

## 1. Two samples, two jobs

- **Random sample, stratified by class**: the only source of a class rate. Draw it at a fixed size per class per period, at random inside the class.
- **Oversample**: low-confidence classifications, escalations, thumbs-down, unclassified or new requests, long tool chains. It is for finding new failure modes. It is read and coded (`error-analysis`), never added to the class rate: these traces fail more often, so mixing them in makes the rate fall whenever their volume rises.

## 2. Sample size per class

Write δ, the drop that matters for the class (usually the margin between its normal level and its signed threshold). Limits sit at p̄ ± 3σ with σ = √(p̄(1−p̄)/n).

| Normal rate p̄ | δ = 10 points | δ = 5 points | δ = 3 points |
| --- | --- | --- | --- |
| 95% | 43 | 171 | 475 |
| 90% | 81 | 324 | 900 |
| 80% | 144 | 576 | 1,600 |

These are n ≥ 9·p̄(1−p̄)/δ²: the lower limit sits exactly δ below the centre. A sustained drop of δ then lands below the limit about half the time in its first period; the run rule catches it within a few periods. If it must be caught in its first period most of the time, use n ≥ 16·p̄(1−p̄)/δ² (about 84%): 576 at 90% and 5 points.

A class whose traffic cannot fill n in a week is charted over two or four weeks; the plan states the detection delay this costs. A class with legal, financial or irreversible effects is sized on its own δ, whatever its traffic share.

Worked check: 100 judged traces a week at p̄ = 91% give σ = 2.86 points and limits of 82.4% to 99.6% (±8.6). A week at 86% is inside: noise. Split over four classes, 25 traces each give about ±17 points per class: a per-class reading at that size is indicative only. To see a 5-point drop with limits at δ: 295 traces per class per week.

## 3. Centre line

Estimate p̄ from the first 8 to 12 production periods scored by the same judge version, not from the offline score: the golden set's mix and difficulty differ from traffic. Until then, mark the chart provisional. Re-estimate after each release and each quarter. A new judge model or rubric version restarts the chart.

## 4. Rules that raise an alert

- One period outside the limits.
- Eight periods in a row on the same side of the centre line (catches small sustained shifts).
- Optional: two of three periods beyond 2σ on the same side.
- Any deterministic red-line hit (forbidden action, personal data leak): no statistics needed.

Every extra rule and every extra class adds false alarms (eval-statistics §10): name one primary metric per class. For shifts of 1–2σ, an EWMA or CUSUM chart detects faster than the plain chart (Montgomery); use one only if someone can read it.

## 5. Judge rate versus true rate

While the judge does not change, chart its observed pass rate: the correction (observed + TNR − 1) / (TPR + TNR − 1) is a fixed linear map, so a shift in the observed rate is a shift in the true one, magnified by 1 / (TPR + TNR − 1). With TPR 92% and TNR 80%, a 5-point observed drop is about a 7-point true drop. Report the corrected level, with its interval, when stating how good the system is.

## 6. Re-checking the judge

Each month, experts label a random slice of the judged traces (e.g. 50 per class). At a 90% pass rate a slice holds few expert failures, so TNR is poorly estimated: pool three months, or sample judge-passes and judge-fails separately and reweight by their shares. When TPR or TNR falls below the bar of its validation (`llm-judge-calibration`), the judge stops gating and the experts' rate is used meanwhile.
