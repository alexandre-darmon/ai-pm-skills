---
name: process-ai-redesign
description: 'Redesign a business process with AI: autonomy level and gate per step, three scenarios with ROI lines, trade-offs, migration path. Use for "automate this process" or an efficiency target.'
stage: transform
version: 0.2.0
depends_on: [ai-opportunity-assessment, conversation-analysis, ai-roi-quantification, ai-act-classification, cse-consultation, agent-design-and-tooling]
feeds: [ai-initiative-pitch, ai-adoption-plan, agent-design-and-tooling]
autonomy_relevant: true
sources: [hammer-reengineering, own-process-redesign, repo-chanmeng]
eval_threshold: 0.90
status: draft
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
3. Keep decisions with legal or financial effect on people (accept, refuse, compensate, sanction) at L1 or L2. Routing, extraction and checks can go higher once their gate passes.
4. When exceptions exceed about a quarter of cases, redesign the exception handling first and lower the target levels: autonomy on a process that is mostly exceptions moves work, it does not remove it.
5. Build three scenarios (conservative, target, ambitious), each with the five ROI lines of references/roi-model.md: volume, quality, unit value, run cost, change cost.
6. Compare scenarios in a trade-off table on cost per outcome, risk, reversibility and obligations, not on "efficiency". Every scenario keeps a human fallback, and sizes it: expected review and exception items per period × time per item = reviewer hours, against the hours the team still has. Name the queue owner, the SLA and what happens at timeout. The hours go into the change cost line. If time per item is unknown, write the formula and mark it to measure; do not invent it. A fallback the team cannot staff does not count: lower the level or the volume.
7. Check triggers. A step at L4 or above calls `ai-act-classification` for a re-check. A step that changes how employees work, or measures them, calls `cse-consultation`. The migration path moves one level at a time, each move behind its gate from `build-evals`. Each step also names its demotion trigger: the observed value that sends it back one level, also read after a model change, and who acts on it. Moving down needs no approval (ladder rule 3). The rollback mechanism belongs to `release-to-production`.
8. Write the plan with milestones and owners.

## Output
`templates/redesign-dossier.md`, all headings present. The step table follows the ladder's step table format, plus the Approach column after its five columns.

## Rules and red lines
- Levels per step, never per process; every target level has its gate.
- No decision with legal or financial effect on a person above L2.
- No scenario without a human fallback sized in reviewer hours, or its formula marked to measure.
- No full automation (L5) of a process with exceptions or decisions on people.
- Every L4+ step references `ai-act-classification`; any step touching employees' work or evaluation references `cse-consultation`.

## Links
references/autonomy-ladder.md · references/roi-model.md · build-evals · release-to-production · ai-act-classification · cse-consultation · agent-design-and-tooling · ai-initiative-pitch

## Sources
- hammer-reengineering: redesign the process, do not automate the old one.
- own-process-redesign: level per step, exception redesign first, scenarios on cost per outcome, fallback sized in reviewer hours, demotion trigger per step.
- repo-chanmeng: technique chosen per step; a human takeover queue has an owner, an SLA and a timeout.
