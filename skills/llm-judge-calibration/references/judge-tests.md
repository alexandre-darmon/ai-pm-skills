# Judge tests: sizing, bias protocols, intervals

Loaded on demand by `llm-judge-calibration`. Formulas for Wilson, kappa, bootstrap and the Rogan–Gladen correction are in references/eval-statistics.md; this file adds what is specific to judges.

## 1. How many expert fails the test split needs

TNR is estimated on the expert fails only, so its interval depends on their number. Wilson 95% intervals:

| Expert fails in the test split | TNR 80% | TNR 90% |
| --- | --- | --- |
| 20 | 58% to 92% | 70% to 97% |
| 30 | 63% to 91% | 74% to 97% |
| 50 | 67% to 89% | 79% to 96% |
| 60 | 68% to 88% | 80% to 95% |
| 100 | 71% to 87% | 83% to 95% |

Reading: to show TNR ≥ 80% on the lower bound when the judge's true TNR is about 90%, plan about 60 expert fails. With 9 fails, even 9 caught out of 9 only shows TNR ≥ 70%.

The same table holds for TPR with expert passes. Passes are usually plentiful; fails are the constraint.

Enrichment: when fails are rare in traffic, add likely fails to the labelling sample (answers flagged in `error-analysis`, low-confidence answers, complaints). TPR and TNR are computed within each expert class, so enrichment does not bias them. It does change raw agreement, one more reason not to report agreement.

## 2. Splits

| Split | Share | Used for | Reported? |
| --- | --- | --- | --- |
| Few-shot pool | 10–20% | examples pasted into the judge prompt | never |
| Dev | about 40% | iterating the prompt, reading disagreements | as tuning progress only |
| Test | about 40% | one scoring per judge version | yes: TPR, TNR, intervals |

Draw the splits at random within each expert class before writing the prompt. Once the test split's disagreements have been read to change the prompt, it is dev data: label a fresh test split for the next version.

## 3. Bias protocols

| Bias | When it applies | Test | Pass condition |
| --- | --- | --- | --- |
| Position | pairwise judging (A vs B) | judge every pair twice, order swapped | the verdict holds in both orders on nearly all pairs; report the flip rate |
| Verbosity | answers of varied length | verdict against answer length on the test split; then length-matched pairs that differ only on the criterion | no trend of passes with length once the criterion is fixed |
| Self-preference | judge and system from the same model family | re-judge a sample (50+) with a judge from another family | TPR and TNR within their intervals of each other |
| Prompt sensitivity | always | re-run the test split with a paraphrased instruction | TPR and TNR within their intervals |
| Model drift | judge called through an alias or a hosted endpoint | pin the version; re-test when it changes | a moved version is a new judge |

## 4. Interval of the corrected rate without Python

The corrected rate c = (p + TNR − 1) ÷ J, with J = TPR + TNR − 1. A first-order (delta-method) approximation of its standard error, with p observed on n answers and the test split holding n₊ expert passes and n₋ expert fails:

SE ≈ √( p(1−p)/n + c²·TPR(1−TPR)/n₊ + (1−c)²·TNR(1−TNR)/n₋ ) ÷ J

95% interval ≈ c ± 1.96 × SE, clipped to 0–100%, marked approximate. The bootstrap of `scripts/judge_metrics.py` is the reference; the two agree closely when every class has 30+ answers.

What the formula shows: when most answers pass (c high), the uncertainty of TPR dominates, so more expert-pass labels tighten the interval; when most fail, TNR dominates. A small J inflates everything: below 0.5, do not use the judge for a rate.

## 5. Re-validation

| Trigger | What to do |
| --- | --- |
| Judge model, version or provider change | new test split, targets restated before scoring |
| Prompt or criterion change | new test split |
| Schedule (monthly or quarterly, by risk) | 50+ production answers labelled by the expert, fails enriched; TPR and TNR compared with the last test |
| Corrected rate outside 0–100% before clipping | the judge and the traffic disagree: re-test now |
| Production incident the judge passed | add the case to the labelled set; re-test if it reveals a new failure mode |

## 6. Cost

Judge cost per call = input tokens × input price + output tokens × output price (the critique counts as output). Monthly cost = calls per answer × answers scored per month × cost per call. A judge per failure mode multiplies the calls: state the number of judges.
