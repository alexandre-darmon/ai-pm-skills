**Recommendation: use neither one alone. Run the small model with a confidence threshold, and send the low-confidence cases to the frontier model.** You can't confirm the exact split from the numbers you've given me, but the arithmetic shows how much room there is.

**Cost at 60,000 conversations a month**
- Small model only: about 24 EUR a month.
- Frontier model only: about 720 EUR a month.
- The gap is roughly 700 EUR a month, or about 8,400 EUR a year. That's small against the cost of wrong KPIs, but it's also not nothing at the scale of a classifier.

**Why not the small model alone**
- 78% agreement means about 13,000 conversations a month are misclassified. That error feeds your KPIs directly.
- It's an average. Use case and resolution are separate dimensions, and one may be much worse than the other. Resolution is often the harder one.
- Errors are rarely random. If the small model confuses two close classes, it biases the volume per use case, not just adds noise.

**Why not the frontier model alone**
- 92% is a good number, but it's measured on only 200 conversations. That gives a margin of roughly ±4 points, so the real figure could be anywhere from about 88% to 96%.
- You haven't said how well two human labellers agree with each other. That's the ceiling for any classifier. If humans agree only 90% of the time, the frontier model is already at the ceiling and you can't expect more from it.
- It costs 30 times as much for the cases where the small model is already right.

**Routing by confidence**
- The small model keeps the conversations it's confident about. The frontier model or a human takes the rest.
- Say the small model is confident on 70% of conversations and is right about 92% of the time on those. Then the blended cost is about 0.0004 + 0.3 × 0.012 ≈ 0.004 EUR per conversation, or about 240 EUR a month. Agreement would be close to the frontier model's. Those figures are an illustration, not a result.
- This only works if the small model's confidence actually separates right answers from wrong ones. You can check that on your 200 labelled conversations at no extra cost.

**What to do next**
1. Check the agreement per dimension (use case and resolution separately), and the confusion between the closest classes, for both models.
2. Have two labellers label at least 50 of the 200 conversations, to get the human ceiling.
3. Collect the small model's confidence on each conversation. Pick the threshold, then report blended agreement and blended cost per conversation.
4. Don't force low-confidence cases into a class. Route them to the stronger model or to review, or mark them "unclassified".
5. Re-measure every month on a fresh sample of 50–100 labelled conversations, and track the share of "other" (keep it under 10%) and of low-confidence cases.

**Before anything else:** mask personal data (names, emails, IBANs, ids) before any conversation reaches either model. GDPR art. 5(1)(c) requires it. Check a sample of at least 100 masked conversations by hand. If you haven't done this for the 200 labelled ones, the comparison is already tainted.

I can draft the full classification plan using the template, or write the script that picks the threshold from your labelled set. Which would you like?