# Classification plan — <assistant or agent name>

## Masking (blocks every later step)
| Personal data | Method (pattern, NER) | Placeholder |
| --- | --- | --- |
| names | NER | `[NAME]` |
| IBAN, card, account numbers | pattern | `[IBAN]` |
| emails, phone numbers | pattern | `[EMAIL]`, `[PHONE]` |
| customer or employee ids | pattern | `[ID]` |

Why: GDPR art. 5(1)(c), data minimisation: a classifier needs the request, not the identity, so no model sees personal data it does not need.

Check: <n masked conversations read by hand, by whom>. Residual leak rate: <x%>. Status: <passed / not started>.

Retention: masked text and classifier logs kept <period>, deleted by <who> (GDPR art. 5(1)(e)).

## Dimensions
| Dimension | Values | Feeds (KPI, decision) |
| --- | --- | --- |
| use case | taxonomy below | volume, ROI |
| domain / KB | | quality by KB |
| resolution | resolved · escalated · abandoned · unresolved | quality, cost per correct outcome |
| sentiment | | |
| language | | |

## Taxonomy — version <n>, frozen on <date>
Derived from: <existing draft / free-form notes on n masked conversations, clustered>.

| Use case | Definition | Examples (2) | Counter-example |
| --- | --- | --- | --- |

8–12 use cases. "Other" target: under 10%.

Edge-case rules:
- <two requests in one conversation → ...>
- <overlap between X and Y → merged, or the rule that separates them>

## Annotation
Labelled set: <150–200 conversations, sampled by period, channel, population>. Double-labelled: <≥ 50>. Human agreement per dimension: <...>.

## Candidates
| Classifier | Agreement: use case | Agreement: resolution | Agreement: other dimensions | Cost per conversation | Latency |
| --- | --- | --- | --- | --- | --- |

## Chosen setup
Threshold: <confidence>. Above: <cheap model>. Below: <stronger model / human review / unclassified>.
Blended agreement per dimension: <...>. Blended cost per conversation: <...>. Monthly cost at <volume>: <...>.

## Monthly drift check
Fresh sample: <50–100>, labelled by <who>. Alert when: agreement drops by <x points> on a dimension, "other" > 10%, or a new recurring request appears.

## Output schema
`trace_id`, `use_case`, `domain`, `resolution`, `sentiment`, `language`, `confidence`, `classifier_version`, `taxonomy_version`. Joined to `assistant-kpis-cost-per-outcome` on `trace_id`.

## Unresolved clusters
| Use case | Volume | Unresolved share | Masked sample handed to `build-evals` |
| --- | --- | --- | --- |

## Open questions
| Question | Owner |
| --- | --- |
