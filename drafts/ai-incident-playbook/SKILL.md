---
name: ai-incident-playbook
description: 'Prepare the response to an AI incident: classes, severities, first 60 minutes, named rollback owner, reporting clocks, review. Use at go-live at L3+, after a near-miss or during an incident.'
stage: govern
version: 0.1.0
last_verified: 2026-11-05
depends_on: [system-prompt-and-guardrails, ai-act-classification, model-card-ai-registry, release-to-production]
feeds: [build-evals]
autonomy_relevant: true
sources: [eu-ai-act, gdpr, own-incident-practice]
eval_threshold: 0.90
status: draft
---

# ai-incident-playbook

## When to use
- A system goes live at L3 or above, or compliance asks for a playbook.
- After a near-miss, or during an incident (harmful output, data leak, wrong action, drift).
- Do not use for a pure infrastructure outage with no AI behaviour involved.
- Do not use to classify the system: use `ai-act-classification`.

## Inputs
Mandatory: what happened or what could happen, the autonomy level, who can roll back.
Ask if missing: guardrail spec, monitoring, the AI Act classification, whether personal data is involved, when the incident was detected.

## Method
1. Classify: harmful output, data leak, wrong action, drift. Set severity from impact on people and reversibility: `Severity: SEV1` to `SEV4`. Drift with no harm stays low (SEV3 or SEV4) and leads to an eval refresh.
2. First 60 minutes: contain (stop the action, drop the level, roll back), preserve traces, name the incident lead.
3. Name the rollback owner: one role, with a deputy, not a committee.
4. Check reporting and compute the clocks as dates from the detection time. All for counsel and the DPO to confirm.
   - Personal data breach (GDPR art. 33): the controller notifies the authority without undue delay and, where feasible, within 72 hours of becoming aware, with reasons if later. No notification if a risk to people is unlikely; the DPO decides and records it. People concerned are told if the risk is high (art. 34). A processor alerts its controller without undue delay. Take the detection time as the prudent start of the clock.
   - Serious incident (AI Act art. 3(49)) on a high-risk system: the deployer immediately informs the provider, then the importer or distributor and the authority (art. 26(5), from 2 December 2027 for Annex III). The provider's limits under art. 73, from awareness: 15 days in general, 10 days in case of death, 2 days for a widespread infringement or critical infrastructure; an incomplete first report is allowed. When art. 73 itself starts to bite for Annex III systems is an open question for counsel.
5. Write communications: users, sponsor, DPO, the CSE if work is affected.
6. Post-incident review: timeline, cause, fix. Every incident becomes eval cases through `build-evals`. Update the card with `model-card-ai-registry`.

## Output
`templates/playbook.md`, all headings present.

## Rules and red lines
- Rollback authority is a named role.
- Deadlines are computed as dates, not described.
- Checklist, not verdict: the skill never decides that a breach needs no notification; the DPO does.
- Every incident becomes eval cases.

## Links
references/autonomy-ladder.md · build-evals · ai-act-classification · model-card-ai-registry · cse-consultation

## Sources
- eu-ai-act: art. 3(49), 26(5), 73.
- gdpr: art. 33, 34.
- own-incident-practice: first 60 minutes, named owner, cases from incidents.
