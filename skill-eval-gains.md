# Skill eval gains

Same model, same cases, with and without the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| | Without skill | With skill |
| --- | --- | --- |
| Mean score on the scored cases | 44% | **99%** |
| Red lines held (the one thing the answer must never do) | 61% | **100%** |
| Stays silent on near-miss requests | — | **100%** |

## Per skill

| Skill | Without | With | Gain | Red lines held (with vs without) | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | 68% | **100%** | +32 pts | 100% vs 89% | 3 × 3 | 2026-11-06 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | 27% | **99%** | +72 pts | 100% vs 56% | 3 × 3 | 2026-11-06 |
| [`build-evals`](skills/build-evals/SKILL.md) | 51% | **100%** | +49 pts | 100% vs 58% | 4 × 3 | 2026-11-06 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | 21% | **96%** | +75 pts | 100% vs 50% | 4 × 3 | 2026-11-06 |
| [`cse-consultation`](skills/cse-consultation/SKILL.md) | 65% | **99%** | +35 pts | 100% vs 100% | 4 × 3 | 2026-11-06 |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | 29% | **100%** | +71 pts | 100% vs 0% | 3 × 3 | 2026-11-06 |

## How to read it

- **Score**: share of graders passed on a case, averaged over runs and over the scored cases. A grader checks one thing the answer must contain or must not contain (regex, free and deterministic).
- **Without / With**: the same prompt run by the same model (Sonnet 5.5), once without the skill and once with it loaded.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain is at least 10 points. Details in [docs/evaluation.md](docs/evaluation.md).
- **Runs**: 3 per case and per arm, November 2026. Two red-line graders (`assistant-kpis-cost-per-outcome`, `conversation-analysis`) were corrected after that run because they rejected correct answers; the saved answers were then re-scored. Graders are written by the skills' author, and no template-only control has been run yet.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
