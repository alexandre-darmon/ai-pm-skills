# AI Act classification memo — <use case>

Freshness: skill verified on <last_verified>. <If more than 90 days old: "Application dates and guidance may have changed: counsel to confirm.">

## System and role
| System or step | What it does and decides | Autonomy level (references/autonomy-ladder.md) | Role (art. 3(3) provider / art. 3(4) deployer / art. 25 deployer turned provider) |
| --- | --- | --- | --- |

## Prohibited practices (art. 5)
<None identified, with the points checked, or the possible hit and the question for counsel.>

## Risk category
| Category | Basis (article, annex point) | Facts it rests on | Open point |
| --- | --- | --- | --- |
| prohibited · high-risk · transparency obligations · minimal | | | |

Art. 6(3) exception: <not relevant / question for counsel, with the facts>.

## Transparency (art. 50)
<Which paragraphs apply, who does what.>

## General-purpose model
<Model, provider, how it is used (API, fine-tuned), what is asked of the model provider (art. 53(1)(b)).>

## Obligations
| Who | Obligation | Article | Applies from | Owner | Evidence status |
| --- | --- | --- | --- | --- | --- |

Evidence records paper, not conformity (status values: Method step 7).

## Eval evidence per article
<High-risk: obligations. Below high risk: good practice. Details: references/evals-as-evidence.md.>
| Article | Evidence | Produced by | Status (on file / claimed / missing) |
| --- | --- | --- | --- |
| 9(8) | Thresholds per class, defined and signed before testing | `build-evals` | |
| 10(3)-(4) | Test set composition per class and risk, synthetic share | `build-evals`, `synthetic-eval-data` | |
| 15(3) | Accuracy metrics and levels declared in the instructions for use | `model-card-ai-registry` | |
| 17(1)(d) | Test procedures before, during and after development, with frequency | quality system | |
| 26(5) / 72 | Monitoring of operation / post-market monitoring plan | `production-evals-monitoring` | |
| 73 | Serious incident classes and reporting | `ai-incident-playbook` | |

## If a step moves to L+1
| Step | From → to | What changes in the classification | Obligations that appear or tighten (article) |
| --- | --- | --- | --- |

## Questions for counsel
| Question | Facts counsel needs | Why it matters |
| --- | --- | --- |

This memo is a checklist for counsel, not a conformity assessment.
