---
name: prd-to-claude-code
description: 'Turn an AI feature PRD into a build brief for an agentic coding tool: AGENTS.md, specs with executable criteria, risk-ordered tasks. Use when a PRD is approved or prototyping starts.'
stage: build
version: 0.1.0
depends_on: [llm-feature-prd, build-evals]
feeds: [agent-design-and-tooling, release-to-production]
autonomy_relevant: false
sources: [anthropic-claude-code, own-specs-folder]
eval_threshold: 0.80
status: draft
---

# prd-to-claude-code

## When to use
- A PRD for an AI feature is approved and an agentic coding tool will build it.
- A prototype or vibe-coding session is about to start.
- Do not use to write the PRD: use `llm-feature-prd`.
- Do not use for a non-AI feature with no evals: a generic spec is enough.

## Inputs
Mandatory: the PRD, the stack constraints.
Ask if missing: the existing repo, eval cases from `build-evals`, data the build may touch.

## Method
1. Write `AGENTS.md` (or `CLAUDE.md`): stack, conventions, commands, and what is out of bounds.
2. Create one file per module in `specs/`. Each acceptance criterion is executable: a test or an eval case. Every criterion maps to one. A vague requirement ("fast", "accurate") gets a number from the PM, or a stated default that a test enforces, marked as to be confirmed.
3. Order tasks by risk: the riskiest assumption first, usually the model behaviour on real inputs, then integration, then interface.
4. Define done: tests and the eval suite pass in the build loop, not only at the end.
5. Write the "do not build" list from the PRD's non-goals. Scope outside `specs/` is refused.
6. Protect data: secrets and client data never enter the repo. Fixtures are synthetic; state how they are generated.

## Output
`templates/build-brief.md`, all headings present.

## Rules and red lines
- Acceptance criteria are tests or eval cases, never prose.
- The eval suite runs in the build loop.
- No client data and no secrets in the repo, including fixtures.

## Links
llm-feature-prd · build-evals · agent-design-and-tooling · release-to-production

## Sources
- anthropic-claude-code: how to brief an agentic coding tool.
- own-specs-folder: one spec per module, risk-ordered tasks.
