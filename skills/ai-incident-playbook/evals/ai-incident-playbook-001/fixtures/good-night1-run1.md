**Class: wrong action. Severity: SEV2, provisional.** It stays provisional until every refund since the prompt change has been counted. 40 wrong refunds is only what's been found so far.

## Settle the meeting: contain by slice, not on/off

**Drop the agent from L4 to L2 now.** It proposes refunds and a human approves each one. Nobody needs to vote on this. Moving down the autonomy ladder needs no approval, and a named rollback owner (with a deputy) acts immediately.

- **Stops:** autonomous refund execution.
- **Keeps running:** triage, drafting, and customer replies, with refunds going to human validation.
- **If nobody can say which slice is safe,** stop the whole agent and route refunds to the manual queue. Don't let the debate run while it keeps issuing refunds.
- **Rollback:** revert the prompt to the last known-good version. Check whether that rollback has ever been rehearsed. If not, mark it untested and have a human watch the first refunds after it.

## First 60 minutes

1. **Name the incident lead and the rollback owner.** One role each, no committee.
2. **Preserve evidence before any change.** Keep the traces, the prompt versions, and the full version bundle (model, prompt, tools, config) for the window.
3. **Size the damage.** Pull every refund since the prompt change was deployed, not only the 40 reported. Count the customers affected, and split overpayments from refunds that were wrongly denied. Then revise the severity. The money is only part of the harm, because wrongly refused customers also count.
4. **Recover the money.** Finance decides how to reverse or claw back overpayments, and legal decides how. Don't claw back from customers before you've decided how to tell them.

## Reporting clocks (for counsel and the DPO to confirm)

I need the detection time to turn these into dates. Say it was detected at T.

- **GDPR art. 33 (72 hours):** this applies only if personal data was breached. Wrong refunds alone may not be a personal data breach. The DPO should decide and record that decision. For safety, start the clock at detection: the deadline is T + 72h, which is three days after T.
- **AI Act art. 73 / 26(5):** this applies only if the system is high-risk and the incident is "serious" under art. 3(49). A refund agent probably isn't, but counsel should confirm. The 15-day provider limit would be T + 15 days. The deployer duties in art. 26(5) start on 2 December 2027 for Annex III systems.

I'm not deciding whether any notification is required. Counsel and the DPO decide that.

## Communications (drafts)

**Affected customers:**
> We made an error processing your refund on [date]. [You received €X more/less than you were owed.] We are correcting this and will confirm by [date]. You don't need to do anything. Contact [channel] with questions.

**Sponsor and leadership:**
> A prompt change on [date] caused our refund agent to issue wrong refunds. 40 are confirmed, worth about €6,000, and we are counting the full window now. The agent is at L2 with human approval on refunds. Next update at [time].

Also send a short note to the DPO and legal now, and to employee representatives if staff workload or evaluation is affected.

## Before the fix ships

1. **Error analysis on every affected refund in the window.** For each, write what went wrong, the failure mode, whether it's new or known, and which type of refund case it was.
2. **Add regression cases to the golden set** (via `build-evals`) that fail on the faulty prompt.
3. **Ship the fix only when** the regression cases pass and the full eval suite shows no class below its threshold, compared with the previous version on the same cases. A fix checked only on the 40 reported cases isn't verified.
4. **Add a monitoring check.** It was found "yesterday night", so ask why nothing alerted. Add an online eval or guardrail on refund amounts or anomalies, so you aren't relying on uptime or user reports.
5. **Record it** in the model card changelog, then hold a post-incident review covering timeline, cause, fix, and what monitoring missed.

## Process lesson for the review

A prompt change reached an L4 agent without an eval gate that caught this. Prompt changes should be treated as releases, with the golden set run before deploy.

## What I need from you

- The detection time, so I can turn the clocks into dates.
- Whether the system is classified high-risk, and whether personal data was exposed.
- Who owns rollback, and when it was last rehearsed.
- The date of the prompt change, so I can define the window to count.