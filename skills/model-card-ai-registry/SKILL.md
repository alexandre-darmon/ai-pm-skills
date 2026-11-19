---
name: model-card-ai-registry
description: 'Write an AI system''s model card and registry entry as its eval record: results per class with intervals, set, judge, signed thresholds, limits, monitoring. Use at go-live, a new version or an audit.'
license: CC-BY-4.0
metadata:
  stage: "prove"
  version: "0.3.3"
  status: "tested"
  eval_threshold: "0.90"
  legal: "true"
  last_verified: "2026-11-09"
  autonomy_relevant: "true"
  depends_on: "build-evals, error-analysis, llm-judge-calibration, production-evals-monitoring, release-to-production, ai-act-classification"
  feeds: "release-to-production, ai-incident-playbook"
  sources: "mitchell-model-cards, eu-ai-act, wilson-interval, miller-error-bars, husain-shankar-evals, own-registry, repo-chanmeng, repo-yoseph"
---

# model-card-ai-registry

## When to use
- An AI system goes live, ships a new version (prompt, model, knowledge base), is being retired, or faces an audit.
- Compliance asks for a registry entry, or for the accuracy figures to declare in the instructions for use.
- A card exists but its eval section is a single score, or nobody can say when its thresholds were set.
- Do not use to classify the system under the AI Act: use `ai-act-classification` and carry its result over.
- Do not use to run or design the evals themselves: that is `build-evals`; the card records their result.

## Inputs
Mandatory: purpose, owners, the version bundle (or at least model and version), the eval results.
Ask if missing: results per question class with their number of cases, set composition, the judge and its validation (`llm-judge-calibration`), each threshold with who signed it and when, failure modes (`error-analysis`), the monitoring plan (`production-evals-monitoring`), the guardrail spec, the classification.
A missing fact (a result, a date, a signature, a snapshot) is listed with who provides it, never invented: an invented figure on a card becomes false audit evidence. A missing control or procedure (guardrail, stop rule, oversight, retirement steps, review date) is different: propose a concrete default, marked "proposed, to confirm by <owner>", because a reader left with a blank has nothing to approve.

## Method
Deliver the record itself, not a plan to write it: a reader preparing for an audit needs text they can file, and a list of instructions leaves the work undone. Fit the shape to the request:
- **Asked to register a system**: open with one decision, stated once, for example "Not registered: <n> required items missing". Do not also log it as registered, even as a draft, or call the draft "ready" or "complete", even with a condition ("ready once…"): two statuses read as a contradiction, and a sentence lifted out of context reads as approval. Then the draft card, then a table of what is missing and who provides each item (a role: system owner, engineering, eval owner, compliance), so every gap has someone to chase.
- **Told about one change** (a new prompt, model or knowledge base): lead with the changelog entry itself, filled in from what was given (step 12): version, change, eval delta per class (tie or not), approved by and on, recorded after the fact on, review date. Then the few items to add. A full-card exercise buries the one record that was asked for.
- **Asked for a full card or one section**: the card with every heading; each gap an open item with its owner.

Write for a reader who does not know this method: name things in plain words ("the AI Act classification", "the error analysis", "the release process"), not by file names or internal scales they cannot look up.

1. **Identity.** Purpose and out-of-scope uses, owners, status, autonomy level per step from references/autonomy-ladder.md, review date.
2. **Version bundle**, part by part, as `release-to-production` defines it: system prompt version, dated model snapshot, parameters, tool definitions, knowledge base snapshot. A vendor's model name may still move under you; an alias such as `latest` tells an auditor nothing about what ran. Any part unknown makes the card incomplete; ask for the prompt version and the pinned snapshot by name.
3. **Eval record per class**, for this version (references/evals-as-evidence.md): class, number of cases, pass rate, 95% interval (references/eval-statistics.md), threshold, pass or fail. Compute the interval when only n and the rate are given: 48 of 50 is 96%, 87% to 99%. A class whose threshold guards a costly error passes on the lower bound. Name the worst class next to any overall figure. An overall score alone, or a rate with no number of cases, makes the section incomplete.
4. **Set composition**: cases per class, real and synthetic share (and, when the synthetic share is high, two rows in the eval table: real cases only and generated cases only, each with its n and interval, so an auditor sees whether the score holds on real inputs; cases generated from the same source files are not independent, so say the interval may be too narrow, without putting a number on the effective size, which nobody has measured), where the real cases come from and over which period, the set version, and the size of the private holdout. The holdout's content never enters the card.
5. **Judge**, when any grader is an LLM: judge model and version, the expert-labelled set it was validated on (size, who labelled), its TPR (share of truly good answers it passes) and TNR (share of truly bad answers it fails), and whether reported rates are corrected for its errors. Raw agreement alone hides a judge that passes everything: record it as not validated.
6. **Thresholds and signatures**: per class, the threshold, who signed it and the date, and the date of the run it judges. A threshold signed after the results only describes them: record it as set after the run, never present it as a gate passed, and require a new threshold signed before the next run. A moved threshold or a failed run stays on record with who decided and why.
7. **Known failure modes and limits**, from the error analysis: each mode with the class it hits and how often it was seen on the reviewed sample. Refuse a card with no limits or failure modes: it is incomplete.
8. **Declared accuracy.** For a high-risk system, the accuracy level and metrics declared in the instructions for use (AI Act art. 13(3)(b)(ii) and 15(3)) should be traceable to this record: metric, level per class, interval, and the conditions where it drops. Annex IV point 2(g) expects test logs and reports dated and signed by the responsible persons; the card points to them. These are checklist items for counsel, not conclusions.
9. **Monitoring plan**: what is sampled per period, how it is graded, the alert threshold, who can suspend the system, and where incidents go (`ai-incident-playbook`).
10. **Guardrails and oversight** for L3 and above: who sees exceptions, who can stop the system, how, and how work goes back to people when it stops. Every field gets a concrete value, never a bare "missing": turn the limits the user gives into operational rules (measurement window, minimum volume before a rate counts, who restarts and on what evidence) and fill the rest with defaults marked "proposed, to confirm by <owner>", because a control that reads "missing" cannot be approved or run. The classification is carried over from the AI Act classification with its real source only ("Classification: <result>, from <the `ai-act-classification` assessment or counsel's document, date>; counsel review: <on file | to confirm by compliance>"), never a conformity statement and never a counsel review the request did not mention.
11. **End of life**: status (pilot, live, retiring, retired), what would retire the system, what happens on shutdown (fallback to the manual process, migration to a replacement version re-run on the same cases), the provider's deprecation date for the model, with the review date before it. Write these as proposed defaults to confirm, as in step 10. How long records stay after retirement is a question for counsel. A retired system keeps its entry, marked retired.
12. **Changelog per version**: what changed in the bundle, the eval delta per class on the same cases, whether it is outside the noise (references/eval-statistics.md: with d cases where exactly one version passes, a gap under 2√d / n is a tie), who approved and when. A provider's model update counts as a version. When the entry is missing, write it now from what is known (the change, the before and after figures), marked as recorded after the fact with today's date, never backdated, and list what the diff cannot tell (who approved, why, the per-class figures). Each entry states the review date and whether this change moves it, and why. The release process updates the card at each release.
13. Write the registry entry in the company's format; if none, use the template's fields.

## Output
`templates/model-card.md`, all headings present. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Checklist, not verdict: a card never says the system is compliant, conformant or safe.
- Every card has a review date.
- Limits and failure modes are mandatory.
- No pass rate without its number of cases and interval; no overall score without the scores per class.
- No judge-graded result without the judge's TPR and TNR.
- A threshold set after the results is recorded as such, never presented as a gate passed.
- Unfavourable results, moved thresholds and failed runs stay on record.

## Links
references/evals-as-evidence.md · references/eval-statistics.md · references/autonomy-ladder.md · build-evals · error-analysis · llm-judge-calibration · production-evals-monitoring · release-to-production · ai-act-classification · ai-incident-playbook

## Sources
- mitchell-model-cards: card structure, results reported per group.
- eu-ai-act: art. 13(3)(b)(ii) and 15(3) on declared accuracy, Annex IV point 2(g) on dated and signed test reports, art. 26(5) and 72 on monitoring; as inputs to counsel.
- wilson-interval: the interval on a pass rate with few cases.
- miller-error-bars: paired comparison of two versions on the same cases.
- husain-shankar-evals: a judge read with TPR and TNR against expert labels.
- own-registry: changelog convention and registry fields.
- repo-chanmeng: a vendor model update as a product change, tracking deprecations.
- repo-yoseph: per-slice results and retirement on the card.
