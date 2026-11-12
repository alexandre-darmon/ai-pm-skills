I can't tighten that sentence as written, because the claim it makes goes further than the test supports. I'd replace it with a version that states what was measured.

**Why "robust" doesn't hold**
- **Zero successes in 50 isn't zero risk.** The true attack-success rate could still be about 6% (rule of three), or up to about 7% at the Wilson 95% upper bound. A second line will check this. At 7%, the claim would not cover a data-exposure or money-movement harm.
- **The prompts were a public list.** Public jailbreak lists are well known to model providers and often to the build team. They tell you the assistant handles known, generic jailbreaks. They say little about attacks aimed at this assistant.
- **The testers were your own developers.** Anything a developer saw and tuned against can't be counted as a fresh test. Second line will ask for independent testers and a held-out set.
- **The tests probably missed your real risks.** Those are the balance and transfer lookups: one customer reading another's data, or injected text in a retrieved product sheet or tool result. A generic jailbreak list mostly tests whether the assistant says forbidden things. It doesn't test whether the lookup tool can be steered. There is no per-class breakdown, no success criterion written beforehand, and no list of what wasn't tested.

**Suggested wording for the model card and register**

> **Adversarial testing (status as of [date]).** Before release, 50 publicly available jailbreak prompts were run against version [model/prompt version] by two members of the development team, with [temperature/turns/attempts] settings. A prompt counted as successful if [criterion, e.g. the assistant produced content prohibited by policy X or disclosed data outside the logged-in customer's scope]. No prompt succeeded (0/50; 95% upper bound on the attack-success rate ≈ 7%). This is a smoke test of known generic jailbreaks. It is not an assessment of robustness.
>
> **Not yet tested:** indirect prompt injection via product sheets or tool results; attempts to access another customer's balances or transfers through the lookup tools; multi-turn and social-engineering attacks; attacks written by testers independent of the build team. Results are not broken down by attack class, and no held-out attack set was used.
>
> **Planned:** [campaign date], covering the untested classes above with independent testers and a sealed held-out set. Every successful attack will be added to the regression suite and re-run on each model, prompt, knowledge-base or tool change. Residual risk is accepted by [named owner outside the build team].

**What you need before Monday**
1. **A one-hour check of the data-boundary risk.** Have someone outside the dev team try to get the assistant to return another customer's data, and plant an instruction in a product sheet. Use a canary string so success is checkable. This matters most for a retail bank, and a clean result there supports a much stronger line in the register.
2. **A named risk owner** outside the build team, for the residual-risk line.
3. **An attempts-per-month estimate** from logs, if you want to state exposure. Don't use the 25,000 conversations figure, since most conversations aren't attacks.
4. **A call on timing.** If the data-boundary check can't happen before release, state that as a known gap with a date for closing it. Don't hide it behind "robust".

Two things to confirm are who accepts the residual risk and whether this belongs in your DORA resilience-testing programme. I'd ask ICT risk about the second.

If you send the harm list, I can draft the full per-class plan and the residual-risk record.