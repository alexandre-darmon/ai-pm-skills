# AI Act classification memo: chatbot executing account actions

**Freshness:** I couldn't see the skill's `last_verified` date. Counsel should confirm the application dates, since the Digital Omnibus (Reg. 2026/1744) only entered into force on 27 July 2026.

**Short answer:** Most of the change comes from the overdraft step, and probably the limit-raise step.
- If the chatbot's overdraft decision involves any assessment of the customer's creditworthiness, that step is likely high-risk under Annex III point 5(b).
- The art. 6(3) exception cannot apply, because that assessment is profiling of a natural person.
- Address change and card block look outside Annex III. They stay under the transparency and AI-literacy duties.
- The high-risk obligations apply from **2 December 2027**. Your go-live next quarter comes before that date, but the design choices you make now will have to meet them.

## System and role
| Step | What it does and decides | Level | Role |
| --- | --- | --- | --- |
| Change of address | Executes a customer data change | L2 → L3 | Open (see questions) |
| Card block | Blocks the card on request | L2 → L3 | Open |
| Raise card payment limit | Raises a limit for a natural person | L2 → L3 | Open |
| Overdraft up to 500 EUR | Grants credit | L2 → L3 | Open |

- Advisers validating every action is L2. Acting within caps with a weekly sample is L3 (human on the loop). Caps with an automatic stop are L4 features.
- The ladder says to set the level per step, not per product. It also says never to skip a level in production. The L3 gates are a shadow run of at least 2 weeks, a known guardrail false-positive rate and a tested escalation path.
- **Role:** this depends on build or buy. If you build the chatbot, including on a general-purpose model API, you are provider (art. 3(3)) and deployer. If you buy it, you are deployer (art. 3(4)). You become a provider if you rebrand it or change its purpose (art. 25(1)).

## Prohibited practices (art. 5)
Nothing identified from the facts given. One point to screen: art. 5(1)(b), exploiting vulnerabilities due to a social or economic situation. A chatbot that grants overdrafts on its own should not be able to push credit at customers in financial difficulty. If the design allows that, I would put it to counsel.

## Risk category
| Step | Category | Basis | Open point |
| --- | --- | --- | --- |
| Overdraft ≤500 EUR | Likely high-risk | Annex III point 5(b), art. 6(2) | Does the decision rest on a creditworthiness assessment or score by an AI component? |
| Card payment limit raise | Open | Annex III point 5(b) if the limit is credit-like or tied to a score | Is the limit a credit exposure, and does an AI component assess the customer? |
| Card block | Not high-risk on these facts | Not in Annex III (fraud detection is excluded from 5(b)) | Confirm the block is not driven by a creditworthiness assessment |
| Address change | Not high-risk on these facts | Not in Annex III | None |
| All steps | Transparency obligations | Art. 50(1) | None |

**Art. 6(3) exception:** this is a question for counsel. The exception never applies when the system profiles natural persons, and a creditworthiness assessment is profiling. A "small amount" is not an exception criterion.

**Where the answer turns:** if the chatbot only executes a limit that your existing, non-AI credit engine has already decided, the chatbot is an interface. In that case the classification of the engine and of the chatbot's role is a question for counsel. If the chatbot or an LLM component decides, or materially influences, who gets the overdraft, point 5(b) is in play.

## Transparency (art. 50)
- Art. 50(1) applies from 2 August 2026, so it already applies. Customers must be told they are dealing with an AI system unless that is obvious. The provider carries this duty, which means you if you build the chatbot.
- Autonomous execution makes it more important to say clearly who acted. Whether the customer is told that the AI executed the action, not just chatted, is a question for counsel.

## General-purpose model
- If the chatbot runs on a general-purpose model through an API, the art. 53 and 55 duties stay with the model provider. Your system is classified on its own use.
- Ask the model provider for the downstream documentation it owes you (art. 53(1)(b)).
- Fine-tuning makes you a model provider only above one third of the original training compute. Counsel would need your compute figures.

## Obligations
| Who | Obligation | Article | From | Owner |
| --- | --- | --- | --- | --- |
| Provider and deployer | AI literacy measures for the staff who operate or oversee the chatbot, including the sampling advisers | 4 | Applies now (since 2 Feb 2025) | Bank |
| Provider | Tell users they interact with an AI | 50(1) | 2 Aug 2026 (applies now) | Bank if built, vendor if bought |
| Provider, if the overdraft step is high-risk | Risk management, data governance, documentation, logging, instructions, human oversight design, accuracy and robustness | 9–15 | 2 Dec 2027 | Bank if built |
| Provider, if high-risk | Quality management, conformity assessment, registration | 17, 43, 49 | 2 Dec 2027 (arts. 43 and 49 date: counsel to confirm) | Bank if built |
| Deployer, if high-risk | Human oversight by competent, trained people with authority | 26(2) | 2 Dec 2027 | Bank |
| Deployer, if high-risk | Monitoring, suspension on risk, serious-incident reporting (financial institutions: internal governance rules count) | 26(5) | 2 Dec 2027 | Bank |
| Deployer, if high-risk | Keep the logs it controls for at least 6 months, within financial-services documentation | 26(6) | 2 Dec 2027 | Bank |
| Deployer, if high-risk | Inform the customers subject to the decisions | 26(11) | 2 Dec 2027 | Bank |
| Deployer, if point 5(b) | Fundamental rights impact assessment before first use, notified to the authority; may refer to the GDPR DPIA | 27 | 2 Dec 2027 | Bank |
| Deployer, if high-risk | On request, explain the system's role in a decision with significant adverse effects | 86 | Counsel to confirm | Bank |
| Provider | Post-market monitoring, serious-incident reporting | 72–73 | Counsel to confirm | Bank if built |

If you buy the chatbot, a vendor's "AI Act compliant" claim does not transfer the deployer duties in art. 26 and 27.

## If a step moves to L+1
| Step | From → to | What changes | Obligations that appear or tighten |
| --- | --- | --- | --- |
| Overdraft | L2 → L3 | The system now decides about a person's credit, with no human review before the effect. This is where the 5(b) risk is sharpest. | Art. 14 and 26(2): a weekly sample is much thinner than what oversight normally means. Art. 26(6) logs, art. 27 impact assessment, art. 86 explanations |
| Limit raise | L2 → L3 | Same, if the raise involves an assessment | Same as overdraft |
| Card block, address change | L2 → L3 | Lower risk. Wrongful or fraudulent changes are an operational risk more than an AI Act one. | Art. 50(1), art. 4, logging |

If you later move to L4, the ladder lists a high-risk classification check, art. 14 oversight design and a model card as the obligations that rise.

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Is the overdraft step Annex III point 5(b)? | How the 500 EUR decision is made: rules, a score, an LLM, or a pre-approved limit. Which component decides. | Decides high-risk status and the whole obligations table |
| Is the card limit raise within 5(b)? | Whether the limit is credit exposure, and what data drives approval | Same |
| Can any step use the art. 6(3) exception? | The facts above, plus whether the system profiles customers | It cannot be used when profiling is involved |
| Provider or deployer? | Built in-house, bought, or built on a general-purpose model API. Any rebranding or purpose change. | Decides who carries arts. 9–17, 43 and 49 |
| Does moving from validate-all to a weekly sample count as a substantial or design change? What applies to a system already live before 2 Dec 2027? | Go-live date next quarter. Whether the system is placed on the market before 2 Dec 2027. | Transitional treatment is not in my reference map |
| Does a weekly sample satisfy human oversight under arts. 14 and 26(2)? | Sample size, reviewers' authority, ability to reverse actions | The main design risk of the plan |
| When do arts. 72–73 and 86 apply to an Annex III system? | Not applicable | Open in the reference map |
| Which authority? | Not applicable | Under the French bill the ACPR would cover 5(b), but it is not yet promulgated. Check Légifrance. |

## Outside this memo
- GDPR art. 22 on automated decisions, and consumer-credit rules on creditworthiness checks, are separate regimes and may bite sooner than the AI Act high-risk duties. For the GDPR side, `dpia-prescreen` is the right next step.
- If the chatbot is built on your own stack, `system-prompt-and-guardrails` is the place to design caps, approvals and the automatic stop.

This memo is a checklist for counsel, not a conformity assessment.