---
name: ai-initiative-pitch
description: 'Turn an assessed AI initiative into a one-page pitch, a spoken version, an objection table and one dated ask, every number anchored. Use for a budget committee, comex or sponsor meeting.'
stage: strategy
version: 0.1.0
depends_on: [ai-opportunity-assessment, ai-moat-7-powers, ai-roi-quantification, ai-act-classification]
feeds: [ai-adoption-plan]
autonomy_relevant: true
sources: [cole-online-writing, cialdini-influence, hagel-power-of-pull, own-copywriting]
eval_threshold: 0.80
status: draft
---

# ai-initiative-pitch

## When to use
- An assessed AI initiative needs a sponsor or a budget: budget committee, comex slot, sponsor meeting.
- Someone asks to "write the one-pager" or review a pitch draft for an AI project.
- Do not use before the opportunity is assessed: run `ai-opportunity-assessment` first.
- Do not use for a pitch with no AI component or for a general marketing text.

## Inputs
Mandatory: the assessment (problem, decision, approach), the audience (DSI, business, comex), the ROI lines or the facts behind them.
Ask if missing: target autonomy level, risk flags from `ai-act-classification`, the business owner who will present, a demo.

## Method
1. Write the thesis in the first sentence: the problem, the fix, the ask. Then the 1/3/1 rhythm: one line, three supporting points, one line.
2. Anchor every number. A gain is volume × quality × unit value − run cost − change cost, as in references/roi-model.md. A percentage with no line behind it is rewritten as an anchored figure or removed, and the memo says it was removed.
3. When the ROI is weak or unmeasured, the ask is a measurement pilot with its success criterion, not a rollout.
4. Name the risk before the objections: a high-risk flag, personal data, employees affected. A sponsor who learns the risk later withdraws.
5. Build the objection table: the top five objections and the verifiable fact that answers each.
6. Use influence levers (social proof, authority, commitment, scarcity, reciprocity) only on a verifiable fact; name the fact.
7. Write the single ask: what, how much, for how long, decided by whom, by which date. The ask is a pilot, not a programme. The business owner presents; the DSI supports. Demo before discourse.
8. Add the three-minute spoken version and the one slide.

## Output
`templates/pitch.md`, all headings present. The ask line reads `Ask: <pilot>, <amount>, <duration>, decision by <date>`.

## Rules and red lines
- No unanchored percentage.
- The ask is a pilot with a date, never a rollout or a programme.
- A risk flag is named before the objection table.
- Never call the initiative compliant: compliance is a checklist owned by counsel.

## Links
references/roi-model.md · references/autonomy-ladder.md · ai-opportunity-assessment · ai-act-classification · ai-adoption-plan

## Sources
- cole-online-writing: thesis first, specificity over adjectives.
- cialdini-influence: levers used only on facts.
- hagel-power-of-pull: the business pulls the initiative; the DSI does not push it.
- own-copywriting: the 1/3/1 rhythm and the single dated ask.
