Here's a draft. I've put placeholders in square brackets where I don't have the facts.

---

**Subject: Robustness evidence for [chatbot name]: proposed approach ahead of January go-live**

Hi [name],

You asked for robustness evidence before go-live. I'll attach the vendor's security whitepaper to the file as documentation, but we won't offer it as our evidence. We propose to run our own campaign instead, and I've outlined it below.

**Why the whitepaper can't be our evidence**

The whitepaper reports "99% jailbreak resistance" on the vendor's internal benchmark of 10,000 adversarial prompts. That figure describes a different system from ours:

- It was measured on the vendor's attacks, under the vendor's success criteria and generation settings. We don't know whether those attacks were tuned against.
- It measures generic jailbreaks (getting the model to say forbidden things). Our risks are specific to our integration, and a generic benchmark doesn't cover them.
- It is a single pooled number with no breakdown by attack class and no stated uncertainty.
- Taken at face value, a 1% failure rate means roughly 1 in 100 attack attempts succeeds. We would need to decide whether that is tolerable for the harms below, and nobody has made that decision yet.

We'll still request the full methodology, test conditions and the provider's declared robustness levels, and file them. We'll use them to inform which attacks we write.

**What is specific to our deployment**

The bot reads the customer's last 10 card transactions and can open a dispute ticket. I'd structure testing around these harms:

1. **Cross-customer disclosure.** Getting the bot to reveal another customer's transactions or account data, or more card data than the customer should see.
2. **Misuse of the dispute tool.** Opening disputes on transactions that aren't the user's, or mass or fraudulent disputes.
3. **Indirect injection.** Merchant descriptors and other transaction text are written by third parties and are read by the model. They are an entry point we control nothing about.
4. **Unauthorised commitments.** The bot promising refunds, chargeback outcomes or timelines, or giving credit or regulatory advice it shouldn't.
5. **Policy and system-prompt bypass.** Direct jailbreaks, multi-turn manipulation, and extraction of the system prompt or configuration.
6. **Social engineering.** Impersonation and urgency scripts of the kind real fraudsters use against contact centres.

The disputes tool acts only on the customer's own account, at the customer's request. So I'm treating this as an assistant with user-triggered tools, not an autonomous agent. If a later release adds actions that run without the customer asking, such as automatic refunds or account changes, it needs separate agent-level testing.

**Proposed campaign**

- **Per-class results.** Each class gets its own attack-success rate with a 95% confidence interval, measured against a tolerance signed off before testing. We won't report one pooled number.
- **Success criteria fixed in advance.** For example, a planted canary record appearing in output, or a tool call outside the user's scope in the trace. Code checks are preferred to human or model grading.
- **Sealed held-out attack set.** Kept by a tester independent of the build team. Attacks the vendor or build team have seen go into the regression suite.
- **Mixed testers.** Automated generation to scale known attacks, plus human red-teamers (security plus contact-centre or fraud experts) to find new ones. Each tester's independence is recorded.
- **Sizing.** Zero successes in n attacks still allows a true rate of up to about 4/n. To show a class is below 1%, we need roughly 380 independent attack seeds with no success. For 0.5%, about 765. For the costly classes (cross-customer data and money commitments) I propose a tolerance of [0.5% / to be agreed], with sizing to match.
- **Regression suite.** Every successful attack becomes a regression case, re-run on any model, prompt or tool change from the vendor or us.
- **Residual-risk record.** It covers what was tested, what wasn't, the rates and intervals, open findings, and who accepts the remaining risk. I'd suggest that is a named owner outside the build team.

**What I need from you and others**

1. Your sign-off on the per-class tolerances (or your view on where they should sit).
2. An independent tester, from security or the second line, to hold the sealed set.
3. From the vendor: the full benchmark methodology, a test environment with logging and tool-call traces, model and prompt versioning, and notice of model changes.
4. An estimate of monthly attack attempts, from fraud or contact-centre logs. We should size exposure on that figure, not on the roughly 60,000 monthly conversations.
5. Guidance from counsel or ICT risk on whether this falls under our DORA resilience testing programme, and whether we are the deployer for any applicable AI Act obligations.

**Timeline**

[Dates to be confirmed.] Roughly: criteria and tolerances signed by [date]; attack set built and sealed by [date]; campaign run by [date]; fixes and re-test on fresh attacks by [date]; residual-risk record to you by [date]. If time runs short, a reduced scope is possible. In that case we would report the untested classes and the indicative rates openly, and recommend a restricted launch (for example, a limited rollout or the dispute tool disabled) until the campaign completes.

I can walk you through this whenever suits.

Thanks,
[Name]

---

**Notes for you (not for the email):**

- Procurement's suggestion is the weak point. Model risk asked for robustness evidence, and a vendor's pooled marketing figure doesn't answer that. If the file shows only the whitepaper, I'd expect it to be rejected or to become a finding later.
- The merchant-descriptor injection point is the one I'd lead with in conversation. It's easy to explain and the vendor's benchmark almost certainly doesn't cover it.
- I haven't invented an attack volume or tolerances. Those need real inputs from you and the business before the sizing numbers are final.
- I can turn this into the campaign plan and residual-risk templates once you have the tolerances and the attempts estimate.