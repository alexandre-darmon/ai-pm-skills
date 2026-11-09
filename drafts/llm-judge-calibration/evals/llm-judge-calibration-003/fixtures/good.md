Tell her the 85% is not the figure to decide on, and that we are not shown to be below 88%, nor above it.

**Why the 85% is biased.** On September's test split the judge passes 92% of good memos (TPR 0.92) and fails 80% of bad ones (TNR 0.80). So it wrongly fails 8% of good memos and wrongly passes 20% of bad ones. With most memos good, the wrong fails outweigh the wrong passes: the raw rate understates the true rate.

**Corrected rate.** (0.85 + 0.80 − 1) ÷ (0.92 + 0.80 − 1) = 0.65 ÷ 0.72 = 90.3%. Approximate 95% interval, carrying the uncertainty of TPR (100 passes), TNR (50 fails) and the 400-memo sample: 82% to 99%. The bootstrap (`scripts/judge_metrics.py --observed-pass 340 --observed-n 400` on the test split) gives 82% to 99.6%.

**Reading.** 88% lies inside the interval: we cannot say the assistant is below the bar, nor that it clears it. The dashboard should show the corrected rate and its interval, not the raw 85%. If the committee gates on the lower bound, as it should for a costly false pass, the bar is not demonstrated either: stepping down is her call, and moving down a level is always allowed.

**What settles it.** Have the credit analyst label a fresh sample of 150 of last month's production memos: it re-validates the judge on current traffic (September's split may no longer match it) and narrows the interval. Expert-pass labels tighten it most, since TPR's uncertainty dominates when most memos pass.
