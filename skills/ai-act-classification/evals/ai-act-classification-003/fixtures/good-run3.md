# AI Act classification memo: account-action chatbot moving from adviser validation to autonomous execution

**Freshness:** I couldn't read the skill's `last_verified` date, so counsel should confirm the application dates and guidance. The draft Commission guidelines on high-risk classification (19 May 2026) are not yet final. French authority designations are still a bill.

**Short answer:** Most of the change comes from one action, the overdraft grant. Address change and card block look outside Annex III. An overdraft decision can fall under Annex III point 5(b) (creditworthiness), and whether it does is the main question for counsel. Removing the adviser also weakens the argument that the chatbot only prepares the decision.

## System and role
| Step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| Change of address | Updates customer data | L2 → L3 | Open (see questions) |
| Card block | Blocks a card | L2 → L3 | Open |
| Raise card payment limit | Changes a spending limit | L2 → L3 | Open |
| Overdraft up to 500 EUR | Grants credit to a natural person | L2 → L3 | Open |

- **Level:** Weekly sampling plus caps is L3 (human on the loop). If you add automatic stop, rollback and report-only review, it becomes L4. Don't skip a level in production.
- **Role:** I don't know whether you built the chatbot or bought it. If it runs under your name, you are provider (art. 3(3)) and deployer (art. 3(4)). If a vendor supplies it, you are a deployer, and a vendor's "AI Act compliant" claim doesn't transfer your art. 26 duties.

## Prohibited practices (art. 5)
- **Emotion recognition (5(1)(f)):** Not applicable. It applies to the workplace and education, and the chatbot doesn't infer emotions.
- **Manipulation (5(1)(a)):** No hit identified.
- **Exploiting vulnerabilities (5(1)(b)):** Possible risk to design out. A chatbot that offers or grants overdrafts could target customers in financial difficulty. I found no hit, but counsel should confirm that the flow doesn't nudge or push credit at those customers.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| Possibly high-risk (overdraft) | Annex III point 5(b), via art. 6(2) | Overdraft is credit to a natural person. The decision may depend on an assessment of creditworthiness. | Does the chatbot, or a scoring tool it calls, assess creditworthiness? |
| Probably not high-risk (address, card block) | Not listed in Annex III | Administrative or protective actions | Counsel to confirm. A card block for fraud falls under the fraud-detection carve-out in 5(b). |
| Open (card limit raise) | 5(b) only if it is a credit limit | Depends on whether it is a debit spending limit or a credit line | What kind of card is it? |
| Transparency obligations | Art. 50(1) | Customers talk to a chatbot | None |

**Art. 6(3) exception:** This is a question for counsel, not a conclusion. At L2 you could argue the system only prepares the decision (art. 6(3)(d)). At L3 the adviser no longer validates each action, so the system materially influences or makes the decision, and the exception is harder to claim. It never applies if the system profiles natural persons. If the overdraft decision uses a customer score or profile, the exception is out.

## Transparency (art. 50)
- **Art. 50(1):** Customers must be told they are talking to an AI, unless that is obvious. It has applied since 2 August 2026, so it is already live. The provider owns it, and the deployer should check it is in place.
- **Art. 50(2)–(4):** Not relevant unless the chatbot publishes synthetic content or uses emotion recognition.

## General-purpose model
- The underlying model and how it is used (API or fine-tuned) are not given.
- Calling a model through an API doesn't make you its provider. Ask the model provider for the documentation it owes downstream providers (art. 53(1)(b)).
- Fine-tuning counts only above one third of the original training compute, which is a question for counsel with the compute figures.

## Obligations
| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| Provider and deployer | AI literacy for staff who operate or use the system | 4 | Since 2 Feb 2025 | To assign |
| Provider | Tell customers they are talking to an AI | 50(1) | Since 2 Aug 2026 | To assign |
| Deployer, if overdraft is high-risk | Use per instructions | 26(1) | 2 Dec 2027 | To assign |
| Deployer, if high-risk | Human oversight by competent, trained people with authority | 26(2) | 2 Dec 2027 | To assign |
| Deployer, if high-risk | Monitor, suspend on risk, report serious incidents (internal governance rules count for financial institutions) | 26(5) | 2 Dec 2027 | To assign |
| Deployer, if high-risk | Keep logs for at least 6 months, within financial-services documentation | 26(6) | 2 Dec 2027 | To assign |
| Deployer, if high-risk | Inform customers subject to the decisions | 26(11) | 2 Dec 2027 | To assign |
| Deployer of 5(b) | Fundamental rights impact assessment before first use (may refer to the GDPR DPIA) | 27 | 2 Dec 2027 | To assign |
| Deployer | Explain the system's role on request for decisions with significant adverse effects | 86 | Counsel to confirm | To assign |
| Provider, if high-risk | Risk management, data governance, documentation, logging, human oversight design, accuracy | 9–15 | 2 Dec 2027 | To assign |
| Provider, if high-risk | Quality management, conformity assessment, registration | 17, 43, 49 | 2 Dec 2027 | To assign |
| Provider, if high-risk | Post-market monitoring and serious incident reporting | 72–73 | Counsel to confirm | To assign |

**Timing:** If the overdraft step is high-risk, the Annex III obligations apply from 2 December 2027. Your go-live next quarter is earlier. Counsel should confirm whether that makes a difference. I don't have the transitional rule for systems already in service, and a move to autonomous execution may count as a significant change. The safer course is to design to these obligations now.

## If a step moves to L+1
| Step | From → to | What changes in the classification | Obligations that appear or tighten |
| --- | --- | --- | --- |
| Overdraft | L2 → L3 | Now acts on customers without prior human review. The art. 6(3)(d) "preparatory task" argument weakens. | Human oversight design (art. 14, art. 26(2)). A weekly sample is after-the-fact review, so counsel should say whether it satisfies oversight. Logging (arts. 12, 26(6)), customer information (art. 26(11)), art. 86 explanation, art. 27 impact assessment. |
| Card limit raise | L2 → L3 | Same if it is credit | Same as overdraft |
| Address change, card block | L2 → L3 | Probably unchanged | Art. 4 literacy, art. 50(1) |
| Any step | L3 → L4 | Needs a high-risk check and a model card | Art. 14 oversight design |

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Does the overdraft grant fall under Annex III 5(b)? | Decision logic: fixed rule, existing bank score, or model assessment. Whether the chatbot calls a scoring tool. | Decides whether the high-risk regime applies. |
| Can art. 6(3) apply? | Whether the system profiles customers, and how much the adviser's validation shaped the decision. | If it profiles, the exception is out. |
| Is the card limit raise credit or only a spending limit? | Card type and the contract terms. | May bring it under 5(b). |
| Provider or deployer? | Who built the system and under whose name it runs. | Decides whether arts. 9–17, 43 and 49 are yours. |
| What happens between now and 2 Dec 2027? | Go-live date and system-in-service date. | Which obligations bind at launch. |
| Does a weekly sample meet art. 14 and art. 26(2) oversight? | Cap levels, sample size, ability to reverse an action. | Core design question. |
| When do arts. 72–73 and 86 apply to an Annex III system? | None | The amended text leaves this open. |
| Which authority supervises you? | Your supervisor. As proposed, the ACPR for 5(b) in France. | The bill is not yet law. |

## Outside the AI Act (not assessed here)
- **GDPR art. 22:** Automated decisions with significant effects. The overdraft grant is the obvious case. Run `dpia-prescreen`.
- **Consumer credit and payment rules:** Sector rules on consumer credit and strong customer authentication for sensitive changes.
- **Employee representatives:** If advisers' work changes, check `cse-consultation`.

This memo is a checklist for counsel, not a conformity assessment.