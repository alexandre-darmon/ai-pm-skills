# AI Act classification memo: CV screening and ranking tool

**Freshness:** I couldn't read the skill's `last_verified` date (the lookup was denied). Counsel should confirm the application dates below. They follow the AI Act as amended by Regulation (EU) 2026/1744.

## Short answer
Yes, this is almost certainly a high-risk system, and you are its **deployer**. The vendor's "AI Act compliant" claim covers the vendor's own duties as provider. It doesn't transfer your duties, and I can't verify the claim from here.

## System and role
| System | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| CV scoring and ranking | Scores each candidate against the job description, ranks them, and shows recruiters the top 30 per job. | L2 if recruiters validate every outcome. In practice it may sit closer to L3, because candidates outside the top 30 are rarely opened. | Deployer (art. 3(4)). The vendor is the provider (art. 3(3)). |

You stay a deployer only if you use the tool as is. You become a provider (art. 25(1)) if you put your name on it, substantially modify it, or change its purpose.

## Prohibited practices (art. 5)
I found no hit on the facts given. I checked these points:
- **Art. 5(1)(f):** emotion recognition at work. Ask the vendor whether the tool analyses video, voice or facial features. If it does, that is a question for counsel.
- **Art. 5(1)(g):** biometric categorisation to infer sensitive traits.
- **Art. 5(1)(c):** social scoring. Check that the tool doesn't use data from unrelated contexts, such as social media profiling.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| High-risk | Art. 6(2), Annex III point 4(a): AI used to analyse and filter applications and evaluate candidates. | The tool scores and ranks candidates for recruitment. | The art. 6(3) exception, below. |

**Art. 6(3) exception (question for counsel):** I would not expect it to apply, for these reasons.
- The ranking materially influences who gets seen. Candidates outside the top 30 are practically filtered out, even though they are technically visible.
- The exception never applies if the system profiles natural persons. Scoring individuals against a job profile likely counts as profiling.

The vendor may argue that the tool is only "preparatory" under art. 6(3)(d). If so, it must have documented that assessment and registered the system (arts. 6(4), 49(2)). Ask to see both.

## Transparency (art. 50)
Art. 50(1) applies only if candidates interact directly with an AI system, such as a chatbot, and that isn't obvious. A back-office ranking tool doesn't trigger it. Candidates must still be informed under art. 26(11), covered below.

## General-purpose model
Unknown. Ask the vendor whether the tool is built on a general-purpose model. Ask for the documentation it receives from that model's provider (art. 53(1)(b)). The model-provider duties stay with the model provider, and you are not affected as the deployer.

## Obligations
| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| You (deployer) | Measures to support AI literacy of the staff who use the tool. | 4 | Already applicable (2 Feb 2025) | HR with training |
| You | Use the tool per the provider's instructions, with technical and organisational measures. | 26(1) | 2 Dec 2027 | HR |
| You | Human oversight by trained, competent people with real authority to override. | 26(2) | 2 Dec 2027 | HR |
| You | Input data (CVs, job descriptions) relevant and representative, where you control it. | 26(4) | 2 Dec 2027 | HR |
| You | Monitor operation. On a risk, suspend use and inform the provider and the authority. Report serious incidents to the provider first. | 26(5) | 2 Dec 2027 | HR with the vendor |
| You | Keep logs under your control for at least six months, unless GDPR or other law requires otherwise. | 26(6) | 2 Dec 2027 | IT |
| You | Inform workers' representatives and affected workers before use. In France this feeds the CSE process. | 26(7) | 2 Dec 2027 | HR |
| You | Use the vendor's information for your GDPR impact assessment. | 26(9) | 2 Dec 2027 | DPO |
| You | Inform candidates that the system is used in decisions about them. | 26(11) | 2 Dec 2027 | HR |
| You | On request, explain the system's role in a decision with significant adverse effects. | 86 | Open point for counsel | HR and legal |
| Vendor (provider) | Risk management, data governance, documentation, logging, instructions, human oversight design, accuracy, quality management, conformity assessment, registration, post-market monitoring. | 9–17, 43, 49, 72–73 | 2 Dec 2027 for arts. 6–27 | Vendor |

A fundamental rights impact assessment (art. 27) isn't required. You don't appear to be a public body, you don't provide public services, and Annex III point 4(a) isn't one of the points that triggers it for any deployer.

The date is 4 Nov 2026, so the high-risk duties aren't binding yet. Contracts signed now will run past 2 December 2027, so write the duties into them now.

## If the tool moves to L+1
| Step | From → to | What changes | Obligations that tighten |
| --- | --- | --- | --- |
| Ranking | L2 → L3/L4 (for example auto-rejecting below a threshold, or reviewing only a sample) | The classification stays high-risk. Art. 6(3) becomes even harder to argue. | Art. 26(2) oversight must be real. Art. 26(11) and art. 86 become more likely to be triggered. A GDPR art. 22 issue (solely automated decisions) may arise. |

## What to do with the vendor
Put these in the contract or ask for them before signing:
1. The vendor's classification of the tool, and its art. 6(3) assessment if it claims the exception.
2. The conformity assessment and declaration, the CE marking, and the EU database registration (once required).
3. The instructions for use (art. 13), including accuracy, known limits and bias testing across protected groups.
4. Access to logs, support for incident reporting, and a duty to tell you about substantial changes.
5. Your input to the oversight design: what recruiters see, what the score means, and how to override it.

## Practical points beyond the AI Act
- **GDPR:** do a DPIA (`dpia-prescreen`). Scoring candidates at this scale is very likely to need one. Art. 22 limits solely automated decisions.
- **CSE (France):** inform or consult the employee representatives (`cse-consultation`).
- **Oversight in practice:** recruiters seeing only the top 30 may be real oversight or a rubber stamp. Sample the rest regularly and check whether the ranking disadvantages any group.

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Does the art. 6(3) exception apply? | The vendor's documentation, how the score is produced, and whether candidates outside the top 30 are ever reviewed. | It decides whether the whole high-risk regime applies. |
| When do arts. 72–73 and 86 apply to an Annex III system? | The 2026 amendments. | It sets the date for your explanation duty. |
| Does the tool use emotion or biometric analysis? | Vendor feature list. | It could trigger a prohibition (art. 5). |
| Is any modification or rebranding planned? | Contract and configuration. | It could make you a provider (art. 25). |
| Which authority supervises? | French designation law, still a bill at last verification. | The CNIL is proposed for Annex III point 4. |

This memo is a checklist for counsel, not a conformity assessment.