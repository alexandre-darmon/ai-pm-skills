Application dates as last checked on 2026-11-04.

**Category:** outside Annex III, so not high-risk. The only AI Act duties I found are AI literacy (art. 4) and the art. 50(1) disclosure that users are talking to an AI. Whether art. 50(2) text marking applies is a question for counsel.
**Role:** the IT team built the chatbot in-house, so you are probably provider and deployer of the system (art. 3(3), 3(4)). You are not provider of the underlying model.
**First actions:** (1) add a clear "you are talking to an AI" notice, (2) set up AI literacy measures for the IT staff who run it, (3) ask the vendor for its art. 53(1)(b) documentation.

## System and role
| Step | What it does and decides | Autonomy | Role |
| --- | --- | --- | --- |
| Answer questions from IT documentation | Produces text answers, with no decision about any person | L1 (assumed: the employee acts on the answer themselves) | Provider and deployer (assumption: built in-house, used for your own staff) |
| Link to the ticketing tool | Points to a link and takes no action | L1 | Same |

## Prohibited practices (art. 5)
None identified. I checked 5(1)(a)-(b) and (c), and 5(1)(f) and (g). The chatbot reads text only, with no biometric signals, so there is no emotion recognition. Nothing manipulates users or scores them.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| Transparency obligations | Art. 50(1), art. 4 | IT Q&A for employees, no decision about individuals, no action taken | Annex III point 4(b) if the logs are ever used to evaluate or monitor individual employees (see questions) |

Not high-risk: it does not recruit, evaluate, promote, allocate tasks or monitor performance (Annex III point 4), and it is not in the credit, insurance or essential-services points (point 5). The art. 6(3) exception is not relevant.

## Transparency (art. 50)
- **50(1):** the provider must make sure users know they are interacting with an AI unless that is obvious. Do not rely on "obvious"; add a notice in the chat window.
- **50(2):** the chatbot generates text, so counsel should say whether marking applies. Whether it does is a question for counsel.
- **50(3) and 50(4):** do not apply. There is no emotion recognition or biometric categorisation, and nothing is published to inform the public.

## General-purpose model
You call a commercial model through its vendor's API, so you are not its provider. Arts. 53 and 55 stay with the vendor. Ask the vendor for the documentation it owes downstream providers (art. 53(1)(b)). I assumed no fine-tuning. If you fine-tuned, counsel needs the compute figures for the one-third threshold.

## Obligations
| Who | Obligation | Article | Applies from | Owner | Evidence |
| --- | --- | --- | --- | --- | --- |
| Provider and deployer | Support AI literacy of staff who operate or use it | 4 | 2 Feb 2025 | IT / HR | Not seen |
| Provider | Tell users they are interacting with an AI | 50(1) | 2 Aug 2026 | IT product owner | Not seen |
| Provider | Marking of synthetic text, if in scope | 50(2) | 2 Aug 2026; 2 Dec 2026 if placed on the market before 2 Aug 2026 (art. 111(4), art. 113 as amended by Regulation (EU) 2026/1744) | Counsel to decide | Not seen |

Evidence records paper, not conformity. None of the high-risk duties (arts. 9–15, 26, 27, 86) apply at this category. Evals are good practice here, not an obligation.

## If a step moves to L+1
The request names or plans no further action. The chatbot "takes no action itself", so I have nothing to analyse. If you later let it open tickets or reset passwords, rerun this classification. Those would still be IT support tasks, so likely outside Annex III, but that is for counsel.

## Risks outside the AI Act
- **Wrong or outdated answers** (for example, bad security guidance): IT owner.
- **Employees pasting passwords or personal data into the chat, and vendor retention of prompts:** DPO and security.
- **Prompt injection, or documents the bot can read that the asker should not see:** security.
- **Chat logs used to monitor employees:** HR, DPO and employee representatives.

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Are you provider as well as deployer? | In-house build on a vendor API, used only inside your organisation | Art. 50 duties fall on the provider |
| Does art. 50(2) apply, and from which date? | Chatbot answers are plain text for internal use. Is it live in a pilot already, and when did it start? | Date is 2 Aug or 2 Dec 2026 (art. 111(4)) |
| Is the art. 50(1) notice needed, or is it obvious? | Current interface wording | Avoids relying on "obvious" |
| Do any art. 111 transitional rules apply? | Pilot start date | Possible different dates |
| Would logs analysed per employee move it into Annex III point 4(b)? | Who can see logs and for what purpose | It would change the category |
| Is the employee-representative consultation (CSE) required? | Rollout to about 1,800 staff, logging | Art. 26(7) does not apply at this category, so this is for labour law and HR |
| DPO: is a DPIA needed (GDPR art. 35)? | Prompts and logs may contain personal data | Outside this memo |

This memo is a checklist for counsel, not a conformity assessment.