# AI Act classification memo: retail-bank chatbot executing account actions

Freshness: the skill was verified on 2026-11-04 (today), so the application dates below are current. Commission guidelines on high-risk classification are still a draft (19 May 2026).

**Short answer:** most of the change sits in one action, the overdraft of up to 500 EUR. If the chatbot assesses whether a customer qualifies, that is probably creditworthiness evaluation of a natural person (Annex III point 5(b)), which is high-risk. Moving from adviser validation to autonomous execution removes the arguments that could keep it out of that category and makes the human-oversight duties real. Address change and card block are not in Annex III on these facts. The card-limit increase depends on facts we don't have yet.

## System and role
| Step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| Change of address | Updates customer data | L2 → L3/L4 | Unknown (build or buy?) |
| Card block | Protective action | L2 → L3/L4 | Same |
| Raise card payment limit | Changes a spending limit | L2 → L3/L4 | Same |
| Overdraft ≤ 500 EUR | Grants credit | L2 → L3/L4 | Same |

- A weekly sample with caps sits between L3 (human on the loop) and L4 (autonomous with guardrails).
- Per the ladder, no level is skipped in production. Going from L2 to L4 needs L3 first, with a shadow run of at least 2 weeks.
- If the bank built or commissioned the system under its own name, it is the provider (art. 3(3)) and also the deployer (art. 3(4)). If it buys the system, it is a deployer, unless art. 25(1) turns it into a provider by a substantial modification or a change of purpose.

## Prohibited practices (art. 5)
- None identified. I checked 5(1)(a)-(b), 5(1)(c) and 5(1)(f)-(g).
- One point to confirm: the chatbot must not push overdrafts on customers because it infers they are financially vulnerable (5(1)(b)). This is a design check; I see no hit on the facts given.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| High-risk (probable) | Art. 6(2), Annex III point 5(b) | Overdraft is credit to a natural person. The chatbot or a score behind it decides eligibility. | Does a scoring step exist, and is it an AI system? |
| Not high-risk on these facts | Not in Annex III | Address change and card block. Fraud detection is excluded from 5(b). | Confirm the card block is not driven by a fraud or creditworthiness model. |
| Open | 5(b) if the limit depends on solvency | Card payment limit | Is it a spending limit on a debit card, or a credit limit tied to solvency? |
| Transparency | Art. 50(1) | Customers chat with an AI | Applies already. |

**Art. 6(3) exception: question for counsel.**
- It needs no material influence on the decision, plus a narrow procedural or preparatory task.
- It never applies when the system profiles natural persons, and a credit assessment is profiling.
- At L2 the "preparatory task" argument was at best weak. At autonomous execution the chatbot is the decision, so the argument is gone.

## Transparency (art. 50)
- Art. 50(1) applies since 2 August 2026: tell customers they are talking to an AI, unless that is obvious.
- Check that the chatbot says so before it executes anything.

## General-purpose model
- I don't know the model or the provider.
- If it is a general-purpose model called through an API, the art. 53 and 55 obligations stay with the model provider. The bank's system is classified on its own use.
- Ask the model provider for the downstream documentation under art. 53(1)(b). If the model is fine-tuned, counsel needs the compute figures, because the one-third threshold decides whether the bank becomes a model provider.

## Obligations
| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| Provider and deployer | AI literacy of the staff who operate the system | 4 | In force | To assign |
| Provider | Transparency to customers | 50(1) | In force (2 Aug 2026) | To assign |
| Provider (overdraft) | Risk management, data governance, documentation, logging, instructions, oversight design, accuracy | 9–15 | 2 Dec 2027 | To assign |
| Provider | Quality management, conformity assessment, EU database registration | 17, 43, 49 | 2 Dec 2027 | To assign |
| Provider | Post-market monitoring, serious-incident reporting | 72–73 | Counsel to confirm | To assign |
| Deployer (overdraft) | Use per instructions; oversight by competent, trained people with authority | 26(1)–(2) | 2 Dec 2027 | To assign |
| Deployer | Monitoring, suspension, serious-incident reporting (internal governance rules count for financial institutions) | 26(5) | 2 Dec 2027 | To assign |
| Deployer | Logs kept at least 6 months, within financial-services documentation | 26(6) | 2 Dec 2027 | To assign |
| Deployer | Inform customers subject to the decision | 26(11) | 2 Dec 2027 | To assign |
| Deployer of 5(b) | Fundamental rights impact assessment before first use, notified to the market surveillance authority. It may refer to the GDPR impact assessment (27(4)). | 27 | 2 Dec 2027 | To assign |
| Deployer | Explanation on request of the system's role in a decision with significant adverse effects | 86 | Counsel to confirm | To assign |

## If a step moves to L+1
| Step | From → to | What changes | Obligations that appear or tighten |
| --- | --- | --- | --- |
| Overdraft | L2 → L3/L4 | The 6(3) exception loses its basis. The system decides without prior human review. | Art. 14 and 26(2): a weekly sample is not obviously "authority to intervene". It risks automation bias, so design stop, override and escalation. Also logging (12, 26(6)), art. 27, art. 86. |
| Card limit | L2 → L3/L4 | Becomes 5(b) if tied to solvency | Same as overdraft, if it applies. |
| Address change, card block | L2 → L3/L4 | No category change | Art. 4 and 50(1) only. Cap and guardrails are for fraud and operational risk. |

## Questions for counsel
| Question | Facts needed | Why it matters |
| --- | --- | --- |
| Is the overdraft decision creditworthiness evaluation under 5(b)? | How eligibility is decided: AI scoring, a rules engine, or the chatbot itself | It decides whether the heaviest obligations apply. |
| If a deterministic rules engine decides and the chatbot only executes, is the scoring part an AI system (art. 3(1))? | Architecture and what the model does | It could narrow the scope. |
| Does the card-limit increase involve a solvency assessment? | Card type and the criteria for approval | It decides whether 5(b) covers a second action. |
| Does the 6(3) exception hold at L2 today, given profiling? | Current preparation step | The current setup may already be in scope. |
| Does going live in Q1 2027, before 2 Dec 2027, give a transitional position (art. 111)? Does the later change count as a significant design change? | Go-live date, version history | It decides when the high-risk duties bite. I recommend designing for them now. |
| Who is provider and who is deployer? | Build or buy, contract, any fine-tuning | It decides who owes arts. 9–17, 43 and 49. |
| Which authority supervises? | French designation is still a bill. The ACPR is proposed for 5(b). | It decides who receives the art. 27 notification. |
| When do arts. 72–73 and 86 apply to an Annex III system? | n/a | The map flags this as an open point. |

## Outside the AI Act (not classified here)
- **GDPR art. 22:** automated decisions with significant effects need safeguards such as human intervention and the right to contest. Run `dpia-prescreen`.
- **Consumer credit rules:** these may require a creditworthiness check and a right to human review for automated credit decisions. Counsel should confirm the national transposition.
- **Staff consultation:** if advisers' work changes, `cse-consultation` applies.

## Recommendation
Split the rollout by step.
1. Take address change and card block to L3 first, then L4. This needs no high-risk machinery, only art. 4 and 50(1).
2. Keep the overdraft (and the card-limit increase if it is solvency-based) at L2 until counsel confirms the category.
3. If you go autonomous on the overdraft, build the Annex III controls before 2 December 2027: a fundamental rights impact assessment, logging, a real stop and override, and an oversight design that is stronger than a weekly sample.

This memo is a checklist for counsel, not a conformity assessment.