I couldn't write the plan to a file because the Write tool is disabled in this session, so it's below.

**No, we can't use the judge as the release gate yet.** It agrees with the experts on 31 of 50 answers (62%), and the bar for gating is 80% (at least 40 of 50). At 62%, about one verdict in three disagrees with the HR experts. A judge score above 90% would not mean the answers are 90% correct.

A few more things work against the gate as proposed:
- **Error direction is unknown.** If the judge passes wrong answers, the score overstates quality. That is the dangerous direction for leave and expenses. Pull the judge-versus-expert confusion matrix and the agreement per class.
- **Expert agreement matters.** Check how often the three experts agree with each other, because that caps how well any judge can do.
- **A single ">90% overall" threshold is the wrong rule.** A large easy class can hide a failing risky one, such as statutory leave or expense amounts. Use one threshold per class.
- **50 cases is too few to tell 90% from 80%.** A 90% observed score has a 95% interval of roughly 79–96%.

# Eval plan: HR assistant (leave and expenses), Friday release

## Task and what "correct" means
| Class | Traffic share | Risk | Correct means |
|---|---|---|---|
| Leave (entitlement, accrual, carry-over, statutory) | TBD (HR) | Legal for statutory leave | Matches current policy and law, invents nothing, escalates edge cases |
| Expenses (limits, eligibility, process) | TBD | Financial | Matches policy limits and process, invents no amounts |
| Out of scope | TBD | Medium | Says it can't answer and routes to HR |

These classes are a draft. HR needs to confirm them and give traffic shares from real logs.

## Set composition
- **Size:** 50–80 cases, at least 20 real, with 20% kept as a private holdout.
- **Oversampling:** statutory leave and expense amounts get more cases than their traffic share.
- **Seed set:** the 50 labelled answers can seed it if they are real traffic.
- **Status:** provisional until the real and synthetic counts per class are filled in. Flag every synthetic case.

## Graders
- **Policy figures (days, limits, amounts):** exact match against the policy value.
- **Required items (cites policy, names the escalation route):** checklist with one exact check per item.
- **Overall correctness and faithfulness:** LLM judge with a written rubric, only for what text matching can't decide.

Move as many checks as possible to the exact and checklist graders, so the judge decides less.

## Judge calibration
- **Status:** 31/50 = 62%, **not a gate**.
- **Loop to run before Friday:**
  1. Read the 19 disagreements and group them: vague criteria, missing policy context, or experts split.
  2. Revise the rubric. Split vague criteria, add pass and fail examples, and give the judge the policy text.
  3. Re-run on a fresh batch of at least 20 expert-labelled cases, not the original 50, to avoid overfitting.
  4. Repeat until agreement is at least 80%.
- **Until it passes:** a human reviews what the judge would have decided.

## Thresholds per class (proposed, HR and Legal to set)
| Class | Threshold |
|---|---|
| Statutory leave | ≥ 98%, no critical errors |
| Other leave | ≥ 95% |
| Expenses | ≥ 95%, zero wrong amounts or limits |
| Out of scope | ≥ 90% correct deflection |

Report a confidence interval alongside each class score.

## Baseline
Missing. Run the current production version, or the model alone, on the set. Record the model name and version, judge model, date and set version. Without those it isn't a baseline.

## Economics
Cost per correct outcome = total cost ÷ (volume × quality). The inputs are missing: cost per answer, monthly volume, and the cost of a human HR response. Product owns these.

## What this eval gates
The Friday release, decided by the HR lead and the product owner. The rule should be:
- Every class meets its threshold on the exact and checklist graders.
- Judge-graded checks are human-reviewed until the judge is calibrated.
- A judge-only score above 90% is not enough.

## Open questions
| Question | Owner |
|---|---|
| Class list and traffic shares from real logs | HR / product |
| Are the 50 labelled answers real traffic, and what is the per-class split? | Eval owner |
| Confusion matrix and expert-to-expert agreement | Eval owner |
| A fresh batch of at least 20 labelled cases for re-calibration | HR experts |
| Per-class thresholds | HR + Legal |
| Baseline run and cost inputs | Eval owner / product |
| Can Friday's answers be human-reviewed, or does the date move? | Release owner |

**For Friday:** the achievable path is exact and checklist graders plus human review of the judge-graded checks. If the rubric revision reaches 80% on a fresh batch by then, the judge can take over part of the review. I can save this as a file if you re-enable Write or tell me where you'd like it.