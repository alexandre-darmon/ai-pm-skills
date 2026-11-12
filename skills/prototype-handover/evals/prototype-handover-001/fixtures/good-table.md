# Handover file: motor claims triage

## 1. Containment
Production personal data: no (400 anonymised emails) · Production credentials: no · Decision needed: none before go-live.

## 3. Tier
| Step | Level today | Wanted level | Process tier | Autonomy tier | Tier (higher) |
| --- | --- | --- | --- | --- | --- |
| Triage | L2 | L2 | 3 (business-critical) | 3 | 3 |
| Draft | L2 | L2 | 3 | 3 | 3 |

## 4. Proposed outcome
Rebuild by engineering. The prototype is a spec with evidence.

## 5. Handover contract
- Frozen baseline: 364/400, 91%; Wilson interval: 87.8 to 93.4 (%). Per-category recall, fraud signal first: with few cases its interval is wide and it gets its own bar.
- Judge: the 88% comes from a judge with no measured true-positive rate or true-negative rate on expert labels.
- Prompts, model id and parameters: configuration under change control.

## 7. What engineering rebuilds
| Item | Rebuild / reuse as spec / drop | Note |
| --- | --- | --- |
| Authentication, authorisation, row-level access | Rebuild | today anyone with the link sees every email |

## 8. Draft register entry
ICT asset (DORA art. 3(7)): identifier, location, owner, classification, dependencies.

## 10. Questions
- For IT risk: register the prototype now or only the rebuilt service?

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.
