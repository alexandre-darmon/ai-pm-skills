# AI Act classification memo: IT helpdesk chatbot

**Freshness:** I couldn't read the skill's `last_verified` date, so I can't tell whether it's more than 90 days old. Counsel should confirm the application dates and guidance status. The draft high-risk classification guidelines (19 May 2026) were still not adopted when the reference map was last verified.

## System and role

| System or step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| Answers employee IT questions from internal documentation | Generates text answers and links to the ticketing tool. It decides nothing and takes no action. | L1 (assisted). The employee reads the answer and acts on it, and no one validates each output. | Provider of the chatbot system (art. 3(3)) and deployer (art. 3(4)). Your IT team had it built and uses it under your name. This is a judgement call, listed in the questions for counsel. |

## Prohibited practices (art. 5)

None identified. I checked these points:
- **5(1)(a)-(b):** the chatbot answers IT questions and has no manipulative design.
- **5(1)(c):** it does no scoring.
- **5(1)(f):** it does no emotion recognition.
- **5(1)(g):** it does no biometric categorisation.

I didn't check 5(1)(ba)-(bb), which apply from 2 December 2026, because they concern intimate or abuse content, which doesn't fit this use.

## Risk category

| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| Transparency obligations (limited risk) | Art. 50(1), and possibly 50(2). It is not high-risk under Annex III (no point matches). | IT support Q&A. No decision about individuals. No recruitment, task allocation, performance monitoring or evaluation (so not point 4(a) or 4(b)). No credit, insurance or essential-service use (points 5(a)-(c) don't apply). | Use of conversation logs (see questions for counsel). |

Art. 6(3) exception: not relevant, because no Annex III point is engaged. If logs were used to evaluate employee behaviour (point 4(b)), this would need to be re-run. That would also be a purpose change under art. 25(1).

## Transparency (art. 50)

- **Art. 50(1):** people must be told they are talking to an AI unless it is obvious. This falls on the provider, and so on your IT team. It has applied since 2 August 2026. Check that the chat interface says plainly that the user is talking to an AI. Don't rely on the "obvious" exception.
- **Art. 50(2):** providers of systems that generate synthetic text must mark the output in a machine-readable way. The assistive-editing exception does not obviously fit a chatbot. It is unclear whether this falls on you or is covered by the vendor's marking, so it is a question for counsel. If the chatbot was in service before 2 August 2026, the reference map gives a transition to 2 December 2026 for generative systems (art. 111(4)). Your rollout date makes this urgent.
- **Art. 50(3) and 50(4):** not applicable. There is no emotion recognition or biometric categorisation, and nothing is published to the public.

## General-purpose model

- **Model and provider:** the commercial LLM from the vendor, called through its API. Please fill in the vendor and model name.
- **Your position:** calling a model through an API does not make you the model's provider. Arts. 53 and 55 stay with the vendor.
- **Fine-tuning:** I've assumed none. If there is any, counsel needs the compute figures against the one-third threshold.
- **Ask the vendor** for the downstream documentation it owes under art. 53(1)(b).
- **"AI Act compliant" claims:** a vendor claim does not transfer your own duties as provider and deployer of the chatbot.

## Obligations

| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| Provider and deployer | Support the AI literacy of the staff who operate or use the system. No required level. | 4 | 2 Feb 2025 | IT lead / HR |
| Provider | Tell users they are interacting with an AI. | 50(1) | 2 Aug 2026 | IT product owner |
| Provider | Mark generated text, if art. 50(2) applies. | 50(2) | 2 Aug 2026, or 2 Dec 2026 for systems placed earlier | Counsel to decide, then IT |
| Model vendor | General-purpose model duties, including downstream documentation. | 53 | 2 Aug 2025 | Vendor. You request the documentation. |
| Provider and deployer | High-risk duties (arts. 9–27). | — | Not triggered on current facts. | — |

GDPR duties are outside this memo. The `dpia-prescreen` skill covers the pre-screen. Chat logs may contain personal data.

## If a step moves to L+1

| Step | From → to | What changes in the classification | Obligations that appear or tighten |
| --- | --- | --- | --- |
| Answering questions | L1 → L2 | Little changes. A human validating outputs adds no new category. | Logging. |
| Actions such as resetting passwords, granting access or filing tickets | L1 → L4 | Still not Annex III by itself, but it now acts and needs an action-guardrail review. | Human oversight design (art. 14, if it ever became high-risk), the high-risk classification check, a model card, and the `system-prompt-and-guardrails` work. |
| Using logs to assess or rank employees, or to allocate tasks | Purpose change | Annex III point 4(b), so high-risk. You would be a provider under art. 25(1). | Arts. 9–15, 17, 26, 43, 49. Workers' representatives and affected workers must be informed (art. 26(7)). From 2 Dec 2027. |

## Questions for counsel

| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Are we the provider of the chatbot, or only a deployer? | Built in-house by IT on a vendor API, put into service under our name. | It decides who owes the art. 50 duties. |
| Does art. 50(2) marking fall on us, and does the vendor's marking suffice? | Vendor's marking features. Output is shown as text in chat. | Possible gap in obligations. |
| Was the chatbot placed in service before 2 Aug 2026 (art. 111(4) transition)? | Pilot or go-live dates. | The 2 Dec 2026 deadline is close. |
| Are any conversation logs used to monitor or evaluate employees? | Who accesses the logs, for what purpose, and what the retention policy is. | This could bring Annex III point 4(b) into play. |
| Does the chatbot operate in the EU or only for EU staff? | Country or countries of the 1,800 employees. | It determines scope under art. 2. |
| Do arts. 72–73 and 86 matter here? | Not applicable if the system isn't high-risk. | Open point from the reference map. |

This memo is a checklist for counsel, not a conformity assessment.

**Facts I assumed and you should confirm:**
- The chatbot is used only in the EU.
- It has no fine-tuning.
- It gives users no consequential decisions.
- It sits at L1.