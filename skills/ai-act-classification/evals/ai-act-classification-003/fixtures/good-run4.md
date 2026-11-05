# AI Act classification memo: account-actions chatbot, L2 → L3/L4

**Freshness:** I didn't check the skill's `last_verified` date. Counsel should confirm the application dates, since the Digital Omnibus changed them in July 2026.

**Short answer:** Today an adviser validates every action, so the chatbot is a preparatory tool. Once it executes on its own, the overdraft and the card limit increase are likely to be high-risk under Annex III point 5(b), if the system assesses creditworthiness. Address change and card block most likely stay outside Annex III. The high-risk obligations apply from **2 December 2027**, which is after your go-live next quarter. That gives you time to design for them, but not a reason to ignore them.

## System and role
| Step | What it does and decides | Level | Role |
|---|---|---|---|
| Change of address | Executes a data change | L2 → L3 | Provider and deployer if built in-house; deployer if bought (art. 3(3), 3(4)) |
| Card block | Executes a protective action | L2 → L3 | Same |
| Raise card payment limit | Executes a limit change, probably after some risk check | L2 → L3, or L4 if hard caps stop it automatically | Same |
| Overdraft up to 500 EUR | Grants credit to a natural person | L2 → L3, or L4 if hard caps stop it automatically | Same |

"Executes within caps, weekly sample" is L3 on the ladder: the AI acts and the human reviews a sample. It becomes L4 if the caps are enforced technically with automatic stop. You can't skip a level in production, so go through L3 first. The L3 gate is a shadow run of at least 2 weeks, a known guardrail false-positive rate and a tested escalation path. If a vendor supplies the chatbot, art. 25(1) can turn you into a provider. It does so if you put your name on it, modify it substantially, or change its purpose so that it becomes high-risk.

## Prohibited practices (art. 5)
I see no hit on 5(1)(a)–(h). Counsel should check 5(1)(b) (exploiting economic vulnerability) if the chatbot ever pushes overdrafts to customers in financial difficulty.

## Risk category
| Step | Category | Basis | Open point |
|---|---|---|---|
| Overdraft | Likely high-risk | Annex III point 5(b), art. 6(2) | Does the chatbot assess or score creditworthiness, or only apply a fixed eligibility rule? |
| Card limit increase | Possibly high-risk | Annex III point 5(b) | Same question. A limit increase is a credit exposure. |
| Address change, card block | Likely not Annex III | None identified | Check that the card block doesn't feed a fraud or creditworthiness score. The fraud-detection carve-out in 5(b) covers only fraud detection. |

**Art. 6(3) exception.** This is a question for counsel, not a conclusion. At L2 the chatbot arguably performs a preparatory task (6(3)(d)). At L3/L4 it takes the decision, so it materially influences the outcome and the exception looks unavailable. It never applies if the system profiles natural persons, and an automated credit decision is likely to involve profiling.

The other transparency and GPAI points follow.

## Transparency (art. 50)
Art. 50(1) has applied since 2 August 2026 and applies already. Customers must be told they are talking to an AI unless that is obvious. As provider, you design this.

## General-purpose model
I don't know which model you use or how. If it is called through an API, the model obligations (arts. 53 and 55) stay with the model provider. Ask the provider for its art. 53(1)(b) documentation. Fine-tuning makes you the provider of the modified model only above one third of the original training compute.

## Obligations (if 5(b) applies)
| Who | Obligation | Article | From | Suggested owner |
|---|---|---|---|---|
| Provider and deployer | AI literacy for staff | 4 | In force | Compliance/HR |
| Provider | Disclose that the customer is talking to an AI | 50(1) | 2 Aug 2026 | Product |
| Provider | Risk management, data governance, documentation, logging, instructions, human-oversight design, accuracy/robustness | 9–15 | 2 Dec 2027 | Product/Engineering |
| Provider | Quality management, conformity assessment, registration | 17, 43, 49 | 2 Dec 2027 | Compliance |
| Provider | Post-market monitoring, serious-incident reporting | 72–73 | Counsel to confirm | Compliance |
| Deployer | Use per instructions; oversight by competent, trained people with authority | 26(1)–(2) | 2 Dec 2027 | Retail operations |
| Deployer | Monitor, suspend on risk, report incidents | 26(5) | 2 Dec 2027 | Risk |
| Deployer | Keep logs under your control for at least 6 months, within financial-services documentation | 26(6) | 2 Dec 2027 | IT |
| Deployer | Inform customers subject to decisions | 26(11) | 2 Dec 2027 | Legal |
| Deployer | Fundamental rights impact assessment before first use (applies to any deployer of 5(b)); may refer to the GDPR DPIA | 27 | 2 Dec 2027 | Compliance/DPO |
| Deployer | Explain the system's role on request, for decisions with significant adverse effects | 86 | Counsel to confirm | Customer service |

## What changes when you go from L2 to L3/L4
- **Oversight.** A weekly sample is after-the-fact review, not oversight of each decision. Counsel should say whether that meets art. 14 (design) and art. 26(2) (deployer). Plan stop controls, escalation, and an authorised person who can override.
- **Classification.** The overdraft and limit steps move from a preparatory tool to a system that decides, which is what brings point 5(b) into play.
- **Role.** If you are modifying a vendor product, check art. 25(1).
- **Customers.** They must be told about the AI, and for credit decisions they have a right to an explanation.

## Questions for counsel
| Question | Facts needed | Why it matters |
|---|---|---|
| Is the overdraft/limit logic "creditworthiness evaluation" under 5(b)? | Decision rules, data used, any score or profile | Decides whether the high-risk regime applies |
| Does art. 6(3) apply at L3/L4? | Whether the system profiles, and how much it influences the decision | Decides whether registration alone suffices |
| Art. 111(2) transitional rule: if you go live before 2 Dec 2027, are you in scope only after a significant design change? | Go-live date, later changes | Could change when obligations start |
| Does a weekly sample satisfy arts. 14 and 26(2)? | Sample size, reviewers' authority, caps | Core design constraint |
| Who is the provider if the chatbot is a vendor product? | Contract, branding, customisation | Who carries arts. 9–17, 43, 49 |
| When do arts. 72–73 and 86 apply to Annex III systems? | — | Open in the reference map |
| Which authority supervises? | Entity type | The ACPR is proposed in a French bill, not yet law |

## Outside the AI Act, but to check in parallel
- GDPR art. 22 (automated individual decisions) and the DPIA.
- Consumer credit rules for the overdraft.
- Payment-services authentication rules for address and limit changes.

This memo is a checklist for counsel, not a conformity assessment.