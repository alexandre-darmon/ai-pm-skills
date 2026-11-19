---
name: prototype-handover
description: 'Decide what a PM-built AI prototype becomes: rebuilt by engineers, registered at its EUC tier, or retired. Use when a prototype gets users, nears its kill date, or someone asks to keep it.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.2.6"
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
- A PM-built prompt app, notebook or agent has answered its question, and someone wants to keep it, share it or widen it.
- The prototype's kill date is near or past, and nobody has decided what happens to it.
- Engineering is asked to take over a PM-built AI tool.
- IT risk or an auditor asks if a PM-built AI tool is in the ICT inventory.
- Not for releasing an engineering build (`release-to-production`), judging feasibility (`ai-feasibility-spike`), a production eval record (`model-card-ai-registry`) or AI Act classification (`ai-act-classification`).

## Inputs
Mandatory: what the artefact does; who uses it and how many; what data it reads (synthetic, anonymised, production, personal, special category) and with which credentials; what it writes or does (reads only, drafts for a human, acts on a system); the autonomy level of each step, today and wanted (references/autonomy-ladder.md); the model and its version, where the prompts live; the eval cases and scores it produced; the kill date set before the build.
Ask if missing: the judge and its measured TPR and TNR; the sponsor and a named owner; whether the company is a financial entity under DORA; whether outputs feed decisions about people.
A missing fact that changes the tier becomes a question, never an assumption favouring the lower tier.

## Method
Details per regulation and the register fields: references/handover-register-map.md. The frame: references/build-to-learn.md.

1. **Check the red line first.** Does the artefact hold production personal data or production credentials? If yes, and the kill date is past or less than two weeks away, the first line of the file is a containment decision, taken now, not later in the week: stop it today (users go back to the manual process); it restarts only once a named owner has recorded a dated decision with IT risk. Revoke or rotate the personal or production credentials the prototype used, whatever the decision. Waiting for engineering capacity is not a decision, it is a drift (`singer-shape-up`). The RTS derogation for production data outside production covers specific testing occasions, for limited periods, approved by the relevant function and reported to the ICT risk function (Delegated Regulation (EU) 2024/1774, art. 16(6)); it does not cover running a business process, and art. 16(9) extends these rules to systems built by users outside the ICT function. State both in the containment section, so the reader sees why the testing exception does not fit. Whether to accept operational use at all is a question for IT risk, not the sponsor's call. If IT risk accepts it, the exception carries its own end date in weeks, fixed when it is granted and independent of engineering's schedule, never "until the rebuild"; IT risk sets its credentials and access scope (least privilege, logged, revoked on the end date), never the PM's personal credentials.
2. **Inventory the artefact.** One table of the inputs above, each line "known" or "to confirm".
3. **Set the tier on two axes, take the higher.** Process axis, the four EUC tiers (`aws-euc-tiers`): 1 personal, single user, every output reviewed; 2 team, several users, no regulated outcome, failures recoverable; 3 business-critical, it touches customer outcomes, regulatory returns or financial controls; 4 mission-critical, it executes against ledgers, payments, trading or capital. Autonomy axis (references/autonomy-ladder.md): L0–L2 for one user who checks every output fits tier 1; L0–L2 for a team fits tier 2; L2 on a customer, pricing or regulatory output is at least tier 3; L3 and above on such outputs is tier 4. Set the tier on the wanted level, not today's: sharing the tool or raising its level is what moves it, so the wanted tier is the one that governs the handover and the register entry. Lead with it and give today's as context (for example "tier N at L<x> after the change, because <trigger>; tier M at L<y> today"). Read the level from the facts and state it; mark "to confirm" only the missing fact that would change it. A short answer keeps this line. These tiers and the outcome rules below are this method's proposal, not the company's policy: say so once, and that the company's own EUC or model policy prevails where it has one. Give each trigger and outcome with its reason, as a recommendation, not an existing requirement.
4. **Decide one of three outcomes.**
   - **Retire on the kill date** when the question is answered and nobody owns a next step. Keep the cases, the scores and the prompts; delete the data copies.
   - **Register at tier 1 or 2** when it stays a personal or team tool: named owner, inventory entry, a person checking each output before use, prompts and model version under change control, a set of eval cases the owner re-runs on any prompt or model change (this method's addition: `aws-euc-tiers` lists change control on prompts but no test), a review date on the company's EUC review cycle, to set with IT risk. When the facts point to a value, propose it and mark it "proposed" rather than leaving a blank.
   - **Rebuild by engineering** at tier 3 or 4, at L3 and above, or whenever it needs production credentials or production personal data to be useful. At tier 4, propose that no PM-built component stays in the execution path, since it acts with no person between.
5. **Write the handover contract.** This is what makes it an AI handover, not a code drop:
   - the eval suite (cases, graders, version or hash) and the frozen baseline: scores per class with n of N and a Wilson interval (references/eval-statistics.md), model and prompt versions, date. Give n and the interval per class: a rare class whose error costs most gets its own bar, since few cases mean a wide interval (references/eval-statistics.md);
   - the bar per class, signed before the run, and the error that is never acceptable;
   - the judge with its TPR and TNR on expert labels; a judge whose TPR and TNR were not measured cannot gate anything; say so in the sentence that names the judge (`husain-shankar-evals`);
   - prompts, model identifiers and parameters as configuration under change control: any change, including a provider model update or a different gateway version, is a new release (`sierra-adlc`);
   - the autonomy level per step and a proposed gate to the next level: the ladder's durations are defaults to set with model risk, not company rules;
   - the trace fields the prototype logged.
   The baseline is the floor engineering's build must reach on the same suite. It is not release evidence: release evidence is the frozen suite run on the engineering build (`release-to-production`). Write that run as a go-live gate, not as a question: nothing goes live until the build has met the bar on that suite.
6. **Write the intended-vs-implemented note.** Meant vs actual; the shortcuts (keys in a file, no login, all rows visible, a guardrail that is a prompt sentence instead of code, `replit-db-incident`); what it does that nobody asked for; the failure modes seen in the cases. Say which cases were graded under which criteria version (`shankar-validators`).
7. **List what engineering must rebuild.** Each item as rebuild, reuse as spec, or drop: authentication and authorisation with row-level access (the prototype saw every row its credentials allowed), secrets in a vault, separate environments, the logging pipeline and retention, guardrails enforced in code, model access through the gateway, tests. Production credentials never carry over. The prototype is a spec with evidence, not code to harden (`cagan-prototypes-products`, `bloomberg-ing-vibe-coding`).
8. **Draft the register entry.** For a financial entity, end-user tools built outside the ICT function are ICT assets (DORA art. 3(7), `esma-qa-2103`). Draft the asset fields the RTS asks for (RTS art. 4(2)(b): identifier, location, owner, classification, business functions, dependencies), plus the AI fields: model and version, provider, prompt version, autonomy level, data categories, eval suite and baseline date, kill or review date. Fill each field with what the facts already say (the function, the users, the model, the data) and mark only the rest "to confirm": a list of empty field names gives IT risk nothing to accept or change.
9. **Flag the AI Act role.** If the company built the AI system itself and puts it into service for its own use, it may be its provider (art. 3(3), with putting into service for own use in art. 3(11)). If it built on a vendor's system and changed its purpose into an Annex III use, art. 25(1) may make it the provider. Cite the articles, and name the Annex III point the facts suggest as a possibility (references/handover-register-map.md lists the ones met most). Flag it for `ai-act-classification` with the facts; do not classify here.
10. **Write the questions.** For IT risk (asset status, authorised software under RTS art. 11(2)(c), production data outside production under RTS art. 16(5)–(6) and 16(9), whether operational use is accepted at all), for model risk (is it a model under the policy, does the company's own model tiering place it above its EUC tier, who validates it and when, the judge), for counsel (provider role, Annex III), for the DPO (personal data, GDPR art. 35). Each carries the facts the reader needs.
11. **State freshness only when stale.** If `last_verified` is more than 90 days old, warn at the top. Otherwise say nothing about verification: the file verified nothing.

## Output
A handover file following `templates/handover-file.md` (a short answer still states the tier and the L level today and after the change, the outcome and who decides): containment line, inventory, tier on both axes, the outcome, the handover contract, the intended-vs-implemented note, the rebuild list, the draft register entry, the AI Act flag, questions for IT risk, model risk, counsel and the DPO. Lead with the answer to what the user asked. Keep it proportionate: a section with nothing known shrinks to one line, and a table row the facts cannot fill is cut, not left as a placeholder, because each extra specific is one more thing the reader must check. It ends with: "This file is a proposal and a list of questions. IT risk, model risk and counsel decide."

## Rules and red lines
- Never state that the tool is "approved", "compliant", "cleared" or "safe to run": the risk functions decide, and the file only proposes. When a sponsor asks for such a label (or "validated"), refuse it and say what to write instead ("baseline on the prototype model").
- Do not fill in what the user did not give: names, authors, dates, durations, company policies. Write a placeholder, or a value marked "proposed".
- A prototype holding production personal data or credentials never runs past its kill date without a dated decision by a named owner (step 1). An exception has its own end date in weeks, never "until the rebuild", and never keeps the PM's personal credentials: waiting for capacity is a drift, not a decision.
- Prototype numbers are a baseline, never release evidence (step 5).
- Never lower a tier because "a human checks it" unless every output is validated before use, and say who checks.
- A change of model version or prompt after the baseline invalidates it for that version.
- Never redefine autonomy levels: use references/autonomy-ladder.md. Article numbers come from references/handover-register-map.md; an unverified one is phrased without the number.

## Links
references/ (build-to-learn, autonomy-ladder, eval-statistics, evals-as-evidence, handover-register-map) · ai-feasibility-spike · build-evals · llm-judge-calibration · release-to-production · ai-act-classification · model-card-ai-registry

## Sources
aws-euc-tiers (EUC tiers) · esma-qa-2103 (EUC tools are ICT assets) · dora-rts-ict-risk · dora · eu-ai-act · gdpr · cagan-prototypes-products (a prototype is a spec) · bloomberg-ing-vibe-coding (engineers guard live systems) · replit-db-incident (controls in code) · singer-shape-up (kill date as circuit breaker) · shankar-validators (criteria drift) · husain-shankar-evals (judges need TPR and TNR) · wilson-interval · sierra-adlc (prompts and models are configuration) · own-practice (handovers in banks and insurers).
