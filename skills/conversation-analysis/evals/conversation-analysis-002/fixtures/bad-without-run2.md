**Use the frontier model.** The cost gap is small in absolute terms, and the accuracy gap is large.

**Cost at 60,000 conversations a month**
- Small model: about 24 EUR/month.
- Frontier model: about 720 EUR/month.
- The difference is about 696 EUR/month, or roughly 8,400 EUR/year.

**What that buys**
- The small model mislabels about 13,200 conversations a month (22%). The frontier model mislabels about 4,800 (8%).
- That is about 8,400 fewer wrong labels for 696 EUR, or roughly 0.08 EUR per avoided error.
- On 200 samples, the 95% intervals are about ±6 points for 78% and ±4 points for 92%. They don't overlap, so the gap is real and not sampling noise.

**Why accuracy matters more here than the cost suggests**
- These labels feed monthly KPIs. Random errors partly cancel in aggregate, but a small model's errors are usually systematic, such as one use case consistently confused with another or "resolved" over-called. That biases the KPI and can make a trend look like it moved when it didn't.
- A 22% error rate is also hard to defend if someone asks where a KPI came from.

**Before you commit, two cheap checks on your 200 labels**
1. Compare per-class confusion, not just overall agreement. If the small model is only weak on a few classes, a hybrid becomes attractive.
2. Check whether 92% is near your labelling ceiling. If your own annotators agree with each other only about 93% of the time, the frontier model is effectively at the limit.

**Optional middle path:** run the small model first and send only low-confidence or disagreement-prone cases to the frontier model. This could cut the 720 EUR to somewhere around 100–250 EUR with most of the accuracy. It adds pipeline complexity to save at most about 6,000 EUR/year, so I'd only build it if finance pushes back. Validate it on the same 200 labels first.

One caveat: I assumed the 78% and 92% figures cover both tasks together (use case and resolution). If they're averages, check each task separately, because one may be fine on the small model.