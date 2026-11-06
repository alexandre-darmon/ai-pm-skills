**Use both: the small model first, with low-confidence cases sent to the frontier model or to a human. Until you've measured that, run the frontier model alone.**

**The cost gap**

| | Per month (60,000 conversations) | Per year |
|---|---|---|
| Small model | 24 EUR | about 290 EUR |
| Frontier model | 720 EUR | about 8,650 EUR |

The gap is about 700 EUR a month. Against that, the frontier model gets roughly 8,400 more conversations a month right (14 points of 60,000). That is a small cost for KPIs that people will act on. A 78% classifier is too noisy for monthly KPIs, and a use case with a 5% share can easily be distorted.

**Why routing beats either model alone**

- If the small model's confidence separates its right answers from its wrong ones, it keeps the confident cases.
- The frontier model takes the rest, and a human reviews the cases that stay unclear. Never force an unclear case into a class.
- Sending a fraction f of conversations to the frontier model costs about 24 + 720·f EUR a month. At f = 30% that is about 240 EUR.
- The blended agreement at that threshold is unknown. You have to measure it on your labelled set before trusting any number.

**Checks before you decide**

1. **Report agreement per dimension.** Use case and resolution will not behave the same. The small model may be fine on use case and weak on resolution, which needs reading the whole conversation. A single 78% or 92% hides that.
2. **Your 200 labels leave real uncertainty.** The 95% interval is roughly ±4 points on 92% and ±6 on 78%. That is enough to decide here, but not to fine-tune a threshold, so extend the set if you can.
3. **Measure the human ceiling.** Have two labellers double-label at least 50 conversations. If they agree only about 90% of the time, the frontier model's 92% is already at the ceiling.
4. **Mask personal data first.** Names, emails, IBANs and ids must be masked before any model call, including these tests. Check at least 100 masked conversations by hand and report the leak rate.

**Next steps**

1. Run the frontier model alone on the labelled set. It is affordable, and you can start now.
2. Collect the small model's confidence scores on the 200 labelled conversations. Choose a threshold and report blended agreement and blended cost per dimension.
3. Switch to the routed setup if it gets within about 1–2 points of the frontier model's agreement at a clearly lower cost.
4. Each month, label a fresh sample of 50–100 conversations and re-measure agreement per dimension. Also track the share of "other" and of low-confidence cases.

I can draft the full classification plan (taxonomy, annotation guide, threshold study, output schema) if you want it. I'd need your draft taxonomy and the confidence scores, or a way to get them.