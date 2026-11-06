---
name: build-evals
description: Build or review the eval set, graders, thresholds and baseline that decide if an AI feature is good enough. Use for a PRD eval stub, an eval suite to review, a release gate, or disputed quality.
stage: measure
version: 0.2.0
depends_on: [llm-feature-prd]
feeds: [model-selection, release-to-production, system-prompt-and-guardrails, process-ai-redesign]
autonomy_relevant: true
sources: [anthropic-evals, own-golden-sets, repo-chanmeng, repo-vishalhabib, repo-lenny]
eval_threshold: 0.80
status: tested
---

# build-evals

## When to use
- A PRD has an eval stub and the feature needs a real eval set before build or model choice.
- An existing eval suite or its pass rule (sampling, thresholds, judge) needs a review before a release.
- A release, a model change or a level change (references/autonomy-ladder.md) needs a measured gate.
- Quality is disputed: "it works for me", thumbs-up rates, anecdotes.
- An LLM judge exists and nobody knows if it can be trusted.
- Do not use to compare models on an existing suite: that is `model-selection`.
- Do not use for a production KPI: that is `assistant-kpis-cost-per-outcome`.

## Inputs
Mandatory: the task definition (input, expected output, who uses it), real examples, what "correct" means to the business, the question classes and their share of traffic.
Ask if missing: the budget for judge calls, who can label (domain experts, not the build team), the autonomy level the eval must gate.
Fewer than 20 real examples is not enough to build a set: ask for more before anything else. If they cannot exist yet, generate synthetic cases only with the synthetic share stated and flagged per case, and say the set is provisional until real cases replace them.

## Method
1. Restate the task and what "correct" means per question class, in the business's words. A class is a group of questions with the same risk and the same check (e.g. order status, legal claim). Name the one error that costs most and which way costs lean: the thresholds follow from it.
2. Size the golden set: 50–80 cases to start, at least 20 real. Sample per class by traffic and by risk: a rare class with legal or financial impact gets more cases than its traffic share. Keep 20% as a private holdout, never in a public repo, a prompt or an article.
3. If outputs already exist (a previous version, a prototype, production traces, or errors from the human process), read 20 to 50 of them before choosing any grader. Note freely what went wrong in each, group the notes into failure modes, and stop when new outputs add no new mode. Graders then target what was seen. With no outputs yet, mark graders as provisional and do this read at the first prototype. A production failure found later joins the set as a regression case.
4. Pick a grader per check, cheapest first: exact (regex, field equality, tool called) for anything yes/no; checklist (one exact check per mandatory item) for structure; LLM judge with a written rubric only for what text matching cannot decide (coherence, tone, faithfulness). For an agent or a retrieval (RAG) feature, a final-message grader is not enough: load references/agent-evals.md.
5. Calibrate every judge before trusting it: 20 or more cases labelled by domain experts, agreement ≥ 80%. Below 80%, the judge is not a gate: read the disagreements, revise the rubric (split vague criteria, add pass and fail examples), re-run, repeat. Until it passes, a human reviews what the judge would have decided.
6. Set one threshold per question class, never a single global one: a global score lets a large easy class hide a failing risky class. Stricter thresholds for classes with legal, financial or irreversible effects. Report the score per class. Write each threshold down, dated, with who signs it and who may relax it, before the run it judges: a bar drawn after seeing the scores only describes them. At least one class or check can never be relaxed.
7. Freeze a baseline: run the current system (or the model alone, or the human process) on the set, and store the result with model name and version, judge model, date and set version. Later runs compare to it.
8. Score economics with successes as denominator: cost per correct outcome = total cost ÷ (volume × quality), never ÷ all outputs (references/roi-model.md).
9. Write the cases in the target harness format. For a Claude Code skill or plugin, use `claude plugin eval` cases: one folder per case with `prompt.md` and `graders/`.

## Output
An eval plan following `templates/eval-plan.md`: task and classes, set composition (real, synthetic, holdout), failure modes read and graders per check, judge calibration status, dated and signed thresholds per class, baseline, cost per correct outcome, and what the eval gates. Sections that cannot be filled say what is missing and who provides it.

## Rules and red lines
- Never build or accept a set on fewer than 20 real examples without saying it is provisional and stating the synthetic share.
- Never use an uncalibrated judge, or one below 80% agreement, as a release or level gate, whatever the deadline.
- Never one global threshold over several question classes.
- Never move a threshold after seeing the scores it judges unless the named person signs and dates the change, and never move the one marked as not relaxable.
- The holdout never leaves private storage.
- A baseline without model name, judge model and date is not a baseline.
- Score on cost per correct outcome, not on score alone.

## Links
references/autonomy-ladder.md · references/roi-model.md · references/agent-evals.md · llm-feature-prd · model-selection · release-to-production · system-prompt-and-guardrails

## Sources
- anthropic-evals: eval design, grader choice, judge use.
- own-golden-sets: set sizing, per-class thresholds and judge calibration loop from client eval work.
- repo-chanmeng: reading outputs before writing graders, thresholds signed before the run, agent run grading.
- repo-vishalhabib: starting from the costliest error, gates fixed before results.
- repo-lenny: locating the breaking step of an agent run, as an idea.
