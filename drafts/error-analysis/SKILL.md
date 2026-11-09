---
name: error-analysis
description: 'Turn an AI feature''s real traces into counted, priced failure modes before choosing metrics or graders. Use for bad answers with no clear cause, "which metrics should we track?", or unread traces.'
stage: evaluate
version: 0.1.1
legal: false
depends_on: [llm-feature-prd, conversation-analysis]
feeds: [build-evals, llm-judge-calibration, synthetic-eval-data, agent-evals, system-prompt-and-guardrails, production-evals-monitoring]
autonomy_relevant: true
sources: [husain-shankar-evals, shankar-validators, glaser-strauss-grounded-theory, repo-chanmeng, wilson-interval, gdpr, own-error-analysis]
eval_threshold: 0.80
status: draft
---

# error-analysis

## When to use
- "Our assistant gives bad answers, where do we start?", or complaints spike and nobody can say what goes wrong.
- "Which metrics should we track?", or someone proposes generic scores (helpfulness, accuracy, tone, 1–5) before anyone has read the outputs.
- Before writing graders or an LLM judge, and again after a model, prompt, knowledge-base (KB) or provider change.
- Hundreds or thousands of traces or logs exist and nobody knows what to do with them.
- Do not use to count what users ask about (use cases, volumes, resolution rates): that is `conversation-analysis`.
- Do not use to decide whether an existing judge can be trusted or can gate a release: that is `llm-judge-calibration`.

## Inputs
Mandatory: real traces showing what the model saw and did (input, retrieved documents, tool calls, output) and the monthly volume; the spec or system prompt the feature runs on; the accountable domain expert, the person who owns quality for that domain (not the build team); the personal-data rules.
Ask if missing: question classes and their shares (`conversation-analysis`); feedback signals (thumbs, escalations, abandonment, complaints, low confidence); the cost of one wrong answer, sourced (minutes to redo × loaded cost, complaint or leakage cost); the autonomy level of each step (references/autonomy-ladder.md).
No traces yet: generate inputs with `synthetic-eval-data`, run the prototype, read those outputs and label the taxonomy synthetic-based. Fewer than 50 traces: read them all; the taxonomy stays provisional.

## Method
1. **Refuse to pick metrics first.** Generic scores chosen before reading outputs (helpfulness, coherence, tone, toxicity, any Likert 1–5) are rejected: they measure what a template expects, not what this feature gets wrong, and an average of 3.6 tells nobody what to fix. Metrics come out of step 7. Keep a generic proposal only as a hypothesis to check while reading.
2. **Mask, then sample on purpose.** Mask personal data before anyone reads a trace or sends one to a model (GDPR data minimisation); raw text stays in its source system. Draw two streams, about 100 traces in all (references/error-analysis-guide.md):
   - **random**: a simple random draw, or one in proportion to each question class's volume. It is the only stream that estimates how often a mode occurs.
   - **targeted**: thumbs-down, escalations, long or abandoned conversations, low-confidence answers, complaints, and extra traces from small classes with legal or financial effects. It finds modes; it never gives their rate, since it over-represents failures.
   Never read only cherry-picked failures.
3. **One expert reads and writes a free note on each trace (open coding).** The accountable domain expert reads each trace in full and writes, in their own words, what went wrong, or "pass". The note is specific ("quoted the 2024 deductible table for a 2026 policy"), not a category ("inaccurate"). In a multi-step trace, note the first upstream failure: a wrong retrieval followed by a wrong answer is one retrieval failure, because later errors are often its consequences. The PM can sit beside the expert and engineers can read too, but one person's judgment sets the bar. No LLM writes these notes: a model reading first brings its own idea of failure and misses the domain errors only the expert sees.
4. **Read to saturation.** Keep reading until about 20 consecutive traces add no new kind of failure; it usually takes 50 to 100 traces. Log the trace number where the last new mode appeared. Below saturation the taxonomy is provisional, and every output says so.
5. **Group the notes into failure modes (axial coding).** Merge notes that describe the same failure; split a note that hides two. Each mode gets a binary definition (a trace passes or fails it, never a 1–5 score), one pass example and one fail example from the traces. An LLM may help at this step only: it proposes groupings and names for the expert's notes once they are written, and the expert accepts or rewrites each mode. Criteria drift while reading (Shankar et al.): version the taxonomy (v0.1, v0.2) and, when a definition changes, re-check the notes already filed under it. If a second reader codes 30 or more traces against the definitions, a Cohen's kappa under about 0.6 on a mode means its definition is unclear (references/eval-statistics.md).
6. **Count and price.** Count each trace once, under its first upstream failure, per stream and per question class.
   - **Share** = count in the random stream ÷ traces in the random stream, with its Wilson interval: 6 of 60 is 10% (5% to 20%). A mode never seen in 60 random traces can still hit up to about 5% of traffic (rule of three, references/eval-statistics.md). Targeted counts prove a mode exists, not how often it occurs.
   - **Cost per occurrence**, sourced as in references/roi-model.md: the time to catch and redo it (minutes × loaded cost) when a human validates every output (L2), plus what it costs once it reaches a customer, claimant or employee where nobody checks (L3 and above, references/autonomy-ladder.md). An unsourced cost is marked "to source" with an owner, never guessed.
   - **Expected monthly cost** = monthly volume × share × cost per occurrence, with the interval carried through. Rank the modes on it. A mode with legal, privacy, financial or irreversible effects ranks high whatever its count; its exposure goes to counsel as a question, not into a euro figure.
   With the reading log as a CSV, `python3 scripts/failure_modes.py log.csv --costs costs.csv --monthly-volume N` computes counts, shares with intervals, the saturation point and monthly cost; by hand, apply the same rules.
7. **Decide per mode: fix, evaluate or accept.**
   - **Specification failure → fix now, no evaluator yet.** The prompt, the inputs, the KB or a tool never gave the model what it needed: an instruction nobody wrote, the user's country never passed, a new policy missing from the KB. Fix it, re-run the failing traces after the fix, and keep them as regression cases. A judge built for a failure the spec never asked to avoid measures the gap instead of closing it.
   - **Generalisation failure → evaluate.** The instruction and the inputs were there and the model still fails sometimes. Pick the cheapest evaluator that decides it: a code check first (a number against the system of record, a required field or link present, language, length, schema, tool called); an LLM judge only when code cannot decide (an unsupported claim, a wrong reasoning step). One binary judge per mode, never one overall judge, validated against the expert's labels with `llm-judge-calibration` before it scores the full traffic or anyone trusts it: read it as TPR and TNR, since raw agreement hides a judge that passes everything.
   - **Accept**, with a written rationale, an owner and a re-check date, when the expected cost is below the cost of fixing and evaluating and the mode has no legal, privacy or irreversible effect.
8. **Agents and pipelines.** For multi-step traces, also record for each failing trace the last step that succeeded and the first step that failed. The matrix of those pairs shows where runs break; hand it to `agent-evals`. A mode rooted in retrieval goes to `retrieval-evaluation`.
9. **Hand over and re-run.** Modes to evaluate go to `build-evals` (graders, per-class thresholds, the failing traces as cases); judges to `llm-judge-calibration`; classes with too few traces to `synthetic-eval-data`; prompt and guardrail fixes to `system-prompt-and-guardrails`; KB gaps to the KB owner. Re-run the analysis after every significant change (model, prompt, KB, provider version), after a complaint spike, and on a fixed cadence on fresh production traces (`production-evals-monitoring`). Each new mode becomes regression cases.

## Output
A failure-mode report following `templates/failure-modes.md`: sampling plan and masking, reading log summary (traces read per stream, last new mode, saturation reached or not, taxonomy version), failure-mode table (mode, definition, pass and fail example, count, share with interval, classes affected, cost per occurrence and its source, expected monthly cost, priority, action, evaluator), step matrix for agents, handovers, and open questions with owners. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Never choose metrics, graders or a judge from a generic list before real outputs have been read.
- Never let an LLM do the first reading alone. It may cluster the expert's notes afterwards, and later score a mode as a calibrated judge.
- Never declare the taxonomy final below saturation: label it provisional, with the number of traces read since the last new mode.
- Binary pass/fail per mode, never a Likert scale.
- Rates come from the random stream only, with their interval; targeted traces never give a rate.
- Personal data is masked before anyone reads a trace or sends it to a model.
- No failure cost without a sourced unit cost (references/roi-model.md); regulatory exposure goes to counsel as a question.

## Links
references/eval-statistics.md · references/roi-model.md · references/autonomy-ladder.md · references/error-analysis-guide.md · build-evals · llm-judge-calibration · synthetic-eval-data · agent-evals · retrieval-evaluation · conversation-analysis · system-prompt-and-guardrails · production-evals-monitoring

## Sources
- husain-shankar-evals: error analysis before metrics, open then axial coding until no new mode appears, the first upstream failure, binary criteria over Likert scales, specification versus generalisation failures, code checks before judges, the step matrix for agents.
- shankar-validators: criteria drift while grading, hence definitions written after reading outputs and versioned.
- glaser-strauss-grounded-theory: open coding, axial coding and theoretical saturation, the lineage of the method.
- repo-chanmeng: reading real outputs before writing any grader (idea, own words).
- wilson-interval: the interval on a mode's share, and the rule of three for a mode not yet seen.
- gdpr: data minimisation behind masking before reading.
- own-error-analysis: the two sampling streams, pricing per mode and the fix, evaluate or accept decision, from error analyses of assistants in production (method only).
