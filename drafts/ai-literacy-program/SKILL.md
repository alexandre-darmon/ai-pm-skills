---
name: ai-literacy-program
description: 'Train staff to supervise and use an AI tool, by role and autonomy level, with a calibration test and evidence. Use when users over-trust it, reviewers must check it, or AI training or art. 4 comes up.'
stage: transform
version: 0.2.0
depends_on: [ai-adoption-plan, ai-act-classification, model-card-ai-registry]
feeds: [ai-adoption-plan]
autonomy_relevant: true
sources: [eu-ai-act, feynman-method, own-pedagogy, repo-chanmeng]
eval_threshold: 0.80
status: draft
---

# ai-literacy-program

## When to use
- People misuse or over-trust an AI tool, or reviewers must supervise one.
- An adoption plan needs training, a new population joins, or an incident reveals misuse.
- The AI Act literacy measures (art. 4) need a concrete plan.
- Do not use for the wider rollout: use `ai-adoption-plan`.
- Do not use for general digital training with no AI tool in scope.

## Inputs
Mandatory: populations and roles, the tools and their L-levels.
Ask if missing: existing training, time available per person, failed eval cases and incident records for the tool.

## Method
1. State the duty plainly. As amended by Regulation (EU) 2026/1744, art. 4 asks providers and deployers to take measures to support the literacy of staff operating the systems, with no required level. The skill sizes the programme to the role and the risk; whether it suffices goes to counsel through `ai-act-classification`.
2. Write objectives per population, from the level in references/autonomy-ladder.md: what the tool can't do, data rules, and for anyone with oversight duties (L2 and above), its failure modes, the pull to accept its output unread as errors get rare, and how to intervene, override or stop.
3. Choose formats and durations per population: micro-modules, hands-on with their real tasks. Build the material from this tool's own failures: failed cases from `build-evals`, incident cases from `ai-incident-playbook`. Sponsors get limits and governance in about an hour. Reject a generic e-learning as the sole measure; it may serve as a base layer.
4. Explain simply, then test: the learner explains the failure modes back (Feynman method), or corrects real wrong outputs. Anyone who reviews outputs also sits a calibration test before taking up the duty: a batch mixing sound outputs and seeded errors, scored on errors caught and on sound outputs wrongly flagged, per population (references/calibration-test.md). The team sets the pass mark. Sponsors who review no outputs skip it, so their hour stays an hour.
5. Record completion and calibration results as evidence for the registry (`model-card-ai-registry`).
6. Set the refresh: at each change of level or major release, and after an incident. Retest at each refresh, with fresh errors.

## Output
`templates/literacy-programme.md`, all headings present.

## Rules and red lines
- Literacy is role-specific, never one generic e-learning alone.
- Anyone with oversight duties is trained on failure modes.
- Completion is recorded, and never stands as proof that someone can catch a wrong output.
- Pass marks come from the team, never from this skill.
- Never state that the programme makes the company compliant.

## Links
references/autonomy-ladder.md · references/calibration-test.md · ai-adoption-plan · ai-act-classification · model-card-ai-registry · build-evals · ai-incident-playbook · cse-consultation

## Sources
- eu-ai-act: art. 4 as replaced by Reg. 2026/1744; art. 14(4)(b) on over-reliance, for high-risk systems.
- feynman-method: explain, find gaps, iterate.
- own-pedagogy: hands-on with real tasks; the calibration test is our own proposal.
- repo-chanmeng: errors nobody can see lead users to re-check everything or to trust blindly (the problem, not the test).
