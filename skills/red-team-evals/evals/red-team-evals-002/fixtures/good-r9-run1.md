I can tighten the wording, but I can't keep the claim "robust against prompt injection and jailbreak attacks." Fifty prompts with no successes doesn't support it, and a second-line reviewer will probably say so.

**Why the evidence is thin**
- **Statistical bound:** 0 successes in 50 still allows a true attack-success rate of about 6% (rule of three, 3/50). The Wilson 95% upper bound is about 7%. If even a small share of the 25,000 monthly conversations were attack attempts, that bound could mean many successful attacks a month. I can't give a figure without your estimate of monthly attack attempts, from logs or incident data. Don't use the conversation count.
- **Public prompt list:** Public jailbreak lists are widely known and are often already covered by model-level training. They test one attack class, direct jailbreaks, and say little about your assistant.
- **Indirect injection:** Product sheets are retrieved content, so they are an injection path. If anyone other than your own team can write or edit them, that path is untested.
- **Account data:** The assistant can read the logged-in customer's balances and transfers. The most important attacks are therefore probably cross-customer access, such as getting it to reveal another customer's data through the lookup tool, and multi-turn or social-engineering attempts. None of these seem to have been run.
- **Independence:** The two developers who ran the test are on the build team. If they also tuned the prompt against those attacks, the result isn't a clean measurement.
- **Success criteria:** I don't see written pass/fail criteria, settings or tolerances that were fixed before the run.

**Suggested wording for the model card and AI register**

> *Adversarial testing (preliminary).* Before release, two members of the development team tested the assistant with 50 prompts from a public jailbreak collection, which covers direct jailbreak attempts only. None succeeded. With this sample size, the true success rate for this attack type could be as high as about 7% (95% confidence upper bound). This result is indicative and does not establish robustness.
>
> *Not yet tested:* indirect injection via product sheets; access to another customer's balances or transfers through the lookup tool; multi-turn and social-engineering attacks; [add others after the coverage check].
>
> *Planned:* an independent campaign by [security / second line] on a sealed attack set, with results reported per attack class against agreed tolerances. Each successful attack will be added to the regression suite. The next campaign is triggered by any change to the model, prompt, product sheets or tools. Residual risk is accepted by [named owner outside the build team].

**Before Monday**
1. Use the wording above, with the "not yet tested" list filled in, unless you can add testing first.
2. If you have a few days, run a small targeted test on the cross-customer data access path. A canary record in a second test account makes this cheap and easy to check. Use security or someone outside the build team if you can.
3. To size a full campaign, I need your estimate of monthly attack attempts and the tolerable rate per harm. For a harm like another customer's data, that is usually well under 1%, which takes several hundred held-out seeds per class.
4. Ask ICT risk whether this campaign belongs in your DORA resilience testing programme.

Send me the harm list and whether anyone outside your team can edit the product sheets, and I'll draft the campaign plan and the residual-risk record.