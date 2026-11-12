# Residual-risk record: <feature>, <version>, campaign of <dates>

A record for model risk and counsel to read. It states rates and gaps; it does not declare the system robust, secure or compliant.

## Scope
System versions (model, prompt, knowledge base, lookup tools), autonomy level per step, decision this record feeds.

## What was tested
| Class | Attacks (independent seeds) | Testers and independence | Settings |
| --- | --- | --- | --- |

## What was not tested, and why
| Class or taxonomy entry | Why not (not applicable, out of scope, no tester, no time) | Consequence | Planned for |
| --- | --- | --- | --- |

## Rates against the tolerances signed beforehand
| Class | Successes / held-out seeds | Rate and 95% interval | Tolerance (signed, date) | Reading | Upper bound × attack attempts a month (source) | Tries to a first success (about 1 / upper bound) |
| --- | --- | --- | --- | --- | --- | --- |

## Findings and their status
| Finding | Status (fixed and re-tested on fresh attacks, mitigated, accepted, open) | Regression case |
| --- | --- | --- |

## Checklist for counsel and model risk (not a verdict)
| Item | Evidence in this record | Open question for counsel |
| --- | --- | --- |
| AI Act art. 15(5): data poisoning, model poisoning, adversarial examples or model evasion, confidentiality attacks, model flaws (each tested, untested or not applicable) | | |
| AI Act art. 15(4): resilience to errors, faults, inconsistencies, including from users and other systems | | |
| AI Act art. 9(5): residual risk judged acceptable, by whom | | |
| AI Act art. 9(6): testing identifies the risk-management measures and shows consistent performance for the intended purpose | | |
| AI Act art. 9(8): tested against metrics and probabilistic thresholds defined beforehand | | |
| Role: is the organisation provider or deployer of this system? If deployer, have the provider's declared robustness and cybersecurity levels and test conditions (art. 13(3)(b)(ii)) been obtained? The vendor's figure is filed as documentation, not as this feature's rate | | |
| For a bank or insurer: does this campaign belong in the DORA digital operational resilience testing programme, and who in ICT risk records it? (question for counsel or ICT risk) | | |
| Whether these articles apply to this system (ai-act-classification) | | |
| Steps that act on systems (L3 and above, references/autonomy-ladder.md): none, or their attack tests are recorded by agent-evals | | |

## Next campaign triggers
Model, prompt, knowledge base or lookup tool change; new data source; a step that starts acting on systems; new attack class reported; date: <date>.

## Acceptance
Residual risk accepted by: <name, role, outside the build team> · Date · Conditions · Reviewed by model risk: <name>
