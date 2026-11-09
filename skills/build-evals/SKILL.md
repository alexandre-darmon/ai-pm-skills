---
name: build-evals
description: Build or review the eval set, graders, thresholds and baseline that decide if an AI feature is good enough. Use for a PRD eval stub, an eval suite to review, a release gate, or disputed quality.
stage: evaluate
version: 0.3.0
depends_on: [llm-feature-prd, error-analysis]
feeds: [llm-judge-calibration, model-selection, ai-vendor-evaluation, release-to-production, production-evals-monitoring, model-card-ai-registry]
autonomy_relevant: true
sources: [anthropic-evals, husain-shankar-evals, miller-error-bars, wilson-interval, own-golden-sets, repo-chanmeng, repo-vishalhabib, repo-lenny]
eval_threshold: 0.80
status: tested
---

# build-evals

## When to use
- A PRD has an eval stub and the feature needs a real eval set before build or model choice.
- An existing eval suite or its pass rule (sampling, thresholds, judge) needs a review before a release.
- A release, a model change or a level change (references/autonomy-ladder.md) needs a measured gate.
- Quality is disputed: "it works for me", thumbs-up rates, anecdotes.
- Do not use to compare models on an existing suite: that is `model-selection`.
- Do not use to watch quality after release: that is `production-evals-monitoring`.

## Inputs
Mandatory: the task definition (input, expected output, who uses it), real examples, what "correct" means to the business, the question classes and their share of traffic.
Ask if missing: the budget for judge calls, who can label (domain experts, not the build team), the autonomy level the eval must gate.
Fewer than 20 real examples is not enough to build a set: ask for more before anything else. If they cannot exist yet, generate synthetic cases only with the synthetic share stated and flagged per case (method in `synthetic-eval-data`), and say the set is provisional until real cases replace them.

## Method
1. Restate the task and what "correct" means per question class, in the business's words. A class is a group of questions with the same risk and the same check (e.g. order status, legal claim). Name the one error that costs most and which way costs lean: the thresholds follow from it.
2. Size the golden set. Start with 50–80 cases, at least 20 real, sampled per class by traffic and by risk, to find failure modes and set graders. Before the set gates anything, size each gated class for the margin its threshold needs (references/eval-statistics.md §3): reading a rate near 90% within ±10 points takes about 35 cases, within ±5 points about 140. A rare class with legal or financial impact gets the cases its threshold needs, whatever its traffic share. Keep 20% as a private holdout, never in a public repo, a prompt or an article.
3. Read outputs before choosing any grader. If outputs exist (a previous version, a prototype, production traces, errors from the human process), run `error-analysis` on 50 to 100 of them: free notes by a domain expert, grouped into failure modes, until new outputs add no new mode. Graders then target what was seen; a mode the spec never asked for is fixed, not evaluated. With no outputs yet, mark graders as provisional and do this read at the first prototype. A production failure found later joins the set as a regression case.
4. Pick a grader per failure mode, cheapest first: exact (regex, field equality, tool called) for anything yes/no; checklist (one exact check per mandatory item) for structure; an LLM judge only for what code cannot decide (faithfulness, tone, reasoning), with one binary pass/fail verdict per failure mode, never a 1–5 score. For an agent, a final-message grader is not enough: load references/agent-evals.md and hand over to `agent-evals`; for retrieval, score retrieval apart from generation (`retrieval-evaluation`).
5. Validate every judge before trusting it, on expert labels kept apart from the ones used to write its prompt. Read it as a classifier: TPR (share of expert passes it passes) and TNR (share of expert fails it fails), each at 80% or more, stricter for classes with legal or irreversible effects. Raw agreement is not enough: when most answers pass, a judge that passes everything agrees often and catches nothing. Below the bar, the judge is not a gate: read the disagreements, revise the rubric (split vague criteria, add pass and fail examples), re-test on fresh labels, and meanwhile a human reviews what the judge would have decided. Full method, bias checks and the corrected pass rate: `llm-judge-calibration`.
6. Set one threshold per question class, never a single global one: a global score lets a large easy class hide a failing risky class. Stricter thresholds for classes with legal, financial or irreversible effects. Report each class with its number of cases and its 95% interval. For a class where a false pass is costly, the gate passes only when the lower bound of the interval clears the threshold (references/eval-statistics.md §2, §4): twelve passes out of twelve cannot demonstrate 95%. Write each threshold down, dated, with who signs it and who may relax it, before the run it judges: a bar drawn after seeing the scores only describes them. At least one class or check can never be relaxed.
7. Freeze a baseline: run the current system (or the model alone, or the human process) on the set, and store the result with model name and version, judge model, date and set version. Later runs compare to it on the same cases, paired: a gap inside the noise is a tie (references/eval-statistics.md §5).
8. Score economics with successes as denominator: cost per correct outcome = total cost ÷ (volume × quality), never ÷ all outputs (references/roi-model.md).
9. Write the cases in the target harness format. For a Claude Code skill or plugin, use `claude plugin eval` cases: one folder per case with `prompt.md` and `graders/`. The method does not depend on the harness: the same cases fit Inspect or Promptfoo.

## Output
An eval plan following `templates/eval-plan.md`: task and classes, set composition (real, synthetic, holdout) and the size each gated class needs, failure modes read and graders per check, judge validation status (TPR, TNR), dated and signed thresholds per class, scores with intervals, baseline, cost per correct outcome, and what the eval gates. Sections that cannot be filled say what is missing and who provides it. The plan is evidence for the readers in references/evals-as-evidence.md.

## Rules and red lines
- Never build or accept a set on fewer than 20 real examples without saying it is provisional and stating the synthetic share.
- Never use a judge as a release or level gate unless its TPR and TNR on held-out expert labels each reach the bar set beforehand (80% by default), whatever the deadline. Raw agreement alone never qualifies a judge.
- Never one global threshold over several question classes.
- Never sign off a costly class on a point score when its interval's lower bound is under the threshold: add cases first.
- Never move a threshold after seeing the scores it judges unless the named person signs and dates the change, and never move the one marked as not relaxable.
- The holdout never leaves private storage.
- A baseline without model name, judge model and date is not a baseline.
- Score on cost per correct outcome, not on score alone.

## Links
references/autonomy-ladder.md · references/roi-model.md · references/eval-statistics.md · references/evals-as-evidence.md · references/agent-evals.md · llm-feature-prd · error-analysis · llm-judge-calibration · synthetic-eval-data · agent-evals · retrieval-evaluation · model-selection · release-to-production · production-evals-monitoring · system-prompt-and-guardrails

## Sources
- anthropic-evals: eval design, grader choice, judge use.
- husain-shankar-evals: reading outputs before metrics, binary criteria per failure mode, judges read as TPR and TNR.
- miller-error-bars: scores with standard errors, paired comparisons on the same cases.
- wilson-interval: intervals for a class score with few cases; zero failures is not zero risk.
- own-golden-sets: set sizing, per-class thresholds and the judge revision loop from client eval work.
- repo-chanmeng: reading outputs before writing graders, thresholds signed before the run, agent run grading.
- repo-vishalhabib: starting from the costliest error, gates fixed before results.
- repo-lenny: locating the breaking step of an agent run, as an idea.
