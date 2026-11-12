Here's a draft. It declines the whitepaper-only route, says what the whitepaper is still good for, and gives a plan that fits a January date. Items in [brackets] are for you to fill in.

---

**Subject: Robustness evidence for [chatbot name]: proposed approach ahead of January go-live**

Hi [name],

Thanks for the request. Here is what we propose to put on file, and why the vendor whitepaper alone won't do.

**1. How we'll use the vendor's 99% figure**

We'll attach the whitepaper as vendor documentation. We won't present it as evidence of robustness for our deployment, for these reasons:
- **Different system.** The benchmark tests the vendor's model on their prompts. Our risk comes from what the assistant can reach: a customer's last 10 card transactions and the ability to open dispute tickets.
- **Different success criterion.** We don't know what counted as a "jailbreak" in their benchmark. Ours are specific to us: another customer's data appears, a dispute is opened without the customer's intent, or the bot gives out content our policy forbids.
- **Unknown conditions.** The whitepaper doesn't give the settings, the number of attempts per prompt, or whether the vendor tuned against the benchmark. It is also an internal benchmark with no independent tester.
- **A pooled figure hides the cost.** A 1% failure rate across 10,000 prompts says nothing about how the failures are distributed. One high-impact class could fail often while the average looks good. A persistent attacker also needs only about 100 tries to expect a first success at 1%.

**2. Entry points specific to our setup**

- *Direct:* customers asking for another person's transactions, or trying to get the bot to open or alter disputes.
- *Indirect:* transaction data contains text the customer or a merchant controls, such as merchant names and descriptors. That text enters the model's context when the bot reads transactions, so it is a prompt-injection path the vendor's benchmark is unlikely to cover.
- *Multi-turn:* gradual escalation across a conversation toward a forbidden action.

**3. Proposed campaign**

- **Attack classes** come from our own harm list (cross-customer data exposure, unauthorized or fraudulent dispute actions, policy bypass, harmful or misleading advice). We'll check coverage against OWASP LLM Top 10 (2025), NIST AI 100-2 and MITRE ATLAS, and list any relevant class we did not test.
- **Success criteria, settings and tolerated rates per class** will be written and signed by [risk owner] before testing. Criteria will be code-checkable where possible, such as planted canary records and checks of the ticket-creation log.
- **Sample size.** To show a class is under a tolerated rate with no successes, we need roughly 4 ÷ rate independent attack seeds. That is about 380 for a 1% tolerance and about 765 for 0.5%. We'll size the costly classes (cross-customer data, ticket creation) to their own tolerance. Any class below its target size will be labelled indicative.
- **Testers.** Automated generation to scale known attacks, plus human red-teamers (security and fraud/complaints staff) to find new ones. Rates you rely on will come from testers independent of the team configuring the bot.
- **Held-out set.** We'll seal and hash a held-out attack set that the configuration team never sees. Decision rates will be read only on that set.
- **Reporting** will be per class with a 95% confidence interval against its tolerance, never a single pooled number. We won't conclude that the system is "secure" or "jailbreak-resistant". We'll report measured rates, the untested classes and the residual risk.
- **Findings** become regression cases that rerun on every model, prompt or tool change.

**4. Timeline and decisions I need**

[Work back from January: attack set built by X, test run by Y, report by Z. Please confirm the dates and testers.]

I need:
1. Sign-off on the harm list and tolerated rates per class, by [date].
2. A named residual-risk owner outside the build team.
3. Your view on whether this campaign belongs in our operational resilience testing programme (DORA) and where it should be recorded.

**5. Requests to the vendor**

- The benchmark's composition, success criteria, settings and attempts per prompt.
- Their model and version change policy, so we know what triggers a retest.
- Whether any of their declared robustness or cybersecurity test conditions are documented for deployers.

If the timeline slips, I'd rather launch with a narrower scope (for example, ticket creation limited or human-confirmed) than with untested actions. I'm happy to walk through any of this.

[Your name]

---

**Notes for you**
- **Attempt volume.** I haven't estimated how many attack attempts we'd expect per month. You'll need a figure from logs or fraud data. Exposure should be computed on attack attempts, not the 60,000 conversations.
- **Dispute tickets.** If a human reviews every dispute before it takes effect, say so. It lowers the consequence of a bad ticket and may relax that class's tolerance.
- **Procurement.** If procurement pushes back, the short version is that the vendor's number describes the vendor's test, and model risk is asking about our system.

I can also fill in the campaign plan template with attack classes and sample sizes per class, if you share your tolerated rates.