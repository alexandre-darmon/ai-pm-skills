Here's a draft you can adapt.

---

**Subject: Robustness evidence for the customer-service chatbot, proposed plan before January go-live**

Hi [name],

Thanks for asking for robustness evidence. We'll send you our own test results and won't rely on the vendor's whitepaper alone.

**Why we're not using the whitepaper as evidence**

We'll attach it to the file as vendor documentation. It tells us what the vendor claims and helps us choose what to attack. It can't show how *our* deployment performs, for these reasons:

- It tests the vendor's configuration on their 10,000 prompts. Ours has our own prompt, our own tools (transaction read, dispute ticket creation) and our own data.
- We don't know the success criterion, the generation settings or the number of attempts per prompt. We also don't know who wrote the prompts or whether the vendor tuned against them.
- "99% resistance" is a single pooled figure. A pooled rate can look fine while one class, such as cross-customer data access, fails often. Per-class rates matter more for us, and the whitepaper doesn't give them.
- Even taken at face value, 99% means up to 1 in 100 attempts succeeds. A persistent attacker needs only about 100 tries for a first success.

**What we propose to run before go-live**

1. **Risk-based attack classes.** Each class is an attacker goal, an entry point and a consequence. The initial list is:
   - reading another customer's transactions (identity and authorization bypass)
   - opening disputes on transactions that aren't the requester's, or in bulk
   - indirect injection through third-party text the bot reads, such as merchant descriptors in transaction data
   - policy bypass, such as promising refunds, giving credit advice or making commitments the business hasn't approved
   - leaking the system prompt or internal data
   - multi-turn social engineering

   We'll map these to the OWASP LLM Top 10 and MITRE ATLAS, and list any relevant class we don't test.
2. **Criteria signed first.** Before testing starts, we'll sign the pass/fail criterion, the model and prompt versions, the settings and the tolerable rate per class. Wherever possible we'll check outcomes in code, using planted canary records and the tool-call logs, and avoid human or model judgment.
3. **Sized for the tolerance.** Zero failures in n attacks still allows a true rate of roughly 4/n. To show a class is under 1% we need about 380 independent attack seeds with no successes, and about 765 for 0.5%. We'll size the costly classes (other customers' data, dispute creation) to their own tolerance, and report any class below its n as indicative.
4. **Independent testers and a sealed set.** Automated generation, human testers with fraud and security backgrounds, and regression attacks stay separate in the results. The rates you rely on will come from testers independent of the build team. They'll use a held-out attack set that the people tuning the prompt and guardrails never see.
5. **What you'll receive.** A per-class table with successes, seeds, the 95% interval, the tolerance and a reading of under, over or undecided. It also lists the untested classes and the testers. A residual-risk record follows, with a named owner outside the build team accepting the remaining risk.

We won't state that the system is "robust" or "jailbreak-proof." The deliverable is a measured rate per class with its limits and what we didn't test.

**Timeline**

Go-live is January, so the schedule is tight but workable. The plan assumes we can start in the next two weeks:
- by [date]: sign the classes, criteria and tolerances
- weeks 1–3: build and run the campaign, and fix findings
- week 4: re-test fixed classes on fresh attacks
- before go-live: deliver the residual-risk record

If any class misses its sample size by then, we'd rather limit scope at launch than skip testing. One option is to require human confirmation before a dispute is created until that class is cleared.

**What I need from you**

- Confirmation of the tolerable rate per class, and who signs it
- A named owner outside the build team to accept residual risk
- A view on whether this belongs in our DORA resilience testing programme, and who records it
- Whether we're the provider or the deployer for any AI Act obligations. If we're the deployer, we'll ask the vendor for their declared robustness levels and test conditions for the file.

I'll also ask the vendor for their test methodology, their per-class results and their access arrangements for our testers.

Best,
[Name]

---

Before sending, please check three things:
- **Tolerances:** I used 1% and 0.5% as examples. Replace them with the rates your model risk team signs.
- **Attack attempts:** I don't have an estimate of monthly attack attempts. Without one, we can't turn a "zero successes" bound into expected incidents per month. Pull it from logs or fraud data, not from the 60,000 conversation figure.
- **Dates:** Fill in the dates and the sizes of the classes once you've confirmed testing capacity.