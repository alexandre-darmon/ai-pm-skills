# Eval plan — <feature name>

## Task and what "correct" means
| Question class | Share of traffic | Risk (legal, financial, irreversible?) | Correct means |
| --- | --- | --- | --- |
<Costliest error, and which way costs lean.>

## Set composition
| Class | Real cases | Synthetic cases (flagged) | Holdout (20%, private) | Cases needed for the threshold's margin |
| --- | --- | --- | --- | --- |
<Total. Provisional until <date or condition> if real cases < 20. Size per class from references/eval-statistics.md §3.>

## Failure modes read
<Outputs read (how many, from where), failure modes found. If none exist yet: graders provisional until the first prototype is read.>

## Graders
| Check | Failure mode it targets (seen or provisional) | Grader (exact, checklist, judge) | Why this grader |
| --- | --- | --- | --- |

## Judge validation
<Per judge: the failure mode it checks (binary), expert labels (how many passes and fails, kept apart from the prompt-writing ones), TPR and TNR with intervals, the bar set beforehand, status: gate / not a gate yet. Disagreements read and rubric changes. Details: llm-judge-calibration.>

## Thresholds per class
<All written before the run they judge. At least one row says "nobody" under who may relax.>
| Class | Threshold | Gate on (point or lower bound) | Why | Date set | Signed by | Who may relax |
| --- | --- | --- | --- | --- | --- | --- |

## Baseline
<System run, model and version, judge model, date, set version, scores per class with number of cases and 95% interval.>

## Economics
<Cost per correct outcome = total cost ÷ (volume × quality), with inputs.>

## What this eval gates
<Release, model choice, or autonomy level move (references/autonomy-ladder.md), and who decides.>

## Open questions
| Question | Owner |
| --- | --- |
