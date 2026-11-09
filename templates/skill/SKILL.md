---
name: my-skill
description: <What the skill produces>. Use when <trigger situation, in the user's words>. Max 200 characters.
stage: specify  # specify | evaluate | prove
version: 0.1.0
last_verified: 2026-11-01  # mandatory for legal skills
legal: false  # true if the skill reads the law: no judge grader, eval_threshold >= 0.90, last_verified
depends_on: []
feeds: []
autonomy_relevant: false
sources: [own-practice]  # ids from foundations/sources.md
eval_threshold: 0.80  # 0.90 for legal and flagship skills
status: draft  # draft | tested | verified-in-mission
---

# my-skill

## When to use
- <Trigger situation 1>
- <Trigger situation 2>
- <Trigger situation 3>
- Do not use when <anti-trigger 1>.
- Do not use when <anti-trigger 2>.

## Inputs
Mandatory: <inputs the agent must have; refuse or ask if missing>.
Ask if missing: <optional inputs>.

## Method
1. <Step: what to produce, and the rule it applies.>
2. <Step.>
3. <Step.>

## Output
`templates/<artefact>.md`, all headings present, no empty section.

## Rules and red lines
- <What the skill refuses to do.>

## Links
references/autonomy-ladder.md (synced copy of the foundation) · <other skills>

## Sources
- own-practice: <what this skill takes from it, one line>.
