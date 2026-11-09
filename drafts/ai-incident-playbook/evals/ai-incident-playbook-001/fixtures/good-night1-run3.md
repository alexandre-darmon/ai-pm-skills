**Class: wrong action. Severity: SEV2, provisional until the count is in.** About €6,000 across 40 refunds is a small loss. But money went out through an autonomous agent, and the prompt change that caused it may still be live. The count in step 2 below sets the final severity.

## Decision on the meeting: contain by slice, don't argue on/off

**Drop the agent from L4 to L2 now.** Refunds go back to human approval, and the agent only drafts them. Per the autonomy ladder, moving down needs no vote. If nobody can name a slice that is safe, such as small amounts in a category the bad prompt never touched, stop the agent entirely. Do not leave the faulty version issuing refunds while the team debates.

**Rollback owner:** one named role plus a deputy, for example the head of support ops with the agent's tech lead as deputy. They act now and the meeting doesn't vote. Revert the prompt to the last version that was known to be good. Check whether that rollback was ever rehearsed. If it wasn't, record it as untested.

## First 60 minutes

1. **Preserve first.** Save the traces and the full version bundle (prompt, model, tools, config) for the window before anything changes. Name the incident lead.
2. **Size the damage.** Pull every refund since the prompt change shipped, not just the 40 found. Check each one against policy and count the affected customers. Anything found beyond the 40 raises the severity.
3. **Fix what already went out.** Decide whether each wrong refund is recovered, written off, or corrected. Over-refunds and under-refunds are both customer-facing errors. A customer who was wrongly refused needs the same attention as one who was overpaid.

## Reporting clocks (for counsel and the DPO to confirm)

- **GDPR art. 33 (72 hours):** this applies only if personal data was exposed or mishandled, for example refunds sent to wrong accounts or payment details leaked. If so, the 72 hours run from detection. Take the detection time as the start. Say "detected yesterday night" and compute the exact deadline from that timestamp. If it was around 23:00 on 2026-11-08, the limit is 23:00 on 2026-11-11. The controller decides on notification, on the DPO's advice, and records the decision. I can't decide that for you.
- **AI Act art. 73 (15 days in general):** this is relevant only if counsel classes the refund agent as a high-risk system and this as a serious incident. Refunds of this size probably don't qualify, but counsel should confirm that and record the answer.

## Communications to send today

- **Affected customers (first):** "Your refund of [amount] on [date] was processed in error by our automated system. Here is what it means for you [kept, corrected, or reissued]. A person will review your case, and you can reach [contact]."
- **Sponsor/finance:** 40 wrong refunds, about €6,000, cause identified as the prompt change, contained at [time] by dropping to L2, full count to follow by [time].
- **DPO:** the facts above, plus whether personal data was involved.
- **Support team:** refunds are now manual, and here is the approval path.

## Before the fix ships

- Write an error-analysis note on each affected output. Say what went wrong, which failure mode it is, and whether it is new or known.
- Add regression cases from those outputs to the golden set. They must fail on the faulty prompt.
- Ship the fix only when those cases pass and the full suite shows no class below its threshold, compared with the previous version. Checking only the reported examples doesn't count as verification.
- Then return the agent to L4 in stages, for example small amounts first. Record the incident, the fix and the eval delta in the card's changelog.
- **Post-incident review:** timeline, cause, fix, and why monitoring missed this. If no alert fired and a person found it the next day, add a refund-correctness check to online evals.

## What to say in the meeting

"We are not choosing between on and off. Refunds go to human approval from now. The prompt reverts to the last good version. We count every refund since the change, and the agent returns to L4 only after the regression cases pass."

If you give me the detection time, the refund volume since the change, and whether personal data was involved, I can compute the exact dates and tighten the severity.