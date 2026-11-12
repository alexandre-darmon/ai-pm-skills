---
name: build-evals
description: 'Build or review AI eval sets, graders, thresholds. For an eval stub, disputed quality, which pipeline step fails, a costly class at N of M just over its signed bar. Not to pick between scored models.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.6.4"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "llm-feature-prd, error-analysis"
  feeds: "llm-judge-calibration, model-selection, ai-vendor-evaluation, release-to-production, production-evals-monitoring, model-card-ai-registry"
  sources: "anthropic-evals, husain-shankar-evals, miller-error-bars, wilson-interval, text-to-sql-benchmarks, kalai-hallucinate, ai2-signal-noise, anthropic-agent-evals, own-golden-sets, kohavi-experiments, repo-chanmeng, repo-vishalhabib, repo-lenny"
---

# build-evals

## When to use
- A PRD has an eval stub and the feature needs a real eval set before build or model choice.
- An existing eval suite or its pass rule (sampling, thresholds, judge) needs a review before a release.
- A pipeline of several steps (extraction, routing, text-to-SQL, generation, validation rules) misses its target, or someone wants to swap one of its models or components before knowing which step fails.
- Quality is disputed: "it works for me", thumbs-up rates, anecdotes.
- A costly class scores just above its signed threshold (say 97 of 100 against 95%) and its release depends on it: decide whether the evidence clears the gate.
- Do not use to pick between models already scored on an existing suite (which one goes to production, at what cost): that is `model-selection`.
- Do not use to run a release (shadow, canary, a provider model update): that is `release-to-production`, which applies this skill's gate.
- Do not use for a retrieval assistant or an agent that acts: that is `retrieval-evaluation` or `agent-evals`.

## Inputs
Mandatory: the task definition (input, expected output, who uses it), real examples, what "correct" means to the business, the question classes and their share of traffic.
Ask if missing: the budget for judge calls, who can label (domain experts, not the build team), the autonomy level the eval must gate.
Fewer than 20 real examples is not enough to build a set: ask for more before anything else. If they cannot exist yet, generate synthetic cases only with the synthetic share stated and flagged per case (method in `synthetic-eval-data`), and say the set is provisional until real cases replace them.

## Method
1. Restate the task and what "correct" means per question class, in the business's words. A class is a group of questions with the same risk and the same check (e.g. order status, legal claim). Name the one error that costs most and which way costs lean: the thresholds follow from it. Say per class whether a hand-off or "not sure" is an acceptable answer. Where a confident wrong answer costs more than a hand-off, grade correct, abstained and wrong apart, since accuracy alone rewards guessing: score correct − k × wrong, with k = cost of a wrong answer ÷ cost of a hand-off fixed before the run, and report coverage (share answered) beside the error rate on the answers given (references/eval-statistics.md §12).
2. Size the golden set. Start with 50–80 cases, at least 20 real, sampled per class by traffic and by risk, to find failure modes and set graders. Before the set gates anything, size each gated class for the margin its threshold needs (references/eval-statistics.md §3): reading a rate near 90% within ±10 points takes about 35 cases, within ±5 points about 140. A rare class with legal or financial impact gets the cases its threshold needs, whatever its traffic share. Keep 20% as a private holdout, never in a public repo, a prompt or an article.
3. Read outputs before choosing any grader. If outputs exist (a previous version, a prototype, production traces, errors from the human process), run `error-analysis` on 50 to 100 of them: free notes by a domain expert, grouped into failure modes, until new outputs add no new mode. Graders then target what was seen; a mode the spec never asked for is fixed, not evaluated. With no outputs yet, mark graders as provisional and do this read at the first prototype. A production failure found later joins the set as a regression case.
4. Pick a grader per failure mode, cheapest first: exact (regex, field equality, tool called) for anything yes/no; checklist (one exact check per mandatory item) for structure; an LLM judge only for what code cannot decide (faithfulness, tone, reasoning), with one binary pass/fail verdict per failure mode, never a 1–5 score. For an agent, a final-message grader is not enough: hand over to `agent-evals`; for retrieval, to `retrieval-evaluation`.
5. For a pipeline of several steps, run two evals, never one (references/component-evals.md, which also covers text-to-SQL and a confidence score shown to users):
   - **End to end gates the release**, per class, including a model or component swap: a component that improves while the end-to-end score does not move does not ship.
   - **Per component locates the failure**: each step gets its own labelled check, 30 to 50 cases with that step's output labelled (more for a step that gates a costly class), graded with the cheapest check for that step.
   - Before choosing what to change, label on every failed end-to-end case the first step that went wrong; the counts per step say where to work.
   - Score a downstream step on frozen upstream outputs, stored once, so two changes never move at once. Change one component at a time, compare old and new paired on the same cases (step 8), then re-run end to end.
6. Validate every judge before trusting it, on expert labels kept apart from the ones used to write its prompt. Read it as a classifier: TPR (share of expert passes it passes) and TNR (share of expert fails it fails), each at 80% or more, stricter for classes with legal or irreversible effects. Raw agreement is not enough: when most answers pass, a judge that passes everything agrees often and catches nothing. Below the bar, the judge is not a gate: read the disagreements, revise the rubric (split vague criteria, add pass and fail examples), re-test on fresh labels, and meanwhile a human reviews what the judge would have decided. Full method, bias checks and the corrected pass rate: `llm-judge-calibration`.
7. Set one threshold per question class, never a single global one: a global score lets a large easy class hide a failing risky class. Stricter thresholds for classes with legal, financial or irreversible effects. Report each class with its number of cases and its 95% interval. For a class where a false pass is costly, the gate passes only when the lower bound of the interval clears the threshold (references/eval-statistics.md §2, §4): twelve passes out of twelve cannot demonstrate 95%, nor can 97 of 100 (lower bound about 92%). A point score above the bar with the lower bound under it is "not demonstrated", never "passes as written": ship the classes that clear their gate, keep the costly one under human review (or hold it), and size it. When the true rate sits just above the bar, the lower bound clears 95% only with about 200 cases at a true 98%, 450 at 97%, 1,800 at 96%; a one-point gap needs over a thousand cases at any bar. Say so, since more cases before the planned date will not settle it. Reading a costly class's threshold on its lower bound tightens it, it does not move it; only the signer can accept the residual risk, in writing. Write each threshold down, dated, with its reading (lower bound or point), who signs it and who may relax it, before the run it judges: a bar drawn after seeing the scores only describes them. At least one class or check can never be relaxed.
8. Freeze a baseline: run the current system (or the model alone, or the human process) on the set, and store the result with model name and version, judge model, date and set version. Later runs compare to it on the same cases, paired: a gap inside the noise is a tie (references/eval-statistics.md §5). Keep two suites with different jobs (§14): a regression suite of cases the baseline passes, which must stay near 100% on every change, provider model updates included, and a capability suite of hard cases it mostly fails, which shows progress. A case moves to regression once it passes in every run of two releases in a row; a case every candidate passes, or whose result flips more between runs than between systems, leaves the decision set.
9. Score economics with successes as denominator: cost per correct outcome = total cost ÷ (volume × quality), never ÷ all outputs (references/roi-model.md).
10. When a class misses its bar, improve in controlled runs: rank fixes by failure share, record a prediction before each run, test one variant against the frozen baseline, stop on a rule fixed in advance (references/improve-loop.md).
11. Write the cases in the target harness format. For a Claude Code skill or plugin, use `claude plugin eval` cases: one folder per case with `prompt.md` and `graders/`. The method does not depend on the harness: the same cases fit Inspect or Promptfoo.

## Output
An eval plan following `templates/eval-plan.md`: task and classes, set composition (real, synthetic, holdout) and the size each gated class needs, failure modes read and graders per check, a check per step for a pipeline, judge validation status (TPR, TNR), dated and signed thresholds per class, scores with intervals (and coverage where abstaining is allowed), baseline with its regression and capability suites, cost per correct outcome, and what the eval gates. Sections that cannot be filled say what is missing and who provides it. The plan is evidence for the readers in references/evals-as-evidence.md.

## Rules and red lines
- Never build or accept a set on fewer than 20 real examples without saying it is provisional and stating the synthetic share.
- Never use a judge as a release or level gate unless its TPR and TNR on held-out expert labels each reach the bar set beforehand (80% by default), whatever the deadline. Raw agreement alone never qualifies a judge.
- Never one global threshold over several question classes.
- In a pipeline, never ship a model or component swap on its component score: the end-to-end score per class gates the release.
- Never sign off a costly class on a point score when its interval's lower bound is under the threshold: the class stays under human review or held until enough cases clear it; the other classes ship on their own results.
- Never move a threshold after seeing the scores it judges unless the named person signs and dates the change, and never move the one marked as not relaxable.
- The holdout never leaves private storage.
- A baseline without model name, judge model and date is not a baseline.
- Score on cost per correct outcome, not on score alone.

## Links
references/autonomy-ladder.md · references/roi-model.md · references/eval-statistics.md · references/evals-as-evidence.md · references/agent-evals.md · references/component-evals.md · references/improve-loop.md · llm-feature-prd · error-analysis · llm-judge-calibration · synthetic-eval-data · agent-evals · retrieval-evaluation · model-selection · release-to-production · production-evals-monitoring · system-prompt-and-guardrails

## Sources
- anthropic-evals: eval design, grader choice, judge use.
- husain-shankar-evals: reading outputs before metrics, binary criteria per failure mode, judges read as TPR and TNR.
- miller-error-bars: scores with standard errors, paired comparisons on the same cases.
- wilson-interval: intervals for a class score with few cases; zero failures is not zero risk.
- text-to-sql-benchmarks: grading text-to-SQL on the executed result, in references/component-evals.md.
- kalai-hallucinate: accuracy alone rewards guessing; abstention graded apart, a confident error priced above a hand-off.
- anthropic-agent-evals: capability suites apart from regression suites.
- ai2-signal-noise: dropping cases whose run-to-run noise exceeds the spread between systems.
- own-golden-sets: set sizing, per-class thresholds and the judge revision loop from client eval work.
- repo-chanmeng: reading outputs before writing graders, thresholds signed before the run, agent run grading.
- repo-vishalhabib: starting from the costliest error, gates fixed before results.
- repo-lenny: locating the breaking step of an agent run, as an idea.
- kohavi-experiments: the improve loop in references/improve-loop.md (one change against a fixed control, decision rule and stopping rule written before the run).
