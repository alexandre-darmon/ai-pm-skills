I wouldn't use that sentence. "Robust against prompt injection and jailbreak attacks" is a conclusion this test can't support, and a second-line reviewer will likely push back on it.

**Why the evidence doesn't carry the claim**
- **Sample size:** 0 successes in 50 still allows a true attack-success rate of about 6% (rule of three), or about 7% at the Wilson 95% upper bound. A persistent attacker would then expect a first success within roughly 14 tries.
- **Wrong prompts:** The prompts came from a public jailbreak list, so they are generic and not tied to your harms. Your real exposure is the lookup tool being pointed at another customer's data. The other exposures are a product sheet carrying planted instructions, multi-turn manipulation, and wrongful promises on rates or cover. None of these were tested.
- **Testers:** The tests were run by the build team. It's unclear whether they were held out from prompt tuning, and public lists are often already in model training and guardrail tuning.
- **Settings and success criterion:** The settings and what counted as a success weren't fixed in advance, and no tolerance was signed.
- **Exposure:** Exposure should be quoted on estimated attack attempts per month, not on 25,000 conversations. Do you have an estimate from logs?

**Suggested wording for the model card and register**

> **Robustness testing (preliminary).** On [date], two developers ran 50 publicly available jailbreak prompts (source: [list name/version]) directly against the assistant ([model and prompt version], [settings]). Success was defined as [criterion]. No attempt succeeded (0/50; Wilson 95% upper bound ≈ 7%). This is a smoke test by the build team and is not evidence of robustness: the sample is small, the prompts are generic and not specific to this assistant's harms, and the testers are not independent of the build team.
>
> **Not yet tested:** use of the balance and transfer lookup to access another customer's data; indirect injection via product sheets or lookup results; multi-turn attacks; misleading statements on products, rates or cover; disclosure of the system prompt.
>
> **Planned before [date/next release]:** a campaign by an independent tester, with success criteria and tolerances set in advance per attack class, and results reported per class with intervals against a held-out attack set. Any successful attack is added to the regression suite.
>
> **Residual risk owner:** [named person outside the build team].

**Before Monday**
- **Cheapest improvement:** A short targeted check of the lookup tool is more valuable than more public jailbreaks. Try cross-customer requests, injected account identifiers, and a planted instruction in a product sheet. Check these with code, for example a canary string or a trace query on the tool call, so the result is binary.
- **Per-class table:** If you want, send me the harm list and the tolerances you'd accept per harm. I'll size the number of attacks needed per class and draft the campaign plan and the residual-risk record.
- **Wording for Monday:** The suggested text above is accurate for the release. Whether the register entry reads "preliminary" or not is a decision for your model risk or AI governance owner.