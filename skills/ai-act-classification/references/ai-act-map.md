# AI Act map

Working map of Regulation (EU) 2024/1689 for `ai-act-classification`, in the repo's own words, as amended by Regulation (EU) 2026/1744 (the "Digital Omnibus on AI", OJ L of 24 July 2026, in force since 27 July 2026). It points to the articles; it does not replace them. Before citing a date, check the consolidated text on EUR-Lex (CELEX 32024R1689) and any corrigendum. Last verified: see the skill's `last_verified`.

## Application dates (art. 113, as amended)

| From | What applies |
| --- | --- |
| 1 August 2024 | Entry into force |
| 2 February 2025 | Chapters I and II: general provisions, AI literacy (art. 4), prohibited practices (art. 5) |
| 2 August 2025 | Notifying authorities and notified bodies (Chapter III Section 4), general-purpose AI models (arts. 51–56), governance, penalties, confidentiality (art. 78); art. 101 (fines on model providers) from 2 August 2026 |
| 2 August 2026 | General date: everything not listed elsewhere, including transparency (art. 50) and arts. 40–49 |
| 27 July 2026 | Arts. 102–110 (amendments to other EU acts), art. 113(3)(d) |
| 2 December 2026 | New prohibitions art. 5(1)(ba)-(bb) and 5(1a)-(1b); art. 50(2) marking for generative systems placed on the market before 2 August 2026 (art. 111(4)) |
| 2 December 2027 | Chapter III Sections 1–3 (arts. 6–27, except art. 6(5)) for Annex III high-risk systems (art. 6(2)) |
| 2 August 2028 | Chapter III Sections 1–3 for high-risk systems under art. 6(1) (Annex I products) |

Open point for counsel: when the high-risk provisions outside Chapter III Sections 1–3 (post-market monitoring and incident reporting, arts. 72–73; right to an explanation, art. 86) bite for an Annex III system.

What else the Omnibus changed: art. 4 rewritten (support literacy, no required level); new art. 4a (special-category data for bias detection, under conditions); simplified technical documentation and proportionate quality management for SMEs and small mid-caps (arts. 11(1), 17(2), 63(1)); art. 6(1a)-(1c) narrowing "safety component"; machinery moved to Annex I Section B; Annex VIII Section B shortened; art. 27(4) lets the fundamental rights impact assessment refer to the GDPR impact assessment.

## Roles (art. 3)

| Role | Who | Article |
| --- | --- | --- |
| Provider | develops an AI system or general-purpose model, or has it developed, and places it on the market or puts it into service under its own name | 3(3) |
| Deployer | uses an AI system under its authority, outside personal non-professional use | 3(4) |
| Deployer turned provider | puts its name on a high-risk system, substantially modifies it, or changes its intended purpose so that it becomes high-risk | 25(1) |
| Provider of a modified general-purpose model | modifies or fine-tunes a model with more than one third of the original training compute (Commission guidelines on model providers); obligations limited to the modification | 3(3), recital 109 |

## Prohibited practices (art. 5)

| Point | Practice |
| --- | --- |
| 5(1)(a) | subliminal, manipulative or deceptive techniques that materially distort behaviour and cause, or are reasonably likely to cause, significant harm |
| 5(1)(b) | exploiting vulnerabilities due to age, disability or a social or economic situation, with the same distortion and harm |
| 5(1)(ba) | from 2 December 2026: generating realistic intimate or sexually explicit material of an identifiable person without explicit consent |
| 5(1)(bb) | from 2 December 2026: generating child sexual abuse material |
| 5(1)(c) | social scoring over time that leads to detrimental treatment in unrelated contexts, or treatment unjustified or disproportionate to the behaviour |
| 5(1)(d) | predicting criminal offences based only on profiling or personality traits |
| 5(1)(e) | untargeted scraping of facial images to build facial recognition databases |
| 5(1)(f) | emotion recognition in the workplace and in education, except for medical or safety reasons |
| 5(1)(g) | biometric categorisation of individuals to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation |
| 5(1)(h) | real-time remote biometric identification in public spaces for law enforcement, with narrow exceptions |

Arts. 5(1a)-(1b) limit (ba) and (bb): for providers, when that output is the intended purpose, or foreseeable without adequate safeguards; for deployers, when they use the system for it.

## High-risk: Annex III points most product teams meet

| Point | Area | Examples |
| --- | --- | --- |
| 1 | Biometrics | remote biometric identification, biometric categorisation, emotion recognition (where not prohibited) |
| 2 | Critical infrastructure | safety components in digital infrastructure, road traffic, water, gas, heating, electricity |
| 3 | Education and vocational training | admission, evaluating learning outcomes, steering learning, proctoring |
| 4(a) | Employment: recruitment | targeted job ads, analysing and filtering applications, evaluating candidates |
| 4(b) | Employment: work relationship | decisions on terms, promotion, termination; task allocation based on behaviour or traits; monitoring and evaluating performance and behaviour |
| 5(a) | Public assistance | systems used by or for public authorities to decide eligibility for essential public benefits and services; a private company's own eligibility tool is not covered here |
| 5(b) | Credit | creditworthiness or credit score of natural persons, except fraud detection |
| 5(c) | Insurance | risk assessment and pricing for natural persons in life and health insurance |
| 5(d) | Emergency | evaluating and classifying emergency calls, dispatch, triage |
| 6, 7, 8 | Law enforcement, migration, justice and democratic processes | |

Exception (art. 6(3)): an Annex III system is not high-risk when it poses no significant risk of harm to health, safety or fundamental rights, including by not materially influencing the outcome of decisions, and at least one of these holds: (a) a narrow procedural task; (b) it improves the result of a previously completed human activity; (c) it detects decision patterns or deviations without replacing or influencing the completed human assessment without proper review; (d) a preparatory task to an Annex III assessment. It never applies when the system profiles natural persons. A provider relying on it documents the assessment before placing the system on the market or putting it into service, and registers it (arts. 6(4), 49(2)). Commission guidelines on high-risk classification: draft of 19 May 2026, not yet adopted at last verification.

## Obligations

| Who | Obligation | Article |
| --- | --- | --- |
| Providers and deployers | take measures to support the AI literacy of staff and others operating or using the system on their behalf; no required level | 4 (as replaced by Reg. 2026/1744) |
| Provider, high-risk | risk management system | 9 |
| | data and data governance | 10 |
| | technical documentation (simplified form for SMEs and small mid-caps) | 11 |
| | automatic logging | 12 |
| | transparency and instructions for use to deployers | 13 |
| | human oversight designed in | 14 |
| | accuracy, robustness, cybersecurity | 15 |
| | quality management system | 17 |
| | conformity assessment, declaration, CE marking | 43, 47, 48 |
| | registration in the EU database | 49 |
| | post-market monitoring; serious incident reporting | 72, 73 |
| Deployer, high-risk | use according to the instructions; technical and organisational measures | 26(1) |
| | human oversight by competent, trained people with the necessary authority and support | 26(2) |
| | input data relevant and sufficiently representative for the purpose, to the extent the deployer controls it | 26(4) |
| | monitor operation per the instructions; on a risk, inform provider and market surveillance authority and suspend use; report serious incidents to the provider first, then importer or distributor and authorities (financial institutions: internal governance rules count) | 26(5) |
| | keep the logs under its control for a period appropriate to the purpose, at least six months unless EU or national law (e.g. GDPR) says otherwise; financial institutions within their financial-services documentation | 26(6) |
| | inform workers' representatives and affected workers before putting into service at the workplace | 26(7) |
| | use the provider's information for the GDPR impact assessment | 26(9) |
| | inform natural persons subject to decisions made or assisted by an Annex III system | 26(11) |
| Deployer, Annex III high-risk (except point 2): public bodies, private entities providing public services, and any deployer of 5(b) or 5(c) | fundamental rights impact assessment before first use, updated when its elements change, results notified to the market surveillance authority; may refer to the GDPR impact assessment | 27 |
| Deployer, towards an affected person | on request, clear explanation of the system's role and the main elements of a decision based on an Annex III output (except point 2) with legal or similarly significant adverse effects, unless EU law already provides it | 86 |
| Provider | people told they interact with an AI system, unless obvious to a reasonably well-informed person | 50(1) |
| Provider | synthetic audio, image, video or text marked in a machine-readable, detectable way (not for assistive standard editing) | 50(2) |
| Deployer | people exposed to emotion recognition or biometric categorisation informed | 50(3) |
| Deployer | deep fakes disclosed; AI-generated text published to inform the public on matters of public interest disclosed unless human-reviewed under editorial responsibility | 50(4) |
| General-purpose model provider | technical documentation (a), information for downstream providers (b), copyright policy (c), public training-content summary (d); open-source models without systemic risk exempt from (a)-(b) | 53 |
| General-purpose model provider, systemic risk | evaluation with adversarial testing, systemic-risk mitigation, serious incident reporting, cybersecurity | 55 |

## Guidance status

Final: Commission guidelines on the AI system definition (6 February 2025) and on prohibited practices (4 February 2025), and on general-purpose model provider obligations. Draft: high-risk classification guidelines (19 May 2026). Guidelines are not binding.

## France

Status at last verification: no French law yet designates the AI Act authorities (art. 70). The designations are in the "DDADUE" bill (Senate text n° 118, 2025-2026, adopted by the Senate on 18 February 2026, pending first reading at the Assemblée nationale as n° 2518). As proposed, subject to change: DGCCRF coordinates market surveillance and is the single point of contact; the CNIL covers most prohibited practices and most Annex III points, including employment (point 4); the ACPR covers credit scoring and life and health insurance pricing (5(b)-(c)) for the entities it supervises; Arcom covers parts of art. 50; sector authorities keep Annex I products. Check Légifrance for the promulgated text before naming an authority.
