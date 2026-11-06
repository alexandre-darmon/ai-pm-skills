# PRD — <feature name>

## Problem
<One sentence: who suffers what, how often, at what cost.>

## Outcome metric
<One sentence: the business outcome that proves it works, with its current value.>

## Users
<Target users and their context.>

## Non-goals
- <What this feature will not do.>
- Never: <actions it must be unable to take, absent from its tools and credentials, not just forbidden in the prompt.>

## Steps and autonomy levels
| Step | Target level | Why not L+1 | Gate to reach it | Reversible? (how, by whom) |
| --- | --- | --- | --- | --- |

## Happy path

## Failure paths
| Failure | What the user sees | What the system does |
| --- | --- | --- |
| Wrong answer | | |
| No answer | | |
| Out of scope | | |
| Prompt injection | | |

## Eval plan
- What "correct" means, per step:
- Case sampling:
- Reference outputs and rubric (for generated text):
- Who labels:
- Threshold:

## Guardrails
| Layer | Requirement |
| --- | --- |
| Input | |
| Output | |
| Action | |

## Data and compliance
- Data requirements: <pointer to ai-data-requirements>
- Compliance flags: <personal data, high-risk domain, employee impact>

## KPIs
| KPI | Type (outcome / quality / usage) | Definition | Source |
| --- | --- | --- | --- |

## Rollout
Shadow → canary → general availability, with the gate for each.

## Stop conditions
| Metric | Threshold | Read where and when | Action |
| --- | --- | --- | --- |

Move to the next stage if <metric> is at <value> on <date>, read on <n> samples. If not: <action>.

## Open questions
| Question | Owner |
| --- | --- |
