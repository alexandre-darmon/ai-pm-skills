---
name: ai-adoption-plan
description: 'Diagnose low use of a live AI tool and plan the human side of a deployment: waves, champions, training, objections, metrics. Use when go-live nears, use stalls or a sponsor wants to fix low adoption.'
stage: transform
version: 0.2.0
depends_on: [process-ai-redesign, assistant-kpis-cost-per-outcome, cse-consultation, ai-interaction-patterns]
feeds: [ai-literacy-program, ai-initiative-pitch]
autonomy_relevant: true
sources: [kotter-change, rogers-diffusion, cialdini-influence, own-coaching, repo-chanmeng, repo-lenny]
eval_threshold: 0.80
status: draft
---

# ai-adoption-plan

## When to use
- An AI go-live approaches, or a process redesign was approved.
- Adoption is below target, a sponsor asks how to get people to use it, or someone asks why a live tool is underused or proposes a fix before the cause is known.
- Do not use for AI Act literacy content: use `ai-literacy-program`.
- Do not use for a non-AI tool rollout: generic change management is enough.

## Inputs
Mandatory: populations and sizes, what each population uses for this task today, the tool and its autonomy level, the adoption data if live.
Ask if missing: known objections, CSE timeline, training capacity.

## Method
1. Map personas per population with sizes: champions, pragmatists, sceptics, blockers. Name each population's current workaround (the old tool, a personal chatbot account) as the real rival and state what the new tool must beat it on: if the personal account stays easier, the wave moves nobody and the data leaves unseen. Data rules for personal accounts go to `ai-literacy-program`.
2. Diagnose before prescribing when adoption is low: split the funnel into awareness, access, first use, repeat use. High satisfaction with low use points to awareness or access, not quality. Opening a tool is not adoption, so read one stage past repeat use: depth and trust among regular users, from the acceptance, redo and bypass metrics that `assistant-kpis-cost-per-outcome` defines. Regular use with routine rewriting or people going around the tool points to trust or quality: the fix is in `ai-interaction-patterns` or `build-evals`, not more communication. Each check gets a named owner, and any proposed fix waits for its result.
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
- Logins and ratings never prove adoption on their own.

## Links
references/autonomy-ladder.md · process-ai-redesign · ai-literacy-program · cse-consultation · assistant-kpis-cost-per-outcome · ai-interaction-patterns · build-evals

## Sources
- kotter-change: sequencing.
- rogers-diffusion: adopter segments.
- cialdini-influence: communication on verifiable facts.
- own-coaching: real-task training, sceptics at the table.
- repo-chanmeng: low adoption as a possible trust problem, bought is not used (idea only, own wording).
- repo-lenny: staff already on personal AI accounts as the real alternative (idea only, no guest quote reused).
