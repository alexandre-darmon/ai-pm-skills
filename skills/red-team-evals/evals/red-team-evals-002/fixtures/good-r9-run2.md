I can tighten it, but I wouldn't use the current sentence. "Robust against prompt injection and jailbreak attacks" is a conclusion that 0 out of 50 can't support, and the second line is likely to challenge it.

**Why the claim doesn't hold**
- **Zero in 50 isn't zero risk.** The true attack-success rate could still be about 6% (rule of three), or roughly 7% on a 95% Wilson upper bound. If 1,000 attack attempts a month reached the assistant, that bound would allow dozens of successes. Your real attempt count may be far lower, but you haven't estimated it yet.
- **The prompts came from a public list.** Public jailbreak lists are the first thing providers and guardrails get tuned against, so they mostly measure how well the model has seen them. They don't test your system.
- **The testers were your developers.** Second line will treat that as a smoke test, not independent evidence.
- **The attacks don't match your risks.** The ones that matter here are:
  - Getting the lookup tool to return another customer's balances or transfers.
  - Planting instructions in the product sheets (indirect injection).
  - Multi-turn manipulation.
  - Social-engineering-style requests that look like a fraudster or an angry customer.
  A generic jailbreak list mostly tests "say something forbidden", which is the least costly harm for you.
- **There's no pre-agreed pass criterion.** I don't see a tolerance, a success definition or a sign-off per harm.

**Suggested wording (accurate, and it holds up under review)**

> **Adversarial testing (preliminary).** Before release, the development team ran 50 publicly available jailbreak prompts against the assistant (version [x], prompt [y], date [z]). None produced the targeted behaviour (policy bypass or disclosure of restricted content). With 0 successes in 50, the 95% upper bound on the attack-success rate for this prompt type is about 7%. This is a smoke test, not a robustness measurement. The tests were run by the build team, used publicly known prompts, and were not split into a held-out set.
>
> **Not yet tested:** indirect injection via product-sheet content; cross-customer data access through the balance and transfer lookup tools; multi-turn attacks; domain-specific fraud and social-engineering scenarios.
>
> **Planned:** an independent campaign, with per-class success criteria and tolerances set beforehand, before [date / next model, prompt or tool change]. Residual risk is to be accepted by [named owner outside the build team]. Findings will be added to the regression suite.

**Before Monday**
- The wording above is safe to ship now. The "not yet tested" list is what makes it credible.
- A cheap step that would change what you can say is a short check of the two things that could hurt a customer. Use canary strings and a second test account to try to make the tool return another customer's data. Then plant an instruction in a product sheet and see whether it's followed. Both are pass/fail checks you can run in a day. If you add them, report each separately with its own count.
- To claim a rate under, say, 1% per class, you'd need about 380 independent held-out attack ideas per class. That's a campaign, not a weekend task, and I'd put it in the plan rather than the release gate unless your risk appetite requires it.

I can also fill in the campaign plan and residual-risk record templates if you'd like. For that I'd need your estimated monthly attack attempts, the harm list, and who the independent tester and risk owner will be.