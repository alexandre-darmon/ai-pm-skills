# Autonomy ladder (L0–L5)

The single definition of "how autonomous" used by every skill. A process step, an assistant or an agent is always at one level, and moving up requires passing a gate.

Skills cite levels as `L3 (references/autonomy-ladder.md)`, a synced copy of this file inside the skill, and never redefine them locally.

## Levels

| Level | Name | Who acts | Human role | Gate to enter this level | Typical obligations that rise |
| --- | --- | --- | --- | --- | --- |
| **L0** | Manual | Human | Does the work | — | — |
| **L1** | Assisted | Human | Does the work, AI suggests | Offline eval on golden set ≥ threshold; user tested on 5 people | Transparency to users; AI literacy (AI Act art. 4) |
| **L2** | Human in the loop | AI produces, human validates every output | Validates 100% | L1 in production 4 weeks; quality KPI stable; guardrails on output tested | Logging; DPIA pre-screen if personal data |
| **L3** | Human on the loop | AI acts, human sees exceptions and a sample | Reviews exceptions + sample | Shadow run ≥ 2 weeks; false-positive rate of guardrails known; escalation path tested | Incident playbook; CSE consultation if it changes work organisation |
| **L4** | Autonomous with guardrails | AI acts within limits; automatic stop | Sets limits, reviews reports | Action guardrails (scope, caps, approvals) tested in redteam; canary passed; rollback in one click | High-risk classification check (AI Act annex III); human oversight design (art. 14); model card |
| **L5** | Self-improving loop | AI acts and improves on its own outcomes until plateau | Intervenes at plateau | L4 stable 3 months; eval gate automated; drift detection live | Continuous monitoring; change-management of the model itself; registry update on each version |

The gate numbers (5 people, 4 weeks, 2 weeks, 3 months) are defaults, not measured laws. Adjust them to the cost of an error and write down why; the gate itself stays a measured fact.

The last column shows when an obligation typically becomes salient as autonomy rises. It is not a legal map: whether an obligation applies depends on the use case, not on the level (AI Act classification, personal data, effect on employees). `ai-act-classification` checks the actual AI Act triggers; GDPR and labour-law triggers go to the DPO and HR.

## Rules

1. **Per step, not per product.** A product can be L3 on routing and L1 on drafting.
2. **No skipping in production.** You never skip a level in production. You may skip in design.
3. **Down is free.** Moving down a level is always allowed and never needs approval.
4. **Gates are facts.** A gate is a measured fact (a score, a run, a test), never an opinion.

## Which skill provides the gate evidence

| Gate evidence | Produced by |
| --- | --- |
| Offline eval on golden set, threshold, baseline; eval gate automated | `build-evals` |
| Judge validated against expert labels (TPR, TNR) | `llm-judge-calibration` |
| Agent reliability over repeated trials (pass^k), forbidden events, end state | `agent-evals` |
| Output and action guardrails tested, redteam results, guardrail false-positive rate | `system-prompt-and-guardrails` |
| Shadow run, canary, rollback | `release-to-production` |
| Quality KPI stable in production | `assistant-kpis-cost-per-outcome`, `production-evals-monitoring` |
| Drift check design | `conversation-analysis`, `production-evals-monitoring` |
| Escalation path | `ai-interaction-patterns`, `chat-with-your-data-scoping` |

No skill produces "user tested on 5 people", "L1 in production 4 weeks" or "L4 stable 3 months": they are measured facts recorded in the release plan.

## Which skill handles the obligations

| Obligation | Handled by |
| --- | --- |
| Transparency to users | `ai-interaction-patterns` |
| AI literacy | `ai-adoption-plan` |
| Logging (trace schema, outcome events) | `agent-design-and-tooling`, `assistant-kpis-cost-per-outcome` |
| DPIA pre-screen | the DPO; `ai-data-requirements` flags personal data |
| Incident playbook | `ai-incident-playbook` |
| Continuous monitoring, post-market monitoring plan | `production-evals-monitoring` |
| CSE information or consultation | HR and employee representatives; `ai-act-classification` lists art. 26(7) |
| High-risk classification check, deployer duties | `ai-act-classification` |
| Human oversight design (art. 14) | `system-prompt-and-guardrails`, `agent-design-and-tooling` |
| Model card, registry update | `model-card-ai-registry` |

## Step table format

`llm-feature-prd` and `process-ai-redesign` assign a level per step and output this table. `agent-design-and-tooling` takes it as input and turns it into its permission matrix (tool × level × approval). `ai-opportunity-assessment` and `chat-with-your-data-scoping` give a single target level.

| Step | Current level | Target level | Why not L+1 | Gate to reach target |
| --- | --- | --- | --- | --- |
