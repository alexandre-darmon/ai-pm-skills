# Skill eval gains

Same cases, Sonnet 5.5 answering, three arms: the model alone, the model given only the skill's output template, and the model with the skill. Generated from [`baselines/`](baselines/) by `python3 scripts/eval_gains.py`; do not edit by hand.

| Test performed | Model alone | Skill's template only | With the skill | Gain over the model alone | Gain over the template |
| --- | --- | --- | --- | --- | --- |
| Regex graders: 29 skills, 109 cases × 3 runs | 39% | — | **97%** | +57 [+55, +60] | — |
| Blind LLM judge, Haiku 5.5: 11 of these skills, 40 cases, earlier runs | 70% | — | 79% | +9 [+7, +11] | — |
| Blind LLM judge, Opus 5.5: 29 of these skills, 109 cases, recorded runs | 70% | — | 85% | +15 [+14, +17] | — |
| Blind LLM judge, Sonnet 5.5: 9 of these skills, 29 cases, earlier runs | 72% | — | 82% | +9 [+6, +13] | — |
| Blind LLM judge, openai/gpt-6.1-sol: 29 of these skills, 109 cases, recorded runs | 63% | — | 72% | +9 [+7, +11] | — |
| Blind decision model, typesafe/jev-1.14: 29 of these skills, 109 cases, recorded runs | 80% | — | 90% | +10 [+8, +12] | — |
| Red lines held (the one thing the answer must never do) | 71% | — | **100%** | | |
| Cost per correct answer, API equivalent (29 skills) | $0.128 | — | **$0.068** | -47% | |
| Stays silent on near-miss requests | — | — | **100%** | | |

Gains in points. Brackets: 95% interval over cases (see below).

## Per skill, regex graders

| Skill | Without | Template only | With | Gain over the model alone (lowest to highest case) | Gain over the template | Red lines held: without / template / with | Cost per correct answer: without → with | Cases × runs | Run date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [`agent-design-and-tooling`](skills/agent-design-and-tooling/SKILL.md) | 36% | — | **99%** | +63 pts (+40 to +100) | — | 67% / — / 100% | $0.114 → $0.083 | 3 × 3 | 2026-11-19 |
| [`agent-evals`](skills/agent-evals/SKILL.md) | 34% | — | **97%** | +63 pts (+46 to +83) | — | 60% / — / 100% | $0.000 → $0.087 | 4 × 3 | 2026-11-19 |
| [`ai-act-classification`](skills/ai-act-classification/SKILL.md) | 39% | — | **100%** | +61 pts (+52 to +67) | — | 100% / — / 100% | $0.128 → $0.149 | 3 × 3 | 2026-11-18 |
| [`ai-adoption-plan`](skills/ai-adoption-plan/SKILL.md) | 51% | — | **96%** | +45 pts (+23 to +70) | — | 92% / — / 100% | $0.000 → $0.060 | 4 × 3 | 2026-11-11 |
| [`ai-data-requirements`](skills/ai-data-requirements/SKILL.md) | 53% | — | **94%** | +41 pts (+22 to +67) | — | 93% / — / 100% | $0.000 → $0.000 | 5 × 3 | 2026-11-09 |
| [`ai-feasibility-spike`](skills/ai-feasibility-spike/SKILL.md) | 40% | — | **95%** | +56 pts (+42 to +71) | — | 61% / — / 100% | $0.102 → $0.069 | 5 × 3 | 2026-11-12 |
| [`ai-incident-playbook`](skills/ai-incident-playbook/SKILL.md) | 38% | — | **99%** | +62 pts (+30 to +97) | — | 67% / — / 100% | $0.138 → $0.074 | 5 × 3 | 2026-11-18 |
| [`ai-interaction-patterns`](skills/ai-interaction-patterns/SKILL.md) | 48% | — | **94%** | +46 pts (+36 to +67) | — | 83% / — / 100% | $0.080 → $0.067 | 4 × 3 | 2026-11-12 |
| [`ai-opportunity-assessment`](skills/ai-opportunity-assessment/SKILL.md) | 48% | — | **93%** | +45 pts (+21 to +74) | — | 87% / — / 100% | $0.079 → $0.106 | 5 × 3 | 2026-11-11 |
| [`ai-roi-quantification`](skills/ai-roi-quantification/SKILL.md) | 65% | — | **97%** | +32 pts (+14 to +45) | — | 100% / — / 100% | $0.000 → $0.000 | 3 × 3 | 2026-11-09 |
| [`ai-vendor-evaluation`](skills/ai-vendor-evaluation/SKILL.md) | 46% | — | **98%** | +51 pts (+44 to +57) | — | 81% / — / 100% | $0.000 → $0.075 | 3 × 3 | 2026-11-18 |
| [`assistant-kpis-cost-per-outcome`](skills/assistant-kpis-cost-per-outcome/SKILL.md) | 23% | — | **96%** | +73 pts (+56 to +100) | — | 56% / — / 100% | $0.181 → $0.067 | 3 × 3 | 2026-11-18 |
| [`build-evals`](skills/build-evals/SKILL.md) | 25% | — | **98%** | +73 pts (+42 to +89) | — | 33% / — / 100% | $0.189 → $0.057 | 6 × 3 | 2026-11-11 |
| [`conversation-analysis`](skills/conversation-analysis/SKILL.md) | 17% | — | **100%** | +83 pts (+70 to +100) | — | 50% / — / 100% | $0.577 → $0.057 | 4 × 3 | 2026-11-19 |
| [`error-analysis`](skills/error-analysis/SKILL.md) | 15% | — | **98%** | +83 pts (+75 to +93) | — | 0% / — / 100% | $0.324 → $0.069 | 3 × 3 | 2026-11-11 |
| [`llm-feature-prd`](skills/llm-feature-prd/SKILL.md) | 10% | — | **100%** | +90 pts (+83 to +95) | — | 0% / — / 100% | $0.798 → $0.111 | 3 × 3 | 2026-11-18 |
| [`llm-judge-calibration`](skills/llm-judge-calibration/SKILL.md) | 47% | — | **96%** | +49 pts (+33 to +62) | — | 89% / — / 100% | $0.082 → $0.064 | 3 × 3 | 2026-11-19 |
| [`model-card-ai-registry`](skills/model-card-ai-registry/SKILL.md) | 57% | — | **97%** | +40 pts (+17 to +53) | — | 100% / — / 100% | $0.000 → $0.074 | 4 × 3 | 2026-11-18 |
| [`model-selection`](skills/model-selection/SKILL.md) | 60% | — | **100%** | +40 pts (+24 to +52) | — | 100% / — / 100% | $0.000 → $0.054 | 3 × 3 | 2026-11-19 |
| [`multi-turn-evals`](skills/multi-turn-evals/SKILL.md) | 34% | — | **93%** | +59 pts (+50 to +67) | — | 78% / — / 100% | $0.134 → $0.072 | 4 × 3 | 2026-11-12 |
| [`process-ai-redesign`](skills/process-ai-redesign/SKILL.md) | 53% | — | **96%** | +43 pts (+37 to +47) | — | 100% / — / 100% | $0.000 → $0.099 | 3 × 3 | 2026-11-18 |
| [`production-evals-monitoring`](skills/production-evals-monitoring/SKILL.md) | 18% | — | **100%** | +82 pts (+73 to +89) | — | 33% / — / 100% | $0.405 → $0.113 | 3 × 3 | 2026-11-18 |
| [`prototype-handover`](skills/prototype-handover/SKILL.md) | 37% | — | **99%** | +62 pts (+31 to +74) | — | 83% / — / 100% | $0.138 → $0.116 | 5 × 3 | 2026-11-18 |
| [`red-team-evals`](skills/red-team-evals/SKILL.md) | 36% | — | **97%** | +61 pts (+41 to +73) | — | 58% / — / 100% | $0.118 → $0.070 | 5 × 3 | 2026-11-12 |
| [`release-to-production`](skills/release-to-production/SKILL.md) | 57% | — | **99%** | +42 pts (+41 to +43) | — | 100% / — / 100% | $0.000 → $0.052 | 3 × 3 | 2026-11-18 |
| [`retrieval-evaluation`](skills/retrieval-evaluation/SKILL.md) | 29% | — | **85%** | +56 pts (+38 to +67) | — | 17% / — / 100% | $0.000 → $0.000 | 3 × 3 | 2026-11-09 |
| [`synthetic-eval-data`](skills/synthetic-eval-data/SKILL.md) | 17% | — | **96%** | +79 pts (+58 to +100) | — | 33% / — / 100% | $0.000 → $0.000 | 3 × 3 | 2026-11-09 |
| [`system-prompt-and-guardrails`](skills/system-prompt-and-guardrails/SKILL.md) | 66% | — | **97%** | +31 pts (+23 to +37) | — | 100% / — / 100% | $0.000 → $0.065 | 3 × 3 | 2026-11-13 |
| [`trace-review-tool`](skills/trace-review-tool/SKILL.md) | 37% | — | **91%** | +55 pts (+42 to +74) | — | 100% / — / 100% | $0.134 → $0.077 | 4 × 3 | 2026-11-11 |

## Per skill, blind LLM judges

| Skill | Judge | Without | Template only | With | Gain over the model alone | Gain over the template | Judge noise | Words: without / template / with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ai-act-classification` | Haiku 5.5 | 74% | — | 75% | +2 pts | — | 6 pts | 735 / — / 1,486 |
| `ai-incident-playbook` | Haiku 5.5 | 64% | — | 74% | +10 pts | — | 4 pts | 659 / — / 922 |
| `ai-roi-quantification` | Haiku 5.5 | 71% | — | 78% | +7 pts | — | 7 pts | 401 / — / 770 |
| `ai-vendor-evaluation` | Haiku 5.5 | 69% | — | 82% | +13 pts | — | 5 pts | 537 / — / 980 |
| `assistant-kpis-cost-per-outcome` | Haiku 5.5 | 67% | 83% | 82% | +15 pts | -1 pts | 5 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Haiku 5.5 | 76% | 81% | 79% | +3 pts | -2 pts | 8 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Haiku 5.5 | 68% | 71% | 75% | +8 pts | +4 pts | 5 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Haiku 5.5 | 72% | 76% | 87% | +16 pts | +12 pts | 4 pts | 1,469 / 2,290 / 1,783 |
| `model-card-ai-registry` | Haiku 5.5 | 74% | — | 79% | +5 pts | — | 3 pts | 480 / — / 654 |
| `production-evals-monitoring` | Haiku 5.5 | 72% | — | 83% | +11 pts | — | 4 pts | 1,029 / — / 1,236 |
| `prototype-handover` | Haiku 5.5 | 66% | — | 77% | +11 pts | — | 5 pts | 775 / — / 1,286 |
| `agent-design-and-tooling` | Opus 5.5 | 74% | — | 91% | +16 pts | — | — | 679 / — / 1,117 |
| `agent-evals` | Opus 5.5 | 80% | — | 94% | +14 pts | — | 2 pts | 731 / — / 1,275 |
| `ai-act-classification` | Opus 5.5 | 78% | — | 84% | +6 pts | — | 5 pts | 746 / — / 1,611 |
| `ai-adoption-plan` | Opus 5.5 | 70% | — | 82% | +12 pts | — | — | 569 / — / 750 |
| `ai-data-requirements` | Opus 5.5 | 72% | — | 82% | +10 pts | — | — | 635 / — / 901 |
| `ai-feasibility-spike` | Opus 5.5 | 63% | — | 83% | +21 pts | — | — | 595 / — / 766 |
| `ai-incident-playbook` | Opus 5.5 | 63% | — | 81% | +18 pts | — | 5 pts | 659 / — / 1,078 |
| `ai-interaction-patterns` | Opus 5.5 | 60% | — | 87% | +27 pts | — | — | 667 / — / 957 |
| `ai-opportunity-assessment` | Opus 5.5 | 66% | — | 80% | +14 pts | — | — | 588 / — / 1,278 |
| `ai-roi-quantification` | Opus 5.5 | 59% | — | 75% | +16 pts | — | — | 436 / — / 877 |
| `ai-vendor-evaluation` | Opus 5.5 | 76% | — | 88% | +13 pts | — | — | 537 / — / 1,039 |
| `assistant-kpis-cost-per-outcome` | Opus 5.5 | 64% | — | 77% | +13 pts | — | — | 701 / — / 1,219 |
| `build-evals` | Opus 5.5 | 70% | — | 86% | +16 pts | — | — | 545 / — / 586 |
| `conversation-analysis` | Opus 5.5 | 62% | — | 81% | +19 pts | — | 3 pts | 570 / — / 684 |
| `error-analysis` | Opus 5.5 | 68% | — | 88% | +19 pts | — | — | 767 / — / 928 |
| `llm-feature-prd` | Opus 5.5 | 76% | — | 89% | +13 pts | — | — | 1,389 / — / 1,858 |
| `llm-judge-calibration` | Opus 5.5 | 76% | — | 87% | +11 pts | — | 4 pts | 478 / — / 617 |
| `model-card-ai-registry` | Opus 5.5 | 73% | — | 85% | +12 pts | — | — | 480 / — / 999 |
| `model-selection` | Opus 5.5 | 78% | — | 88% | +10 pts | — | 4 pts | 338 / — / 602 |
| `multi-turn-evals` | Opus 5.5 | 75% | — | 88% | +13 pts | — | — | 616 / — / 792 |
| `process-ai-redesign` | Opus 5.5 | 64% | — | 83% | +19 pts | — | — | 806 / — / 1,521 |
| `production-evals-monitoring` | Opus 5.5 | 74% | — | 91% | +17 pts | — | 3 pts | 1,029 / — / 1,317 |
| `prototype-handover` | Opus 5.5 | 69% | — | 85% | +16 pts | — | — | 775 / — / 1,352 |
| `red-team-evals` | Opus 5.5 | 72% | — | 91% | +18 pts | — | — | 662 / — / 833 |
| `release-to-production` | Opus 5.5 | 62% | — | 86% | +24 pts | — | — | 490 / — / 627 |
| `retrieval-evaluation` | Opus 5.5 | 75% | — | 88% | +13 pts | — | — | 635 / — / 765 |
| `synthetic-eval-data` | Opus 5.5 | 69% | — | 81% | +12 pts | — | — | 663 / — / 814 |
| `system-prompt-and-guardrails` | Opus 5.5 | 72% | — | 87% | +14 pts | — | — | 653 / — / 1,138 |
| `trace-review-tool` | Opus 5.5 | 62% | — | 82% | +20 pts | — | — | 907 / — / 1,122 |
| `agent-design-and-tooling` | Sonnet 5.5 | 76% | — | 82% | +6 pts | — | 2 pts | 679 / — / 1,012 |
| `ai-roi-quantification` | Sonnet 5.5 | 64% | — | 76% | +12 pts | — | 3 pts | 401 / — / 770 |
| `assistant-kpis-cost-per-outcome` | Sonnet 5.5 | 66% | 77% | 82% | +16 pts | +5 pts | 2 pts | 726 / 1,723 / 1,213 |
| `build-evals` | Sonnet 5.5 | 79% | 83% | 84% | +4 pts | 0 pts | 3 pts | 705 / 1,466 / 838 |
| `conversation-analysis` | Sonnet 5.5 | 62% | 70% | 78% | +15 pts | +8 pts | 3 pts | 554 / 1,251 / 662 |
| `llm-feature-prd` | Sonnet 5.5 | 74% | 75% | 82% | +9 pts | +7 pts | 3 pts | 1,469 / 2,290 / 1,783 |
| `llm-judge-calibration` | Sonnet 5.5 | 78% | — | 84% | +6 pts | — | 3 pts | 478 / — / 589 |
| `model-selection` | Sonnet 5.5 | 76% | — | 80% | +4 pts | — | 2 pts | 338 / — / 492 |
| `system-prompt-and-guardrails` | Sonnet 5.5 | 77% | — | 89% | +12 pts | — | 4 pts | 653 / — / 1,138 |
| `agent-design-and-tooling` | openai/gpt-6.1-sol | 77% | — | 81% | +4 pts | — | — | 679 / — / 1,117 |
| `agent-evals` | openai/gpt-6.1-sol | 75% | — | 78% | +4 pts | — | — | 731 / — / 1,275 |
| `ai-act-classification` | openai/gpt-6.1-sol | 67% | — | 62% | -6 pts | — | — | 746 / — / 1,611 |
| `ai-adoption-plan` | openai/gpt-6.1-sol | 68% | — | 77% | +9 pts | — | — | 569 / — / 750 |
| `ai-data-requirements` | openai/gpt-6.1-sol | 65% | — | 71% | +5 pts | — | — | 635 / — / 901 |
| `ai-feasibility-spike` | openai/gpt-6.1-sol | 52% | — | 68% | +16 pts | — | — | 595 / — / 766 |
| `ai-incident-playbook` | openai/gpt-6.1-sol | 62% | — | 65% | +3 pts | — | — | 659 / — / 1,078 |
| `ai-interaction-patterns` | openai/gpt-6.1-sol | 54% | — | 75% | +21 pts | — | — | 667 / — / 957 |
| `ai-opportunity-assessment` | openai/gpt-6.1-sol | 57% | — | 68% | +10 pts | — | — | 588 / — / 1,278 |
| `ai-roi-quantification` | openai/gpt-6.1-sol | 49% | — | 58% | +9 pts | — | — | 436 / — / 877 |
| `ai-vendor-evaluation` | openai/gpt-6.1-sol | 69% | — | 76% | +7 pts | — | — | 537 / — / 1,039 |
| `assistant-kpis-cost-per-outcome` | openai/gpt-6.1-sol | 53% | — | 65% | +12 pts | — | — | 701 / — / 1,219 |
| `build-evals` | openai/gpt-6.1-sol | 63% | — | 72% | +9 pts | — | — | 545 / — / 586 |
| `conversation-analysis` | openai/gpt-6.1-sol | 54% | — | 68% | +13 pts | — | — | 570 / — / 684 |
| `error-analysis` | openai/gpt-6.1-sol | 56% | — | 78% | +22 pts | — | — | 767 / — / 928 |
| `llm-feature-prd` | openai/gpt-6.1-sol | 61% | — | 71% | +10 pts | — | — | 1,389 / — / 1,858 |
| `llm-judge-calibration` | openai/gpt-6.1-sol | 71% | — | 75% | +4 pts | — | — | 478 / — / 617 |
| `model-card-ai-registry` | openai/gpt-6.1-sol | 62% | — | 65% | +3 pts | — | — | 480 / — / 999 |
| `model-selection` | openai/gpt-6.1-sol | 69% | — | 77% | +8 pts | — | — | 338 / — / 602 |
| `multi-turn-evals` | openai/gpt-6.1-sol | 67% | — | 71% | +5 pts | — | — | 616 / — / 792 |
| `process-ai-redesign` | openai/gpt-6.1-sol | 53% | — | 64% | +12 pts | — | — | 806 / — / 1,521 |
| `production-evals-monitoring` | openai/gpt-6.1-sol | 64% | — | 69% | +4 pts | — | — | 1,029 / — / 1,317 |
| `prototype-handover` | openai/gpt-6.1-sol | 60% | — | 68% | +9 pts | — | — | 775 / — / 1,352 |
| `red-team-evals` | openai/gpt-6.1-sol | 66% | — | 80% | +14 pts | — | — | 662 / — / 833 |
| `release-to-production` | openai/gpt-6.1-sol | 53% | — | 74% | +21 pts | — | — | 490 / — / 627 |
| `retrieval-evaluation` | openai/gpt-6.1-sol | 70% | — | 78% | +8 pts | — | — | 635 / — / 765 |
| `synthetic-eval-data` | openai/gpt-6.1-sol | 67% | — | 76% | +9 pts | — | — | 663 / — / 814 |
| `system-prompt-and-guardrails` | openai/gpt-6.1-sol | 76% | — | 81% | +5 pts | — | — | 653 / — / 1,138 |
| `trace-review-tool` | openai/gpt-6.1-sol | 59% | — | 73% | +14 pts | — | — | 907 / — / 1,122 |
| `agent-design-and-tooling` | typesafe/jev-1.14 | 90% | — | 87% | -3 pts | — | 0 pts | 679 / — / 1,117 |
| `agent-evals` | typesafe/jev-1.14 | 88% | — | 94% | +5 pts | — | 1 pts | 731 / — / 1,275 |
| `ai-act-classification` | typesafe/jev-1.14 | 74% | — | 75% | +1 pts | — | 1 pts | 746 / — / 1,611 |
| `ai-adoption-plan` | typesafe/jev-1.14 | 86% | — | 91% | +6 pts | — | 1 pts | 569 / — / 750 |
| `ai-data-requirements` | typesafe/jev-1.14 | 81% | — | 87% | +6 pts | — | 1 pts | 635 / — / 901 |
| `ai-feasibility-spike` | typesafe/jev-1.14 | 68% | — | 88% | +20 pts | — | 1 pts | 595 / — / 766 |
| `ai-incident-playbook` | typesafe/jev-1.14 | 79% | — | 87% | +8 pts | — | 1 pts | 659 / — / 1,078 |
| `ai-interaction-patterns` | typesafe/jev-1.14 | 71% | — | 90% | +19 pts | — | 1 pts | 667 / — / 957 |
| `ai-opportunity-assessment` | typesafe/jev-1.14 | 77% | — | 90% | +14 pts | — | 1 pts | 588 / — / 1,278 |
| `ai-roi-quantification` | typesafe/jev-1.14 | 85% | — | 92% | +8 pts | — | 1 pts | 436 / — / 877 |
| `ai-vendor-evaluation` | typesafe/jev-1.14 | 73% | — | 90% | +16 pts | — | 1 pts | 537 / — / 1,039 |
| `assistant-kpis-cost-per-outcome` | typesafe/jev-1.14 | 70% | — | 90% | +20 pts | — | 0 pts | 701 / — / 1,219 |
| `build-evals` | typesafe/jev-1.14 | 81% | — | 90% | +8 pts | — | 1 pts | 545 / — / 586 |
| `conversation-analysis` | typesafe/jev-1.14 | 61% | — | 87% | +26 pts | — | 1 pts | 570 / — / 684 |
| `error-analysis` | typesafe/jev-1.14 | 82% | — | 93% | +11 pts | — | 1 pts | 767 / — / 928 |
| `llm-feature-prd` | typesafe/jev-1.14 | 83% | — | 91% | +8 pts | — | 1 pts | 1,389 / — / 1,858 |
| `llm-judge-calibration` | typesafe/jev-1.14 | 82% | — | 85% | +3 pts | — | 1 pts | 478 / — / 617 |
| `model-card-ai-registry` | typesafe/jev-1.14 | 78% | — | 91% | +14 pts | — | 1 pts | 480 / — / 999 |
| `model-selection` | typesafe/jev-1.14 | 84% | — | 86% | +2 pts | — | 1 pts | 338 / — / 602 |
| `multi-turn-evals` | typesafe/jev-1.14 | 84% | — | 93% | +9 pts | — | 1 pts | 616 / — / 792 |
| `process-ai-redesign` | typesafe/jev-1.14 | 89% | — | 87% | -2 pts | — | 1 pts | 806 / — / 1,521 |
| `production-evals-monitoring` | typesafe/jev-1.14 | 80% | — | 88% | +9 pts | — | 1 pts | 1,029 / — / 1,317 |
| `prototype-handover` | typesafe/jev-1.14 | 79% | — | 90% | +12 pts | — | 0 pts | 775 / — / 1,352 |
| `red-team-evals` | typesafe/jev-1.14 | 77% | — | 93% | +16 pts | — | 1 pts | 662 / — / 833 |
| `release-to-production` | typesafe/jev-1.14 | 80% | — | 90% | +10 pts | — | 1 pts | 490 / — / 627 |
| `retrieval-evaluation` | typesafe/jev-1.14 | 90% | — | 94% | +5 pts | — | 0 pts | 635 / — / 765 |
| `synthetic-eval-data` | typesafe/jev-1.14 | 82% | — | 93% | +11 pts | — | 1 pts | 663 / — / 814 |
| `system-prompt-and-guardrails` | typesafe/jev-1.14 | 93% | — | 93% | +1 pts | — | 0 pts | 653 / — / 1,138 |
| `trace-review-tool` | typesafe/jev-1.14 | 64% | — | 88% | +24 pts | — | 1 pts | 907 / — / 1,122 |

## How to read it

- **Regex graders**: share of graders passed on a case, averaged over runs, then over a skill's scored cases, then over skills. A grader checks one thing the answer must contain or must not contain. The skills' author wrote them, so they reward what the skill asks for.
- **Template only**: the model gets the skill's own output template without its method. The gain over the template is what the method adds beyond the format ([template-only control](docs/evaluation.md)). A row shows it only when every skill in the row has a template-only run on its current cases, so all its columns cover the same skills.
- **Blind LLM judge**: a model grades each answer twice on a generic rubric (sound, actionable, honest about unknowns, risk-aware, specific) without knowing the arm. It tends to favour longer answers. On the legal skills it grades the same rubric and does not check legal correctness: counsel's review stays the evidence there. Judge noise is the mean gap between its two passes on the same answer.
- **Intervals**: resample the cases within each skill 10,000 times and keep the middle 95% of the gains, with a small-sample correction (Rao-Wu rescaling, [scripts/eval_stats.py](scripts/eval_stats.py)). They show how much the gain depends on which cases were written. They do not cover the choice of graders, the judge's biases, or another model. Per skill, 3 to 5 cases are too few for an interval: the table gives the lowest and highest case gain instead.
- **Cost per correct answer**: the API-equivalent cost of one answer (as `claude plugin eval` reports it) divided by its regex score, averaged over skills; shown only for skills whose frozen run recorded the cost of each arm. A skill makes answers longer, so each answer costs more; the question is whether a correct one costs less.
- **Red lines**: a red line fails the case on its own (e.g. a refund agent launched without human validation, a "compliant" verdict). Shown as the share of runs where it held.
- **Pass rule**: a skill enters the catalogue when its regex score reaches the threshold (0.80, 0.90 for govern and flagship skills), every red line holds in every run, and the gain over the model alone is at least 10 points. Details in [docs/evaluation.md](docs/evaluation.md).
- **Runs**: 3 per case and per arm, November 2026. Two red-line graders (`assistant-kpis-cost-per-outcome`, `conversation-analysis`) were corrected after that run because they rejected correct answers; the saved answers were then re-scored.
- **Without** scores are not zero: the base model often gets part of the job right. The gain is what the skill adds on top.
