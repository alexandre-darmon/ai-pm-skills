**Not tonight, at least not as "fix verified, incident closed."** A fix tested only on the 3 reported memos isn't verified. Shipping it and closing the incident are two separate gates, and the first one hasn't passed.

**Class and severity (provisional):** wrong output, in this case wrong collateral values. I'd put it at SEV3 for now. Analysts validate every draft, which limits the harm and keeps it reversible. The severity isn't final until the affected outputs are counted.

**Before the fix ships**
1. **Count the damage.** Pull every memo drafted since the window opened (the last prompt, model or deploy change), not just the 3 that were reported. Check each one's collateral values against source. Also find out whether any wrong draft got past the analysts to the credit committee. Revise the severity from that count. Fixing the prompt doesn't correct memos that already went out.
2. **Preserve evidence first.** Save the traces and the version bundle (prompt, model, retrieval data) for the window before anything changes.
3. **Do error analysis on every affected memo.** Record what went wrong in each, the failure mode (for example a misread table, a stale value, or a wrong unit or currency), whether it's new or known, and which question class it belongs to.
4. **Add regression cases to the golden set.** They must fail on the current prompt and pass on the fix.
5. **Run the full suite on both versions.** Run the old and new prompts on the same cases. The fix ships only if the regression cases pass and no class falls below its threshold. Prompt fixes often shift behavior elsewhere, such as other fields or other memo types.

**Containment until the gate passes:** the analyst validation is your current control. Add a specific check on collateral values, such as a mandatory source tie-out, so a long run of clean memos doesn't dull the review. Don't treat the fix as the mitigation.

**Ownership:** name an incident lead. Name one rollback owner with a deputy, and confirm the prompt change can be rolled back and when that was last rehearsed. If it has never been rehearsed, record it as untested.

**Reporting clocks:** this looks like a quality incident and not a personal-data breach or an AI Act serious incident. Ask your DPO and counsel to confirm that, and record the decision. If it does count, the GDPR 72-hour clock would have started on detection. I don't have the detection date, so I can't compute the date yet. Last Thursday's alert is the prudent start, which makes the limit last Sunday, and that has already passed. Send me the exact detection time and I'll compute it.

**Also needed**
- Check the alert against its noise. On n sampled traces the control limits are p̄ ± 3√(p̄(1−p̄)/n). What was n?
- Add a new monitoring check on collateral-value accuracy. Analyst review caught this, not your monitoring, so it's a missed alert.
- Log the incident, the fix and the eval delta in the model card changelog, then hold a post-incident review.

**Draft message to analysts and the credit committee:** "Our drafting assistant produced incorrect collateral values in at least 3 memos. We're checking all drafts since [date] and will tell you which are affected. Until further notice, please verify collateral values against source documents before sign-off. A fix is in testing and will be released once it passes the full evaluation."

If the counted set is small and the regression and full-suite checks pass, you can ship the fix within a day or two. Close the incident only after that and the post-incident review.