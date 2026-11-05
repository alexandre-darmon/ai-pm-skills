**Use the frontier model.** The extra cost is small next to the quality gap.

**Cost at 60,000 conversations a month**
- Small model: about 24 EUR/month.
- Frontier model: about 720 EUR/month.
- The difference is about 700 EUR/month, or roughly 8,400 EUR/year.

**Quality**
- At 78% agreement, about 13,200 conversations a month are labelled differently from your labels.
- At 92%, that falls to about 4,800.
- With 200 labels, the 95% intervals are roughly ±5.7 points for the small model and ±3.8 for the frontier one. They don't overlap, so the gap is real.

The bigger issue is that the errors aren't random noise. A small model's mistakes are usually systematic, such as consistently confusing "resolved" with "partially resolved". That biases the KPI itself, which is worse than adding noise. Spending 700 EUR a month to avoid that is cheap, and the cost is trivial compared with the decisions the KPIs feed.

**Before you commit**
1. **Check the errors by category.** If the small model's misses are concentrated in a few labels, such as resolution, the aggregate 78% hides that. Compare the confusion matrices.
2. **Check what "agrees" means.** Is it per field or both fields at once? Joint agreement on use case and resolution is lower than either field alone, for both models.
3. **Check your labels.** If humans only agree with each other about 90–95% of the time, the frontier model's 92% is close to the ceiling.

**A cheaper option worth testing**
Run the small model on everything and escalate low-confidence cases, or the label types it handles badly, to the frontier model. Batch pricing, if your provider offers it, would also cut the frontier cost, since monthly KPIs aren't latency-sensitive. This could bring the cost to about 100–250 EUR a month with accuracy close to 92%. You'd need to measure it on the 200 labels, and I wouldn't assume it works until you have.

**For the finance–data disagreement**
If the monthly cost is the concern, the frontier model costs about 0.012 EUR per conversation, or 720 EUR a month in total. Finance could compare that with the cost of acting on KPIs that are wrong for roughly 1 conversation in 5.