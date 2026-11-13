# Judge calibration report — <failure mode> · judge v<n>

System under test: <name, model and version, prompt version>. Judge: <model and pinned version>, prompt v<n>. Date: <date>.

## Criterion
Failure mode (from error analysis): <one sentence>.
Pass means: <...>. Fail means: <...>.
Written by: <domain expert>, after reading <n> real outputs, on <date>. Output format: critique, then verdict (pass / fail).
Decision this judge feeds: <release gate · level gate (L<n> → L<n+1>) · production rate · dashboard>. Costlier error: <false pass / false fail>, because <...>.

## Labellers and agreement
| Labeller | Role | Answers labelled | Overlap with the other labeller | Kappa |
| --- | --- | --- | --- | --- |

Labels made without seeing the judge's verdicts: <yes / no>.

## Label splits
| Split | Answers | Expert pass | Expert fail | Used for |
| --- | --- | --- | --- | --- |
| Few-shot pool | | | | examples in the prompt |
| Dev | | | | prompt iterations |
| Test | | | | this report, scored once |

Enrichment of fails: <none / how>.

## Targets, set before measuring
| Metric | Target | Gate on | Signed by (or: proposal, unsigned) | Date |
| --- | --- | --- | --- | --- |
| TPR | | point / lower bound | | |
| TNR | | point / lower bound | | |

## Confusion matrix (test split)
| | Judge pass | Judge fail |
| --- | --- | --- |
| Expert pass | | |
| Expert fail | | |

## TPR and TNR
| Metric | Value | 95% interval | Target | Met? |
| --- | --- | --- | --- | --- |
| TPR | | | | |
| TNR | | | | |

Raw agreement: <x>, not used for the decision (a judge passing everything would agree <y> on this split). Kappa judge vs expert: <...>.

## Bias checks
| Bias | Applies? | Test run | Result |
| --- | --- | --- | --- |
| Position | | | |
| Verbosity | | | |
| Self-preference | | | |
| Prompt sensitivity | | | |

## Corrected pass rate on traffic
Sample: <n answers, period, how sampled>. Judge pass rate (observed): <x>.
Corrected rate: <x>, 95% interval <lo> to <hi> (<method>). Largest source of uncertainty: <sample / TPR / TNR, from the computed terms>. Threshold of the decision: <t>. Reading: <met / missed / inside the interval, not decided>.

## Status
<Gate for this failure mode / Not a gate yet>. Until it is a gate: <who reviews what the judge would decide>.

## Next revision
| Disagreement pattern | Change to criterion or rubric | Fresh labels needed | Owner | Date |
| --- | --- | --- | --- | --- |

## Re-validation triggers
| Trigger | Action | Owner |
| --- | --- | --- |
| Judge model or version change | | |
| Prompt or criterion change | | |
| Schedule | | |

## Cost
Cost per judge call: <...>. Calls per month at the sampling volume: <...>. Monthly judge cost: <...>.

## Open questions
| Question | Owner |
| --- | --- |
