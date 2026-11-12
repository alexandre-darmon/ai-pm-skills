---
name: trace-review-tool
description: 'Spec the thin trace-labelling app a coding agent builds for domain experts, and the fields each model call must log. Use for "build us a labelling tool" or before experts review outputs.'
license: CC-BY-4.0
metadata:
  stage: "build"
  version: "0.2.0"
  status: "tested"
  eval_threshold: "0.80"
  legal: "false"
  last_verified: "2026-11-11"
  autonomy_relevant: "true"
  depends_on: "agent-design-and-tooling, system-prompt-and-guardrails"
  feeds: "error-analysis, llm-judge-calibration, build-evals, prototype-handover, production-evals-monitoring"
  sources: "husain-field-guide, repo-evals-skills, husain-shankar-evals, eu-ai-act, eu-digital-omnibus-ai, gdpr, esma-qa-2103, dora-rts-ict-risk, aws-euc-tiers, otel-genai, wilson-interval, own-review-apps"
---

# trace-review-tool

## When to use
- "Can you build us a quick tool so the experts can label the answers?", or a spreadsheet of pasted outputs is slowing a review down.
- Domain experts (complaints officers, underwriters, credit analysts) must read and label a few hundred AI outputs before an error analysis, a judge calibration or a release decision.
- The exported traces lack what a reviewer needs to judge them (only question and answer, no prompt version, no retrieved ids, no overrides), and engineering asks what to add before the experts start.
- Someone asks how long the review traces and labels must be kept, or who may see them.
- Do not use to read the labels and group them into failure modes: that is `error-analysis`.
- Do not use to count what users ask about at scale (use cases, volumes, resolution): that is `conversation-analysis`.
- Do not use to design the agent's own loop, tools and trace schema: that is `agent-design-and-tooling`.
- Do not use to instrument production traces or set their retention for live monitoring: that is `production-evals-monitoring`, which instruments the same capture fields.

## Inputs
Mandatory: the feature and what its traces contain; who labels (named domain experts, not the build team) and how many traces; the decision the labels feed (error analysis, judge calibration, release); the personal-data rules and who the DPO is.
Ask if missing: monthly volume and question classes; feedback signals for targeted sampling (thumbs-down, escalations, low confidence); minutes per trace and the reviewers' loaded hourly cost; the storage the bank already approves for this data class; whether the system may be high-risk (`ai-act-classification`).

## Method
The PM decides what the app does; the coding agent builds it; engineers own anything that runs in production (references/build-to-learn.md). The generic idea, a thin custom viewer built in hours, comes from Husain and from the build-review-interface skill of ai-evals-course/evals-skills. What this skill adds is what a regulated company needs around it. Write the brief with `templates/review-app-brief.md`.

1. **Check the gap first.** If an approved tool already shows a whole trace and records the fields of step 5, use it and stop. Build only when none does. The app is a build-to-learn artefact: one file, the bank's approved stack, no framework or vendor choice in the brief, a kill date and an owner.
2. **Answer the asset question, then load exported traces masked before load.** The app is an ICT asset whatever data it holds (`esma-qa-2103`). Before it loads anything derived from production, even masked, it is identified, documented and approved at its end-user computing tier (`aws-euc-tiers`, `prototype-handover`); until then it runs on synthetic or anonymised cases (references/build-to-learn.md, red line 1). Masked traces are pseudonymised, so they are still personal data under GDPR. The DORA ICT rules allow pseudonymised production data in a non-production tool only inside the development and testing procedure (RTS 2024/1774 art. 16(5)(a)), and extend that procedure to systems built outside the ICT function on a risk basis (art. 16(9)); unmasked production data in a test setting needs an approved, time-limited exception (art. 16(6)) and has no place in a review app. The app reads a file exported from the logging store. It never connects to production. Personal data is masked in the export step with typed, consistent placeholders (`<CUSTOMER_1>`, `<IBAN_2>`, the same value keeps the same placeholder within a trace), so the expert can still follow the reasoning. A second person checks residual leaks by hand before anyone labels, sized from the leak rate you can tolerate: zero leaks in n traces still allows a rate up to about 3/n (references/eval-statistics.md), so 50 clean traces only bound it at 6%, 300 at 1%. For a review set of a few hundred traces, read all of it, free-text fields first, where leaks concentrate, and state the bound. The raw text stays in its source system. When a judgement truly needs the real value (does the name match the sanctions hit?), that check runs in the source system under its own access rights, or by code against the system of record, never by loading raw data into the app.
3. **Sample in a separate script, never in the app.** A script with a fixed seed writes the sample file and a `stream` column: **random** (simple or in proportion to class volume, the only stream that gives a rate) and **targeted** strata (thumbs-down, escalations, low confidence, small classes with legal or financial effect, which find failure modes but over-count them). The app shows the file in the order given. A pass rate comes from the random stream only, with its Wilson interval (references/eval-statistics.md). For judge calibration, the script also assigns a `split` (dev or test) so the test labels never reach the judge's prompt writer.
4. **One screen per trace, one binary label.** Show everything the model saw and did: the input, the retrieved passages with their ids, the tool calls and results, guardrail hits, the output, the prompt version. The expert gives pass or fail and a free-text critique in their own words, mandatory on a fail. No 1–5 scale and no failure-mode dropdown in the first round: modes come later from `error-analysis`. No model pre-labels or pre-fills the critique: the expert reads first. Keyboard shortcuts, a progress counter (n of N), and a "not sure" flag that never counts as pass.
5. **Every label carries who and when.** Each saved row holds `trace_id`, `label`, `critique`, `reviewer_id` (from the company login, never a typed name), `labelled_at` (UTC timestamp), app version, sample file version. The app refuses to save without a reviewer identity. A change of mind is a new row, never an overwrite: the label history is the audit trail an auditor, a model-risk reviewer or the judge calibration will ask for. Two experts on the same 30 traces give the agreement that says whether the definitions hold.
6. **Labels go to approved storage.** Rows are written to a store the bank already approves for this data class (an internal database or share with an access list and a retention period), never the laptop, the browser's local storage or the coding agent's sandbox. Name who can read raw critiques and log that access.
7. **Export in the formats the next skills read.** For `error-analysis`: a reading log `trace_id,stream,class,mode,critique,reviewer_id,labelled_at`, `mode` left empty until the notes are grouped. For `llm-judge-calibration`: `trace_id,split,human` with `human` = pass or fail, the judge's column added later. Same column names every time, so their scripts read them unchanged.
8. **Smoke test and review.** Before the experts start: 10 known traces (pass, fail, one with masked personal data, one with a tool error) go through load, label, save, export and re-import. Checks: no row without reviewer and timestamp, placeholders intact, exports read by the next scripts, nothing written outside approved storage. A fresh session or another model reviews the code the agent wrote.
9. **Price the review run.** Review cost = traces × minutes per trace × loaded hourly cost ÷ 60, plus the build hours. Say it before asking for experts' time (300 traces × 2 min × 85 EUR/h = 850 EUR). From the capture fields, report the model cost per run of the reviewed feature and the cost per correct answer once labels exist (references/roi-model.md).
10. **State the minimum capture contract per model call.** What the upstream system must log, or the traces cannot be judged (references/capture-contract.md): prompt version, model asked and model that answered with version, retrieved document ids, tool calls with arguments and result status, guardrail hits, human overrides (who changed what), tokens and cost, latency, and a join key to the business outcome (case, claim or loan id). The override field matters most at L2 and L3 (references/autonomy-ladder.md): it is the only record that the human in the loop changed anything, and the override rate per class is evidence for or against moving up a level. Engineers build the logging pipeline; the PM signs the field list. Missing fields become a request to engineering, not a workaround in the app.
11. **Retention as questions for counsel, never a verdict.** If the system is high-risk, AI Act art. 12 asks for automatic logging over its lifetime, art. 19 has providers keep the logs they control at least six months, and art. 26(6) has deployers do the same, in both cases unless other Union or national law, in particular data protection law, provides otherwise; a financial institution keeps them inside the documentation financial-services law already requires. GDPR minimisation and storage limitation (art. 5(1)(c), (e)) are part of that other law. Annex III duties, these included, apply from 2 December 2027 (`eu-digital-omnibus-ai`). Ask counsel and the DPO: is the system high-risk? From which date does the floor bind, and must logs created now meet it if the system still runs then? Is the bank provider, deployer or both for an in-house build? Do labels and critiques count as logs? Which period wins? Then hand the app's fate (rebuilt, registered at its end-user computing tier, or retired on its kill date) to `prototype-handover`.

## Output
A brief for the coding agent following `templates/review-app-brief.md`: purpose and decision fed, data in and masking, sampling script, screen and label, audit fields, storage, exports, smoke test, review cost, capture contract, retention questions for counsel, kill date and owner. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Never load unmasked production personal data into the app, whatever the reviewers' seniority or the app's location; mask in the export step. Masked data is still personal data: no production-derived data, even masked, before the app is identified and approved as an ICT asset.
- Never save a label without reviewer identity and timestamp, and never overwrite one.
- Never let the app choose or sort what is shown; sampling lives in a separate script, and rates come from the random stream only.
- Never a 1–5 score, and no model pre-labels before the expert reads.
- Labels live in approved storage only.
- No vendor or framework click-paths; the method stays harness-neutral.
- Retention and role questions go to counsel and the DPO; never call the logging or the app compliant.
- The app is not production code: no production credentials, a kill date, a handover.

## Links
references/build-to-learn.md · references/autonomy-ladder.md · references/eval-statistics.md · references/roi-model.md · references/capture-contract.md · error-analysis · llm-judge-calibration · conversation-analysis · agent-design-and-tooling · production-evals-monitoring · ai-act-classification · prototype-handover

## Sources
- husain-field-guide: a custom data viewer as the first investment, built in hours for domain experts.
- repo-evals-skills: its build-review-interface skill as the generic model of the review app, credited, ideas only.
- husain-shankar-evals: binary pass/fail with a free critique, the expert reads before any model.
- eu-ai-act: art. 12 logging, art. 19 and 26(6) retention and their data-protection qualifier, as questions for counsel.
- gdpr: masking before reading and data minimisation against retention.
- esma-qa-2103: an end-user tool built outside IT is an ICT asset.
- dora-rts-ict-risk: pseudonymised or anonymised production data only in non-production tools, under development and testing rules extended to user-built systems (art. 16(5)(a), 16(6), 16(9)).
- aws-euc-tiers: the end-user computing tier the app is approved at before it loads production-derived data.
- eu-digital-omnibus-ai: annex III duties, logging and retention included, apply from 2 December 2027.
- otel-genai: names for the capture fields.
- wilson-interval: rates from the random stream with their interval.
- own-review-apps: audit fields, smoke test and export formats from review apps built in client missions.
