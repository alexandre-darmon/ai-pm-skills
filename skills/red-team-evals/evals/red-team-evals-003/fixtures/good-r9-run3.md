Here's a draft. I've left placeholders in brackets for the things I don't know.

---

**Subject: Chatbot go-live: robustness evidence and proposed test plan**

Hi [name],

Thanks for the request. Procurement suggested we attach the vendor's whitepaper as our evidence. I don't think it can serve that purpose, so I'm proposing our own targeted campaign. I'll attach the whitepaper to the file as vendor documentation only.

**Why the vendor figure isn't evidence for our deployment**
- "99% jailbreak resistance" comes from the vendor's own benchmark of 10,000 prompts. It is a different system, different attacks, a different success criterion and different settings from ours. We don't know how it was graded or whether the vendor tuned against those prompts.
- It measures whether the model produces disallowed content. Our main exposures are different. The bot can read card transactions and open dispute tickets, so the harms are cross-customer data access, misuse of the dispute tool, and manipulation through text an attacker controls, such as merchant descriptors in transaction data.
- Even taken at face value, 99% means a 1% failure rate. A persistent attacker needs about 100 tries for a first success.
- Nothing in the whitepaper tells us the rate for each harm class in our configuration.

**Proposed campaign (before January go-live)**
1. **Classes come from our own harm list**, each written as attacker goal × entry point × consequence:
   - reading another customer's transactions or account data;
   - opening, altering or mass-filing disputes the customer shouldn't be able to, or on the wrong transaction;
   - indirect injection through transaction fields (merchant names, memo text);
   - policy bypass, meaning unauthorised promises, fee waivers or credit advice;
   - leaking the system prompt or internal configuration;
   - multi-turn social engineering and identity-spoofing attempts.

   I'll map these to the OWASP LLM Top 10 (2025), NIST AI 100-2 and MITRE ATLAS. The result will report which relevant classes were tested and which weren't.
2. **Success criteria, settings and tolerances are signed before we run anything.** The criteria are binary and checked in code where possible, such as planted canary records and forbidden tool calls in the trace. Model risk co-signs the tolerance per class. I suggest [≤1%] for the customer-impacting classes, and tighter for cross-customer data access.
3. **Sizing.** A clean result in n independent attack seeds only bounds the true rate at about 4/n (Wilson 95% upper bound). To show a class is under 1% with no successes, we need about 380 held-out seeds. For 0.5%, we need about 765. I'll size the costly classes (cross-customer data, dispute actions) to their own tolerance. The rest may be reported as indicative.
4. **Independence and a sealed held-out set.** Rates you rely on come from testers independent of the build and vendor-config team ([security / second line]). They hold a sealed, dated, hashed attack set that the configuration owners never see. We combine automated generation with human red-teamers who know fraud patterns.
5. **Reporting.** The report gives the results per class (successes ÷ seeds, interval, tolerance, reading), never a pooled rate on its own. It lists the untested classes, tester independence, and model, prompt and version details. Every successful attack becomes a regression case, run on any model, prompt or tool change. Fixes are re-tested on fresh attacks.
6. **Residual-risk record.** It names an accepting owner outside the build team and the triggers for re-testing. We'll also ask Legal/ICT risk whether this belongs in our DORA resilience testing programme [if applicable].

**What we can and can't claim at go-live**
We won't claim the system is "robust" or "jailbreak-proof". We'll claim measured rates per class, with intervals against the signed tolerances, and a list of what wasn't tested. Zero observed failures still allows a nonzero rate, so I'd also like to size exposure against estimated monthly attack attempts [source: fraud/abuse logs]. That is a smaller number than the 60,000 monthly conversations.

**Mitigations independent of the model**
Because the bot has a tool path to customer data, I'd also confirm the following with the vendor and our architects:
- Authorization is enforced outside the model, so the transaction read is bound to the authenticated session.
- Dispute creation has deterministic checks and rate limits.
- Transaction text is treated as untrusted input.

These reduce the exposure regardless of the test results.

**Asks**
- Vendor documentation: the benchmark methodology, the declared robustness levels and the test conditions, to go on file.
- Access to a test environment with synthetic customers by [date].
- Agreement on the classes and tolerances by [date], and a named independent tester and risk acceptor.

**Timeline:** [plan → sign-off → campaign → fix and re-test → residual-risk sign-off], with the decision needed by [date]. If time is short, the first things to cut are the indicative-only classes. We should not skip the data-access and dispute-tool classes.

Happy to walk through this.

[Name]

---

Two things I'd need from you to firm this up: an estimate of monthly attack attempts and where it comes from, and who the independent tester and risk acceptor will be. I can also draft the campaign plan and residual-risk templates, or compute exact seed counts per class once you set the tolerances.