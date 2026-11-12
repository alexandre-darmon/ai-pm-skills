---
name: ai-act-classification
description: Classify an AI use case under the EU AI Act (role, risk category, obligations, questions for counsel). Use for a new AI use case, an autonomy level change, or a vendor's AI Act claim.
license: CC-BY-4.0
metadata:
  stage: "prove"
  version: "0.3.0"
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
- Do not use to design how quality is watched after release: that is `production-evals-monitoring`, which maps its plan to arts. 72 and 26(5).
- Do not use to vet a vendor's contract, hosting and data terms: that is `ai-vendor-evaluation`.

## Inputs
Mandatory: what the system does and what it decides or influences, in one sentence; the domain (HR, credit, insurance, education, essential services, critical infrastructure…); who is affected (employees, candidates, customers, the public); build or buy; the autonomy level of each step (references/autonomy-ladder.md); the model used (own, a general-purpose model through an API, fine-tuned).
Ask if missing: whether a human reviews each output before it has an effect, whether outputs feed decisions about individuals, whether the organisation is a public body or provides a public service, whether the system is used in the EU.
A missing fact that changes the category becomes a question for counsel, not an assumption.

## Method
Article numbers refer to Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force since 27 July 2026). Details per article and dates: references/ai-act-map.md.
1. **Check scope.** Is it an AI system (art. 3(1))? Is it excluded (art. 2, e.g. military, scientific research only)? If unclear, write it as a question for counsel.
2. **Fix the role per system.** Provider (art. 3(3)): you develop it, or have it developed, and place it on the market or put it into service under your name. Deployer (art. 3(4)): you use it under your authority. A deployer becomes a provider when it puts its name on a high-risk system, substantially modifies it, or changes its purpose so that it becomes high-risk (art. 25(1)).
3. **Screen the prohibited practices first (art. 5).** Examples: emotion recognition at work or in education (art. 5(1)(f)), social scoring (art. 5(1)(c)), manipulation or exploitation of vulnerabilities (art. 5(1)(a)-(b)), biometric categorisation inferring sensitive traits (art. 5(1)(g)). A possible hit stops the analysis: question for counsel, no design work.
4. **Check high-risk.** Annex III first for HR, credit, insurance and essential services (art. 6(2)), then Annex I products (art. 6(1)). Name the annex point and letter, e.g. Annex III point 4(a) for recruitment and screening of applications, point 4(b) for decisions on promotion, termination, task allocation or performance monitoring, point 5(b) for creditworthiness, point 5(c) for life and health insurance risk and pricing. Then the art. 6(3) exception: it needs no significant risk of harm, including no material influence on the decision, and a narrow procedural task, an improvement of a completed human activity, pattern detection that does not replace human assessment, or a preparatory task; it never applies when the system profiles natural persons. Write it as a question for counsel, with the facts, never as a conclusion; a provider relying on it documents its assessment and registers the system (arts. 6(4), 49(2)).
5. **Check transparency (art. 50).** People interacting with the system are told it is an AI unless obvious (art. 50(1)); synthetic content is marked (art. 50(2)); emotion recognition and biometric categorisation are disclosed to the people exposed (art. 50(3)); deep fakes, and AI-generated text published to inform the public, are disclosed (art. 50(4)).
6. **Flag general-purpose model use separately.** Calling a general-purpose AI model through an API does not make you its provider: the model obligations (art. 53, art. 55 for systemic risk) stay with the model provider. Fine-tuning makes you provider of the modified model only above one third of the original training compute (Commission guidelines): a question for counsel, with the compute figures. Your own system is classified on its own use. Ask the model provider for the documentation it owes downstream providers (art. 53(1)(b)).
7. **List the obligations by role**, each with its article and application date:
   - Providers and deployers, at any risk level: measures to support the AI literacy of the staff who operate or use the system (art. 4, as rewritten in 2026; no required level).
   - High-risk deployer (art. 26): use per the provider's instructions; human oversight by competent, trained people with authority (art. 26(2)); input data relevant and sufficiently representative, where the deployer controls it (art. 26(4)); monitoring, suspending use on a risk, and reporting serious incidents to the provider first (art. 26(5)); logs under the deployer's control kept at least six months unless other law says otherwise (art. 26(6)); workers' representatives and affected workers informed before use at the workplace (art. 26(7)); people subject to its decisions informed (art. 26(11)); a fundamental rights impact assessment before first use for public bodies, private entities providing public services and any deployer of Annex III points 5(b)-(c) (art. 27); on request, an explanation of the system's role in a decision with significant adverse effects (art. 86).
   - High-risk provider: risk management, data governance, technical documentation, logging, instructions, human oversight design, accuracy and robustness (arts. 9–15), quality management (art. 17), conformity assessment (art. 43), registration (art. 49), post-market monitoring and serious-incident reporting (arts. 72–73).
   - Dates (art. 113 as amended in 2026): prohibitions and AI literacy from 2 February 2025; general-purpose model obligations from 2 August 2025; transparency (art. 50) from 2 August 2026; Annex III high-risk obligations (arts. 6–27) from 2 December 2027; Annex I high-risk from 2 August 2028. Say which date applies to each obligation, and ask counsel for arts. 72–73 and 86.
   - Evidence: for each obligation, record what is on paper: document on file (link), claimed, not verified, or missing. A vendor's claim stays at claimed, not verified until the document is shown; for a high-risk system, ask for the instructions for use (art. 13), the EU declaration of conformity (art. 47) and the registration (art. 49). These provider duties may not be due yet (dates above), so ask what exists today. The status records paper, not conformity.
8. **Map the eval evidence.** For a high-risk system, list per article the eval evidence that answers it, the skill that produces it and its evidence status (references/evals-as-evidence.md): thresholds defined before testing (art. 9(8), `build-evals`), test data composition (art. 10(3)-(4), `build-evals`, `synthetic-eval-data`), accuracy metrics declared in the instructions (art. 15(3), `model-card-ai-registry`), test procedures inside the quality system (art. 17(1)(d)), deployer monitoring (art. 26(5)) and post-market monitoring (art. 72, `production-evals-monitoring`), serious incidents (art. 73, `ai-incident-playbook`). Below high risk, mark the same rows as good practice, not as obligations.
9. **Write the L+1 line.** For each step, what changes if it moves one level up (references/autonomy-ladder.md): does it now decide about people, act without prior human review, or fall into an Annex III point? Name the obligations that appear or tighten (human oversight design, logging, informing affected people).
10. **List the questions for counsel**: every judgement call (role, art. 6(3) exception, scope, dates), each with the facts counsel needs. If personal data are processed, add a question for the DPO on a data protection impact assessment (GDPR art. 35): it is outside this memo.
11. **State freshness.** If `last_verified` is more than 90 days old, say so at the top of the memo and ask counsel to confirm the application dates.

## Output
A classification memo following `templates/classification-memo.md`: system and role, prohibited-practice screen, risk category with article and annex point, transparency, general-purpose model flag, obligations by role with dates and evidence status, the eval evidence per article, the L+1 line, questions for counsel, freshness line. It ends with: "This memo is a checklist for counsel, not a conformity assessment."

## Rules and red lines
- Never state that a system, a vendor or the organisation is "compliant", "AI Act compliant" or "has no obligations". The memo is a classification, a checklist and questions; counsel decides.
- Every category and every obligation cites its article, and its annex point when there is one.
- HR, credit scoring, insurance pricing and essential services are checked against Annex III before anything else.
- A vendor's "AI Act compliant" claim does not transfer deployer duties: list what remains yours (art. 26), and record the claim as unverified until a document is shown.
- General-purpose model use is flagged in its own section.
- Never redefine autonomy levels: use references/autonomy-ladder.md.

## Links
references/ai-act-map.md · references/autonomy-ladder.md · references/evals-as-evidence.md · build-evals · production-evals-monitoring · model-card-ai-registry · ai-incident-playbook · ai-vendor-evaluation · system-prompt-and-guardrails

## Sources
- eu-ai-act: Regulation (EU) 2024/1689, articles as cited.
- ec-ai-act-guidelines: Commission guidelines on the AI system definition and prohibited practices (final, 2025), on general-purpose model providers, and the draft on high-risk classification (2026); not binding.
- cnil-ai: CNIL resources on AI systems and personal data.
- gdpr: art. 35, only to route the impact-assessment question to the DPO.
- eu-digital-omnibus-ai: the amended application dates and art. 4.
- fr-ai-act-implementation: French designation of competent authorities, still a bill at last verification (references/ai-act-map.md).
- repo-vishalhabib: the idea of marking a claim with nothing to point at as unverified (agent-trust-review, MIT), applied here to obligations.
