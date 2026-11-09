# Eval plan — <feature name>

## Task and what "correct" means
| Question class | Share of traffic | Risk (legal, financial, irreversible?) | Correct means | Hand-off acceptable? Price of a wrong answer (k) |
| --- | --- | --- | --- | --- |
<Costliest error, and which way costs lean. Where abstaining is allowed: score = correct − k × wrong, k = cost of a wrong answer ÷ cost of a hand-off, set before the run.>

## Set composition
| Class | Real cases | Synthetic cases (flagged) | Holdout (20%, private) | Cases needed for the threshold's margin |
| --- | --- | --- | --- | --- |
<Total. Provisional until <date or condition> if real cases < 20. Size per class from references/eval-statistics.md §3.>

## Failure modes read
<Outputs read (how many, from where), failure modes found. If none exist yet: graders provisional until the first prototype is read.>

## Graders
| Check | Failure mode it targets (seen or provisional) | Grader (exact, checklist, judge) | Why this grader |
| --- | --- | --- | --- |

## Pipeline steps (if several)
<End to end gates the release; these checks only locate the failure. Downstream steps scored on frozen upstream outputs.>
| Step | Correct means (its output alone) | Labelled cases | Check | First failing step on failed end-to-end cases (count) |
| --- | --- | --- | --- | --- |

## Judge validation
<Per judge: the failure mode it checks (binary), expert labels (how many passes and fails, kept apart from the prompt-writing ones), TPR and TNR with intervals, the bar set beforehand, status: gate / not a gate yet. Disagreements read and rubric changes. Details: llm-judge-calibration.>

## Thresholds per class
<All written before the run they judge. At least one row says "nobody" under who may relax.>
| Class | Threshold | Gate on (point or lower bound) | Why | Date set | Signed by | Who may relax |
| --- | --- | --- | --- | --- | --- | --- |

## Baseline
<System run, model and version, judge model, date, set version, scores per class with number of cases and 95% interval (coverage and error rate on answers given where abstaining is allowed).>
<Regression suite: cases the baseline passes, must stay near 100% on every change. Capability suite: hard cases it mostly fails, shows progress. Cases retired (every candidate passes, or more noise between runs than between systems).>

## Economics
<Cost per correct outcome = total cost ÷ (volume × quality), with inputs.>

## What this eval gates
<Release, model choice, or autonomy level move (references/autonomy-ladder.md), and who decides.>

## Open questions
| Question | Owner |
| --- | --- |
