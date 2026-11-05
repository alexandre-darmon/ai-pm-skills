**Use the frontier model.** The cost gap is small next to the quality gap.

| | Small | Frontier |
|---|---|---|
| Cost per month (60,000 conversations) | about 24 EUR | about 720 EUR |
| Agreement with your labels | 78% | 92% |
| Conversations misclassified per month | about 13,200 | about 4,800 |

The extra spend is about 700 EUR a month, or roughly 8,400 EUR a year. In return you get about 8,400 fewer wrong labels every month in the data behind your KPIs. At 22% error, the small model's use-case volumes and resolution rates are too noisy to steer on. Small classes could be off by more than they change month to month.

**Before you commit, check these.**
1. **Agreement per dimension.** The 78% and 92% are single averages. Use case and resolution can behave very differently, and resolution is usually the harder one. Check each dimension separately. If the small model is fine on use case and weak on resolution, that changes the answer.
2. **The human ceiling.** Have two labellers label at least 50 of the 200 conversations. If they only agree about 90% of the time, the frontier model's 92% is near the maximum possible.
3. **Sampling noise.** With 200 conversations, 78% is roughly ±6 points and 92% roughly ±4. The gap is still clearly real.
4. **Masking.** Names, emails, IBANs and ids must be masked before any model sees the text, whichever model you pick. Check a sample of 100 or more masked conversations by hand. If you haven't done this yet, do it first. It also matters more with a frontier model, because the text is sent to an external provider.

**A way to cut the cost later.** Run the small model first and keep its answer only when its confidence is high. Send the rest to the frontier model or to a human. Total cost is about 24 EUR plus the escalated share × 720 EUR. This only works if the small model's confidence actually separates its right answers from its wrong ones. Test that on your 200 labels before relying on it. Even a good result saves at most about 700 EUR a month, so it's optional.

**Keeping it reliable.** Label a fresh sample of 50–100 conversations each month. Compare agreement per dimension with the previous month, and track the share of "other" and of low-confidence cases. Drift in the taxonomy or the model will show up there.

If you want, I can draft the full classification plan: taxonomy, annotation guide, threshold and output schema.