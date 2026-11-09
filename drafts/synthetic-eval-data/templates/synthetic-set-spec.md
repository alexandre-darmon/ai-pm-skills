# Synthetic set spec — <feature name>

## Real material read
<Real examples (how many, from where, period), error-analysis notes, traffic statistics available.>

## Dimensions
| Dimension | Values | Grounded in (real example, failure hypothesis, or "assumed") |
| --- | --- | --- |

## Tuple plan
| Class | Traffic share | Weight in the set | Tuples | Exclusion rules |
| --- | --- | --- | --- | --- |
<Reviewed by, date.>

## Generation
<Generator model and version, prompt version, anchors used, separate step from tuples, model under test.>

## Review and realism
| Dimension value | Reviewed | Rejected | Rejection rate | Action |
| --- | --- | --- | --- | --- |

| Measure | Real traffic | Synthetic | Tolerance | Within? |
| --- | --- | --- | --- | --- |

## Expected answers
<Who writes them, from which documents; judge used and its validation.>

## Composition and flags
| Class | Real cases | Synthetic cases | Synthetic share | Holdout (real / synthetic, flagged) |
| --- | --- | --- | --- | --- |
<Flag schema. Scores reported on real and synthetic separately.>

## Contamination check
<Prompts, few-shot examples and training data checked for overlap with the set, date.>

## Privacy
<Personal data rules, check for copied names or identifiers, no paraphrase of a real person's case.>

## Replacement plan
| Class | Synthetic share today | Target share | Real source | Date |
| --- | --- | --- | --- | --- |

## Open questions
| Question | Owner |
| --- | --- |
