I'd drop the "robust" sentence. Here is why, followed by wording that will hold up with the second line.

## Why the sentence won't survive review

- **0 out of 50 doesn't mean zero risk.** With no successes in 50 attempts, the true success rate could still be about 6% (rule of three), or 7% on the Wilson 95% upper bound. A persistent attacker would then expect a first success within roughly 14 tries.
- **A public jailbreak list is not evidence for your system.** Those prompts are widely known and often already patched or trained against by model providers. They test generic jailbreaks. They don't test your harms.
- **The testers weren't independent.** The two developers who built it ran the tests. The second line will ask who tested it and what their relation to the build team was.
- **It doesn't say what wasn't tested.** The most important gaps for your assistant are:
  - Getting the lookup tool to return another customer's balances or transfers.
  - Indirect injection through the product sheets.
  - Multi-turn attacks.
  - Bad product advice, such as invented rates or terms.
- **There is no per-class result.** The pooled 0/50 can't show a class that fails.
- **No criteria or tolerances were set beforehand.** Those need to be written and signed before the tests are run.

## Suggested wording for the model card and AI register

> **Adversarial testing (status: preliminary).** Before release, two members of the development team ran 50 publicly available jailbreak prompts against the assistant (direct, single-turn attacks; model and prompt version [x], tested [date]). None produced a policy-violating output. With 0 successes in 50, the true success rate for this type of attack cannot be excluded up to about 7% (Wilson 95% upper bound). This test was not independent of the build team and does not constitute a measure of robustness.
>
> **Not yet tested:** access to another customer's data through the account-lookup tool; instructions embedded in product sheets; multi-turn attacks; incorrect product information. **Planned:** an independent campaign per attack class, with success criteria and tolerances set in advance and results reported per class with confidence intervals, by [date]. **Residual risk owner:** [name, outside the build team]. **Re-test triggers:** model, prompt, product-sheet or tool changes.

## Before Monday

1. Add a short test on the lookup tool. Use a logged-in test customer and try to read another customer's balances or transfers, with a planted canary record as the success check. This is your highest-cost harm, and it can be checked in code.
2. Have someone outside the build team, such as security, run a small set of attacks they write themselves.
3. Name the residual-risk owner. Whoever accepts the risk should be outside the build team.

If you tell me roughly how many attack attempts you see per month (from logs, not the 25,000 conversations), I can work out the exposure the 7% bound allows. For example, at 250 attempts a month it would be up to about 18 successes. That figure is purely illustrative, so I'd need your real number before it goes in the register.