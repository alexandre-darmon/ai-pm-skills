**Not yet. Don't close the incident tonight.** You can ship the fix if you want to, but only as a mitigation. The incident stays open until the checks below are done.

**Class and severity (provisional):** wrong output, SEV3 for now. Analysts validate every draft, which limits the harm, but the 3 memos reached the stage where they were reviewed. The severity can't be final until someone counts the affected memos.

**Why testing on the 3 reported memos isn't enough**
- Those 3 are only the ones the alert caught. A fix checked only on the reported examples is not verified.
- Analyst validation is a safety net, not proof that nothing else went out. An analyst who misses a wrong collateral value passes it to the credit committee.
- Nothing yet shows the fix doesn't break other memo types, such as different collateral classes or valuation formats.

**Before shipping tonight**
1. **Size the damage.** Pull every memo drafted since the window opened. That means the date of the last prompt, model or data change, not just last Thursday. Check each collateral value against the source and count the wrong ones. Then see how many of those went past analyst validation to the committee. If any did, tell the committee about those memos and have them corrected.
2. **Preserve evidence.** Save the traces and the version bundle (prompt, model, retrieval or data version) from the window before you change anything.
3. **Error analysis on every affected memo.** For each one, note what went wrong and which failure mode it is. For example: wrong field extracted, stale value, confusing appraisal with market value, currency or unit slips, or a value invented rather than retrieved. Check whether the fix targets that cause.
4. **Add regression cases to the golden set.** Build them from all affected memos, not only the 3. They must fail on the current version and pass on the fixed one.
5. **Run the full eval suite.** Compare the fix against the current version on the same cases. No question class should fall below its threshold. Ask engineering for the sample size behind the alert, so you can tell real drift from noise.
6. **Name the rollback owner and a deputy**, and confirm the rollback has been rehearsed. If it hasn't, record it as untested.

**Contain tonight whatever you decide about the fix.** Consider a stopgap: collateral values must be shown with their source and flagged for mandatory analyst verification against it. If you can't confirm the fix is safe, keep it off and keep the drafting assistant on the stopgap.

**Reporting.** If any memo involved personal data or reached a customer or a regulator, ask your DPO and counsel to check the reporting clocks. Take the detection date as the start. That date is last Thursday, the alert's date, unless the issue was seen earlier. 72 hours from then has already passed under GDPR art. 33, if that article applies. The controller decides whether notification is needed, on the DPO's advice. This is a checklist for them, not a verdict.

**Closing the incident.** Close it only when:
- the affected memos are counted and corrected;
- the regression cases and the full suite pass;
- the changelog records the incident, the fix and the eval results;
- a new monitoring check exists for collateral-value accuracy (the alert missed this until a weekly run);
- the post-incident review (timeline, cause, fix, what monitoring missed) is written.

**Draft message to the first people affected** (analysts and the credit committee, for any memos with wrong values):
> "Between [date] and [date], the drafting assistant produced some memos with incorrect collateral values. We have identified [N] affected memos, listed here. Please re-verify the collateral figures in these against source documents before any decision relies on them. We are deploying a fix and will confirm once all memos are rechecked."

If engineering can show steps 1, 4 and 5 are done tonight, shipping is reasonable. Otherwise ship the stopgap and finish the rest tomorrow.