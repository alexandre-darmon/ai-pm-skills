---
name: ai-brand-positioning
description: 'Build an AI product''s category, claims ledger and copy, every claim checked against evals and autonomy level. Use for its landing page, launch text or tagline, or when "AI-powered" says nothing.'
stage: strategy
version: 0.1.0
last_verified: 2026-11-06
depends_on: [ai-opportunity-assessment, ai-moat-7-powers, build-evals]
feeds: [ai-initiative-pitch, ai-adoption-plan]
autonomy_relevant: true
sources: [category-pirates-snow-leopard, calloway-category-of-one, cole-online-writing, hagel-power-of-pull, own-copywriting]
eval_threshold: 0.80
status: draft
---

# ai-brand-positioning

## When to use
- A landing page, launch text, name or tagline for an AI product.
- "AI-powered" says nothing, or competitors using the same models sound the same.
- Marketing copy says "autonomous", "agent", "10x" or "99%", and someone must check it.
- Do not use for a budget pitch: use `ai-initiative-pitch`. Internal rollout: `ai-adoption-plan`. A defensibility question with no copy to write: `ai-moat-7-powers`.
- Do not use for a brand with no AI in the product: a standard brand or copy brief applies.

## Inputs
Mandatory: the product; what it does at each step and who validates; the existing copy or claims; the audience.
Ask if missing: eval results with set and date, KPIs, the alternatives buyers compare it with, the data owned and the workflow position (the `ai-moat-7-powers` scan if there is one). What cannot be supplied is recorded as unmeasured, not assumed.

## Method
1. **Difference test.** The model is a commodity, so "AI-powered" is never the differentiator. Look for a real difference in data, workflow position or proof. If there is none yet, say so: state what is not ownable today and what would have to be true to own it, and write only copy that is true now.
2. **Category and point of view.** Only from a real difference. Name the category in the buyer's problem, make the alternative look like the old way, and tie it to something you deliver, not a slogan. Test: does a buyer with this problem exist who would use these words? If not, it is jargon; say so. Plan obvious content for attention and non-obvious content for the category.
3. **Claims ledger.** One row per claim: evidence, level, status (keep, downgrade, remove). A claim on accuracy names the eval set, its size and its date, and says when the set is too small to carry the wording. A gain shows the five lines of `references/roi-model.md`, or it is removed. A projection with its five lines stays in the ledger, labelled; it does not reach the copy.
4. **Vocabulary check.** Set each autonomy word ("autonomous", "agent", "handles it for you", "suggests", "drafts for your review") against the measured level of that step, L0-L5 (`references/autonomy-ladder.md`). Copy never promises more than the current level; a target level is roadmap, labelled as such.
5. **Failure line.** The copy says what the product does when it is unsure and when a human takes over. A claim that hides this creates the trust failure that adoption then pays for.
6. **Pull plan.** Two or three mechanisms, each with who pulls and why: public proof, real outputs, published limits, so that people who already have the problem find it. A launch blast is not a mechanism.
7. **Copy pack.** A before and after on the user's own text, built only from kept or downgraded claims. Thesis first, one specific reader, specifics over adjectives.
8. **Questions for counsel.** Hand legal questions over, do not answer them: does AI Act art. 50(1) (informing people they interact with an AI system, unless obvious) apply, and who is the provider? Could a performance or autonomy claim be misleading ("AI washing")?

## Output
`templates/brief.md`, all headings present, no empty section.

## Rules and red lines
- No word promises more autonomy than the measured level.
- No gain without the five lines; "10x" is anchored or removed.
- An unmeasured or contradicted number never reaches the final copy, even on request.
- Never invent a difference, and never claim a moat or a category from the prompt, the model or the interface.
- Never call a product compliant, in the copy or in the analysis.

## Links
`references/autonomy-ladder.md` · `references/roi-model.md` · `ai-moat-7-powers` (the difference) · `build-evals` (accuracy evidence) · `assistant-kpis-cost-per-outcome` (acceptance metrics) · `ai-interaction-patterns` (transparency inside the product) · `ai-act-classification` (legal questions)

## Sources
Book ideas are cited from summaries, not quoted, and carry no attributed framework.
- category-pirates-snow-leopard: a category of one; obvious and non-obvious content.
- calloway-category-of-one: defy comparison; win on what you deliver, not gimmicks.
- cole-online-writing: thesis first, specificity.
- hagel-power-of-pull: pull, not push.
- own-copywriting: own judgment, from no book: the ledger, the vocabulary check against the ladder, the failure line, the buyer test for jargon.
