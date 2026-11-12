Not today. With 100 judged conversations a week, the weekly rate moves by chance.

Centre line: 91% (mean of the ten weeks). σ = √(0.91 × 0.09 / 100) = 2.86 points, so the 3-sigma control limits are 91% ± 8.6 points, i.e. 82.4% to 99.6%. Last week's 86% is inside the limits: on this point alone it is noise, not a shift. The run rule (8 weeks in a row below the centre line) has not fired either.

So do not roll back on this number. Investigate this week:
1. Breakdown per class (claims, coverage, payments): 100 traces give about 33 per class, so per-class rates are indicative; read the failing conversations.
2. Silent changes: did the provider update the model behind your alias? Compare `gen_ai.response.model` values over the last weeks. Did the judge model or its rubric version change? A judge change restarts the chart.
3. Have experts re-label 50 of last week's judged conversations to re-check the judge's TPR and TNR.

Then increase the sample: to see a 5-point drop with 3-sigma limits you need n ≥ 9 × 0.91 × 0.09 / 0.05² ≈ 295 traces per class per week.

If the provider or judge model changed, treat it as a release: re-run the offline gate, and roll back to the pinned version if it fails. If the next weeks go outside the limits, the owner rolls back without waiting for approval.
