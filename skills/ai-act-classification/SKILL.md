---
name: ai-act-classification
description: Classify an AI use case under the EU AI Act (role, risk category, obligations, questions for counsel). Use for a new AI use case, an autonomy level change, or a vendor's AI Act claim.
license: CC-BY-4.0
metadata:
  stage: "prove"
  version: "0.8.3"
  status: "tested"
  eval_threshold: "0.90"
  legal: "true"
  last_verified: "2026-11-04"
  autonomy_relevant: "true"
  depends_on: "ai-opportunity-assessment, llm-feature-prd, system-prompt-and-guardrails"
  feeds: "model-card-ai-registry, production-evals-monitoring, ai-vendor-evaluation, process-ai-redesign"
  sources: "eu-ai-act, ec-ai-act-guidelines, cnil-ai, gdpr, eu-digital-omnibus-ai, fr-ai-act-implementation, repo-vishalhabib"
---

# ai-act-classification

## When to use
- A new AI use case is scoped, before build: after `ai-opportunity-assessment` or `llm-feature-prd`.
- A step moving up the autonomy ladder (e.g. L2 → L4) starts to decide about people without prior human review, or the use case changes purpose, users or domain.
- Legal, compliance or a sponsor asks "is this high-risk?" or "what does the AI Act require of us?".
- A vendor says its product is "AI Act compliant" and you need to know what remains yours to do.
- Do not use to design monitoring after release: that is `production-evals-monitoring`.
- Do not use to vet a vendor's contract and hosting: that is `ai-vendor-evaluation`.

## Inputs
Mandatory: what the system does and what it decides or influences, in one sentence; the domain (HR, credit, insurance, education, essential services, critical infrastructure…); who is affected (employees, candidates, customers, the public); build or buy; the autonomy level of each step (references/autonomy-ladder.md); the model used (own, a general-purpose model through an API, fine-tuned).
Ask if missing: whether a human reviews each output before it has an effect, whether outputs feed decisions about individuals, whether the organisation is a public body or public-service provider, whether the system is used in the EU.
A missing fact that changes the category becomes a question for counsel, not an assumption.

## Method
Article numbers refer to Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force since 27 July 2026). Details per article and dates: references/ai-act-map.md; state no legal fact that is not in it or in the request. In the memo, cite the amending act in full wherever a date it changed is given (e.g. "art. 113 as amended by Regulation (EU) 2026/1744"); do not repeat it elsewhere. Write for counsel and the sponsor: name documents, not this repo's skills. Open with three lines: category, role, first actions. A fact the request does not give is an assumption or a question, never a fact.
1. **Check scope.** AI system (art. 3(1))? Excluded (art. 2, e.g. military, research only)? If unclear: a question for counsel.
2. **Fix the role per system.** Provider (art. 3(3)): you develop it, or have it developed, and place it on the market or put it into service under your name. Deployer (art. 3(4)): you use it under your authority. A deployer becomes a provider when it puts its name on a high-risk system, substantially modifies it, or changes its purpose so that it becomes high-risk (art. 25(1)).
3. **Screen the prohibited practices first (art. 5).** Examples: emotion recognition at work or in education, which means inferring emotions from biometric data (art. 5(1)(f), art. 3(39)): face, voice, posture or keystroke signals count, sentiment read from written text alone does not; social scoring (art. 5(1)(c)), manipulation or exploitation of vulnerabilities (art. 5(1)(a)-(b)), biometric categorisation inferring sensitive traits (art. 5(1)(g)). A possible hit stops the analysis: question for counsel, no design work.
4. **Check high-risk.** Annex III first for HR, credit, insurance and essential services (art. 6(2)), then Annex I products (art. 6(1)). Point 5(b) covers evaluating the creditworthiness or setting the credit score of natural persons, except fraud detection: a step is 5(b) when it assesses a person's capacity to repay or sets a credit amount; whether a limit change does so is a fact to establish or a question for counsel. The use sets the category: a step inside an Annex III point is high-risk with or without human review. Whether a decision is solely automated is a GDPR art. 22 question for the DPO. Name the annex point and letter, e.g. Annex III point 4(a) for recruitment and screening of applications, point 4(b) for promotion, termination, task allocation or performance monitoring, point 5(b) for creditworthiness, point 5(c) for life and health insurance risk and pricing. Then the art. 6(3) exception: it needs no significant risk of harm, including no material influence on the decision, and a narrow procedural task, an improvement of a completed human activity, pattern detection that does not replace human assessment, or a preparatory task; it never applies when the system profiles natural persons (scoring or ranking people on personal aspects, e.g. work performance or reliability, is profiling). State the category plainly when the facts settle it; raise the exception only when they leave it open, as a question for counsel with the facts, never as a conclusion; a provider relying on it documents its assessment and registers the system (arts. 6(4), 49(2)).
5. **Check transparency (art. 50).** People interacting with the system are told it is an AI unless obvious (art. 50(1)); synthetic content is marked (art. 50(2), from 2 August 2026; 2 December 2026 for systems placed on the market before 2 August 2026 (art. 111(4)); whether this output is in scope, e.g. assistive standard editing, is a question for counsel); emotion recognition and biometric categorisation are disclosed to the people exposed (art. 50(3)); deep fakes, and AI-generated text published to inform the public, are disclosed (art. 50(4)).
6. **Flag general-purpose model use separately.** Calling a general-purpose model through an API does not make you its provider: model obligations (art. 53, art. 55 for systemic risk) stay with the model provider. A modifier becomes provider of the modified model above about one third of the original training compute (Commission guidelines, indicative): a question for counsel, with the figures. Your own system is classified on its own use. Ask the model provider for the documentation it owes downstream providers (art. 53(1)(b)).
7. **List the obligations of the category found**, by role, each with its article and application date. Below high risk, that is art. 4 and the art. 50 paragraphs that apply, with their dates, and nothing from the high-risk lists:
   - Providers and deployers, at any risk level: measures to support the AI literacy of the staff who operate or use the system (art. 4).
   - High-risk deployer (art. 26): use per the provider's instructions; human oversight by competent, trained people with authority (art. 26(2)); input data relevant and sufficiently representative, where the deployer controls it (art. 26(4)); monitoring; on a risk, informing the provider or distributor and the market surveillance authority and suspending use; reporting a serious incident to the provider first, then to the importer or distributor and the market surveillance authority (art. 26(5)); logs under the deployer's control kept at least six months unless other law says otherwise (art. 26(6)); workers' representatives and affected workers informed before use at the workplace (art. 26(7)); people subject to its decisions informed (art. 26(11)); a fundamental rights impact assessment before first use for public bodies, private entities providing public services and any deployer of Annex III points 5(b)-(c) (art. 27); on request, an explanation of the system's role in a decision with significant adverse effects (art. 86).
   - High-risk provider: arts. 9–15, 17, 43, 49, 72–73 (references/ai-act-map.md).
   - Dates (art. 113 as amended in 2026): prohibitions and AI literacy from 2 February 2025; general-purpose model obligations from 2 August 2025; transparency (art. 50) from 2 August 2026; Annex III high-risk obligations (arts. 6–27) from 2 December 2027; Annex I high-risk from 2 August 2028. Give only the dates of the obligations listed. Other transitional rules for systems already on the market (art. 111) go to counsel as a question, not as a date. State them plainly as the law at the freshness date, unhedged unless step 11 applies, one per obligation; ask counsel for arts. 72–73 and 86.
   - Evidence per obligation: document on file (link), claimed (only for a claim the request reports), or not seen. A vendor's claim stays claimed until the document is shown; for a high-risk system, ask for the instructions for use (art. 13), the EU declaration of conformity (art. 47) and the registration (art. 49), which may not be due yet. The status records paper, not conformity.
8. **Map the eval evidence.** For a high-risk system, per article (9(8) thresholds set before testing, 10(3)-(4) test data, 15(3) declared accuracy, 17(1)(d) test procedures, 26(5) and 72 monitoring, 73 serious incidents): the evidence, the document that holds it and its status (references/evals-as-evidence.md). Below high risk, one line: the eval plan is good practice, not an obligation.
9. **Write the L+1 line.** For each action the request names or plans (none hypothetical), what changes one level up (references/autonomy-ladder.md): its Annex III point, or outside Annex III with the reason, and the fact that would change that. Use the request's words, level labels in brackets (the team's scale, not law), and no ladder gate as a requirement. Below high risk, two lines at most. For a step inside an Annex III point, propose the oversight design the deployer controls for the use as planned now, not only after a move (who reviews which actions, before or after execution, how to stop or reverse one, which checks detect its harm): counsel checks it. Keep the duties at both levels, each with its start date (art. 27 where it applies), apart from what the move changes: oversight, logging, informing affected people. A step outside Annex III enters it only if the move changes its use, not because a human stops reviewing. A step that relied on the art. 6(3) exception can lose it when the move removes human review or gives it material influence on the decision: a question for counsel.
10. **List the questions for counsel**: every judgement call (role, art. 6(3) exception, scope, dates), each with the facts counsel needs. If personal data are processed, add a question for the DPO on a data protection impact assessment (GDPR art. 35; a high-risk deployer uses the provider's information for it, art. 26(9)): it is outside this memo.
11. **State freshness.** At the top of every memo: "Application dates as last checked on <last_verified>". If that is more than 90 days old, add that they may have changed and counsel confirms them. Never invent today's date.

## Output
A classification memo following `templates/classification-memo.md`, in the order of the method; before the questions for counsel, which come last, the main risks outside the Act (wrong outputs or actions, data leakage, security, unequal treatment), one line each with its owner, no legal detail. About one page below high risk; full tables only for a high-risk system. It ends with: "This memo is a checklist for counsel, not a conformity assessment."

## Rules and red lines
- Never state that a system, a vendor or the organisation is "compliant", "AI Act compliant" or "has no obligations", nor reassure in its place ("likely fine", "low risk overall"). The memo is a classification, a checklist and questions; counsel decides.
- Every category and every obligation cites its article, and its annex point when there is one.
- HR, credit scoring, insurance pricing and essential services are checked against Annex III before anything else.
- A vendor's "AI Act compliant" claim does not transfer deployer duties: list what remains yours (art. 26), and record the claim as unverified until a document is shown.
- General-purpose model use is flagged in its own section.
- Every memo carries the `last_verified` freshness stamp: amendments move dates, so counsel must see when they were checked.
- A date moved by Regulation (EU) 2026/1744 cites it: counsel needs the legal basis.
- Never redefine autonomy levels: use references/autonomy-ladder.md.

## Links
references/ai-act-map.md · references/autonomy-ladder.md · references/evals-as-evidence.md · build-evals · synthetic-eval-data · production-evals-monitoring · model-card-ai-registry · ai-incident-playbook · ai-vendor-evaluation · system-prompt-and-guardrails

## Sources
- eu-ai-act: Regulation (EU) 2024/1689, articles as cited.
- ec-ai-act-guidelines: Commission guidelines on the AI system definition, prohibited practices, general-purpose model providers, and the draft on high-risk classification (2026); not binding.
- cnil-ai: CNIL resources on AI systems and personal data.
- gdpr: art. 35, only to route the impact-assessment question to the DPO.
- eu-digital-omnibus-ai: the amended application dates and art. 4.
- fr-ai-act-implementation: French designation of competent authorities, a bill at last verification.
- repo-vishalhabib: marking a claim with nothing to point at as unverified (agent-trust-review, MIT).
