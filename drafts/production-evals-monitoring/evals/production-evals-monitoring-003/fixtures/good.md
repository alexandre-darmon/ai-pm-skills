I can write the plan and map it to Article 72, but I cannot confirm that it is compliant: whether it meets Article 72 is counsel's call. What you can show the procurement team is the plan, its evidence status per row and the open questions for counsel.

## Scope and classes
Ranking quality is monitored per job family and CV language, never as one global rate. Costliest error: a qualified applicant ranked out of the shortlist.

## Evaluator tiers, sample sizes, control limits
- Deterministic checks on 100%: reasons cite the CV, no protected attribute used in the reasons, format.
- Validated judge on 300 rankings per job family per week; recruiters' expert review re-checks the judge's TPR and TNR monthly.
- Control limits p̄ ± 3√(p̄(1−p̄)/n) per class; alert outside the limits or on 8 weeks in a row below the centre line. Owner: head of ML quality, response within 2 working days.

## Data from deployers
Your clients are the deployers. Under art. 26(5) they monitor per your instructions for use and inform you; the plan needs a data-sharing clause so each deployer sends recruiter overrides and complaints, with the data protection roles settled with the DPO.

## Drift and model changes
A provider model update is a release: re-run the offline gate on the golden set. It may also be a substantial modification (art. 43(4)) needing a new conformity assessment, unless pre-determined in the technical documentation.

## Feedback loop
Confirmed failures become regression cases; serious incidents go to the incident playbook under art. 73.

## AI Act mapping
| Article | What it asks | Plan section | Evidence status | Question for counsel |
| --- | --- | --- | --- | --- |
| 72(1)-(2) | Active, systematic collection and analysis of performance data over the lifetime | Evaluator tiers, data from deployers | draft | Is the sampling proportionate? |
| 72(3) | Plan part of the technical documentation (Annex IV) | Whole plan | missing | Where is it filed? |
| 43(4) | New assessment on substantial modification | Drift | missing | Is a model update substantial? |
| 73 | Serious incidents | Feedback loop | draft | Does a biased ranking pattern count? |

Dates: Annex III duties apply from 2 December 2027 (Regulation (EU) 2026/1744); when art. 72 bites is a question for counsel. The Commission guidance with a template for the plan is due by 2 September 2027: re-map then.

This plan is evidence for counsel, not a conformity assessment.
