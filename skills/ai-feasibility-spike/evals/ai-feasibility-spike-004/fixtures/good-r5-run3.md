I can't write this as a go note, because the numbers don't support "both meet the bar". I've drafted the note below as a recommendation to reshape the registry side.

**Why the bar isn't met**

"Meets the bar" means the Wilson 95% lower bound is at or above 90%, not just the point estimate. I worked these out by hand and haven't run `spike_readout.py`.

| Document type | Result | 95% interval | Reading against the 90% bar and 75% line |
|---|---|---|---|
| Passports | 28/30 (93%) | about 79–98% | **Promising.** The point is above the bar, the lower bound is below 90% but above 75%. Plausible, not demonstrated. |
| Registry extracts | 9/10 (90%) | about 60–98% | **Undecided.** The interval straddles the 75% line. 9 of 10 fits a true rate near 60%. |

The registry sample was too small to ever pass. With 10 cases, even 10/10 has a lower bound of about 72%, below the 75% line. Passing a 75% line with one error allowed needs about 19 cases, and passing it with no error needs 12. This is a sizing gap in the spike design, not a failure of the model.

Cost is fine. At 0.03 EUR per document, cost per correct answer is about 0.032 EUR for passports and 0.033 EUR for registry extracts.

**Draft note for Thursday's steering committee**

> **Decision requested: Reshape. Proceed on passports, extend the registry test, no PRD sign-off yet.**
>
> **Question:** can the approved model extract all fields from director passports and company registry extracts at the signed bar (90% per document type, all fields correct; 75% drop line)?
>
> **Results (anonymised test-environment documents):**
> - Passports: 28/30 correct. Promising, not demonstrated. The 95% interval is about 79–98%.
> - Registry extracts: 9/10 correct. Undecided. The interval is about 60–98%, and 10 cases cannot distinguish 90% from below the drop line.
> - Cost: about 0.03 EUR per document, about 0.032 EUR per correct answer, well under the ceiling.
>
> **Neither type is below the 75% drop line, so the idea is not dead.** Neither has demonstrated the 90% bar.
>
> **Recommendation:**
> 1. Run a second short spike on registry extracts only, with at least 20 cases and a new appetite and kill date signed by the head of onboarding.
> 2. Passports can go into the PRD as "promising, not demonstrated". Sizing the passport eval to demonstrate 90% is for the evaluation phase. It needs roughly 70 or more cases at an expected 95%.
> 3. These figures are spike results, not release evidence. They must not be quoted as the system's accuracy.
>
> **Open items before the PRD:** the 2 passport misses and the 1 registry miss need a failure analysis, to check whether they cluster on a field or a document format.

**Gaps to close before Thursday**

- **Appetite and kill date:** you gave me the bar and the stop line, but not a signed time box, a cost ceiling in EUR, or a kill date. Please confirm those existed.
- **Tool and data check:** I can't tell whether the model account and tooling were authorised and registered with IT risk. The anonymisation of the documents should also be confirmed with the DPO.
- **Lethal-trifecta check:** these are private identity documents and untrusted uploads. Please confirm the prototype has no outbound channel.
- **Hours spent:** these should come from the logs.

If the committee wants a faster path, the alternative is a signed, dated lowering of the registry bar. That would only count as a decision, not as a result.