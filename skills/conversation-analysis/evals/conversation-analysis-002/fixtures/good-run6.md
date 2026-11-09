**Recommendation:** use neither one alone. Target a routed setup, where the small model keeps the conversations it is confident about and the frontier model (or a human) takes the rest. Use the frontier model alone only as an interim until the threshold is measured.

**Why not the small model alone:** 78% agreement means about 1 conversation in 5 is mislabelled. That would distort the monthly KPIs, and finance would be saving money on numbers it can't trust. The saving is also small. The small model costs about 24 EUR a month and the frontier model about 720 EUR, a gap of roughly 700 EUR a month (about 8,400 EUR a year).

**Why not the frontier model alone:** it is the safe fallback, and 720 EUR a month is modest for KPI data. But you'd be paying frontier prices for many easy conversations the small model already gets right.

**Illustration of routing, not a measurement:** if the small model's confidence let it keep 60% of conversations, the blended cost would be about 0.0052 EUR per conversation. That is roughly 310 EUR a month. Agreement would land somewhere between 78% and 92%, probably close to the top. The real figures depend on the next step.

**What to do next, on your 200 labelled conversations:**
1. **Get a confidence score from the small model** and check that it separates right answers from wrong ones. Pick a threshold, then report blended agreement and blended cost at that threshold.
2. **Report agreement per dimension.** Use case and resolution will probably behave differently. You may find the small model is fine on one and weak on the other.
3. **Measure human agreement.** Have two labellers label at least 50 of the 200. That is the ceiling, and 92% may already be close to it.
4. **Treat the numbers as noisy.** With 200 samples, 78% is roughly ±6 points and 92% roughly ±4.
5. **Send low-confidence cases to review or an "unclassified" bucket.** Don't force them into a class.
6. **Re-measure monthly** on a fresh sample of 50–100 conversations, and track the share of "other" and of low-confidence cases.

**Before any of this:** mask personal data before any model call, including these comparisons, and set a retention period for the masked text and the classifier logs.

If you share the per-dimension agreement and the confidence scores, I can work out the threshold and the blended cost. I can also draft the full classification plan.