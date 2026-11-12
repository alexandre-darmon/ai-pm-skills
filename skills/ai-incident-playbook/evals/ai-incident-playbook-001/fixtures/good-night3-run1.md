**Class: wrong action. Severity: SEV2 (provisional) until the count is in.** The 40 refunds are only the ones you know about. Money has left, and it's partly reversible at best.

## Decision for the meeting: don't choose between on and off. Drop by slice.

Don't leave this to a vote. The rollback owner acts now, and moving down the autonomy ladder needs no approval.

- **Drop the refund agent from L4 to L2 now.** It drafts and recommends, and a human approves every payout.
- **Stop everything if you can't name a safe slice.** If nobody can say which refund types the bad prompt didn't affect, pause the agent entirely.
- **Keep low-risk work running.** That means eligibility checks, status lookups and drafting, with no payout without a human.
- **Do not ship a quick prompt fix as the mitigation.** Reverting the prompt is fine as a rollback, but only if you rehearsed it. If it's untested, say so. The human-approval gate is what carries the risk until the fix passes the gate below.

## First 60 minutes

1. **Name the incident lead and the rollback owner.** Each is one role with a deputy, not a committee.
2. **Preserve evidence before you change anything.** Save the traces and the version bundle (prompt, model, tools, config) for the window. Snapshot the prompt diff.
3. **Size the damage.** Pull every refund since the prompt change deployed, not only the 40 you've found. Count the affected customers and the total EUR. Set a time limit, such as 2 hours. Revise the severity from that count.
4. **Stop further loss on the payment side.** Check whether the payments team can still hold or recall the pending refunds.

## Reporting clocks (for counsel and the DPO to confirm)

- **Personal data.** If the wrong refunds went to the wrong people, or exposed personal data, GDPR art. 33 applies. You must notify the authority within 72 hours of becoming aware, if there is a risk to people. The DPO advises and the controller decides. Treat detection time as the start of the clock.
- **Dates.** If you detected this this morning, 10 Nov 2026, the 72 hours run out on 13 Nov 2026 at the same time of day. Put the actual detection timestamp into that calculation.
- **AI Act.** A refund agent is probably not high-risk, so art. 73 likely doesn't apply. Counsel should confirm the classification.
- **Wrong amounts only.** If the problem is wrong amounts to the right customers, with no personal data exposed, this is probably not a GDPR breach. It's still the DPO's call to record, not yours.

## Communications to send today

- **Affected customers** (those who got refunds they shouldn't have, or the wrong amount). Say what happened, what it means for them, and what you'll do. For example: "A refund was processed incorrectly on [date]. You don't need to do anything yet. We'll contact you by [date] about next steps." Don't demand repayment before finance and legal decide the approach.
- **Sponsor and finance.** Send the incident, the count so far, the containment, and when the next update comes.
- **DPO.** Send the facts and the detection timestamp.
- **Customer support.** Give them a holding line, so they don't improvise.

## Before the fix ships (gate 1)

1. **Error analysis on every affected output in the window.** For each one, note what went wrong, the failure mode, whether it's new or known, and the question class.
2. **Regression cases.** Add them to the golden set, and they must fail on the faulty prompt.
3. **Full eval suite.** Compare the fixed version against the previous version on the same cases, with no class below its threshold. A fix checked only on the 40 reported cases is not verified.
4. **Close the loop.** Add the incident, fix and eval delta to the model card changelog. Add a monitoring check for what the alerts missed. Then run the post-incident review.

Closing the incident is a second gate, and it comes after this one.

## What I need from you

- The detection timestamp.
- Whether personal data was involved.
- Who owns rollback.
- Whether the prompt rollback was ever rehearsed.
- The sample size on any quality alert that fired or didn't.

With those I can draft the customer message, the DPO note and the eval cases. I can also write the full playbook document if you want it.