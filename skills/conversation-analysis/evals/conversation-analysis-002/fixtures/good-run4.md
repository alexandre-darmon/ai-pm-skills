**Recommendation: don't pick either one alone. Run the small model first and send its low-confidence cases to the frontier model. If that doesn't work in a test, use the frontier model for everything.**

**What the numbers say**
- The small model costs 24 EUR a month (60,000 × 0.0004). The frontier model costs 720 EUR a month (60,000 × 0.012).
- The gap is about 700 EUR a month, roughly 8,400 EUR a year. That is small next to the cost of KPIs built on bad labels.
- Disagreement with your labels is 22% for the small model and 8% for the frontier model. On 60,000 conversations that is about 13,200 versus 4,800 mislabelled a month. The small model gets about 8,400 more wrong.
- Finance's saving is real but small. The data team's accuracy gain is large. So the question is how to get most of the accuracy for less than 720 EUR.

**Cascade**
1. The small model classifies everything and returns a confidence.
2. Above a threshold, its label is kept.
3. Below the threshold, the frontier model or a human reviews the case. Never force a low-confidence case into a class.

For illustration only, I haven't measured this. Suppose the small model keeps 60% of conversations at about 95% agreement. The blended cost is then about 24 + 0.4 × 60,000 × 0.012 ≈ 312 EUR a month, with agreement close to the frontier model's. Whether this holds depends on whether the small model's confidence actually separates its right answers from its wrong ones. You can test that on the 200 conversations you already have.

**What to check before deciding**
1. **Agreement per dimension.** Use case and resolution are separate dimensions. The 78% and 92% may hide a model that is fine on use case and weak on resolution, or the reverse. Don't average them.
2. **The human ceiling.** Have two people label at least 50 of the 200 conversations. If they agree only about 90% of the time, the frontier model's 92% is already at the ceiling, and nothing can do better.
3. **Sampling error.** With 200 conversations, 78% is about ±6 points and 92% is about ±4 points. The gap is clearly real, but the exact figures are loose.
4. **Which classes get confused.** Check whether the small model's errors are concentrated in a few close classes. If so, fixing the taxonomy rules may help more than switching models.
5. **Blended results.** Report agreement and cost per conversation at the chosen threshold, so finance and the data team argue over one set of numbers.

**Before any model sees the transcripts**
- Mask personal data (names, emails, IBANs, ids) with placeholders.
- Check at least 100 masked conversations by hand and report how many still leak.
- Do this for both candidates, and for any model used to draft the taxonomy.
- Don't run either model on raw text, even as a test.

**Afterwards**
- Each month, label a fresh sample of 50–100 conversations and re-measure agreement per dimension.
- Track the share of "other" and the share of low-confidence cases. If agreement drops or "other" goes above 10%, review the taxonomy.

If you want, I can draft the full classification plan from the template. I'd need the draft taxonomy, the 200 labelled conversations (masked), and the confidence outputs from both models.
