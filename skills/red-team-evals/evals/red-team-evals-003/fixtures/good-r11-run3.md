Here's a draft. Bracketed items are for you to fill in or confirm.

---

**Subject: Chatbot go-live: robustness evidence plan (proposal for your sign-off)**

Hi [name],

Thanks for the request. We will not rely on the vendor whitepaper as our robustness evidence. We'll attach it to the file as vendor documentation. We propose to run our own campaign, scoped so it fits the January date.

**Why the whitepaper isn't enough**

- **It describes a different system.** The "99% jailbreak resistance" figure comes from the vendor's own 10,000 prompts, success criteria and settings. It says nothing about our configuration, our prompt, or our tools (transaction read, dispute creation).
- **The vendor may have tuned against its own benchmark.** We can't tell, and a score on a set the defences were tuned against overstates resistance to new attacks.
- **It is a pooled rate.** The harms that matter to us are specific, such as one customer seeing another's transactions or a dispute opened without authorisation. A pooled figure can look excellent while one class fails badly.
- **Taken at face value, it still allows meaningful exposure.** A 1% failure rate means a persistent attacker gets a first success in roughly 100 tries. That is minutes of effort for someone scripting it.

We'll request the vendor's benchmark methodology, settings and attack categories. We'll use them to inform our attack classes, not as a rate we rely on.

**What we propose to test**

Each class comes from what an attacker would want from this deployment:

1. **Cross-customer data access.** Getting another customer's transactions or PII through the transaction-read tool, by direct request or multi-turn social engineering.
2. **Unauthorised or fraudulent dispute creation.** Opening disputes on transactions that aren't the customer's, or in bulk, or with manipulated arguments.
3. **Indirect injection.** Merchant names and descriptors on transactions are third-party-controlled text the bot reads. We'll test whether a crafted descriptor can steer the bot.
4. **System prompt and configuration leakage.**
5. **Policy and harmful output.** Misleading statements on fees, credit terms or dispute outcomes, and off-policy commitments.
6. **Multi-turn and persistence attacks** across all of the above.

We'll map these to OWASP LLM Top 10 (2025) and MITRE ATLAS. We'll report which relevant classes were tested and which weren't, and we'll record the untested ones in the file.

**How we'll run it, so the results can be relied on**

- **Success criteria, settings and tolerated rates per class are written and signed before testing.** That means model and prompt version, temperature and attempts per attack. We ask model risk to sign the tolerances. For cross-customer data and unauthorised disputes, we propose the tolerance be as close to zero as the test can support.
- **Sealed held-out attack set.** The vendor and our build team don't see it or tune against it. Decision rates are read only on this set.
- **Independent testers.** Automated generation to scale known attacks, plus human red-teamers (security and people who know how fraud and complaints actually look). Rates you rely on come from testers independent of the build team.
- **Per-class reporting.** For each class we'll report successes out of attacks, a 95% confidence interval, the tolerance and a reading (under, over or undecided). We won't report a single pooled number.
- **Sizing.** To show a class is under a 1% rate with no successes needs about 380 independent attack seeds. For 0.5% it's about 765. Zero failures in a smaller test doesn't show zero risk. We'll state the upper bound and the exposure it implies on our estimated attack volume. That estimate is based on [source: logs or pilot data], not the 60,000 monthly conversations. Classes below their target size will be labelled indicative.
- **Deterministic controls tested alongside the model.** The tools should enforce authorisation themselves (the transaction read bound to the authenticated session, dispute creation limited to that customer's own transactions, rate limits). We'll test those controls directly, because they shouldn't depend on the model behaving.
- **Regression suite.** Every successful attack becomes a regression case, re-run on every model, prompt or tool change. After any fix we retest on fresh attacks.

**Deliverables for the file**

1. The campaign plan with signed criteria and tolerances (by [date]).
2. A results table per class with intervals.
3. A residual-risk record covering what was tested, what wasn't, findings and their status, what triggers the next campaign, and the named risk owner. The risk owner should sit outside the build team and accept the residual risk.
4. The vendor's methodology documents, and confirmation of which robustness and test information they provide us.

**Proposed timeline (go-live in January)**

- Week of [date]: agree classes and tolerances with model risk, and request vendor documentation.
- By [date]: held-out set sealed and testers assigned.
- [dates]: campaign run, with findings fixed and retested.
- By [date]: results and residual-risk record to model risk.

If time runs short, we would cut scope by prioritising classes 1–3, where the consequences are highest (customer data, money movement, regulatory exposure). We would label the rest as untested or indicative in the file. We would not substitute the vendor's figure for them. Alternatively, a phased go-live with a limited rollout and tighter monitoring is an option we can discuss.

**Decisions needed from you**

- Sign-off on the classes and tolerances.
- Who accepts residual risk.
- Whether this campaign belongs in our operational resilience testing programme, and who records it there.

Regards,
[Name]

---

A few notes:

- **Attack-volume estimate:** I left the source blank on purpose. If you have a figure from logs or a pilot, use that, because exposure should be computed on attack attempts, not the 60,000 conversations.
- **Procurement:** Consider sending procurement a one-line version: "The vendor figure goes in the file as documentation, but model risk asked for robustness evidence on our configuration, and the vendor benchmark can't provide that."
- **Legal and vendor roles:** Ask legal whether we're a deployer or provider for any regulatory purposes. If the former, ask the vendor for their declared robustness levels and test conditions.

I can also draft the campaign plan and residual-risk templates, or work out per-class seed counts once you have draft tolerances.