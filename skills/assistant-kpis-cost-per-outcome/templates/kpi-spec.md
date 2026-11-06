# KPI spec — <assistant or agent name>

## Source inventory
| Field | In the traces today? | System | Needed for |
| --- | --- | --- | --- |
| trace id | | | every KPI |
| use case | | | volume, quality, cost |
| KB / domain | | | quality, stale-answer rate |
| user population | | | adoption |
| tokens, cost | | | cost per correct outcome |
| outcome | | | quality, cost per correct outcome |
| link to the system where humans redo the work | | | redo rate, bypass rate |

## Outcome event
Attached to the trace id. Model and token fields follow the OpenTelemetry GenAI conventions (`gen_ai.*`).

| Field | Type | Meaning |
| --- | --- | --- |
| `outcome_id` | string | unique id of the outcome |
| `trace_id` | string | the conversation or agent run it closes |
| `use_case` | string | from the frozen taxonomy |
| `result` | enum | success · failure · escalated · abandoned · redone (a human later redid a logged success; latest event on the trace wins) |
| `value_eur` | number, empty until sourced | value of one correct outcome (references/roi-model.md) |
| `source` | enum | user · system · reviewer |
| `timestamp` | datetime | |

Interim, until outcomes are logged: <n conversations per use case and per KB per week, reviewed by <who> against <rubric>>.

## KPIs
| Family | KPI | Definition | Formula | Source | Grain | Refresh | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Volume | | | | | use case | | | computable · interim · not computable yet |
| Quality | | | | | KB / domain | | | |
| Quality | Redo rate | logged successes a human later redid or took over | redone ÷ logged successes | | use case | | | |
| Adoption | | | | | population, week | | | |
| Adoption | Bypass rate; accept, edit, reject ratios (if the UI allows) | | | | use case | | | |
| Cost per correct outcome | | | cost ÷ (volume × quality) | | use case | | | |
| Stale-answer rate | | | | | KB | | | |

Redo window: <per use case>. Redone outcomes are excluded from the successes in the denominator.

Numerator of cost per correct outcome: <run cost: tokens, infra, licences; change cost counted: review time, or none>.

## Dashboard layout
| Panel | Shows | Paired with | Threshold | Sample size |
| --- | --- | --- | --- | --- |
| Volume by use case | | quality of the same use case | | |
| Quality by KB | | | | |
| Adoption by population | | quality for that population | | |
| Cost per correct outcome | | | | |
| Stale-answer rate by KB | | | | |

## Monthly review
| KPI | This month | Last month | Target | Decision | Owner |
| --- | --- | --- | --- | --- | --- |

Autonomy: <steps whose L2 gate reads the quality KPI (references/autonomy-ladder.md); stable since <date>, with sample sizes>.

## Open questions
| Question | Owner |
| --- | --- |
