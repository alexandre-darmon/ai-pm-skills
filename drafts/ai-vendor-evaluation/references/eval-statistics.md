<!-- Synced copy of foundations/eval-statistics.md. Edit the original, then run: python3 scripts/validate_skills.py --sync -->
# Eval statistics

The numbers every eval skill uses, with the formula and a worked value. A PM does not need more than this page; a data scientist can check every line.

## 1. The unit is the case

Repeated runs of one case share its prompt and its difficulty: they are not independent evidence. Average the runs of a case first, then compute over cases. When several cases come from the same conversation, document or customer, treat that source as the unit (clustered errors), or the interval will be too narrow.

When cases cluster, count effective cases: design effect = 1 + (m − 1) × ρ, with m the cases per source and ρ how alike their results are (0 to 1). Effective n = n ÷ design effect. Fifty cases drawn from ten documents at ρ = 0.3 behave like about 22 cases. Bootstrap whole sources, not cases (§6).

## 2. A pass rate always comes with its interval

Use the Wilson interval, which holds with few cases and with rates near 0% or 100%. For k passes out of n cases, p = k/n, z = 1.96 for 95%:

centre = (p + z²/2n) / (1 + z²/n) · half-width = z · √(p(1−p)/n + z²/4n²) / (1 + z²/n)

| Passes | Rate | 95% interval |
| --- | --- | --- |
| 18 of 20 | 90% | 70% to 97% |
| 45 of 50 | 90% | 79% to 96% |
| 90 of 100 | 90% | 83% to 94% |
| 180 of 200 | 90% | 85% to 93% |
| 12 of 12 | 100% | 76% to 100% |

Zero failures does not mean a zero failure rate: with no failure in n cases, the true rate can still be up to about 3/n (rule of three). Thirty clean runs allow up to 10% failures; three hundred, up to 1%.

## 3. Size each class for the decision it supports

To estimate a rate near p within ±e at 95%: n ≈ 1.96² × p(1−p) / e².

| Expected rate | ±10 points | ±5 points | ±3 points |
| --- | --- | --- | --- |
| 95% | 19 | 73 | 203 |
| 90% | 35 | 139 | 385 |
| 80% | 62 | 246 | 683 |

A class with legal, financial or irreversible effects is sized for the margin its threshold needs, whatever its share of traffic. A class with fewer cases is reported with its interval and marked indicative.

## 4. Gate on the lower bound when a false pass is costly

For a costly class, the gate passes when the lower bound of the interval clears the threshold, not the point estimate. Twelve passes out of twelve does not demonstrate 95%: the lower bound is 76%. Elsewhere, gate on the point estimate and publish the interval.

## 5. Compare two versions on the same cases

Run both versions on the same cases and work on the paired differences. For pass/fail graders, count d, the cases where exactly one version passes: a gap smaller than 2√d / n can come from the choice of cases, so it is a tie. For scores, take the per-case difference: interval = mean ± 1.96 × sd / √n, or a bootstrap. A paired comparison needs far fewer cases than two separate scores.

Before the run, write the smallest gap the comparison can detect: minimum detectable effect ≈ (1.96 + 0.84) × sd of the paired differences ÷ √n, at 5% significance and 80% power. If that gap is larger than the one that would change the decision, add cases before running, not after.

## 6. Bootstrap when the formula does not fit

Resample the cases with replacement, 1,000 to 10,000 times, recompute the metric, keep the middle 95%. Resample within each class when the headline averages classes, and resample whole sources when cases cluster. With fewer than about 10 cases per class, a plain bootstrap is too narrow; stretch each resampled class mean by √(n/(n−1)) (Rao and Wu).

## 7. A judge's rate must be corrected by its errors

Read a judge as a classifier against expert labels kept apart from the ones used to write its prompt:

- TPR (sensitivity): share of answers experts pass that the judge passes.
- TNR (specificity): share of answers experts fail that the judge fails.

Raw agreement hides a lazy judge. If 90% of answers are good, a judge that passes everything agrees 90% of the time, with a TNR of 0. Report TPR and TNR, never agreement alone.

When the judge then scores unlabelled traffic, the observed pass rate is biased by its errors. Corrected rate = (observed + TNR − 1) / (TPR + TNR − 1), clipped to 0–100% (Rogan and Gladen). With TPR 92%, TNR 80% and 85% observed, the corrected rate is 90%. The interval must carry the uncertainty of TPR and TNR too: bootstrap the labelled set and the scored sample together. If TPR + TNR − 1 is small, the correction explodes: the judge is not usable.

Between two human labellers, use Cohen's kappa = (observed agreement − chance agreement) / (1 − chance agreement). Below about 0.6, the criterion itself is unclear: fix the definition before blaming the judge.

## 8. Agents: reliability is pass^k, not pass@k

pass@k asks whether one of k trials succeeds; pass^k asks whether all k do. For an agent that acts, users meet every trial, so report pass^k. If each trial succeeds with probability p, pass^k ≈ p^k: 95% per trial gives 77% over five trials, 60% over ten.

## 9. Online: alert on a shift, not on noise

A production pass rate measured on n sampled traces per period moves by chance. Control limits: p̄ ± 3 × √(p̄(1−p̄)/n). Alert when a period falls outside, or when several periods in a row sit on the same side of the centre line. Set the sample size so the limits are tighter than the drop you must catch.

## 10. More checks, more false alarms

Twenty independent checks at 95% will raise about one false alarm by chance. Name the primary metric before the run; treat the others as signals to investigate, not as verdicts.

## 11. Online experiments

Sample size per arm for an A/B on a rate p and a lift δ, at 80% power and 5% significance: n ≈ 16 × p(1−p) / δ². If the traffic cannot fill it within a reasonable window, use shadow and canary instead.

## 12. Reward abstaining when a wrong answer costs more than a hand-off

Accuracy alone rewards guessing. Grade each answer correct, abstained (hand-off, "I don't know") or wrong. Set the price of a wrong answer from the cost ratio before the run: score = correct − k × wrong, with k = cost of a wrong answer ÷ cost of a hand-off, abstention at 0. Report per class: coverage (share answered), error rate on the answers kept, abstention rate. A system that answers less but is wrong far less often can be the better one at L2 or L3.

## 13. Robustness to rewording

A score measured on one wording of each case can flip on another. For a release or a model choice, run each case in several meaning-preserving variants (paraphrase, field order, typos, the users' language): five is a reasonable minimum. Report the mean, the worst-variant pass rate and the share of cases whose verdict flips between variants. Gate on the worst variant when the class is costly; if two systems' variant ranges overlap, call it a tie.

## 14. Two suites: capability and regression

A capability suite holds hard cases the system mostly fails today; it shows progress. A regression suite holds cases the system already passes; it must stay near 100% on every change, including provider model updates. A case graduates from the first to the second once it passes in every run of two consecutive releases. A case every candidate passes, or whose result flips from run to run more than between systems, adds cost and no evidence: retire it from the decision set.
