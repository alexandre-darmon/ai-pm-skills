---
name: ai-incident-playbook
description: 'Prepare or run the response to an AI incident: severity, containment, rollback owner, reporting clocks, the regression case it adds. Use at L3+ go-live, after a quality alert or in an incident.'
license: CC-BY-4.0
metadata:
  stage: "prove"
  version: "0.5.0"
  status: "tested"
  eval_threshold: "0.90"
  legal: "true"
  last_verified: "2026-11-12"
  autonomy_relevant: "true"
  depends_on: "production-evals-monitoring, system-prompt-and-guardrails, ai-act-classification, release-to-production, model-card-ai-registry"
  feeds: "error-analysis, build-evals, model-card-ai-registry"
  sources: "eu-ai-act, gdpr, dora-incident-reporting, google-sre, montgomery-spc, husain-shankar-evals, own-incident-practice, repo-chanmeng"
---

# ai-incident-playbook

## When to use
- A system goes live at L3 or above, or compliance asks for a playbook.
- An alert fires from `production-evals-monitoring`, a near-miss is reported, or an incident is under way (harmful output, data leak, wrong action, drift).
- A fix is ready after an incident and someone wants to ship it and close the case.
- Do not use for a pure infrastructure outage with no AI behaviour involved.
- Do not use to classify the system: use `ai-act-classification`.

## Inputs
Mandatory: what happened or what could happen, the autonomy level, who can roll back.
Ask if missing: the alert and its sample size, guardrail spec, the AI Act classification, whether personal data is involved, whether the company is a financial entity (DORA), when the incident was detected, the version bundle running in the window.

## Method
1. Classify: harmful output, data leak, wrong action, drift. Set severity from impact on people and reversibility: `Severity: SEV1` to `SEV4`. Drift with no harm stays low (SEV3 or SEV4) and leads to an eval refresh. Detection comes first from `production-evals-monitoring`: online evals on sampled traffic, guardrail triggers, override and reopen rates, then user reports. For a quality drop, check it against the noise before calling it drift: on n sampled traces, the control limits are p̄ ± 3√(p̄(1−p̄)/n) (references/eval-statistics.md); ask for n when it is not given.
2. First 60 minutes, once something wrong has reached people. Drift with no harm skips this step: no emergency rollback.
   - Contain by slice, not on or off: say which part stops and which keeps running, with a level drop written from and to, such as L4 to L2 (`references/autonomy-ladder.md`). High-stakes actions go back to human validation; low-risk ones continue. If no slice is known to be safe, stop everything.
   - Size the damage: pull every output or action since the window opened (the change, the deploy), not only the ones reported, and count the people affected, within a stated time. Fixing the system does nothing for what already went out. Revise the severity and step 4 from that count.
   - Preserve the traces and the version bundle of the window before any change, and name the incident lead.
3. Name the rollback owner: one role, with a deputy, not a committee. The owner acts at once, with no vote: moving down the ladder needs no approval (ladder rule 3). The rollback itself and its last rehearsal come from the release plan (`release-to-production`); show a rollback never rehearsed as untested.
4. Check reporting and compute the clocks as dates from the detection time. State each legal limit beside its date, also in a short answer, so counsel can check the arithmetic. All for counsel and the DPO to confirm.
   - Personal data breach (GDPR art. 33): the controller notifies the authority without undue delay and, where feasible, within 72 hours of becoming aware, with reasons if later. No notification if a risk to people is unlikely; the controller decides on the DPO's advice and records it. People concerned are told if the risk is high (art. 34). A processor alerts its controller without undue delay. Take the detection time as the prudent start of the clock.
   - Financial entity (bank, insurer, investment firm): ask counsel whether the incident is a major ICT-related incident under DORA (art. 18 criteria; art. 19 reporting). If it is, the clocks run beside the GDPR one and are shorter: initial notification within 4 hours of classifying it as major and no later than 24 hours from awareness, intermediate report within 72 hours of the initial one, final report within one month of the last intermediate report (Delegated Regulation (EU) 2025/301, art. 5). A leak of customer data through the AI system is the kind of case to put to counsel.
   - Serious incident (AI Act art. 3(49)) on a high-risk system: the deployer immediately informs the provider, then the importer or distributor and the authority (art. 26(5), from 2 December 2027 for Annex III). The provider's limits under art. 73, from awareness: 15 days in general, 10 days in case of death, 2 days for a widespread infringement or critical infrastructure; an incomplete first report is allowed. When art. 73 itself starts to bite for Annex III systems is an open question for counsel.
5. Write communications: users, sponsor, DPO, employee representatives if work is affected. In a live incident, put them in the answer rather than offering them for later. Start with the people who received the wrong output or action, called what the business calls them: what happened, what it means for them, what you will do.
6. Feed the evidence loop before the fix ships (references/evals-as-evidence.md):
   - an `error-analysis` note on every affected output of the window, not only the reported ones: what went wrong in each, which failure mode, new or known, which question class;
   - regression cases from those outputs added to the golden set through `build-evals`, failing on the faulty version;
   - the fix ships only when the regression cases pass and the full suite shows no class below its threshold, compared with the previous version on the same cases. A fix checked only on the reported examples is not verified. Shipping the fix and closing the incident are two gates, and this one comes first: an unverified fix never ships as a mitigation, nor because the rollback is quick; until it passes, the containment of step 2 (a slice stopped, a human check added) carries the risk;
   - the incident, the fix and the eval delta go to the card's changelog (`model-card-ai-registry`); a missed alert goes back to `production-evals-monitoring` as a new check.
   For a serious incident on a high-risk system, ask counsel before any investigation that alters the system whether the authority must be informed first (art. 73(6)).
   Then the post-incident review: timeline, cause, fix, what the monitoring missed.
7. When preparing before go-live, write at least three failure scenarios specific to this system: symptom, how to confirm it, action, how to verify the fix. One is the service looking healthy while its answers are wrong, so detection needs an alarm on an AI quality signal, not uptime alone. State the fallback path while the system is off.

## Output
`templates/playbook.md`, all headings present when preparing. During an incident or for a quick triage question, answer with what is needed now, and open with the class and the severity, provisional until the count is in. Asked whether a fix can ship, the first line answers it: not before the gate of step 6.

## Rules and red lines
- Rollback authority is a named role.
- Deadlines are computed as dates, never a limit alone or a date alone.
- Checklist, not verdict: the skill never decides that a breach needs no notification; the controller does, on the DPO's advice.
- Every incident becomes regression cases in the golden set before its fix ships; a fix checked only on the reported examples is not verified, and does not ship as a mitigation either.
- Once something wrong has reached people, no severity is final before the affected outputs are counted.

## Links
references/autonomy-ladder.md · references/evals-as-evidence.md · references/eval-statistics.md · production-evals-monitoring · error-analysis · build-evals · release-to-production · ai-act-classification · model-card-ai-registry

## Sources
- eu-ai-act: art. 3(49), 26(5), 73, including 73(6) on not altering the system before informing the authority.
- gdpr: art. 33, 34.
- dora-incident-reporting: DORA arts. 17–19 on major ICT-related incidents and Delegated Regulation (EU) 2025/301 art. 5 on their reporting time limits.
- google-sre: alerting on what users feel, not on uptime alone.
- montgomery-spc: a quality drop read against its control limits before it is called drift.
- husain-shankar-evals: reading every affected output and naming its failure mode before writing the regression case.
- own-incident-practice: first 60 minutes, named owner, cases from incidents before the fix.
- repo-chanmeng: containing by risk tier, pulling every output in the window, failure scenario form (ideas, own words).
