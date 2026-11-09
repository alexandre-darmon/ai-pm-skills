# Skill eval gains

Same model, same cases, three arms: the model alone, the model given only the skill's output template, and the model with the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| Same cases, Sonnet 5.5 answering | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |
| --- | --- | --- | --- | --- | --- |
| Regex graders: 6 skills, 21 cases × 3 runs | 44% | 83% | **99%** | +55 [+49, +63] | +16 [+9, +23] |
| Blind LLM judge, Haiku 5.5: 4 of these skills, 14 cases, not calibrated | 71% | 78% | 81% | +10 [+6, +14] | +3 [+1, +5] |
| Blind LLM judge, Sonnet 5.5: 4 of these skills, 14 cases, not calibrated | 70% | 76% | 82% | +11 [+6, +17] | +5 [+3, +7] |
| Red lines held (the one thing the answer must never do) | 61% | 91% | **100%** | | |
| Stays silent on near-miss requests | — | — | **100%** | | |

Gains in points. Brackets: 95% interval over cases (see below).

## Per skill, regex graders

| Skill | Without | Template only | With | Gain over the model alone (lowest to highest case) | Gain over the template | Red lines held: without / template / with | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | 68% | 91% | **100%** | +32 pts (+27 to +41) | +9 pts | 89% / 100% / 100% | 3 × 3 | 2026-11-06 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | 27% | 78% | **99%** | +72 pts (+48 to +100) | +21 pts | 56% / 100% / 100% | 3 × 3 | 2026-11-06 |
| [`build-evals`](skills/build-evals/SKILL.md) | 51% | 85% | **100%** | +49 pts (+33 to +67) | +15 pts | 58% / 100% / 100% | 4 × 3 | 2026-11-06 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | 21% | 80% | **96%** | +75 pts (+48 to +100) | +17 pts | 50% / 83% / 100% | 4 × 3 | 2026-11-06 |
| [`cse-consultation`](skills/cse-consultation/SKILL.md) | 65% | 91% | **99%** | +35 pts (+28 to +44) | +8 pts | 100% / 100% / 100% | 4 × 3 | 2026-11-06 |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | 29% | 76% | **100%** | +71 pts (+67 to +75) | +24 pts | 0% / 50% / 100% | 3 × 3 | 2026-11-06 |

## Per skill, blind LLM judges

| Skill | Judge | Without | Template only | With | Gain over the model alone | Gain over the template | Judge noise | Words: without / template / with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `assistant-kpis-cost-per-outcome` | Haiku 5.5 | 67% | 83% | 82% | +15 pts | -1 pts | 5 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Haiku 5.5 | 76% | 81% | 79% | +3 pts | -2 pts | 8 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Haiku 5.5 | 68% | 71% | 75% | +8 pts | +4 pts | 5 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Haiku 5.5 | 72% | 76% | 87% | +16 pts | +12 pts | 4 pts | 1,469 / 2,290 / 1,783 |
| `assistant-kpis-cost-per-outcome` | Sonnet 5.5 | 66% | 77% | 82% | +16 pts | +5 pts | 2 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Sonnet 5.5 | 79% | 83% | 84% | +4 pts | 0 pts | 3 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Sonnet 5.5 | 62% | 70% | 78% | +15 pts | +8 pts | 3 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Sonnet 5.5 | 74% | 75% | 82% | +9 pts | +7 pts | 3 pts | 1,469 / 2,290 / 1,783 |

## How to read it

- **Regex graders**: share of graders passed on a case, averaged over runs, then over a skill's scored cases, then over skills. A grader checks one thing the answer must contain or must not contain. The skills' author wrote them, so they reward what the skill asks for.
- **Template only**: the model gets the skill's own output template without its method. The gain over the template is what the method adds beyond the format ([template-only control](docs/evaluation.md)).
- **Blind LLM judge**: a model grades each answer twice on a generic rubric (sound, actionable, honest about unknowns, risk-aware, specific) without knowing the arm. Not calibrated on human scores yet, so a signal, not a measure; it tends to favour longer answers and never grades the legal skills. Both judges are shown until the calibration rule committed in [docs/evaluation.md](docs/evaluation.md) picks one. Judge noise is the mean gap between its two passes on the same answer.
- **Intervals**: resample the cases within each skill 10,000 times and keep the middle 95% of the gains, with a small-sample correction (Rao-Wu rescaling, [scripts/eval_stats.py](scripts/eval_stats.py)). They show how much the gain depends on which cases were written. They do not cover the choice of graders, the judge's biases, or another model. Per skill, 3 to 5 cases are too few for an interval: the table gives the lowest and highest case gain instead.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its regex score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain over the model alone is at least 10 points. Details in [docs/evaluation.md](docs/evaluation.md).
- **Runs**: 3 per case and per arm, November 2026. Two red-line graders (`assistant-kpis-cost-per-outcome`, `conversation-analysis`) were corrected after that run because they rejected correct answers; the saved answers were then re-scored.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
