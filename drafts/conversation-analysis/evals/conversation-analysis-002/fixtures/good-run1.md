**Use the frontier model, or better, route between the two by confidence. Don't use the small model alone.**

**Cost**
- Small model: 60,000 × 0.0004 = **24 EUR/month**.
- Frontier model: 60,000 × 0.012 = **720 EUR/month**.
- The most Finance can save is about 700 EUR/month, or roughly 8,400 EUR/year.

**Quality**
- With 200 labels, the 95% margin is about ±6 points for 78% and ±4 points for 92%. The intervals don't overlap, so the gap is real.
- At 78%, about 13,000 conversations a month are misclassified, against about 4,800 at 92%.
- Errors on this scale distort volume by use case and the resolution rate. Those figures feed your KPIs and any KB or ROI decision, so a wrong KPI costs more than 700 EUR/month.

**Before you commit, check these**
1. **Mask personal data first.** Do this before any model call, including these comparisons. Nothing else runs until you've checked a sample of masked conversations and the leak rate is acceptable.
2. **Split agreement by dimension.** 78% and 92% look like single averages. The small model may be fine on resolution and weak on use case, or the reverse. Report each dimension separately, with the confusion between the closest classes.
3. **Find the human ceiling.** Have two labellers label at least 50 of the same conversations. If they agree only 90% of the time, then 92% is already at the ceiling. If your labels are noisy, the real gap between the models may be different.
4. **Test confidence routing.** The small model handles conversations where it is confident, and the frontier model or a human takes the rest. If its confidence separates right from wrong, you could keep most of the 92% for much less than 720 EUR. For example, if 60% of conversations stay with the small model, the cost is about 300 EUR/month. I can't compute the real blended figure without the confidence scores on your 200 conversations. Send those and I'll work it out.
5. **Never force low-confidence cases into a class.** Send them to review or label them "unclassified".

**Plan**
- Start with the frontier model on everything. At 720 EUR/month it is cheap enough to be the safe default.
- Measure the routing threshold on your labelled set.
- Switch to routing only if blended agreement stays near 90% or higher on both dimensions.
- Re-measure every month on a fresh sample of 50–100 labelled conversations to catch drift. Also track the share of "other" and of low-confidence cases.

Finance gets a cost lever through routing, and the data team keeps KPI-grade accuracy.