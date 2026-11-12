**Not as proposed. Shipping the fix tonight is fine only if the checks below pass first, and the incident shouldn't close tonight.**

**Class and severity (provisional):** wrong output, SEV2 for now. The wrong collateral values are material to credit decisions, but analysts validate every draft, so the harm may not have reached the committee. Severity is not final until the affected memos are counted. We know 3 were flagged, not how many were wrong.

**Why testing on the 3 memos isn't enough**
A fix checked only on the reported examples is not verified. Before it ships:
1. **Count the damage.** Pull every memo drafted since the window opened (the prompt, model or data change that introduced the fault, or at least the last 30 days). Check each one's collateral value against source. Find out whether any wrong memo got past the analysts and reached the committee. If one did, that decision needs revisiting. The fix doesn't change what already went out.
2. **Read each wrong output** (the `error-analysis` step). Record what went wrong, the failure mode (wrong field extracted, stale value, mixing up appraisal and book value, and so on) and whether it's new or known. The cause may be wider than the 3 cases.
3. **Add regression cases** to the golden set via `build-evals`, built from those outputs. They must fail on the current version and pass on the fix.
4. **Run the full eval suite.** Compare the fix against the previous version on the same cases. No question class may fall below its threshold. Prompt fixes often trade one error for another.
5. **Preserve traces and the version bundle** from the window before changing anything.

**Check the alert too.** Get the sample size n behind the alert and check it against the control limits, p̄ ± 3√(p̄(1−p̄)/n). I'd treat 3 confirmed errors as real, because they were confirmed by analysts. But the rate matters for sizing.

**Containment until the fix is verified**
Analysts already validate every draft. For now, explicitly require that they check collateral values against source documents, not only read for plausibility. Tell them where the errors were found. That is the slice to tighten, and nothing else needs to stop.

**Owners**
- Name one rollback owner and a deputy. When was the rollback last rehearsed? If it never was, mark it untested.
- Name an incident lead.

**Reporting clocks (for counsel and the DPO to confirm)**
- Detection was last Thursday. I don't know the exact date, so I can't compute dates. Send me the detection timestamp and I'll compute them.
- GDPR art. 33 (72 hours from awareness) applies only if personal data was breached. Wrong collateral values aren't obviously a personal data breach, but the DPO should confirm.
- The AI Act serious-incident rules (art. 73) depend on whether this is a high-risk system. Credit scoring of individuals is Annex III. A drafting assistant may or may not fall under it. Ask counsel. If it does, ask counsel before altering the system whether the authority must be informed first (art. 73(6)).

**Communications**
- **To the analysts and credit committee (first, since they received the wrong outputs):** "The drafting assistant stated incorrect collateral values in at least 3 memos. We are checking all memos since [date]. Until we confirm the fix, check every collateral figure against source. We will list any affected memo by [time]."
- **To the sponsor and the DPO:** the same facts, plus the count when we have it and whether any wrong memo reached the committee.

**What to do tonight**
- Do steps 1–5 above. If the full suite passes and the count shows no wrong memo reached the committee, ship the fix tonight.
- If the count isn't ready, hold the fix. The analyst check is the stopgap.
- Keep the incident open until the post-incident review: timeline, cause, fix, what monitoring missed. The changelog entry goes in the model card. Also add a monitoring check on collateral accuracy, because the weekly alert caught this late.

Tell me the sample size, the window start date and the detection time, and I'll draft the counts and the deadline dates.