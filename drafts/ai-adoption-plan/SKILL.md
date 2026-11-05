---
name: ai-adoption-plan
description: 'Plan the human side of an AI deployment: populations, waves, champions, training, objections, adoption metrics. Use when go-live nears, adoption stalls or a sponsor asks how to get people on board.'
stage: transform
version: 0.1.0
depends_on: [process-ai-redesign, assistant-kpis-cost-per-outcome, cse-consultation, ai-interaction-patterns]
feeds: [ai-literacy-program, ai-initiative-pitch]
autonomy_relevant: true
sources: [kotter-change, rogers-diffusion, cialdini-influence, own-coaching]
eval_threshold: 0.80
status: draft
---

# ai-adoption-plan

## When to use
- An AI go-live approaches, or a process redesign was approved.
- Adoption is below target, or a sponsor asks how to get people to use it.
- Do not use for AI Act literacy content: use `ai-literacy-program`.
- Do not use for a non-AI tool rollout: generic change management is enough.

## Inputs
Mandatory: populations and sizes, the tool and its autonomy level, the adoption data if live.
Ask if missing: known objections, CSE timeline, training capacity.

## Method
1. Map personas per population with sizes: champions, pragmatists, sceptics, blockers.
2. Diagnose before prescribing when adoption is low: split the funnel into awareness, access, first use, repeat use. High satisfaction with low use points to awareness or access, not quality.
3. Sequence waves. Managers before their teams. The pilot population is chosen for learning, not for ease: include hard cases.
4. Run a champion programme: at least one per team or branch, with time allocated.
5. Train on the real tasks of each population. Hand content to `ai-literacy-program`.
6. Write the objection table, each with an owner. Sceptics get a seat in the pilot or steering group, not a memo. Where work changes in France, align on `cse-consultation` timing before any wave.
7. Set adoption metrics per population and per wave, with targets from `assistant-kpis-cost-per-outcome`.
8. Close the loop: feedback goes into `agent-knowledge-base` and `build-evals`.

## Output
`templates/adoption-plan.md`, all headings present.

## Rules and red lines
- Adoption is measured by population, not globally.
- Every objection has an owner.
- Training is tied to real tasks.
- Sceptics get a seat, not a memo.

## Links
references/autonomy-ladder.md · process-ai-redesign · ai-literacy-program · cse-consultation · assistant-kpis-cost-per-outcome

## Sources
- kotter-change: sequencing.
- rogers-diffusion: adopter segments.
- cialdini-influence: communication on verifiable facts.
- own-coaching: real-task training, sceptics at the table.
