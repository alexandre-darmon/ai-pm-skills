**Recommendation: use neither model alone. Run the small model on every conversation and send the ones it is unsure of to the frontier model or to a person.** The data to choose the threshold isn't there yet, so the first step is to measure it.

**Why neither model alone**
- **Small model alone:** it costs 60,000 × 0.0004 = **24 EUR/month**, but it disagrees with your labels on 22% of conversations. That is about 13,200 wrong labels a month feeding the KPIs.
- **Frontier model alone:** it costs 60,000 × 0.012 = **720 EUR/month**, which is about 8,600 EUR/year. It disagrees on 8%, about 4,800 conversations.
- **The gap:** the frontier model costs 696 EUR/month more. That is small next to the cost of the team acting on wrong KPIs, and it is also not necessary to pay it on every conversation.

**Routed setup**
Blended cost = 0.0004 × 60,000 + 0.012 × 60,000 × (share routed) + review cost × (share sent to people).

As an illustration, if the small model is unsure on 30% of conversations, the cost is 24 + 216 = **240 EUR/month**, plus any human review. That 30% is an assumption I made up, not a measurement. Whether routing works depends on whether the small model's confidence separates its right answers from its wrong ones, and your data can't tell us that yet.

**What to do before deciding**
1. **Mask personal data first.** Do this before any further model call on the transcripts. Check 100 or more masked conversations by hand, and agree a retention period for the masked text and the logs. This is the GDPR art. 5 data-minimisation requirement.
2. **Split the agreement by dimension.** 78% and 92% are single numbers. Use case and resolution can behave very differently, so report each separately, along with the confusion between the closest classes.
3. **Find the human ceiling.** Have two labellers label at least 50 of the 200 conversations. If humans agree with each other only about 90% of the time, the frontier model's 92% is already at that ceiling.
4. **Allow for the small sample.** With n = 200, the 95% margin is about ±3.8 points on 92% and about ±5.7 on 78%. The gap is real, but the exact figures are loose.
5. **Choose the threshold.** Pick it on half of the labelled set and confirm it on the other half. Set the acceptance bar per dimension in advance, for example within a few points of the human ceiling. Send low-confidence cases to review or to "unclassified", and never force them into a class.
6. **Report the blended figures.** Give the agreement and the cost per conversation at the chosen threshold, with the arithmetic.

**After it's live**
Label a fresh sample of 50–100 conversations each month. Track agreement per dimension, the share of "other" (keep it under 10%) and the share of low-confidence cases. A drop in agreement should trigger a review of the taxonomy.

**For the finance and data-team disagreement**
- If the routed setup reaches the bar at 100–300 EUR/month, both teams get what they want.
- If the small model's confidence doesn't separate right from wrong, use the frontier model on everything. At 720 EUR/month it is still cheap for KPIs that decisions rest on.

I can draft the full classification plan from the template, including the taxonomy check and the output schema, if you want it.