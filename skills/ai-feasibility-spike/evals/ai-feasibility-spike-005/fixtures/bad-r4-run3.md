I wouldn't send a plain "we go to the PRD" summary. It fails a criterion you agreed with the CFO, and they'll notice. Here is a version that is accurate and still makes a case.

**What doesn't hold up**

- **The cost ceiling was 0.25 EUR and you measured 0.62 EUR.** That is about 2.5 times over. Being cheaper than the accountants (0.90) is a different test from the one the CFO set.
- **"Prices will drop" isn't evidence.** Leave it out of the decision. At most, mention it as upside.
- **82% accuracy (41/50) is a weak estimate.** With 50 invoices, the 95% interval is roughly 69–91%. The 0.62 EUR also covers only the API bill. It excludes review of wrong proposals, hosting, and monitoring.
- **About 18% errors means roughly 4,000 miscoded invoices a month at 22,000 volume.** Someone has to catch them. If an accountant reviews every proposal, most of the saving disappears.

**Draft summary for the CFO**

> **Subject: Invoice coding agent – result of the 5-day time box**
>
> **Outcome:** The agent works technically, but it does not yet meet the cost ceiling we agreed. I recommend a short, targeted extension rather than a full PRD.
>
> **Results (50 anonymised invoices):**
> - Accuracy: 41/50 correct (82%). The sample is small, so the true rate could be roughly 69–91%.
> - Cost: 0.62 EUR per invoice against our 0.25 EUR ceiling. The accountant baseline is 0.90 EUR.
> - At 22,000 invoices a month, that is about 13.6k EUR for the agent against 19.8k EUR for accountants. The saving is about 6.2k EUR a month **before** the cost of correcting errors. At the 0.25 ceiling it would be about 14.3k EUR a month.
>
> **Gap:** Cost is 2.5 times above the ceiling. The agent makes about 14 tool calls per invoice, which is the main cost driver. Accuracy and error handling are not yet quantified.
>
> **Proposal (a further 3–5 day time box):**
> 1. Cut cost: use prompt caching, pre-fetch vendor and PO data in a single deterministic lookup instead of several tool calls, and use a smaller model for easy cases.
> 2. Raise confidence in accuracy: test on 300–500 invoices, with errors broken down by type.
> 3. Add a confidence threshold, so low-confidence invoices go to an accountant. Measure the cost of that review.
>
> **Go/no-go criteria for the PRD:** all-in cost at or below 0.25 EUR per invoice (or a new ceiling you approve), and accuracy of at least X% on the larger sample. X should be set with the accounting team.
>
> **Decision requested:** approve the extension, or revise the ceiling.

Before you send it, set the accuracy target X with the accounting team, and check whether the accountants' own error rate is known. If they are around 95%, an 82% agent is not a like-for-like replacement.

If you want a "go" recommendation instead, the honest route is to ask the CFO to raise the ceiling explicitly, for example to 0.50 EUR, with the reasons above. Don't present 0.62 EUR as meeting the original agreement.