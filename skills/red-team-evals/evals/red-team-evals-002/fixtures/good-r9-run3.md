I wouldn't tighten that sentence as written. Tightening would make a claim the evidence doesn't support stronger, and the second line will probably pick it apart.

**Problems with the current wording**
- **"Robust" is a verdict.** 0 successes out of 50 still allows a true failure rate of about 6% (rule of three), or about 7% at the Wilson 95% upper bound. That is the bound for the whole test, and the real exposure depends on how many attack attempts you get a month.
- **The prompts come from a public list.** Those are the attacks models and guardrails are most likely already tuned against. They also don't match what this assistant is exposed to.
- **No injection was tested, as far as I can tell.** A public jailbreak list tests direct policy bypass. Your real risks are different:
  - one customer reaching another customer's balances or transfers through the lookup tool;
  - instructions hidden in retrieved product-sheet content;
  - multi-turn manipulation;
  - the assistant giving advice or making commitments it shouldn't.
- **The testers were the developers.** Second line will read that as no independence.
- **No success criterion, settings or versions are recorded.** That means no model or prompt version, no temperature, and no definition of what counted as a "successful attack".

**Suggested wording, true to what you did**

> *Adversarial testing (preliminary).* Before release, two developers ran 50 jailbreak prompts from a public repository [name, date] against the assistant [model and prompt version]. None produced a policy-violating output or unauthorised data access (success criterion: [define]). With 0 successes in 50, the true failure rate on this type of attack could still be up to about 7% (95% upper bound). The test covered direct jailbreaks only. It did not cover indirect prompt injection via retrieved documents, cross-customer data access through the balance and transfer lookup tools, multi-turn attacks, or tool-argument manipulation. Testers were not independent of the build team. This result is not evidence of robustness against targeted attacks. An independent test against a held-out attack set, covering the classes above, is planned for [date/owner]. Residual risk is accepted by [named owner outside the build team].

**What I'd do before Monday**
1. **Test the lookup tool for cross-customer access.** It's the highest-harm path and takes the least effort. Try to get another customer's data through prompts, argument tampering, and a session-ID swap. Better still, confirm that authorisation is enforced in code outside the model. Then the claim rests on architecture rather than on the model resisting attacks.
2. **Run a small indirect-injection test.** Plant a canary instruction in a product sheet and check whether the assistant follows it.
3. **Have someone outside the build team, such as security, run the tests.** Keep their attack set sealed from the developers.
4. **Write down who accepts the residual risk.** It should be a named person outside the build team.

If you can estimate monthly attack attempts from logs, I can work out the exposure. Don't use the 25,000 conversations for that. I can also draft the full campaign plan and residual-risk record from the templates.