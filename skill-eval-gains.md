# Skill eval gains

Same model, same cases, with and without the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| | Without skill | With skill |
| --- | --- | --- |
| Mean score on the scored cases | 45% | **99%** |
| Red lines held (the one thing the answer must never do) | 63% | **100%** |
| Stays silent on near-miss requests | — | **100%** |

## Per skill

| Skill | Without | With | Gain | Red lines held (with vs without) | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | 74% | **100%** | +26 pts | 100% vs 100% | 3 × 3 | 2026-11-04 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | 23% | **98%** | +75 pts | 100% vs 44% | 3 × 3 | 2026-11-04 |
| [`build-evals`](skills/build-evals/SKILL.md) | 44% | **100%** | +56 pts | 100% vs 50% | 3 × 1 | 2026-11-02 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | 29% | **95%** | +67 pts | 100% vs 50% | 3 × 1 | 2026-11-04 |
| [`cse-consultation`](skills/cse-consultation/SKILL.md) | 72% | **100%** | +28 pts | 100% vs 100% | 3 × 3 | 2026-11-04 |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | 29% | **100%** | +71 pts | 100% vs 0% | 3 × 3 | 2026-11-04 |

## How to read it

- **Score**: share of graders passed on a case, averaged over runs and over the scored cases. A grader checks one thing the answer must contain or must not contain (regex, free and deterministic).
- **Without / With**: the same prompt run by the same model (Sonnet 5.5), once without the skill and once with it loaded.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain is positive. Details in [docs/evaluation.md](docs/evaluation.md).
- **Re-confirmation pending** (paid runs paused): the `build-evals` and `conversation-analysis` rows are 1-run baselines; on their last 3-run check each missed a red line once, and the graders were refitted since. `llm-feature-prd` changed after its run.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
