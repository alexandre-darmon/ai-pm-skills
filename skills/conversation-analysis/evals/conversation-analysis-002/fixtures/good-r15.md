**Recommendation: don't pick either one alone. Run the small model on everything and send the conversations it's unsure about to the frontier model or a human. This is a recommendation, not a measured result. I need confidence scores from your 200 labelled conversations to confirm it.**

**The cost gap is small next to the quality gap**
- Small model: 60,000 × 0.0004 = **24 EUR/month**.
- Frontier model: 60,000 × 0.012 = **720 EUR/month**.
- The difference is 696 EUR/month, about 8,350 EUR/year. Finance is arguing over a small amount.
- Disagreement with your labels is 22% for the small model and 8% for the frontier model. That is about 13,200 versus 4,800 conversations a month, so roughly 8,400 more wrong rows feeding your KPIs. Where the errors are systematic, they shift volume by use case.

**Why routing is likely better than either**
- Blended cost = 24 EUR + (0.012 × routed share × 60,000), plus any human review.
- For illustration only, if the small model is unsure on 30% of conversations, that is 24 + 216 = **240 EUR/month**. That is a placeholder share, not a measurement.
- The agreement of the routed setup depends on whether the small model's confidence separates its right answers from its wrong ones. Neither of us knows that yet.

**What I'd need before you decide**
1. **Agreement per dimension.** "78%" and "92%" are single figures. Use case and resolution probably behave very differently, and the KPIs need each one separately. Also check which classes get confused.
2. **A human ceiling.** Have two labellers double-label at least 50 of the 200 conversations. If humans only agree about 90% of the time, 92% is already at the ceiling.
3. **Uncertainty from the small sample.** With n=200, 78% is about ±6 points and 92% about ±4. The gap is real, but small differences within a dimension won't be.
4. **Confidence scores.** Choose the threshold on about half the labelled set and confirm it on the other half. Then report blended agreement and blended cost at that threshold.
5. **An acceptance bar per dimension, set in advance.** For example, within a few points of the human ceiling.

**Two things to settle before any model call**
- Mask personal data (names, emails, IBANs, ids) before any conversation reaches either model, and check a sample of at least 100 masked conversations.
- Set a monthly drift check: label a fresh sample of 50–100 conversations each month and compare agreement per dimension with the last run.

If you want a single model right now and can't run the routing test, the frontier model is the safer choice. Its extra 696 EUR/month is small next to the cost of KPIs built on labels that are wrong 22% of the time.

If you can share the per-conversation outputs and confidence scores for the 200 labelled conversations, I can work out the per-dimension agreement and the routing threshold.