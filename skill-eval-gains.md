# Skill eval gains

Same model, same cases, three arms: the model alone, the model given only the skill's output template, and the model with the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| Same cases, Sonnet 5.5 answering | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |
| --- | --- | --- | --- | --- | --- |
| Regex graders: 29 skills, 109 cases × 3 runs | 52% | 82% | **96%** | +45 [+41, +48] | +17 [+6, +32] |
| Blind LLM judge, Haiku 5.5: 5 of these skills, 17 cases, earlier runs | 71% | 78% | 80% | +10 [+6, +13] | +3 [+1, +5] |
| Blind LLM judge, Sonnet 5.5: 9 of these skills, 29 cases, earlier runs | 72% | 76% | 82% | +9 [+6, +13] | +5 [+3, +7] |
| Blind LLM judge, openai/gpt-6.1-sol: 23 of these skills, 86 cases, recorded runs | 63% | — | 72% | +9 [+6, +12] | — |
| Blind decision model, typesafe/jev-1.14: 23 of these skills, 86 cases, recorded runs | 81% | — | 90% | +9 [+7, +11] | — |
| Red lines held (the one thing the answer must never do) | 71% | 88% | **100%** | | |
| Cost per correct answer, API equivalent (20 skills) | $0.102 | — | **$0.078** | -23% | |
| Stays silent on near-miss requests | — | — | **100%** | | |

Gains in points. Brackets: 95% interval over cases (see below).

## Per skill, regex graders

| Skill | Without | Template only | With | Gain over the model alone (lowest to highest case) | Gain over the template | Red lines held: without / template / with | Cost per correct answer: without → with | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`agent-design-and-tooling`](skills/agent-design-and-tooling/SKILL.md) | 49% | — | **96%** | +47 pts (+20 to +90) | — | 67% / — / 100% | — | 3 × 3 | 2026-11-13 |
| [`agent-evals`](skills/agent-evals/SKILL.md) | 45% | — | **98%** | +53 pts (+37 to +67) | — | 60% / — / 100% | $0.098 → $0.066 | 4 × 3 | 2026-11-09 |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | 74% | 91% | **100%** | +26 pts (+20 to +33) | +9 pts | 100% / 100% / 100% | $0.065 → $0.100 | 3 × 3 | 2026-11-09 |
| [`ai-adoption-plan`](skills/ai-adoption-plan/SKILL.md) | 61% | — | **95%** | +34 pts (+23 to +45) | — | 92% / — / 100% | — | 4 × 3 | 2026-11-11 |
| [`ai-data-requirements`](skills/ai-data-requirements/SKILL.md) | 65% | — | **94%** | +30 pts (+12 to +57) | — | 93% / — / 100% | $0.068 → $0.078 | 5 × 3 | 2026-11-09 |
| [`ai-feasibility-spike`](skills/ai-feasibility-spike/SKILL.md) | 46% | — | **96%** | +50 pts (+36 to +71) | — | 61% / — / 100% | $0.088 → $0.069 | 5 × 3 | 2026-11-12 |
| [`ai-incident-playbook`](skills/ai-incident-playbook/SKILL.md) | 45% | — | **98%** | +53 pts (+23 to +93) | — | 67% / — / 100% | $0.117 → $0.074 | 5 × 3 | 2026-11-12 |
| [`ai-interaction-patterns`](skills/ai-interaction-patterns/SKILL.md) | 64% | — | **95%** | +31 pts (+13 to +45) | — | 83% / — / 100% | $0.060 → $0.066 | 4 × 3 | 2026-11-12 |
| [`ai-opportunity-assessment`](skills/ai-opportunity-assessment/SKILL.md) | 55% | — | **93%** | +38 pts (+21 to +63) | — | 87% / — / 100% | $0.068 → $0.106 | 5 × 3 | 2026-11-11 |
| [`ai-roi-quantification`](skills/ai-roi-quantification/SKILL.md) | 69% | — | **97%** | +28 pts (+11 to +37) | — | 100% / — / 100% | $0.069 → $0.081 | 3 × 3 | 2026-11-09 |
| [`ai-vendor-evaluation`](skills/ai-vendor-evaluation/SKILL.md) | 60% | — | **98%** | +39 pts (+35 to +41) | — | 81% / — / 100% | $0.066 → $0.068 | 3 × 3 | 2026-11-09 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | 27% | 78% | **97%** | +70 pts (+48 to +100) | +20 pts | 56% / 100% / 100% | — | 3 × 3 | 2026-11-11 |
| [`build-evals`](skills/build-evals/SKILL.md) | 39% | — | **98%** | +59 pts (+42 to +67) | — | 33% / — / 100% | $0.122 → $0.057 | 6 × 3 | 2026-11-11 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | 22% | — | **98%** | +75 pts (+48 to +100) | — | 58% / — / 100% | $0.245 → $0.053 | 4 × 3 | 2026-11-11 |
| [`error-analysis`](skills/error-analysis/SKILL.md) | 34% | — | **98%** | +64 pts (+53 to +83) | — | 0% / — / 100% | $0.142 → $0.069 | 3 × 3 | 2026-11-11 |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | 29% | 76% | **100%** | +71 pts (+67 to +75) | +24 pts | 0% / 50% / 100% | — | 3 × 3 | 2026-11-11 |
| [`llm-judge-calibration`](skills/llm-judge-calibration/SKILL.md) | 63% | — | **95%** | +32 pts (+19 to +52) | — | 89% / — / 100% | — | 3 × 3 | 2026-11-13 |
| [`model-card-ai-registry`](skills/model-card-ai-registry/SKILL.md) | 66% | — | **99%** | +33 pts (+17 to +50) | — | 100% / — / 100% | — | 4 × 3 | 2026-11-11 |
| [`model-selection`](skills/model-selection/SKILL.md) | 72% | — | **98%** | +25 pts (+7 to +42) | — | 100% / — / 100% | — | 3 × 3 | 2026-11-13 |
| [`multi-turn-evals`](skills/multi-turn-evals/SKILL.md) | 43% | — | **93%** | +50 pts (+38 to +67) | — | 78% / — / 100% | $0.106 → $0.072 | 4 × 3 | 2026-11-12 |
| [`process-ai-redesign`](skills/process-ai-redesign/SKILL.md) | 57% | — | **99%** | +42 pts (+26 to +53) | — | 100% / — / 100% | $0.076 → $0.103 | 3 × 3 | 2026-11-09 |
| [`production-evals-monitoring`](skills/production-evals-monitoring/SKILL.md) | 45% | — | **100%** | +55 pts (+53 to +58) | — | 33% / — / 100% | $0.158 → $0.102 | 3 × 3 | 2026-11-11 |
| [`prototype-handover`](skills/prototype-handover/SKILL.md) | 48% | — | **96%** | +48 pts (+25 to +56) | — | 83% / — / 100% | $0.105 → $0.127 | 5 × 3 | 2026-11-11 |
| [`red-team-evals`](skills/red-team-evals/SKILL.md) | 49% | — | **96%** | +47 pts (+30 to +64) | — | 58% / — / 100% | $0.086 → $0.071 | 5 × 3 | 2026-11-12 |
| [`release-to-production`](skills/release-to-production/SKILL.md) | 61% | — | **99%** | +38 pts (+33 to +41) | — | 100% / — / 100% | — | 3 × 3 | 2026-11-12 |
| [`retrieval-evaluation`](skills/retrieval-evaluation/SKILL.md) | 51% | — | **87%** | +36 pts (+10 to +56) | — | 17% / — / 100% | $0.077 → $0.065 | 3 × 3 | 2026-11-09 |
| [`synthetic-eval-data`](skills/synthetic-eval-data/SKILL.md) | 30% | — | **96%** | +66 pts (+58 to +79) | — | 33% / — / 100% | $0.131 → $0.060 | 3 × 3 | 2026-11-09 |
| [`system-prompt-and-guardrails`](skills/system-prompt-and-guardrails/SKILL.md) | 77% | — | **97%** | +19 pts (+13 to +24) | — | 100% / — / 100% | — | 3 × 3 | 2026-11-13 |
| [`trace-review-tool`](skills/trace-review-tool/SKILL.md) | 54% | — | **92%** | +37 pts (+19 to +63) | — | 100% / — / 100% | $0.091 → $0.077 | 4 × 3 | 2026-11-11 |

## Per skill, blind LLM judges

| Skill | Judge | Without | Template only | With | Gain over the model alone | Gain over the template | Judge noise | Words: without / template / with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ai-roi-quantification` | Haiku 5.5 | 71% | — | 78% | +7 pts | — | 7 pts | 401 / — / 770 |
| `assistant-kpis-cost-per-outcome` | Haiku 5.5 | 67% | 83% | 82% | +15 pts | -1 pts | 5 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Haiku 5.5 | 76% | 81% | 79% | +3 pts | -2 pts | 8 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Haiku 5.5 | 68% | 71% | 75% | +8 pts | +4 pts | 5 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Haiku 5.5 | 72% | 76% | 87% | +16 pts | +12 pts | 4 pts | 1,469 / 2,290 / 1,783 |
| `agent-design-and-tooling` | Sonnet 5.5 | 76% | — | 82% | +6 pts | — | 2 pts | 679 / — / 1,012 |
| `ai-roi-quantification` | Sonnet 5.5 | 64% | — | 76% | +12 pts | — | 3 pts | 401 / — / 770 |
| `assistant-kpis-cost-per-outcome` | Sonnet 5.5 | 66% | 77% | 82% | +16 pts | +5 pts | 2 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Sonnet 5.5 | 79% | 83% | 84% | +4 pts | 0 pts | 3 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Sonnet 5.5 | 62% | 70% | 78% | +15 pts | +8 pts | 3 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Sonnet 5.5 | 74% | 75% | 82% | +9 pts | +7 pts | 3 pts | 1,469 / 2,290 / 1,783 |
| `llm-judge-calibration` | Sonnet 5.5 | 78% | — | 84% | +6 pts | — | 3 pts | 478 / — / 589 |
| `model-selection` | Sonnet 5.5 | 76% | — | 80% | +4 pts | — | 2 pts | 338 / — / 492 |
| `system-prompt-and-guardrails` | Sonnet 5.5 | 77% | — | 89% | +12 pts | — | 4 pts | 653 / — / 1,138 |
| `agent-design-and-tooling` | openai/gpt-6.1-sol | 75% | — | 79% | +4 pts | — | 3 pts | 679 / — / 1,012 |
| `agent-evals` | openai/gpt-6.1-sol | 76% | — | 81% | +5 pts | — | 2 pts | 731 / — / 918 |
| `ai-adoption-plan` | openai/gpt-6.1-sol | 68% | — | 79% | +11 pts | — | 2 pts | 569 / — / 750 |
| `ai-data-requirements` | openai/gpt-6.1-sol | 65% | — | 72% | +7 pts | — | 3 pts | 635 / — / 901 |
| `ai-feasibility-spike` | openai/gpt-6.1-sol | 51% | — | 67% | +16 pts | — | 3 pts | 595 / — / 766 |
| `ai-interaction-patterns` | openai/gpt-6.1-sol | 54% | — | 76% | +22 pts | — | 2 pts | 667 / — / 957 |
| `ai-opportunity-assessment` | openai/gpt-6.1-sol | 56% | — | 68% | +12 pts | — | 3 pts | 588 / — / 1,278 |
| `ai-roi-quantification` | openai/gpt-6.1-sol | 49% | — | 59% | +10 pts | — | 3 pts | 436 / — / 877 |
| `assistant-kpis-cost-per-outcome` | openai/gpt-6.1-sol | — | — | 67% | — | — | 4 pts | — / — / 1,287 |
| `build-evals` | openai/gpt-6.1-sol | 64% | — | 72% | +8 pts | — | 2 pts | 545 / — / 586 |
| `conversation-analysis` | openai/gpt-6.1-sol | 56% | — | 60% | +4 pts | — | 2 pts | 556 / — / 640 |
| `error-analysis` | openai/gpt-6.1-sol | 56% | — | 78% | +22 pts | — | 2 pts | 767 / — / 928 |
| `llm-feature-prd` | openai/gpt-6.1-sol | — | — | 74% | — | — | 4 pts | — / — / 1,779 |
| `llm-judge-calibration` | openai/gpt-6.1-sol | 70% | — | 74% | +4 pts | — | 1 pts | 478 / — / 589 |
| `model-selection` | openai/gpt-6.1-sol | 70% | — | 72% | +2 pts | — | 2 pts | 338 / — / 492 |
| `multi-turn-evals` | openai/gpt-6.1-sol | 66% | — | 73% | +6 pts | — | 2 pts | 616 / — / 792 |
| `process-ai-redesign` | openai/gpt-6.1-sol | 54% | — | 59% | +5 pts | — | 3 pts | 806 / — / 1,746 |
| `red-team-evals` | openai/gpt-6.1-sol | 66% | — | 78% | +11 pts | — | 2 pts | 662 / — / 833 |
| `release-to-production` | openai/gpt-6.1-sol | 56% | — | 59% | +3 pts | — | 2 pts | 490 / — / 557 |
| `retrieval-evaluation` | openai/gpt-6.1-sol | 70% | — | 78% | +8 pts | — | 3 pts | 635 / — / 765 |
| `synthetic-eval-data` | openai/gpt-6.1-sol | 68% | — | 76% | +7 pts | — | 2 pts | 663 / — / 814 |
| `system-prompt-and-guardrails` | openai/gpt-6.1-sol | 73% | — | 80% | +7 pts | — | 2 pts | 653 / — / 1,138 |
| `trace-review-tool` | openai/gpt-6.1-sol | 57% | — | 73% | +16 pts | — | 3 pts | 907 / — / 1,122 |
| `agent-design-and-tooling` | typesafe/jev-1.14 | 90% | — | 85% | -5 pts | — | 0 pts | 679 / — / 1,012 |
| `agent-evals` | typesafe/jev-1.14 | 88% | — | 94% | +6 pts | — | 1 pts | 731 / — / 918 |
| `ai-adoption-plan` | typesafe/jev-1.14 | 85% | — | 91% | +6 pts | — | 0 pts | 569 / — / 750 |
| `ai-data-requirements` | typesafe/jev-1.14 | 81% | — | 87% | +6 pts | — | 1 pts | 635 / — / 901 |
| `ai-feasibility-spike` | typesafe/jev-1.14 | 68% | — | 88% | +20 pts | — | 1 pts | 595 / — / 766 |
| `ai-interaction-patterns` | typesafe/jev-1.14 | 71% | — | 90% | +19 pts | — | 1 pts | 667 / — / 957 |
| `ai-opportunity-assessment` | typesafe/jev-1.14 | 76% | — | 90% | +14 pts | — | 1 pts | 588 / — / 1,278 |
| `ai-roi-quantification` | typesafe/jev-1.14 | 85% | — | 92% | +7 pts | — | 1 pts | 436 / — / 877 |
| `assistant-kpis-cost-per-outcome` | typesafe/jev-1.14 | — | — | 91% | — | — | 0 pts | — / — / 1,287 |
| `build-evals` | typesafe/jev-1.14 | 81% | — | 90% | +9 pts | — | 1 pts | 545 / — / 586 |
| `conversation-analysis` | typesafe/jev-1.14 | 66% | — | 85% | +19 pts | — | 1 pts | 556 / — / 640 |
| `error-analysis` | typesafe/jev-1.14 | 82% | — | 93% | +11 pts | — | 1 pts | 767 / — / 928 |
| `llm-feature-prd` | typesafe/jev-1.14 | — | — | 92% | — | — | 0 pts | — / — / 1,779 |
| `llm-judge-calibration` | typesafe/jev-1.14 | 82% | — | 85% | +3 pts | — | 1 pts | 478 / — / 589 |
| `model-selection` | typesafe/jev-1.14 | 84% | — | 85% | +2 pts | — | 1 pts | 338 / — / 492 |
| `multi-turn-evals` | typesafe/jev-1.14 | 84% | — | 93% | +8 pts | — | 1 pts | 616 / — / 792 |
| `process-ai-redesign` | typesafe/jev-1.14 | 89% | — | 88% | -1 pts | — | 1 pts | 806 / — / 1,746 |
| `red-team-evals` | typesafe/jev-1.14 | 78% | — | 93% | +16 pts | — | 1 pts | 662 / — / 833 |
| `release-to-production` | typesafe/jev-1.14 | 80% | — | 87% | +7 pts | — | 1 pts | 490 / — / 557 |
| `retrieval-evaluation` | typesafe/jev-1.14 | 90% | — | 95% | +5 pts | — | 0 pts | 635 / — / 765 |
| `synthetic-eval-data` | typesafe/jev-1.14 | 82% | — | 93% | +11 pts | — | 1 pts | 663 / — / 814 |
| `system-prompt-and-guardrails` | typesafe/jev-1.14 | 92% | — | 93% | +1 pts | — | 0 pts | 653 / — / 1,138 |
| `trace-review-tool` | typesafe/jev-1.14 | 64% | — | 88% | +24 pts | — | 1 pts | 907 / — / 1,122 |

## How to read it

- **Regex graders**: share of graders passed on a case, averaged over runs, then over a skill's scored cases, then over skills. A grader checks one thing the answer must contain or must not contain. The skills' author wrote them, so they reward what the skill asks for.
- **Template only**: the model gets the skill's own output template without its method. The gain over the template is what the method adds beyond the format ([template-only control](docs/evaluation.md)).
- **Blind LLM judge**: a model grades each answer twice on a generic rubric (sound, actionable, honest about unknowns, risk-aware, specific) without knowing the arm. It tends to favour longer answers and never grades the legal skills. Judge noise is the mean gap between its two passes on the same answer.
- **Intervals**: resample the cases within each skill 10,000 times and keep the middle 95% of the gains, with a small-sample correction (Rao-Wu rescaling, [scripts/eval_stats.py](scripts/eval_stats.py)). They show how much the gain depends on which cases were written. They do not cover the choice of graders, the judge's biases, or another model. Per skill, 3 to 5 cases are too few for an interval: the table gives the lowest and highest case gain instead.
- **Cost per correct answer**: the API-equivalent cost of one answer (as `claude plugin eval` reports it) divided by its regex score, averaged over skills; shown only for skills whose frozen run recorded the cost of each arm. A skill makes answers longer, so each answer costs more; the question is whether a correct one costs less.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its regex score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain over the model alone is at least 10 points. Details in [docs/evaluation.md](docs/evaluation.md).
- **Runs**: 3 per case and per arm, November 2026. Two red-line graders (`assistant-kpis-cost-per-outcome`, `conversation-analysis`) were corrected after that run because they rejected correct answers; the saved answers were then re-scored.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
