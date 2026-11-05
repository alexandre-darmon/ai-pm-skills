# AI Act classification memo: CV scoring and ranking tool

**Freshness:** I couldn't see the skill's `last_verified` date. Its reference map cites developments up to July 2026, and today is 4 November 2026. If the verification is more than 90 days old, counsel should confirm the application dates.

## System and role
| System or step | What it does and decides | Autonomy level | Role |
| --- | --- | --- | --- |
| CV scoring and ranking | Reads about 25,000 CVs a year, scores each candidate against the job description and ranks them. Recruiters see the top 30 per job. | Closest to L3. The AI produces the ranking and humans review the top 30. The rest are only opened if a recruiter chooses to. | **Deployer** (art. 3(4)), as long as you use the tool as is |

The deployer role changes in two cases (art. 25(1)). You become a provider if you put your own name on the tool, modify it substantially, or change its purpose. Configuring job descriptions within the vendor's instructions should not trigger this, but counsel should confirm.

## Prohibited practices (art. 5)
Nothing identified from what you described. I checked 5(1)(a)-(c) and 5(1)(f)-(g). Two facts would change that:
- **Emotion or biometric inference:** a hit is possible if the tool infers emotions, or sensitive traits from photos, video or interviews (5(1)(f) and (g)).
- **Out-of-context signals:** a hit is possible if it uses signals unrelated to the job, such as social media, which raises the social-scoring question under 5(1)(c).

Ask the vendor to confirm in writing what inputs it uses.

## Risk category
| Category | Basis | Facts it rests on | Open point |
| --- | --- | --- | --- |
| **High-risk** | Annex III point 4(a), via art. 6(2): "analysing and filtering applications, evaluating candidates" | The tool scores and ranks candidates for recruitment | Art. 6(3) exception, below |

**Art. 6(3) exception: question for counsel.** It looks unlikely to apply, for two reasons:
- The exception never applies when the system profiles natural persons, and scoring a candidate against a job profile is a strong candidate for profiling.
- The ranking steers which CVs get read, so it arguably influences the decision materially. Only the top 30 get attention by default.

The vendor may rely on the exception and register the system on that basis. If so, counsel should ask what its assessment says (arts. 6(4), 49(2)).

## Transparency (art. 50)
This is probably not the main issue. Candidates do not interact with the tool directly, and it generates no synthetic content. Check the candidate-facing parts, such as chatbots or automated emails, if the product has any (art. 50(1)).

## General-purpose model
Unknown. Ask the vendor whether the tool runs on a general-purpose model through an API, and which one. Obligations for the model (art. 53) stay with the model provider, not with you. Ask the vendor what documentation it receives under art. 53(1)(b).

## Obligations
| Who | Obligation | Article | Applies from | Owner |
| --- | --- | --- | --- | --- |
| You | Support AI literacy of the staff using the tool, with no required level | 4 | **Now** (since 2 Feb 2025) | HR and training |
| You | Use the tool per the vendor's instructions, with technical and organisational measures | 26(1) | 2 Dec 2027 | HR and IT |
| You | Human oversight by trained people with authority to override the ranking, and a guard against over-reliance on the top 30 | 26(2) | 2 Dec 2027 | HR |
| You | Make sure CV and job-description inputs you control are relevant and representative | 26(4) | 2 Dec 2027 | HR |
| You | Monitor the tool. On a risk, suspend use and inform the vendor and the authority. Report serious incidents to the vendor first. | 26(5) | 2 Dec 2027 | HR and compliance |
| You | Keep the logs you control for at least six months, or longer if GDPR or other law requires | 26(6) | 2 Dec 2027 | IT |
| You | Inform workers' representatives and affected workers before use at the workplace | 26(7) | 2 Dec 2027 | HR |
| You | Inform candidates that an Annex III system assists decisions about them | 26(11) | 2 Dec 2027 | HR and legal |
| You | Use the vendor's information for your GDPR impact assessment | 26(9) | 2 Dec 2027 | DPO |
| You | On request, explain the tool's role in a decision with significant adverse effects (e.g. a rejection) | 86 | Date to confirm | HR and legal |
| Vendor | Arts. 9–15 (risk management, data governance, documentation, logging, instructions, human oversight design, accuracy), art. 17 (quality management), art. 43 (conformity assessment), art. 49 (registration), arts. 72–73 (post-market monitoring and incident reporting) | as listed | 2 Dec 2027 (arts. 72–73 to confirm) | Vendor |

A fundamental rights impact assessment (art. 27) does not look required. You are a private employer, and the other triggers are public bodies, public services and Annex III 5(b)-(c). That holds only if you provide no public service, so confirm it with counsel.

## What "AI Act compliant" means for you
It does not transfer your duties. Everything under art. 26 stays with you, even if the vendor's own obligations are fully met. As of today the high-risk rules are not yet in force for Annex III systems (2 December 2027). So the claim can only mean the vendor is preparing, or relying on the art. 6(3) exception. Ask for the following in the contract and due diligence:
- The classification the vendor assumes, and its art. 6(3) assessment if it has one.
- Instructions for use, and the logs you will have access to.
- Accuracy and bias testing, ideally on warehouse and retail candidate profiles.
- Its commitment to update for the high-risk requirements before December 2027.
- Incident notification and cooperation terms.

## If a step moves to L+1
| Step | From → to | What changes | Obligations that tighten |
| --- | --- | --- | --- |
| Ranking | L3 → L4 (auto-reject below a threshold, or only the top 30 ever seen) | It would clearly decide about people, with no human review before the effect | Art. 14 and 26(2) human oversight, art. 26(11) and 86 (informing and explaining), and GDPR art. 22 (automated decisions) |

Nothing changes in the AI Act category, which is already high-risk. But human oversight becomes much harder to show.

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |
| Does the art. 6(3) exception apply, or is the profiling bar decisive? | How scores are computed, and whether recruiters use the top 30 as a shortlist | Decides whether art. 26 applies to you at all |
| Is the "top 30, rest on demand" design enough human oversight, or effectively automated filtering? | How often recruiters open CVs beyond the top 30, and whether they can override | Art. 26(2), art. 86, and GDPR art. 22 |
| Do we stay a deployer? | Contract, branding, any configuration beyond the vendor's instructions | Art. 25(1) |
| When do arts. 72–73 and 86 apply to an Annex III system? | Not a fact question | The map leaves this open |
| Do you provide a public service, or operate in a sector with extra rules? | Business activities | Art. 27 |
| Do worker-representative duties apply to candidates? | Country and works-council structure | Art. 26(7). Candidates are not yet workers, but existing staff may be affected. |
| Is a GDPR impact assessment needed? | Processing of candidate data at scale | Separate from the AI Act. See the `dpia-prescreen` skill. |

## What to do now, before 2027
1. Start AI literacy for the recruiters who will use the tool. This applies today.
2. Get the vendor's classification and its art. 6(3) position in writing.
3. Run a DPIA pre-screen, because the GDPR applies now.
4. Draft the candidate notice (art. 26(11)) and a process for explaining a rejection (art. 86).
5. Define what "meaningful human oversight" means in the recruiter workflow, including how often to look beyond the top 30.

This memo is a checklist for counsel, not a conformity assessment.