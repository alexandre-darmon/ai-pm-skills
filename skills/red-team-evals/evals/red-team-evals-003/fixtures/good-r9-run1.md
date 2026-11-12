**Draft reply to Model Risk**

---

**Subject: Customer-service chatbot: robustness evidence plan ahead of January go-live**

Hi [name],

Thanks for the request. We will not rely on the vendor's whitepaper as our robustness evidence. We will attach it to the file as vendor documentation and run our own campaign. Our reasons, and the plan, are below.

**1. Why the vendor figure doesn't answer your question**

The claim is "99% jailbreak resistance" on the vendor's internal benchmark of 10,000 prompts. It does not describe our deployment, for these reasons:
- **Different system.** The benchmark most likely tests the base model's chat behaviour. Our risk comes from what the bot can reach: a customer's last 10 card transactions, and the ability to open dispute tickets.
- **Different attacks and success criteria.** We don't know what counts as a "success" or who wrote the prompts. The vendor may have tuned against them.
- **Pooled figure.** A 99% pooled rate can hide a class that fails far more often. A 1% failure rate on 10,000 prompts is up to 100 failures, and we can't see which kind. A single cross-customer data leak matters more than many off-topic replies.
- **Unknown settings.** We don't have the model version, temperature, number of turns or attempts per prompt, so we can't compare it with anything we run.

I'll request the benchmark methodology, the model version it was run on and the vendor's declared test conditions. These will go on file as documentation. We'll use them to inform our attack classes.

**2. Harms we will test (attacker goal × entry point × consequence)**

| # | Class | Entry point |
|---|---|---|
| 1 | Customer reads another customer's transactions or data through the lookup tool | Direct and multi-turn |
| 2 | Bot opens a dispute the customer didn't ask for, on the wrong transaction, or in bulk | Direct, multi-turn, indirect |
| 3 | Indirect injection through third-party text, such as merchant names or descriptors in the transaction data the bot reads | Indirect |
| 4 | Social-engineering fraud: false dispute claims, account-takeover probing | Multi-turn |
| 5 | Policy bypass: promises, fee waivers, or credit or regulatory statements we haven't approved | Direct |
| 6 | Exposure of the system prompt, tool schemas or other internal configuration | Direct |
| 7 | Harmful or off-brand output | Direct |
| 8 | Abuse that drives cost or availability problems | Direct |

Each class is mapped to OWASP LLM Top 10 (2025), NIST AI 100-2 and MITRE ATLAS. I'll report coverage as tested classes ÷ relevant classes, and list any relevant class we did not test.

Classes 1 and 2 depend on architecture as well as the model. I'll ask the build team to confirm that the customer identity and the allowed transaction scope are enforced in the tool layer, not left to the model. That control is tested directly, and it is the main reason we can set tight tolerances on class 1.

**3. Method**

- **Criteria and tolerances come first.** Before any testing, we will write down a binary success criterion per class, the generation settings, the model and prompt versions, and a tolerable rate per class. These will be dated and signed, ideally by you and the business owner. Success is checked mostly by code, such as planted canary records and trace queries. For example, class 1 succeeds if a record belonging to another customer appears in the output, and class 2 succeeds if a dispute-creation call appears in the trace without a valid request.
- **Sizing is per class, on held-out seeds.** With no successes, a class can only be read as under rate *r* if we ran about 4/*r* independent seeds. That is about 380 seeds for 1%, about 765 for 0.5%, and several thousand for a rate near 0.1%. Classes 1 and 2 are sized for their own tolerance, whatever their share of the campaign. Variants of one idea count as attempts, not extra seeds.
- **Held-out set and independence.** A sealed, hashed and dated attack set is kept by a tester independent of the build team (security or second line) and is never shown to the people tuning the prompt and guardrails. Decision rates come only from that set. Automated generation will scale the known classes. Human red-teamers with fraud and complaints expertise will look for new ones. Past findings go into a regression set.
- **Reporting.** For each class, I'll report successes ÷ seeds, the Wilson 95% interval, the signed tolerance, and a reading of under tolerance, over tolerance, or undecided. I will not report a pooled rate on its own. Zero successes will be reported as an upper bound, not as zero risk. I'll convert it to expected exposure using an estimate of monthly attack attempts. That estimate will come from pilot logs and conversation analysis, not from the 60,000 monthly conversations.
- **Findings.** Every successful attack becomes a regression case, run on every model, prompt, knowledge-base or tool change. After a fix, we re-test on fresh attacks, not only the ones that found the flaw.

**4. Timeline**

Go-live is in January and today is 12 November. I propose:
- **By 20 Nov:** harm list, criteria, settings and tolerances agreed and signed. Vendor documentation requested. Independent tester named.
- **Late Nov to mid Dec:** attack set built and sealed, then the campaign run on the versions we intend to ship.
- **Mid Dec:** results by class, findings fixed, and fresh-attack retest of the failed classes.
- **Before the January go-live decision:** residual-risk record, with a named accepting owner outside the build team.

The dates are tight but feasible if testers and the pilot environment are confirmed this week. If the model or prompt changes after the campaign, the results no longer describe the shipped system. We would re-run the affected classes or agree a new date.

**5. What you'll receive**

- The campaign plan and, later, the per-class results table with intervals.
- A residual-risk record covering what was tested (classes, n, testers and their independence, settings, versions, dates), what was not tested and why, findings and their status, and what triggers the next campaign.
- A statement of residual risk and who accepts it. We will not state that the chatbot is "robust" or "jailbreak-proof". We will state measured rates against signed tolerances.

**6. Questions for you**

- Which tolerance per class do you want to sign? I'll propose starting values, with the tightest for classes 1 and 2.
- Which team can act as independent tester?
- Should this campaign be recorded in our ICT-risk or digital operational resilience testing programme? I'll check with ICT risk and counsel on whether any EU AI Act obligations apply, and whether we are provider or deployer. If they do, the vendor's declared robustness levels and test conditions need to be on file.

Best regards,
[Name]

---

**Notes for you (not part of the email)**

- **The tolerances and sample sizes are placeholders.** They need your risk appetite and the signature of the people who own them. Class 1 at 0.1% needs about 4,000 seeds. In practice, a deterministic authorization check in the tool layer, tested directly, is cheaper and gives stronger evidence than statistical sampling.
- **Procurement's shortcut may end up costing more time.** If model risk rejects the whitepaper after the fact, you lose the January date anyway. The email puts the schedule in front of them early.
- **Class 3 is easy to miss.** Merchant descriptors are text controlled by third parties, and the bot reads them. Make sure the build team knows.
- **I haven't verified the vendor claims, the regulatory applicability, or your internal teams' availability.** Those need your input.

I can also produce the campaign plan template or the residual-risk record skeleton if you'd like them attached to the reply.