**Use the frontier model.** The extra cost is small next to the accuracy gain.

**Cost**
- Small model: 60,000 × 0.0004 = **24 EUR/month**
- Frontier model: 60,000 × 0.012 = **720 EUR/month**
- The difference is about 700 EUR/month, or roughly 8,400 EUR/year. That is small for a KPI pipeline, and the choice matters little to Finance at that scale.

**Accuracy**
- On 200 conversations, the 95% intervals are about 78% ± 6 points and 92% ± 4 points. They don't overlap, so the 14-point gap is real.
- With the small model, about 1 in 5 conversations is misclassified. That is about 13,000 wrong labels a month, against about 4,800 with the frontier model.

**Before you commit, check these**
1. **Errors per category.** KPIs are aggregates, so what matters is how the errors are distributed. Random errors mostly wash out. Systematic ones, like "resolved" being over-predicted, skew the KPI and make month-to-month trends misleading. Compare the confusion matrices and the predicted share of each category against your labels. If the small model's category shares are close to the true ones, it may be good enough.
2. **Label quality.** "Agreement with our labels" is not accuracy. If your labels are noisy, the real gap could be larger or smaller. Check a sample of the disagreements by hand, especially where both models disagree with your label.
3. **Use case and resolution separately.** You classify two things. One model may be fine at use case and weak at resolution, which is usually the more subjective of the two.

**A cheaper option if 720 EUR bothers anyone**
- Run the small model first and send only low-confidence or "unresolved/ambiguous" cases to the frontier model.
- Or test a mid-tier model, which often lands near 90% at a fraction of the frontier price.
- Either option needs a re-run on your 200 labelled conversations to confirm it, so I wouldn't assume the numbers.

If you want to go further, I can help set up the comparison on your labelled set, including confusion matrices and a cascade simulation.