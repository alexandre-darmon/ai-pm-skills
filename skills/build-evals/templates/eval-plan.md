# Eval plan — <feature name>

## Task and what "correct" means
| Question class | Share of traffic | Risk (legal, financial, irreversible?) | Correct means |
| --- | --- | --- | --- |
<Costliest error, and which way costs lean.>

## Set composition
| Class | Real cases | Synthetic cases (flagged) | Holdout (20%, private) |
| --- | --- | --- | --- |
<Total. Provisional until <date or condition> if real cases < 20.>

## Failure modes read
<Outputs read (how many, from where), failure modes found. If none exist yet: graders provisional until the first prototype is read.>

## Graders
| Check | Failure mode it targets (seen or provisional) | Grader (exact, checklist, judge) | Why this grader |
| --- | --- | --- | --- |

## Judge calibration
<Labelled cases, labellers, agreement rate, status: calibrated (≥ 80%) / not a gate yet. Disagreement analysis and rubric changes.>

## Thresholds per class
<All written before the run they judge. At least one row says "nobody" under who may relax.>
| Class | Threshold | Why | Date set | Signed by | Who may relax |
| --- | --- | --- | --- | --- | --- |

## Baseline
<System run, model and version, judge model, date, set version, scores per class.>

## Economics
<Cost per correct outcome = total cost ÷ (volume × quality), with inputs.>

## What this eval gates
<Release, model choice, or autonomy level move (references/autonomy-ladder.md), and who decides.>

## Open questions
| Question | Owner |
| --- | --- |
