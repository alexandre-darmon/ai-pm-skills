# Handover file: <artefact name>

Date: <date> · Prepared by: <PM> · Freshness: <last_verified, and a warning if over 90 days>

## 1. Containment
Production personal data: <yes / no> · Production credentials: <yes / no> · Kill date: <date, past or not>
Decision needed: <stop now / dated decision by <named owner> on <date> / none needed> · Credentials to revoke or rotate: <list>

## 2. Inventory
| Item | Value | Known / to confirm |
| --- | --- | --- |
| Function | | |
| Users (number, roles) | | |
| Data read, credentials used | | |
| Actions (reads, drafts, acts) | | |
| Model and version, prompt location | | |
| Eval cases and scores | | |
| Owner, kill date, where it runs | | |

## 3. Tier
| Step | Level today | Wanted level | Process tier | Autonomy tier | Tier (higher) |
| --- | --- | --- | --- | --- | --- |

## 4. Proposed outcome
<Retire on <date> / Register at tier <1 or 2> / Rebuild by engineering>, and why in two lines.

## 5. Handover contract
- Eval suite: <cases, graders, version or hash>
- Frozen baseline: <per class: k of n, rate, 95% Wilson interval; model version; prompt version; date>
- Bar per class, signed by <who> on <date>; never-acceptable error: <...>
- Judge: <model, criterion, TPR, TNR, on how many expert labels / "not validated: cannot gate">
- Configuration under change control: <prompts, model ids, parameters>
- Autonomy level per step and gate to the next level
- Trace fields logged
- The baseline is the floor for the engineering build. Release evidence is the suite run on that build.

## 6. Intended vs implemented
| Intended | Implemented | Gap or shortcut |
| --- | --- | --- |

## 7. What engineering rebuilds
| Item | Rebuild / reuse as spec / drop | Note |
| --- | --- | --- |
| Authentication, authorisation, row-level access | | |
| Secrets | | |
| Environments | | |
| Logging pipeline, retention | | |
| Guardrails in code | | |
| Model access through the gateway | | |
| Tests | | |

## 8. Draft register entry
| Field | Draft value |
| --- | --- |

## 9. AI Act flag
<Built in-house and put into service for own use? Purpose changed? Possible Annex III area?> → for ai-act-classification.

## 10. Questions
- For IT risk:
- For model risk:
- For counsel:
- For the DPO:

This file is a proposal and a list of questions. IT risk, model risk and counsel decide.
