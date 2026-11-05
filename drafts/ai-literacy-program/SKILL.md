---
name: ai-literacy-program
description: 'Design a role-specific AI literacy programme by population and autonomy level, with assessment and evidence (AI Act art. 4). Use when training on an AI tool or an AI literacy duty comes up.'
stage: transform
version: 0.1.0
depends_on: [ai-adoption-plan, ai-act-classification, model-card-ai-registry]
feeds: [ai-adoption-plan]
autonomy_relevant: true
sources: [eu-ai-act, feynman-method, own-pedagogy]
eval_threshold: 0.80
status: draft
---

# ai-literacy-program

## When to use
- The AI Act literacy measures (art. 4) need a concrete plan.
- An adoption plan needs training, a new population joins, or an incident reveals misuse.
- Do not use for the wider rollout: use `ai-adoption-plan`.
- Do not use for general digital training with no AI tool in scope.

## Inputs
Mandatory: populations and roles, the tools and their L-levels.
Ask if missing: existing training, time available per person.

## Method
1. State the duty plainly. As amended by Regulation (EU) 2026/1744, art. 4 asks providers and deployers to take measures to support the literacy of staff operating the systems, with no required level. The skill sizes the programme to the role and the risk; whether it suffices goes to counsel through `ai-act-classification`.
2. Write objectives per population, from the level in references/autonomy-ladder.md: what the tool can't do, data rules, and for anyone with oversight duties (L2 and above), its failure modes and how to intervene, override or stop.
3. Choose formats and durations per population: micro-modules, hands-on with their real tasks. Sponsors get limits and governance in about an hour. Reject a generic e-learning as the sole measure; it may serve as a base layer.
4. Explain simply, then test: the learner explains the failure modes back (Feynman method), or corrects real wrong outputs.
5. Record completion as evidence for the registry (`model-card-ai-registry`).
6. Set the refresh: at each change of level or major release, and after an incident.

## Output
`templates/literacy-programme.md`, all headings present.

## Rules and red lines
- Literacy is role-specific, never one generic e-learning alone.
- Anyone with oversight duties is trained on failure modes.
- Completion is recorded.
- Never state that the programme makes the company compliant.

## Links
references/autonomy-ladder.md · ai-adoption-plan · ai-act-classification · model-card-ai-registry

## Sources
- eu-ai-act: art. 4 as replaced by Reg. 2026/1744.
- feynman-method: explain, find gaps, iterate.
- own-pedagogy: hands-on with real tasks.
