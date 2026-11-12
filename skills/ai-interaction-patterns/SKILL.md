---
name: ai-interaction-patterns
description: 'Decide what users see of an AI answer: sources, a confidence label or score, correction, refusal, hand-off per autonomy level. Use for assistant UX, a "% sure" badge, or reviewers who accept all.'
license: CC-BY-4.0
metadata:
  stage: "specify"
  version: "0.3.2"
  status: "tested"
  eval_threshold: "0.80"
  autonomy_relevant: "true"
  depends_on: "llm-feature-prd, build-evals"
  feeds: "system-prompt-and-guardrails, ai-adoption-plan"
  sources: "ms-hax, google-pair, own-assistant-ux, repo-chanmeng, wilson-interval, eu-ai-act, gdpr"
---

# ai-interaction-patterns

## When to use
- An assistant, copilot or agent is being designed and someone must decide what users see and can click: the draft, its sources, a score, the buttons, refusals, the hand-off to a person.
- Someone wants to show a confidence score, a "% sure" label or a coloured badge.
- Reviewers accept almost everything, or bypass the AI, and someone reads that as trust or distrust.
- A step moves up the autonomy ladder and the reviewer's screen or queue must change with it.
- Do not use for prompt wording, guardrail thresholds or false-positive budgets: use `system-prompt-and-guardrails`.
- Do not use to train users or run the adoption programme: use `ai-adoption-plan`.
- Do not use to decide whether the AI Act applies or which risk class: use `ai-act-classification`.

## Inputs
Mandatory: the feature, who reads the output (staff or the public), the level of each step on references/autonomy-ladder.md.
Ask if missing, and list in the spec what each missing input would change: error profile from evals, a reliability table (scores against labelled outcomes), cost of an error in each direction, who staffs any human queue, the acceptance, edit and review-time baseline.

## Method
1. **Pattern per level.** Read each step's level on references/autonomy-ladder.md and give it the matching pattern; never redefine the levels.
   - L1: the output arrives as an editable draft. What reaches a system of record or a customer is the person's version, saved from the editor once flagged items are resolved, never a one-click send on the raw answer.
   - L2: approve, edit and reject sit side by side, and rejecting costs no more clicks than accepting. The evidence each decision needs sits beside it.
   - L3: an exception queue on explicit triggers plus a random sample, never an inbox of every output.
   - Moving up only through the ladder's gate, a measured fact. For L3: a shadow run, a known guardrail false-positive rate, a tested escalation path, and the audited error rate in each direction (a wrong approval and a wrong rejection cost different things). Acceptance rate, speed or a manager's impression is never a gate. Moving down is free.
2. **Review happens on the screen, not in an attestation.** A "I have reviewed this" checkbox, a confirm dialog or a sign-off button gets clicked unread and proves nothing. Mark what needs a look instead (statements without a source, amounts, names, commitments, mismatches) and require an action on each flagged item, not on the whole output. A duty written in a policy but absent from the screen goes unperformed.
3. **Sources.** Link each claim to its source span, one click away. A statement with no source carries a visible label ("not found in the transcript") and is never styled like the others. When an answer has no source at all, say so.
4. **Confidence only from a reliability table.** A model score is not a frequency. Bucket the scores, count labelled outcomes per bucket (from the `build-evals` test set), compute each bucket's observed rate and its Wilson 95% interval (references/eval-statistics.md §2; `python3 scripts/reliability_table.py 0.9-1=470/500 --claim 0.9-1=0.98 --tolerate 0.85` does it; `--tolerate` is the lowest correct rate the use accepts). Then:
   - Never show a raw score as a percentage.
   - A bucket may carry a figure only with at least 100 labelled cases and a figure no higher than the interval's lower bound, worded as a measured frequency ("in testing, at least 85 in 100 answers like this were right"), in a neutral colour. Green reads as "go".
   - A claimed figure above the bucket's upper bound is contradicted by the data; between the bounds it is not demonstrated. Say which, with the numbers.
   - A bucket below what the use tolerates shows no figure: sources and an invitation to check, or, when an error is costly, no answer at all (step 6).
   - No table yet: no score and no badge; sources carry the trust. Rebuild the table after every model, prompt or retrieval change.
5. **Correction loop.** One action to correct: edit inline, mark a line wrong or missing, override with a reason code. Log the original output, the corrected version, the reason, who and when. Corrections become eval cases through `build-evals` (the skill that owns the test set), and the user is told what happens to them.
6. **Refusal and escalation.** A refusal states the scope, the reason and the next step (where to go, whom to ask). Escalate on explicit conditions: the user asks for a person (honoured at once), the case is out of policy, no progress after a set number of turns, the action sits above the step's level, the reliability bucket is below tolerance. Sentiment is not a trigger, nor is an uncalibrated score. Every human queue has an owner, an SLA, what happens and what the user reads when the SLA lapses (a fallback owner, never the AI's unreviewed output), and a handoff summary (who, the request, what the AI found and tried, what it recommends, why it stopped), because the person taking over does not see the transcript.
7. **Decisions about people.** When a step at L3 or above decides something with legal or similarly significant effect on a person (rejecting a claim, a loan, an account), no human looks at each case: it may become a solely automated decision under GDPR art. 22. Before the level change, list questions for the DPO: the legal basis, how the person obtains human intervention, states their view and contests, and what explanation they get. Keep the costly direction (rejections) at L2 until counsel answers. Log each review action (who, what was shown, time spent, decision) as the oversight record.
8. **Transparency.** When the system talks directly with people, AI Act art. 50(1), applicable since 2 August 2026, asks its provider to make sure they know they are dealing with an AI, clearly and at the latest at the first interaction, unless it is obvious. Put it on the first screen and in the handoff ("you are now talking to a person"). For staff tools, label AI-drafted content in the record (drafted by AI, reviewed by whom) for oversight. Whether the team is provider or deployer, and whether art. 50(2) marking or 50(4) apply, goes to `ai-act-classification` as questions, never as a conclusion.
9. **Latency.** Progressive display, a number for time to first output, no action control until the output is complete.
10. **Trust from behaviour, tested two ways.** Track acceptance and bypass (as `assistant-kpis-cost-per-outcome`, the skill that owns those metrics, defines them), the share edited before use, and review time, with thresholds from the team's own baseline. High acceptance with short review time suggests rubber-stamping; routine bypass suggests under-trust. Both are inferences. Confirm with two different tests, because they measure different things:
    - Seeded errors test the reviewers: insert known-wrong outputs into the live queue, withdrawn before anything goes out, and measure the catch rate.
    - A blind re-review of a random sample tests the AI: error rate in each direction.
    Size both: zero errors in n cases still allows a true rate up to about 3/n (rule of three), so bounding a rate at 1% takes about 300 clean cases, per stratum when a rare category carries a high cost. Answer over-trust on the screen (step 2), never with a badge.

## Output
`templates/interaction-spec.md`, all headings present, ending with the open questions: each missing input and what it would change. Every number not taken from the brief is marked as a placeholder to set from the team's data. When the spec names another skill, it says in a few words what that skill provides.

## Rules and red lines
- No attestation checkbox or confirm dialog stands in for review; flagged items need an action each.
- At L1, no one-click path from the raw AI output to a record or a customer.
- No raw score as a percentage, no badge, no stated figure above the reliability table's lower bound.
- No level change on acceptance rate, speed or opinion: only the ladder's gate.
- Refusals state scope and next step; escalation triggers are explicit; every queue has an owner, an SLA and a lapse path.
- A decision about a person at L3 or above goes to the DPO with GDPR art. 22 questions before the change.
- Corrections are logged and feed the eval set.
- A high acceptance rate alone is not evidence of trust: read it with review time, then test it.

## Links
references/autonomy-ladder.md · references/eval-statistics.md · build-evals · system-prompt-and-guardrails · ai-adoption-plan · assistant-kpis-cost-per-outcome · ai-act-classification

## Sources
- ms-hax, google-pair: trust calibration and correction patterns, as references.
- own-assistant-ux: exception queue, edit-first drafts, flagged items instead of review checkboxes, seeded errors to test reviewers (from our assistant missions).
- repo-chanmeng: escalation conditions, handoff summary, queue ownership. Reading acceptance with review time as rubber-stamping is our own inference.
- wilson-interval: the bucket interval and the rule of three behind the reliability table and the sample sizes.
- eu-ai-act: art. 50 transparency duties. gdpr: art. 22 on solely automated decisions.
