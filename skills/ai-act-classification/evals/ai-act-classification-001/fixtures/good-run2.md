# AI Act classification memo: CV scoring and ranking tool

**Freshness:** the skill was verified on 2026-11-04, which is today. Counsel should still check the application dates against EUR-Lex.

## System and role
| System or step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| CV scoring and ranking (about 25,000 CVs a year, store and warehouse jobs) | Reads CVs, scores each against the job description and ranks them. Recruiters see the top 30 per job and can open the rest. | **L3**, on my reading. The AI filters and ranks, and no human validates every output. Anyone outside the top 30 is effectively deprioritised. | **Deployer** (art. 3(4)). The vendor is the provider (art. 3(3)). |

You stay a deployer only while you use the tool as is. You become a provider (art. 25(1)) if you put your name on it, modify it substantially, or change its purpose. Don't reconfigure it beyond what the vendor's instructions allow without asking counsel.

## Prohibited practices (art. 5)
None identified. I checked 5(1)(a)-(c), 5(1)(f) and 5(1)(g). The tool reads CVs only, so emotion recognition and biometric categorisation shouldn't be in play. **Confirm with the vendor** that it does not analyse photos, video or voice, and does not infer sensitive traits.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| **High-risk** | Art. 6(2), **Annex III point 4(a)**: analysing and filtering job applications and evaluating candidates | The tool scores and ranks candidates for recruitment. | Art. 6(3) exception (below) |

**Art. 6(3) exception: question for counsel.** I don't see it applying, for two reasons:
- The exception never applies when the system profiles natural persons. Scoring candidates against criteria looks like profiling.
- Ranking decides who gets seen. That is a material influence on the outcome, and the exception requires there to be none.

The vendor would also have to have documented the assessment and registered the system (arts. 6(4), 49(2)). Ask whether it did.

## Transparency (art. 50)
Nothing is triggered by the CV scoring as described. It becomes relevant if you add a candidate chatbot (art. 50(1)) or generated text sent to candidates.

## General-purpose model
It is unknown whether the vendor builds on a general-purpose model. If so, the art. 53 and 55 obligations sit with the model provider, not with you or probably the vendor. Ask the vendor which model it uses and what documentation it holds under art. 53(1)(b). Your system is classified on its own use either way.

## Obligations
| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| You | Support the AI literacy of the staff who use the tool | 4 | **Already applies** (2 Feb 2025) | HR / training |
| You | Use per the vendor's instructions, with technical and organisational measures | 26(1) | 2 Dec 2027 | HR + IT |
| You | Human oversight by competent, trained people with real authority to override | 26(2) | 2 Dec 2027 | HR (recruiters) |
| You | Input data relevant and representative, where you control it (CVs, job descriptions, criteria) | 26(4) | 2 Dec 2027 | HR |
| You | Monitor operation. On a risk, suspend use and inform the vendor and authority. Report serious incidents to the vendor first. | 26(5) | 2 Dec 2027 | HR + vendor management |
| You | Keep logs under your control for at least 6 months, reconciled with GDPR retention limits for candidate data | 26(6) | 2 Dec 2027 | IT / DPO |
| You | Inform workers' representatives and affected workers before use at the workplace | 26(7) | 2 Dec 2027 | HR (see counsel questions) |
| You | Use the vendor's information for the GDPR impact assessment | 26(9) | 2 Dec 2027 | DPO |
| You | Inform candidates that a high-risk system assists decisions about them | 26(11) | 2 Dec 2027 | HR |
| You | On request, explain the system's role in a decision with significant adverse effects | 86 | Counsel to confirm | HR / legal |
| You | Fundamental rights impact assessment | 27 | Likely **not applicable**, since it covers public bodies, public-service providers and Annex III 5(b)-(c). Counsel to confirm. | n/a |
| Vendor | Risk management, data governance, documentation, logging, instructions, oversight design, accuracy, quality management, conformity assessment, registration, post-market monitoring | 9–15, 17, 43, 49, 72–73 | 2 Dec 2027 (72–73: counsel to confirm) | Vendor |

**What "AI Act compliant" does not cover.** The vendor's claim can't transfer the art. 26 duties above, which are yours as deployer. Annex III obligations only start on 2 December 2027, so today the claim can't mean full conformity with arts. 9–15. Ask the vendor for these in the contract:
- Instructions for use (art. 13).
- A statement of the intended purpose.
- Its conformity route and EU database registration.
- Access to logs.
- Bias testing and accuracy results.
- Incident notification terms.
- A commitment to tell you about substantial changes.

## If a step moves to L+1
| Step | From → to | What changes | Obligations that appear or tighten |
| --- | --- | --- | --- |
| Ranking | L3 → L4 (auto-reject or auto-shortlist, with no human opening the rest) | Oversight becomes much harder to show in practice. GDPR art. 22 on solely automated decisions is also likely to be engaged. | Art. 14 and art. 26(2) oversight, art. 86 explanation and art. 26(11) information to candidates all tighten |
| Scope | Extended to internal promotion, task allocation or performance monitoring | Falls under Annex III **point 4(b)** | Same high-risk regime, plus workers' representative information (art. 26(7)) |

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Does the art. 6(3) exception apply, or does profiling exclude it? | Scoring and ranking method, whether recruiters in practice read only the top 30 | It decides whether the tool is high-risk at all |
| Does anything we configure make us a provider (art. 25)? | The vendor contract, and whether we adjust criteria, weights or the model | It would move the provider duties to us |
| When do arts. 72–73 and 86 apply to an Annex III system? | The 2 Dec 2027 date | It affects incident reporting and the explanation right |
| Is art. 26(7) triggered for applicants, and how does it fit with CSE information or consultation (France)? | Whether the tool also touches internal candidates or staff | It decides whether and when to inform employee representatives |
| Is the FRIA (art. 27) out of scope for us? | Whether we provide any public service | It would add an assessment before first use |
| How do the AI Act and GDPR interact here (art. 22, profiling, retention, DPIA)? | Data flows, vendor hosting and retention periods | Both regimes apply to the same processing, and GDPR applies now |

**Practical next steps:**
1. Run the `dpia-prescreen` skill (GDPR impact assessment) and the `cse-consultation` skill (employee representatives).
2. Send the vendor the contract requests above.
3. Plan recruiter training now. AI literacy (art. 4) already applies.
4. Decide how recruiters will actually use the ranking, so that "can open the rest" is a real, documented practice and not just a possibility.

This memo is a checklist for counsel, not a conformity assessment.