**Recommendation: start with a routed setup. The small model classifies everything, and a frontier model (or a human) takes the conversations where the small model is unsure. If routing can't be validated, use the frontier model alone, not the small one.**

**Cost at 60,000 conversations a month**

| | Per conversation | Per month | Conversations disagreeing with your labels |
|---|---|---|---|
| Small | 0.0004 € | 24 € | about 13,200 (22%) |
| Frontier | 0.012 € | 720 € | about 4,800 (8%) |

- The most Finance can save is 696 € a month, about 8,400 € a year.
- The price of that saving is about 8,400 more disagreeing conversations every month in the KPIs.
- Per-use-case volumes and resolution rates feed your KPIs. At 78% agreement they will be noisy enough to mislead.
- At this volume, the frontier model's price is small next to the cost of acting on bad KPIs.

**Why routing**
- The small model alone probably misses any reasonable accuracy bar.
- The frontier model alone pays 0.012 € on every conversation, including the easy ones.
- Routing pays the frontier price only on the share the small model is unsure of.
- The blended cost is 24 € + (720 € × share routed to the frontier model) + review cost. If 30% were routed, that would be about 240 €. That figure is only an illustration, because the real share depends on your data.

**What to check before committing**
1. **Agreement per dimension.** Use case and resolution are separate tasks, so 78% and 92% may hide very different results on each. Report them separately, along with the confusion between the closest classes.
2. **Human ceiling.** Have two labellers label at least 50 of the 200 conversations. If they agree with each other only about 90% of the time, the frontier model's 92% is already at the ceiling.
3. **Sample size.** With 200 conversations, 78% is roughly ±6 points and 92% roughly ±4. The gap is real, but the exact figures are loose.
4. **Confidence separates right from wrong.** Pick the threshold on half the labelled set and confirm it on the other half. Send low-confidence cases to the frontier model or to review. Never force them into a class. 200 conversations is thin for that split, so label more if the confirmation is shaky.
5. **Masking.** Confirm the transcripts were masked before the 200 were sent to either model. If they weren't, fix that first.
6. **Monthly drift check.** Label a fresh sample of 50–100 conversations each month and compare agreement per dimension with the previous run.

**How to decide**
- Set the bar per dimension in advance, for example within a few points of the human ceiling.
- If the routed blend meets it for roughly 100–300 € a month, use that.
- If it doesn't, use the frontier model alone. At 720 € a month it's cheap enough.

I can lay this out as a full classification plan, with taxonomy, annotation guide, and drift check, if you want it.