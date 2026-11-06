---
name: conversation-analysis
description: Classify an AI assistant's conversations by use case, resolution and sentiment, PII masked. Use to build or check the taxonomy, pick the classifier, see what people use it for, or act on the results.
stage: measure
version: 0.2.1
depends_on: [build-evals, agent-knowledge-base]
feeds: [assistant-kpis-cost-per-outcome, ai-roi-quantification, process-ai-redesign, build-evals]
autonomy_relevant: true
sources: [gdpr, own-conversation-classification, repo-chanmeng]
eval_threshold: 0.80
status: tested
---

# conversation-analysis

## When to use
- "What do people use the assistant for?", a quarterly review, or knowledge base (KB) prioritisation by volume and resolution.
- A taxonomy of use cases or a labelling plan for an assistant's conversations needs building or checking before labelling starts.
- Choosing the model that classifies the conversations (cheap vs frontier, cost vs agreement), or checking one that has drifted.
- KPIs or ROI need volume by use case (`assistant-kpis-cost-per-outcome`, `ai-roi-quantification`).
- A classification is done and sound, and the question is what to do with the result: do not redo steps 1–7, go to the end of step 8 and answer with its hand-over.
- Do not use to build a classifier that acts in production (routing, triage, auto-reply): that is a feature, use `llm-feature-prd`.
- Do not use to grade whether the assistant's answers were correct: that is `build-evals`.

## Inputs
Mandatory: access to the transcripts (volume per month, period, channels), the personal-data rules (what counts as personal data here, who may read raw text), the decisions the analysis feeds (which KPI, which KB choice, which ROI line).
Ask if missing: a draft taxonomy (step 3 derives one if there is none), 150–200 hand-labelled conversations or labellers who know the domain, candidate classifiers with their price per conversation.
If transcripts contain personal data (names, emails, phone numbers, IBANs, employee or customer ids, health details), masking comes first: nothing else runs until it is done and checked.

## Method
1. **Mask personal data before any model call**, including the classifier candidates and any model used to draft the taxonomy. Deterministic patterns for structured data (IBAN, email, phone, ids), named-entity recognition for names and places, replaced by typed placeholders (`[NAME]`, `[IBAN]`, `[EMAIL]`). Check by hand a sample of masked conversations (100 or more) and report the residual leak rate. Until the check passes, no classification, labelling or taxonomy work starts. Raw text stays in its source system. Say why in the plan: GDPR art. 5(1)(c), data minimisation. Set a retention period for the masked text and the classifier logs and who deletes them: masked chat can still identify someone, so it does not stay forever (GDPR art. 5(1)(e), storage limitation).
2. **Fix the dimensions and what each one feeds**: use case (volume, ROI), domain or KB (quality by KB), resolution (resolved, escalated, abandoned, unresolved), sentiment, language. Drop a dimension that feeds no decision.
3. **Build the taxonomy and freeze it before labelling.** With no draft, or only a few examples, derive one from the data rather than from an org chart, which pushes real requests into "other": read about 50 masked conversations, write a free-form note on what each user wanted, cluster the notes into candidate classes, and keep reading until new conversations add no new class. Then, draft or not: 8–12 use cases, mutually exclusive. Each class has a definition, two examples and a counter-example. Overlapping classes are merged, or separated by a written rule (e.g. "a conversation with two requests takes the class of the first one the user states"). Keep "other" under 10% of conversations. Version the taxonomy: a change after freezing is a new version and the labelled set is relabelled.
4. **Write the annotation guide and label 150–200 conversations**, sampled across the period, channels and populations. Two labellers on at least 50 of them measure human agreement: it is the ceiling a classifier can reach.
5. **Compare the candidate classifiers on the labelled set**: agreement per dimension, never one average, the confusion between the closest classes, cost per conversation, latency. A candidate below the human ceiling on a dimension is not trusted on that dimension without review.
6. **Choose a setup with a confidence threshold.** When a cheap classifier is right most of the time and its confidence separates right from wrong, route by confidence: the cheap model keeps the cases above the threshold, a stronger model or a human takes the rest. Low-confidence cases go to review or to "unclassified", never forced into a class. Report the blended agreement and the blended cost per conversation at the chosen threshold. Recommend this routed setup as the target; one model alone is only an interim while the threshold is measured on the labelled set.
7. **Design the monthly drift check**: a fresh sample (50–100 conversations) labelled each month, agreement per dimension compared with the last run, and the shares of "other" and of low-confidence cases tracked. A drop in agreement, "other" above 10% or a new recurring request opens a taxonomy review. This check is the design behind the L5 gate "drift detection live" (references/autonomy-ladder.md): say which assistant step it gates.
8. **Join the output to the KPIs.** One row per conversation: `trace_id`, `use_case`, `domain`, `resolution`, `sentiment`, `language`, `confidence`, `classifier_version`, `taxonomy_version`. Volume by use case comes from these rows, never from declared usage (references/roi-model.md), and feeds `assistant-kpis-cost-per-outcome`. When a use case combines high volume with a high unresolved share, pull a masked sample of it and hand it to `build-evals` as candidate golden-set cases; scoring them stays there.

## Output
A classification plan following `templates/classification-plan.md`: masking step, its check and retention period, dimensions, frozen taxonomy with edge-case rules, annotation guide, candidate comparison (agreement per dimension, cost per conversation), chosen setup with threshold and routing, monthly drift check, output schema, unresolved clusters handed to `build-evals`. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Personal data is masked before any model call, including drafting the taxonomy. "It's internal" or "just a test" is not an exception.
- Never repeat a name, IBAN, email or id from the transcripts in the output: use the placeholders.
- The taxonomy is frozen before labelling: 8–12 use cases, overlaps merged or separated by a written rule.
- Agreement is reported per dimension, never as one average.
- Low-confidence cases are routed to review, never forced into a class.
- The classifier is re-measured every month on a fresh labelled sample.

## Links
references/roi-model.md · references/autonomy-ladder.md · build-evals · assistant-kpis-cost-per-outcome · ai-roi-quantification · llm-feature-prd

## Sources
- gdpr: data minimisation (art. 5) behind masking before any model call.
- own-conversation-classification: taxonomy size, freeze-then-label, per-dimension agreement and confidence routing, from classifying the conversations of internal assistants in production (method only).
- repo-chanmeng: bottom-up categories from free-form notes on traces, agreed retention for logs (ideas, own words).
