# Red-team campaign: <feature>, <version>

Owner: <name> · Independent tester lead: <name, relation to the build team> · Plan signed: <date, by> · Decision it feeds: <release, level change, audit request> · Due: <date>

## Target and threat model
| Field | Value |
| --- | --- |
| Feature type | assistant / RAG (tools the user triggers on their own records stay here; a feature that acts on systems on its own is an agent: `agent-evals`) |
| Model, prompt, knowledge base, lookup tool versions | |
| Data it can reach (classes) | |
| Lookup tools and the data they return; tools the user triggers (tickets, drafts) and the records they write | |
| Where the output goes (screen, rendered page, a draft a person sends) | |
| Who can write what it reads (users, document authors, third parties) | |
| Autonomy level per step (references/autonomy-ladder.md) | |
| Monthly volume | |
| Estimated attack attempts a month, and source (logs, conversation analysis, incidents) | |

## Attack classes from the feature's risks
| # | Attacker goal | Entry point (direct, indirect, multi-turn) | Consequence in this feature | Cost of one success (sourced) |
| --- | --- | --- | --- | --- |

## Coverage against public taxonomies
| Taxonomy entry (OWASP LLM 2025, NIST AI 100-2 goal, ATLAS technique and release) | Our class # | Relevant? | Tested in this campaign? | Reason if not |
| --- | --- | --- | --- | --- |

Coverage share: <tested classes> of <relevant classes> = <%>.

## Success criteria, settings and tolerances (signed before the campaign)
| Class | Success criterion (binary, how checked: canary, trace, end state, human, calibrated judge) | Tolerable rate | Signed by |
| --- | --- | --- | --- |

Generation settings: model and prompt version, temperature, turns allowed, attempts per seed: <values>.
Unit: n = independent seeds; a seed is one success when the criterion is met in any of its attempts.

## Sizing
| Class | Tolerable rate r | Held-out seeds needed (0 / 1 / 2 successes) | Held-out share | Seeds to write | Indicative if under n? |
| --- | --- | --- | --- | --- | --- |

## Testers and independence
| Source | Who | Relation to the build team (built it, same team, independent internal, external) | Classes | Attacks |
| --- | --- | --- | --- | --- |
| Automated generation | | | | |
| Human red-teamers | | | | |
| Regression attacks from past findings | | | | |

## Held-out set
Development set (build team may see and tune on): <n, where>. Held-out set (sealed): <n, keeper, hash, date>. Burned attacks moved to regression: <n>.

## Results per class
| Class | Successes / held-out seeds | Rate | 95% interval (Wilson) | Tolerance | Reading (under, over, undecided) | Testers |
| --- | --- | --- | --- | --- | --- | --- |

Pooled rate, shown only beside the table: <k/n>. Gap between tuned set and fresh set: <points>.

## Findings and regression cases
| Finding | Class | Attack and context kept | Regression case id | Sent to (system-prompt-and-guardrails, engineers) | Re-test on fresh attacks |
| --- | --- | --- | --- | --- | --- |

## Open questions
