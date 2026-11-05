# AI Act classification memo: CV scoring and ranking tool

**Freshness:** I couldn't see the skill's `last_verified` date. The rules changed in July 2026 (Regulation 2026/1744), so counsel should confirm the application dates.

## System and role
| Step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| Score and rank CVs against the job description | Produces a score and ranking per candidate. Recruiters see the top 30 per job and can open the rest. | L2 on paper (AI produces, human validates). In practice closer to L3 if recruiters rarely open the rest, because the cut-off then decides who gets looked at. | **Deployer** (art. 3(4)). The vendor is the provider (art. 3(3)). |

You stay a deployer only if you use the tool as is. You become the provider if you put your name on it, modify it substantially, or change its purpose (art. 25(1)).

## Prohibited practices (art. 5)
I found none, based on what you described. Counsel should check two points with the vendor:
- The tool must not infer emotions, for example from video or voice (art. 5(1)(f)).
- It must not infer sensitive traits from photos or other data (art. 5(1)(g)).

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| **High-risk** | Art. 6(2), Annex III point 4(a): AI used to recruit, to filter applications and to evaluate candidates | It scores and ranks applicants for jobs | Art. 6(3) exception, below |

**Art. 6(3) exception: question for counsel.** It looks unlikely to help you. It never applies when the system profiles natural persons, and scoring candidates is profiling. It also requires that the system not materially influence the decision, and a top-30 cut-off does influence who gets considered. The provider has to document and register any reliance on the exception (arts. 6(4), 49(2)). Ask the vendor whether it relies on it.

## Transparency (art. 50)
This probably doesn't apply, because candidates don't interact with the tool. It would apply if the tool adds a chatbot, or any emotion recognition or biometric categorisation (art. 50(1), 50(3)).

## General-purpose model
Unknown. Ask the vendor whether the tool is built on a general-purpose model accessed through an API. If it is, the model obligations (art. 53) stay with that model's provider. The vendor should get the documentation owed under art. 53(1)(b).

## Obligations
| Who | Obligation | Article | Applies from |
| --- | --- | --- | --- |
| You and the vendor | Measures to support AI literacy of the recruiters and HR staff who use the tool | 4 | **Already applies** (since 2 Feb 2025) |
| You | Use the tool per the vendor's instructions | 26(1) | 2 Dec 2027 |
| You | Human oversight by trained, competent people with real authority to override | 26(2) | 2 Dec 2027 |
| You | Input data relevant and representative, where you control it (job descriptions, CV intake) | 26(4) | 2 Dec 2027 |
| You | Monitor use. On a risk, suspend use and inform the vendor, and report serious incidents to the vendor first. | 26(5) | 2 Dec 2027 |
| You | Keep the logs you control for at least 6 months, or longer if GDPR or other law requires | 26(6) | 2 Dec 2027 |
| You | Inform workers' representatives and affected workers before use at the workplace | 26(7) | 2 Dec 2027 |
| You | Inform candidates that an Annex III system assists decisions about them | 26(11) | 2 Dec 2027 |
| You | Use the vendor's information for your GDPR impact assessment | 26(9) | 2 Dec 2027 |
| You | Explain the tool's role in a decision to a rejected candidate who asks | 86 | Date to confirm with counsel |
| Vendor | Risk management, data governance, documentation, logging, human oversight design, accuracy, quality management, conformity assessment, registration | 9–17, 43, 49 | 2 Dec 2027 |
| Vendor | Post-market monitoring and serious-incident reporting | 72–73 | Date to confirm with counsel |

A fundamental rights impact assessment (art. 27) is not required on the facts given. It applies to public bodies, private entities providing public services, and deployers of Annex III points 5(b) and 5(c). Counsel should confirm that you aren't a public-service provider.

## What the vendor's "AI Act compliant" claim means for you
- **It doesn't transfer your duties.** Everything in the "You" rows stays yours, whatever the vendor has done.
- **It can't be checked yet.** The high-risk provider obligations only apply from 2 December 2027, so "compliant" today can at most mean "preparing for compliance".
- **Ask for evidence.** Request the instructions for use, the conformity assessment plan, the EU database registration, and the logging and oversight features. Also ask what bias and accuracy testing exists, and whether the tool has been tested on warehouse and store profiles.
- **Put it in the contract.** Cover log access, incident cooperation and notice of material changes. A substantial change could make you the provider.

## If a step moves to L+1
| Step | From → to | What changes | Obligations that tighten |
| --- | --- | --- | --- |
| Ranking | L2/L3 → L4 (auto-rejecting below a threshold or auto-shortlisting) | It becomes a decision about people with no prior human review. | Oversight under art. 26(2) becomes much harder to meet. Art. 86 explanation requests become likely. GDPR art. 22 on solely automated decisions also becomes relevant (that is for `dpia-prescreen`). |

If recruiters in practice look only at the top 30, treat the tool as L3 today, because the ranking is the filter.

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Does the art. 6(3) exception apply? | The tool ranks candidates, it profiles, and recruiters work from the top 30. | It decides whether the whole high-risk regime applies. I expect not. |
| Are we a pure deployer? | The tool is used as is. Do we configure scoring criteria or weights, or supply our own training data? | Configuration or fine-tuning could trigger art. 25. |
| When do arts. 72–73 and 86 apply to an Annex III system? | The dates in the table above. | The Omnibus left this open. |
| Does the vendor's claim hold up? | Vendor documents and contract terms. | You can't rely on the claim as it stands. |
| Which authority supervises us in France? | The designation is still only a bill (DDADUE). | The CNIL is the proposed authority for employment systems. |

**Adjacent checks outside this memo:**
- `dpia-prescreen` for GDPR. CV scoring at 25,000 CVs a year almost certainly needs a DPIA.
- `cse-consultation` for employee-representative information, if you are in France.

This memo is a checklist for counsel, not a conformity assessment.