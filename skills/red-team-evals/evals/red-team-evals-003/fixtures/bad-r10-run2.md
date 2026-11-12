Here's a draft. I've put placeholders in brackets where I don't know your specifics. I'd also tell procurement the whitepaper goes in the file as supplementary vendor material, not as your evidence.

---

**Subject: Robustness evidence for [Chatbot Platform], go-live January**

Hi [Name],

Thanks for the request. Here is where we stand on robustness evidence and what we propose before go-live.

**Vendor evidence**

The vendor's whitepaper claims "99% jailbreak resistance" on an internal benchmark of 10,000 adversarial prompts. We will attach it to the file as supplementary vendor material. We don't think it works as our primary evidence, for these reasons:

- **It is not independent.** The vendor chose the prompts, ran the test and reported the result. We haven't seen the methodology, attack taxonomy, pass/fail criteria or whether the prompts were tuned against.
- **It tests the model, not our deployment.** Our risk comes from the integration. The bot can read a customer's last 10 transactions and open dispute tickets. A generic jailbreak benchmark doesn't cover tool misuse, cross-customer data access, or manipulation of dispute actions.
- **The number is less reassuring at our volume.** A 99% block rate means up to about 100 of 10,000 prompts succeeded. At roughly 60,000 conversations a month, even a small residual failure rate would show up regularly in production. The benchmark also says nothing about how severe those failures are.
- **It doesn't cover indirect injection.** Merchant names and transaction descriptors are third-party text that the model reads. A generic benchmark is unlikely to test this.

**Proposed testing before go-live**

We propose a targeted test campaign on our configured deployment, scoped to fit the January date. It would cover:

1. **Data access and authorization.** Attempts to obtain another customer's transactions or account details, or data beyond the last 10 transactions. We'll also confirm that authorization is enforced by the application layer and session, not by the model's judgment.
2. **Action integrity.** Attempts to open disputes the customer didn't request, open them on the wrong transaction, or open them in bulk. This includes social engineering and multi-turn pressure.
3. **Indirect prompt injection.** Instructions embedded in transaction descriptors or other retrieved content.
4. **Sensitive data and disclosure.** Leakage of PII, system prompts, internal policies or tool schemas, and handling of full card numbers or credentials typed in by customers.
5. **Conduct and regulatory risk.** Incorrect or misleading statements about dispute rights, fees or liability, and out-of-scope advice. These are UDAAP and complaint-handling exposure.
6. **Abuse and availability.** Rate limiting, automated probing, and cost or volume abuse.

We'll report pass/fail results with the attack counts and the severity of any failures, not a single headline percentage. We'll retest after remediation and document any residual risk for your acceptance.

**Controls we'll document alongside testing**

- Tool permissions limited to read-only transactions and dispute creation, bound to the authenticated customer
- Confirmation step or human review for dispute creation, as appropriate
- Logging of conversations and tool calls, with production monitoring and alerting
- Escalation to a human agent and a kill switch
- Vendor change management, so we are notified of model updates and can retest

**Requests to the vendor**

We're asking the vendor for the benchmark methodology and prompt categories, any third-party test reports, their model-update and notification policy, and their incident response commitments.

**Timeline**

[Proposed schedule, e.g. test design by [date], execution by [date], remediation and retest by [date], results to MRM by [date].] We think this fits before the January go-live, but we'd like to align early on scope and on what MRM would consider sufficient evidence.

Could we meet this week to agree the scope and acceptance criteria?

Best,
[Your name]

---

A few notes for you:

- **Timeline:** It's mid-November and go-live is January, so you have about 6–8 weeks. A scoped campaign is feasible if you start now. If it slips, a fallback is a phased launch, for example FAQ-only first, or dispute creation behind human confirmation, with full tool access after testing.
- **Procurement:** If they push back, the short answer is that the vendor's claim is evidence about the vendor's test, not about your deployment. A model risk finding after launch would cost more time than the testing does.
- **Fill in the details:** Add the actual authorization architecture (does the backend scope tool calls to the session?), since that's the control model risk will probe hardest.

I can also draft a more detailed test plan, with attack classes, sizing and coverage, if you'd like.