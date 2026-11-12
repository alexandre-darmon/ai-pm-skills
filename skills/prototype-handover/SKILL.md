---
name: prototype-handover
description: 'Decide what a PM-built AI prototype becomes: rebuilt by engineers, registered at its EUC tier, or retired. Use when a prototype gets users, nears its kill date, or someone asks to keep it.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.2.2"
  status: "tested"
  eval_threshold: "0.90"
  legal: "true"
  last_verified: "2026-11-11"
  autonomy_relevant: "true"
  depends_on: "ai-feasibility-spike, build-evals, llm-judge-calibration, agent-design-and-tooling"
  feeds: "release-to-production, ai-act-classification, model-card-ai-registry"
  sources: "aws-euc-tiers, esma-qa-2103, dora-rts-ict-risk, dora, eu-ai-act, gdpr, cagan-prototypes-products, bloomberg-ing-vibe-coding, replit-db-incident, singer-shape-up, shankar-validators, husain-shankar-evals, wilson-interval, sierra-adlc, own-practice"
---

# prototype-handover

## When to use
- A prompt app, notebook, agent or review tool that a PM built with a coding agent has answered its question, and someone wants to keep it, share it or put it in front of more users.
- The prototype's kill date is near or past, and nobody has decided what happens to it.
- Engineering is asked to "take over" a PM-built AI tool and needs to know what to rebuild and what to rebuild against.
- IT risk, model risk or an auditor asks whether a PM-built AI tool is in the ICT asset inventory.
- Do not use to plan the release of a change engineering has already built (shadow, canary, A/B): that is `release-to-production`.
- Do not use to read a spike's result or decide whether the model can do the task: that is `ai-feasibility-spike`.
- Do not use to write the eval record of a version in production: that is `model-card-ai-registry`; this skill only drafts the inventory line. Do not use to classify the system under the AI Act: that is `ai-act-classification`, which this skill flags.

## Inputs
Mandatory: what the artefact does, in one sentence; who uses it and how many; what data it reads (synthetic, anonymised, production, personal, special category) and with which credentials; what it writes or does (reads only, drafts for a human, acts on a system); the autonomy level of each step, today and wanted (references/autonomy-ladder.md); the model and its version, where the prompts live; the eval cases and scores it produced; the kill date set before the build.
Ask if missing: the judge and its measured TPR and TNR; the sponsor and a named owner; whether the company is a financial entity under DORA; whether outputs feed decisions about people.
A missing fact that changes the tier becomes a question, never an assumption in the lower tier's favour.

## Method
Details per regulation and the register fields: references/handover-register-map.md. The frame: references/build-to-learn.md.

1. **Check the red line first.** Does the artefact hold production personal data or production credentials? If yes, and the kill date is past or less than two weeks away, the first line of the file is a containment decision: stop it, or record a dated decision by a named owner. Revoke or rotate the personal or production credentials the prototype used, whatever the decision. "Keep it running until engineering has capacity" is not a decision, it is a drift (`singer-shape-up`, circuit breaker). The RTS derogation for production data outside production covers specific testing occasions, for limited periods, approved by the relevant function and reported to the ICT risk function (Delegated Regulation (EU) 2024/1774, art. 16(6)); it does not cover running a business process. Whether to accept operational use at all is a question for IT risk, not the sponsor's call. If IT risk accepts it, the exception is time-boxed in weeks, never "until the rebuild", and never runs on the PM's personal or production credentials.
2. **Inventory the artefact.** One table: function, users, data and credentials, actions, model and version, prompt location, eval cases and scores, owner, kill date, where it runs. Mark each line "known" or "to confirm".
3. **Set the tier on two axes, take the higher.** Process axis, the four EUC tiers (`aws-euc-tiers`): 1 personal, single user, every output reviewed; 2 team, several users, no regulated outcome, failures recoverable; 3 business-critical, it touches customer outcomes, regulatory returns or financial controls; 4 mission-critical, it executes against ledgers, payments, trading or capital. Autonomy axis (references/autonomy-ladder.md): L0–L2 for one user who checks every output fits tier 1; L0–L2 for a team fits tier 2; L2 on a customer, pricing or regulatory output is at least tier 3; L3 and above on such outputs is tier 4. Set the tier on the wanted level, not today's: sharing the tool or raising its level is what moves it. Write both: the tier and the ladder level (L0 to L5) of each step today, then after the change asked for. Open references/autonomy-ladder.md before you name a level; if you cannot, still write the code you read from the facts (for example L1–L2) and mark it "to confirm", never a word like "low" in its place. A short answer keeps this line.
4. **Decide one of three outcomes.**
   - **Retire on the kill date** when the question is answered and nobody owns a next step. Keep the cases, the scores and the prompts; delete the data copies.
   - **Register at tier 1 or 2** when it stays a personal or team tool: named owner, inventory entry, a person checking each output before use, prompts and model version under change control, a review date.
   - **Rebuild by engineering** at tier 3 or 4, at L3 and above, or whenever it needs production credentials or production personal data to be useful. At tier 4 no PM-built component stays in the execution path.
5. **Write the handover contract.** This is what makes it an AI handover, not a code drop:
   - the eval suite (cases, graders, version or hash) and the frozen baseline: scores per class with n of N and a Wilson interval (references/eval-statistics.md), model and prompt versions, date;
   - the bar per class, signed before the run, and the error that is never acceptable;
   - the judge with its TPR and TNR on expert labels; a judge with no measured TPR and TNR cannot gate anything and is marked "not validated" (`husain-shankar-evals`);
   - prompts, model identifiers and parameters as configuration under change control: any change, including a provider model update or a different gateway version, is a new release (`sierra-adlc`);
   - the autonomy level per step and the gate to the next level;
   - the trace fields the prototype logged, for the engineering logging pipeline.
   The baseline is the floor engineering's build must reach on the same suite. It is not release evidence: release evidence is the frozen suite run on the engineering build (`release-to-production`).
6. **Write the intended-vs-implemented note.** What it was meant to do; what it actually does; the shortcuts (keys in a file, no login, all rows visible, prompts in code, a guardrail that is a sentence in the prompt instead of a control in code, `replit-db-incident`); what it does that nobody asked for; the failure modes seen in the cases. Criteria moved while you graded, so say which cases were graded under which version (`shankar-validators`).
7. **List what engineering must rebuild.** Each item as rebuild, reuse as spec, or drop: authentication and authorisation with row-level access (the prototype saw every row its credentials allowed), secrets in a vault, separate environments, the logging pipeline and retention, guardrails enforced in code, model access through the gateway, tests. Production credentials never carry over. The prototype is a spec with evidence, not code to harden (`cagan-prototypes-products`, `bloomberg-ing-vibe-coding`).
8. **Draft the register entry.** For a financial entity, end-user tools built outside the ICT function are ICT assets (DORA art. 3(7), `esma-qa-2103`). Draft the asset fields the RTS asks for (Delegated Regulation (EU) 2024/1774, art. 4(2)(b): identifier, location, owner, classification, business functions and dependencies), plus the AI fields: model and version, provider, prompt version, autonomy level, data categories, eval suite and baseline date, kill or review date. Every field is a draft for IT risk to accept or change.
9. **Flag the AI Act role.** If the company built the AI system itself and puts it into service for its own use, it may be its provider (art. 3(3), with putting into service for own use in art. 3(11)). If it built on a vendor's system and changed its purpose into an Annex III use, art. 25(1) may make it the provider. Flag it for `ai-act-classification` with the facts; do not classify here.
10. **Write the questions.** For IT risk (asset status, authorised software under RTS art. 11(2)(c), production data outside production under RTS art. 16(5)–(6) and 16(9), whether operational use is accepted at all), for model risk (is it a model under the policy, does the company's own model tiering place it above its EUC tier, who validates it and when, the judge), for counsel (provider role, Annex III), for the DPO (personal data, GDPR art. 35). Each question carries the facts the reader needs.
11. **State freshness.** If `last_verified` is more than 90 days old, say so at the top of the file.

## Output
A handover file following `templates/handover-file.md` (a short answer still states the tier and the L level today and after the change, the outcome and who decides): containment line, inventory, tier on both axes, the outcome, the handover contract, the intended-vs-implemented note, the rebuild list, the draft register entry, the AI Act flag, questions for IT risk, model risk, counsel and the DPO, freshness. It ends with: "This file is a proposal and a list of questions. IT risk, model risk and counsel decide."

## Rules and red lines
- Never state that the tool is "approved", "compliant", "cleared" or "safe to run". The file proposes a tier and an outcome and asks; the risk functions decide.
- Never let a prototype that holds production personal data or production credentials run past its kill date without a dated decision by a named owner. An exception is time-boxed in weeks, never "until the rebuild", and never keeps the PM's personal or production credentials.
- Spike or prototype numbers are never accepted as release evidence. They set the baseline engineering must reach; the release gate runs on the engineering build.
- Never lower a tier because "a human checks it" unless every output is validated before use, and say who checks.
- A change of model version or prompt after the baseline invalidates it for that version.
- Never redefine autonomy levels: use references/autonomy-ladder.md. Article numbers come from references/handover-register-map.md; an unverified one is phrased without the number.

## Links
references/build-to-learn.md · references/autonomy-ladder.md · references/eval-statistics.md · references/evals-as-evidence.md · references/handover-register-map.md · ai-feasibility-spike · build-evals · llm-judge-calibration · release-to-production · ai-act-classification · model-card-ai-registry

## Sources
- aws-euc-tiers: the four tiers of employee-built AI and the controls per tier.
- esma-qa-2103: end-user computing tools are ICT assets under DORA art. 3(7); it cites RTS art. 11(2)(c) and 16(9).
- dora-rts-ict-risk: asset records (art. 4(2)(b)), authorised software (art. 11(2)(c)), production data outside production and its testing derogation (art. 16(5)(a), 16(6)), extended to user-built systems (art. 16(9)).
- dora: the ICT asset definition (art. 3(7)), the one DORA article this skill cites.
- eu-ai-act: provider and putting into service (art. 3(3), 3(11)), value chain (art. 25).
- gdpr: art. 35, only to route the question to the DPO.
- cagan-prototypes-products: a prototype is a spec, not a product.
- bloomberg-ing-vibe-coding: senior engineers between fast-built tools and live systems.
- replit-db-incident: controls belong in code, not in the prompt.
- singer-shape-up: the kill date as a circuit breaker.
- shankar-validators: criteria drift while grading, so the suite version travels with the scores.
- husain-shankar-evals: a judge is trusted only with its TPR and TNR.
- wilson-interval: the interval on the baseline.
- sierra-adlc: versioned snapshots, so prompts and model versions are configuration.
- own-practice: handovers of PM-built tools to engineering and IT risk in banks and insurers.
