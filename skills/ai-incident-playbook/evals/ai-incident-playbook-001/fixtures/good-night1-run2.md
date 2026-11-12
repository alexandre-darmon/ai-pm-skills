**Class: wrong action. Severity: SEV2, provisional until the full count is in.** 40 wrong refunds worth about 6,000 EUR is financial harm, and it was found only after the fact. Don't treat the 40 as the final number. They are the ones someone noticed.

## Decision for the meeting: contain by slice, don't argue on/off

The agent is acting autonomously (L4) after a prompt change that is now known to be bad. Dropping autonomy needs no vote (ladder rule 3).

1. **Drop the agent from L4 to L2 now.** It drafts refunds and a human approves each one. This stops the damage without losing the whole function.
2. **If nobody can name a refund slice that is safe**, turn it off entirely until someone can. A small-amount, low-risk category might qualify, but that has to be demonstrated, not assumed.
3. **Roll back the prompt change** to the last known-good version. This is probably the fastest fix, but only if the rollback has been rehearsed. If it hasn't, record it as untested.
4. **Name one rollback owner and one deputy, today.** The owner acts immediately, with no committee vote. This is the part the meeting is missing.
5. **Fallback while it's reduced:** the human refund queue handles approvals. Staff it for the extra volume.

## First 60 minutes

- **Preserve evidence first.** Save the traces and the version bundle (prompt, model, tools, config) for the whole window, before changing anything.
- **Name the incident lead.**
- **Size the damage.** Pull every refund issued since the prompt change deployed, not only the 40 flagged. For each one, record whether it was correct, the amount, and the customer. Then count the people affected. Set a deadline, for example within 2 to 4 hours. Revise the severity from that count.
- **Quantify the 40.** At about 150 EUR each, the average is low, but check for outliers and for repeat customers.

## Reporting clocks (for counsel and the DPO to confirm)

I need the detection time to give dates. Use "detected at" as T0, which is the prudent start.

- **GDPR art. 33, if personal data was breached:** notify the authority within 72 hours of becoming aware, so T0 + 3 days. Wrong refunds alone may not be a personal data breach. If money went to the wrong accounts or recipients, it may be. The controller decides on the DPO's advice and records the decision. I won't decide it for you.
- **AI Act art. 3(49)/73:** this applies only if the system is high-risk and the incident is "serious". A refund agent probably isn't Annex III, but confirm the classification. If it is, the provider's limit is 15 days from awareness. Deployer obligations under art. 26(5) apply from 2 December 2027.
- **Also check** your contracts, payment-provider terms, and finance and audit requirements.

## Communications (drafts)

**To the affected customers**, once the count is confirmed:
> We recently issued a refund to you in error, of [amount] on [date]. This was caused by a fault in our automated system, not by anything you did. [State clearly whether you will recover it or not, as decided by finance and legal.] We're sorry, and we'll contact you at [channel] with next steps.

Don't send this until legal and finance have decided whether to claw the money back.

**To the sponsor and leadership:**
> The L4 refund agent issued 40 wrong refunds (about 6,000 EUR) after a prompt change on [date]. Autonomy is reduced to L2 as of [time]. The prompt is being rolled back, and we are counting the full impact by [time]. Rollback owner: [name]. Next update: [time].

**To the DPO:** the facts above, plus whether any personal data went to the wrong party.

**To employee representatives:** only if the human approval queue changes people's work.

## Before the fix ships

- **Error analysis on every affected output in the window.** For each, record what went wrong, the failure mode, whether it is new or known, and which question class it belongs to.
- **Add regression cases to the golden set** (`build-evals`) from those outputs. They must fail on the faulty version.
- **Re-enable L4 only when** the regression cases pass and the full eval suite shows no class below its threshold, compared against the previous version on the same cases. A fix checked only on the reported examples isn't verified.
- **Record** the incident, the fix and the eval delta in the model card changelog.
- **Fix the process.** A prompt change reached production without passing evals, and nothing alerted until the next day. Add a release gate that blocks prompt changes unless evals pass. Add a monitor on the refund-error rate, the override rate, or refund amount against the expected distribution. Alerting on uptime alone is not enough here.
- **Hold a post-incident review:** timeline, cause, fix, and what the monitoring missed.

## What I need from you

1. The time the incident was detected, so I can turn the clocks into dates.
2. Who can roll back, and whether that rollback has ever been rehearsed.
3. When the prompt change deployed, and how many refunds were issued since.
4. Whether personal data was involved, and the AI Act classification.

Do you want me to draft the full playbook from `templates/playbook.md` once you have those?