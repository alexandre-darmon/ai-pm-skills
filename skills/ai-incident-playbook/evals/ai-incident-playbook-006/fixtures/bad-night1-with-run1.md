**Not yet. Don't close the incident tonight.** Shipping the prompt fix is probably fine if the rollback is quick. Closing the incident on that evidence is not.

**Class and severity (provisional):** Wrong output, SEV3 for now. Analysts caught these 3 memos before the credit committee saw them. That limits the harm, but only for the memos where an analyst actually caught the error. The severity isn't final until the affected outputs are counted.

**Why the evidence isn't enough**
- **The fix was tested only on the 3 reported memos.** That shows it fixes those 3 cases. It doesn't show it hasn't broken something else, or that it fixes the same fault elsewhere. Every other output in the window needs the same check.
- **The 3 memos are probably not the whole count.** Analysts validate every draft, but validation is a human catching errors, not proof that none slipped through. Pull every memo drafted since the window opened (the last prompt or model change, or the last deploy). Have someone check the collateral values in each, not only the reported ones. Count how many were wrong, how many analysts caught, and whether any wrong value reached the credit committee or a decision. If any did, the severity goes up and the incident is much bigger than 3.
- **Quiet errors may exist.** An analyst who is moving fast may approve a plausible but wrong collateral value without noticing it.

**Before shipping, or at least before closing**
1. **Preserve the traces and version bundle** (prompt, model, retrieval or source data) for the window before changing anything. Name the incident lead.
2. **Contain by slice, now.** Until the fix is verified, require analysts to check collateral values against source documents, not only read the draft. Or have the assistant stop stating collateral values and flag them for manual entry. The rest of drafting can continue.
3. **Name one rollback owner and a deputy.** Confirm the prompt rollback has been rehearsed. If it hasn't, call it untested.
4. **Read every affected output** and write an error-analysis note for each. Record what went wrong, the failure mode, and the question class (for example, multiple collaterals, appraisals versus book value, or currency). The cause matters. If it's retrieval or extraction, a prompt fix may be a patch over it.
5. **Add regression cases to the golden set** from those outputs. They must fail on the old version and pass on the new one.
6. **Run the full eval suite** on old and new versions with the same cases. The fix ships when the regression cases pass and no question class falls below its threshold.
7. **Check why the alert only fired weekly.** The weekly alert, not the analysts' validation, surfaced this. Add a collateral-value accuracy check on sampled traffic to monitoring.

**Reporting clocks:** I assumed no personal data is involved, but please confirm. Credit memos usually contain borrower data, though wrong collateral values are an accuracy problem, not a breach. If the alert was detected on Thursday (last Thursday was 2026-11-05), a 72-hour GDPR art. 33 window would end 2026-11-08, so it has already passed if it applied. Counsel and the DPO decide whether it does. If the system counts as high-risk under the AI Act (credit scoring is Annex III), counsel should also say whether this is a "serious incident" under art. 3(49) and whether art. 73(6) restricts altering the system before the authority is informed. I'm not deciding either question. That's for the controller, DPO and counsel.

**What to tell engineering:** Shipping tonight is acceptable only if (a) containment is in place, (b) the rollback owner is named, and (c) the full-suite comparison has run. Closing the incident needs the window count, the regression cases and the changelog entry. If the full eval run can't finish tonight, ship with analyst source-checking on collateral values and keep the incident open.

**Communications, first to the analysts who received the drafts:** "Between [window start] and [date], the drafting assistant stated wrong collateral values in some memos. 3 are confirmed. We are checking all drafts from this period. Until we confirm the fix, check each collateral value against the source document. If you approved or sent any memo containing a collateral value in this period, tell [incident lead] so we can re-check it." Send a second note to the credit committee sponsor once the count is in, covering how many memos were affected and whether any wrong value reached a committee.

Please send me the window dates, the number of memos drafted in it, and whether any reached the committee. I can then update the severity and the plan.