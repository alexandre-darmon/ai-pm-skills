# Vendor checks

Working checklist for `ai-vendor-evaluation`, in the repo's own words. It points to the articles; it does not replace them. Last verified: 2026-11-09 on EUR-Lex (Regulation (EU) 2022/2554 DORA, Regulation (EU) 2016/679 GDPR, Regulation (EU) 2024/1689 AI Act as amended by Regulation (EU) 2026/1744). Check the consolidated texts before citing a paragraph to a vendor or a regulator.

## Evidence status

Every document or clause gets one status: **on file** (link, version, date) · **claimed** (the vendor says so, nothing shown) · **missing** (asked, not provided) · **not due yet** (the duty applies later; say from when). A status records paper, not conformity. Whether the paper is enough is counsel's call.

## Bake-off design

| Check | Why |
| --- | --- |
| Cases come from `build-evals`, classes and thresholds signed before the first vendor run | a bar drawn after the scores only describes them |
| The current process (or product) runs on the same cases | the vendor must beat what you have, not zero |
| Same inputs, same format, same configuration time, same instructions for every vendor | a vendor given more help scores higher for the wrong reason |
| A small tuning slice, the same for all; the scored cases are never shown with their expected outputs | blind: no vendor tunes on the answers |
| A private holdout never sent to any vendor, kept for the renewal and every model change | a re-test on cases the vendor has seen measures memory |
| Product version, model version and run date recorded per vendor | without them a later score cannot be compared |
| Generative product: each case run at least twice | outputs vary from run to run |
| Score the business unit (document, file, answer accepted), per class, Wilson interval per class | a field-level rate overstates the outcome; fields of one document are not independent |
| Paired comparison: d = cases where exactly one vendor is right; gap < 2√d / n is a tie | references/eval-statistics.md §5 |
| Class sizing for the margin the decision needs | references/eval-statistics.md §3 |

## Benchmark audit

A benchmark score describes the benchmark's cases and grader as much as the product. Before a vendor's own benchmark or a public leaderboard gets any weight, run three checks. For a public benchmark you run them; for a vendor's own, ask the vendor to run them and show the outputs.

| Check | How | Reading |
| --- | --- | --- |
| Do-nothing answer | Send the grader an empty output, the input copied back, or one constant answer for every case; for an agent, a run that takes no action | Every case it passes is a case the grader passes without the task done: the published score is inflated by at least that share |
| Known-wrong answer | Send well-formed answers you know are wrong: a value from another document, a plausible false amount, the task done on the wrong record | A grader that passes them checks format, not correctness |
| Contamination | Build a fresh matched set: same document types, same difficulty, same scoring, never published, collected after the model's training cut-off. Score the product on both sets | The gap between the public score and the matched-set score estimates what the model learnt from the public cases. A gap wider than both intervals means the public score does not transfer |

A vendor that will not run the first two checks on its own benchmark leaves its figure *claimed*. Your bake-off set measures the vendor's claim only where it matches the claim's document types and difficulty; elsewhere the gap also holds the difference between their data and yours, so record it as *not reproduced on your data*, not as contamination. Publishing a set makes it a training target: a public score ages, your private holdout does not. If the product can flag a field for review instead of guessing, score correct, flagged and wrong apart (references/eval-statistics.md §12); if the inputs vary in layout or wording, check the score on reworded variants (§13).

## GDPR (Regulation (EU) 2016/679)

| Point | What to check in the vendor's terms |
| --- | --- |
| Art. 28(1) | the vendor gives sufficient guarantees of technical and organisational measures |
| Art. 28(2) | no sub-processor without your written authorisation; under a general authorisation, notice of each addition or replacement and a right to object |
| Art. 28(3)(a) | processing only on your documented instructions, transfers included |
| Art. 28(3)(b)-(c) | staff bound by confidentiality; security measures of art. 32 |
| Art. 28(3)(e)-(f) | help with data subject requests and with arts. 32–36 (security, breach, DPIA) |
| Art. 28(3)(g) | at the end, deletion or return of all personal data, at your choice |
| Art. 28(3)(h) | information to demonstrate compliance; audits and inspections by you or your auditor |
| Art. 28(4) | the same duties flow down to sub-processors, the model provider behind the product included |
| Art. 28(10) | a processor that decides its own purposes is treated as a controller for that processing: a vendor that trains its models on your customers' data is acting for its own purpose; question for counsel and the DPO |
| Art. 9 | health and other special-category data (claims, HR files) need a specific condition; trial data are anonymised first |
| Chapter V (arts. 44–49) | any transfer outside the EEA, sub-processors included, has a transfer basis |

Trial data: anonymised (no route back to a person, checked on a sample) or under a signed processing agreement. Pseudonymised data remain personal data.

## AI Act (Regulation (EU) 2024/1689, as amended)

| Document or duty | Article | Who owes it | Note |
| --- | --- | --- | --- |
| Instructions for use: intended purpose, accuracy levels and metrics tested, robustness, known limits | 13(3)(b)(i)-(ii), 15(3) | provider of a high-risk system | put the declared accuracy next to your bake-off interval per class |
| Pre-determined changes to the system and its performance | 13(3)(c) | provider | what the vendor may change without a new assessment |
| Log mechanisms for deployers | 13(3)(f), 12 | provider | what you can collect and keep |
| EU declaration of conformity | 47 | provider | high-risk only |
| Registration in the EU database | 49 | provider | high-risk only |
| New conformity assessment after a substantial modification | 43(4) | provider | whether a model swap is a substantial modification: question for counsel |
| Use per the instructions, oversight, monitoring, logs kept at least six months | 26(1), 26(2), 26(5), 26(6) | you, as deployer | the contract must give you the logs and the instructions |
| Transparency to people interacting with a chatbot | 50(1) | provider designs it, you deploy it | applies from 2 August 2026 |

Dates: Annex III high-risk duties from 2 December 2027, Annex I from 2 August 2028 (art. 113 as amended in 2026). Before those dates, ask what exists today and record *not due yet* rather than *missing*. A product built on a general-purpose model: ask which model and version, and what the model provider passes to the vendor (art. 53(1)(b)). Classification itself: `ai-act-classification`.

## DORA (Regulation (EU) 2022/2554), financial entities, applies since 17 January 2025

| Article | In short | AI reading |
| --- | --- | --- |
| 28(1) | the entity stays fully responsible for what it outsources | the vendor's accuracy is your risk |
| 28(3) | register of information on all ICT contracts, critical or important ones apart; yearly report; notice to the authority of planned contracts on critical or important functions | an AI SaaS or model API is an ICT service: it enters the register (templates: Implementing Regulation (EU) 2024/2956) |
| 28(4) | before contracting: is the function critical or important, supervisory conditions, risks incl. concentration, due diligence, conflicts of interest | the entity decides criticality; record who decided |
| 28(5) | providers with appropriate information security standards | |
| 28(6) | audit and inspection frequency and scope set in advance, on risk | include the right to run your eval set |
| 28(7) | termination rights: significant breach, circumstances altering performance including material changes, weak ICT risk management, supervision impaired | a silent model change is a circumstance altering performance |
| 28(8) | exit strategies for critical or important functions, documented, tested, reviewed; alternatives and transition plans | the eval set and holdout let you test the replacement |
| 29 | concentration risk: substitutability, several contracts with one provider; subcontracting chains, third-country insolvency law and data recovery | the model provider behind the vendor is a subcontractor; the same model may sit under several of your vendors |
| 30(1) | one written contract, SLAs included | |
| 30(2)(a)-(i) | all contracts: services and subcontracting conditions; locations of service and data, advance notice of changes; data availability, integrity, confidentiality; data access and return on exit or insolvency; service level descriptions; incident assistance; cooperation with authorities; termination rights and notice periods; resilience training | locations and sub-processors of the model inference; return of logs and eval results |
| 30(3)(a)-(f) | critical or important functions also: precise quantitative and qualitative service levels; notice of developments with a material impact; contingency plans and security; TLPT participation; unrestricted access, inspection and audit; exit with a mandatory transition period | quality SLA on your metric; notice of a model change; access to traces |

Contractual policy for critical or important functions: Delegated Regulation (EU) 2024/1773. Check both technical standards on EUR-Lex before citing them.

## Clause library (own wording, adapt with counsel)

| Clause | Status | Hook |
| --- | --- | --- |
| No use of customer inputs, outputs, feedback or eval data to train, fine-tune or improve any model, by the vendor or its sub-processors | must-have, blocking | GDPR 28(3)(a), 28(10); bank or insurance secrecy |
| Written notice (e.g. 60–90 days) of any change of model, model version or output-affecting component; right to re-run the buyer's eval set before the switch; right to stay on the tested version meanwhile; exit without penalty on a failed re-test | must-have, blocking | DORA 28(7)(b), 30(3)(b); AI Act 13(3)(c), 43(4) |
| Access to logs and per-request traces (input, output, model version, timestamp), retention you set | must-have | AI Act 26(5)-(6); DORA 30(3)(e) |
| Processing agreement, processing locations named, sub-processor list with notice and objection | must-have | GDPR 28(2)-(4); DORA 30(2)(a)-(b) |
| Exit: data, configurations, logs and eval results returned in a usable format; certified deletion; transition period | must-have | GDPR 28(3)(g); DORA 28(8), 30(2)(d), 30(3)(f) |
| Quality service level on the buyer's metric, measured per class on the buyer's eval set each quarter, with credits and a termination right | negotiable (mandatory in substance for critical or important functions) | DORA 30(2)(e), 30(3)(a) |
| Right to run the eval set at any time at no extra cost | negotiable | DORA 28(6) |
| Incident notice within a set time, including quality incidents | negotiable | DORA 30(2)(f) |
| Price protection on a model change | negotiable | — |

## Questions to send the vendor

Which model and version runs under the product, from which provider, where. How versions change and with what notice. Where inputs, outputs and logs are processed and stored, for how long. Which sub-processors. Whether any customer data trains or improves any model, and where that is written. What data and method stand behind any accuracy figure, per class. Which logs you can export. Which AI Act documents exist today. The exit process and its cost.
