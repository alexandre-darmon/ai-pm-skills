---
name: prd-to-claude-code
description: 'Turn an AI feature PRD into a build brief for an agentic coding tool: AGENTS.md, specs with executable criteria, risk-ordered tasks. Use when a PRD is approved or prototyping starts.'
stage: build
version: 0.2.0
depends_on: [llm-feature-prd, build-evals]
feeds: [agent-design-and-tooling, release-to-production]
autonomy_relevant: false
sources: [anthropic-claude-code, own-specs-folder, repo-pangkaifeng, repo-chanmeng]
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
A PRD known only from a summary, or an open stack, does not stop the work: write the whole brief from what you have, mark each gap as to be confirmed, and list the questions at the end. Stop only if you cannot tell what the feature does.

## Method
1. Write `AGENTS.md` (or `CLAUDE.md`): stack, conventions, commands, and what is out of bounds.
2. Create one file per module in `specs/`. Each acceptance criterion is executable: a test or an eval case. Every criterion maps to one. A vague requirement ("fast", "accurate") gets a number from the PM, or a stated default that a test enforces, marked as to be confirmed.
3. Order tasks by risk. Task 1 tests the riskiest assumption, usually the model: run it end to end on real-shaped inputs with its eval case, with no more scaffolding than that run needs. Then integration, then interface.
4. Define done: tests and the eval suite pass in the build loop, not only at the end.
5. Write the "do not build" list from the PRD's non-goals.
6. Protect data: secrets and client data never enter the repo. Fixtures are synthetic; state how they are generated.
7. Say what enforces each must-hold rule. `AGENTS.md` is guidance a coding tool can ignore, so the eval gate and the paths to real data each name what blocks a breach: a CI check, a hook, a permission rule or a test. Secrets and scope outside `specs/` take one line each. Name the mechanism, not a tool's flags.
8. Check coverage. Every PRD requirement, plus autonomy level, fallback, guardrails, eval threshold and non-goals, points to a spec line and its test, or is excluded with a reason, or is open with who confirms it. These AI fields vanish first. List a missing one, do not invent it; if several are missing, deliver the brief and say the PRD should go back to `llm-feature-prd`.

## Output
`templates/build-brief.md`, all headings present. If the template cannot be read, still write the brief, one section per method step.

## Rules and red lines
- Acceptance criteria are tests or eval cases, never prose.
- The eval suite runs in the build loop.
- No client data and no secrets in the repo, including fixtures.
- A must-hold AI rule that only lives in `AGENTS.md` is not enforced: name what blocks it.

## Links
llm-feature-prd · build-evals · agent-design-and-tooling · release-to-production

## Sources
- anthropic-claude-code: how to brief an agentic coding tool.
- own-specs-folder: one spec per module, risk-ordered tasks.
- repo-pangkaifeng: mapping every PRD item to covered, excluded or unresolved (idea only; the AI field list is ours).
- repo-chanmeng: instructions are advisory, hooks and permissions are deterministic (idea only).
