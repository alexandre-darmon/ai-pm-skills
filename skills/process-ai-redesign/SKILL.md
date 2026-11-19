---
name: process-ai-redesign
description: 'Redesign a business process with AI: autonomy level and gate per step, three scenarios with ROI lines, trade-offs, migration path. Use for "automate this process" or an efficiency target.'
license: CC-BY-4.0
metadata:
  stage: "specify"
  version: "0.2.2"
  status: "tested"
  eval_threshold: "0.90"
  autonomy_relevant: "true"
  depends_on: "ai-opportunity-assessment, conversation-analysis, ai-roi-quantification, ai-act-classification, agent-design-and-tooling"
  feeds: "ai-opportunity-assessment, ai-adoption-plan, agent-design-and-tooling, build-evals"
  sources: "hammer-reengineering, own-process-redesign, repo-chanmeng"
---

# process-ai-redesign

## When to use
- Someone asks to "automate this process" or to put AI into an existing workflow.
- An efficiency programme or an ROI target lands on a process with volume and exceptions.
- Do not use for a single feature inside a product: write its PRD with `llm-feature-prd`.
- Do not use to decide whether AI fits at all: run `ai-opportunity-assessment` first.

## Inputs
Mandatory: the process steps, volumes, time per step, exception rate, current cost.
Ask if missing: data available per step, risk and regulatory context, whether employees' work or evaluation changes, appetite for autonomy.
If the exception rate is unknown, measure it before setting any level above L2.

## Method
1. Map the current process step by step, with volume, time and exception rate per step. Levels are set per step, never per process.
2. Fill the step table from references/autonomy-ladder.md (read it first): current level, target level, why not L+1, gate to reach the target. Every target level names its gate as a measured fact; the gates come from `build-evals`, `system-prompt-and-guardrails` and `release-to-production`. After those five columns, add an Approach column: the simplest technique that does the step, tried in this order: none or rule, workflow, RAG, LLM, agent. If a rule does the step, it gets no model. Technique and level are separate decisions: a step run by a rule still states its level and gate.
3. Set each target by how an error in that step would surface. If a later step or a person catches it by design and it is cheap to undo (a ticket tagged with the wrong language, an internal summary its reader corrects), the step can go higher once gated. If the error flows silently into a record others rely on (a code written to a ledger, a value another system reuses), keep the step at L2 until its error rate is measured. A check is not cheap to undo by default: a hit sent to review is caught, a missed hit flows silently, so its level rests on its miss rate (false negatives) measured on a labelled sample, not only on hits going to review. A decision with legal or financial effect on a person (accept, refuse, compensate, sanction) targets L1: the human decides and the AI prepares the file. L2 is its ceiling, not its default, because a human validating a ready-made decision tends to rubber-stamp it.
4. When exceptions are a large share of cases, redesign the exception handling first and keep the target levels low until it is done: autonomy on a process that is mostly exceptions moves work, it does not remove it. A low exception rate does not by itself justify autonomy; the gates do.
5. Build three scenarios (conservative, target, ambitious), each with the five ROI lines of references/roi-model.md: volume, quality, unit value, run cost, change cost.
6. Compare scenarios in a trade-off table on cost per outcome, risk, reversibility and obligations, not on "efficiency". Every scenario keeps a human fallback, and sizes it: expected review and exception items per period × time per item = reviewer hours, against the hours the team still has. Name the queue owner, the SLA and what happens at timeout. The hours go into the change cost line. If time per item is unknown, write the formula and mark it to measure; do not invent it. A fallback the team cannot staff does not count: lower the level or the volume.
7. Check triggers. AI Act classification depends on the use case, not on the level: run `ai-act-classification` on what the system does to people (decisions on customers, monitoring or evaluating workers), whatever the level, and re-check it when a step reaches L4, because less human oversight changes what oversight design must show. A step that changes how employees work, or measures them, is flagged for HR and counsel: national labour law asks for employee representatives to be informed and consulted before use (in France the CSE, on new technologies and on any means of monitoring employees), so make that a gate before go-live, not a later task. If the system is high-risk (for example Annex III point 4, monitoring or evaluating workers), AI Act art. 26(7) also has the employer inform workers' representatives and affected workers before use, from 2 December 2027. The migration path moves one level at a time, each move behind its gate from `build-evals`. Each step also names its demotion trigger: the observed value that sends it back one level, also read after a model change, and who acts on it. Moving down needs no approval (ladder rule 3). The rollback mechanism belongs to `release-to-production`.
8. Write the plan with milestones and owners.

Keep the dossier proportionate: about 1,000 to 1,500 words, tables over prose, one recommended target per step and one recommended scenario. Use only the figures you were given; anything else is a formula or a named assumption to measure, not a number. Recompute every total you state (hours, FTE, share of volume), since one wrong sum discredits the plan. End with the few inputs you need from the reader.

## Output
`templates/redesign-dossier.md`, all headings present. The step table follows the ladder's step table format, plus the Approach column after its five columns.

## Rules and red lines
- Levels per step, never per process; every target level has its gate.
- No decision with legal or financial effect on a person above L2.
- No scenario without a human fallback sized in reviewer hours, or its formula marked to measure.
- No full automation (L5) of a process with exceptions or decisions on people.
- The use case is checked with `ai-act-classification`, and re-checked at L4+; any step touching employees' work or evaluation is flagged for employee-representative information or consultation before go-live, because labour law requires it before use, not after.

## Links
references/autonomy-ladder.md · references/roi-model.md · build-evals · release-to-production · ai-act-classification · agent-design-and-tooling · ai-opportunity-assessment

## Sources
- hammer-reengineering: redesign the process, do not automate the old one.
- own-process-redesign: level per step, exception redesign first, scenarios on cost per outcome, fallback sized in reviewer hours, demotion trigger per step.
- repo-chanmeng: technique chosen per step; a human takeover queue has an owner, an SLA and a timeout.
