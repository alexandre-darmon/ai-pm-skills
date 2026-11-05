---
name: ai-interaction-patterns
description: 'Design how an AI feature behaves for users: sources, confidence, correction, refusal, escalation, latency. Use for assistant UX, showing uncertainty, or users who over-trust or ignore the AI.'
stage: specify
version: 0.1.0
depends_on: [llm-feature-prd, build-evals]
feeds: [system-prompt-and-guardrails, ai-adoption-plan]
autonomy_relevant: true
sources: [ms-hax, google-pair, own-assistant-ux]
eval_threshold: 0.80
status: draft
---

# ai-interaction-patterns

## When to use
- The UX of an assistant or agent is being designed.
- Someone asks how to show uncertainty, or users over-trust or ignore the AI.
- Do not use for prompt wording or guardrails: use `system-prompt-and-guardrails`.
- Do not use for visual design of a non-AI screen.

## Inputs
Mandatory: the feature, the autonomy level per step.
Ask if missing: user research notes, error profile from evals, whether scores are calibrated.

## Method
1. Start from the level in references/autonomy-ladder.md. L1: the draft is editable first, nothing goes out by itself. L2: approve or edit each output. L3: an exception queue plus a sample to review, not an inbox of everything.
2. Show sources next to the answer so people can check. Show confidence only if calibrated, meaning measured against outcomes; otherwise hide the score and rely on sources.
3. Make every answer correctable in one action, and log the correction.
4. Write refusals that explain scope and point to the next step.
5. Define the escalation to a human, and state that the user is dealing with an AI (hand over to `ai-act-classification` on transparency duties).
6. Set latency expectations: progressive display, a number for first output.
7. Route feedback into the eval set with `build-evals`.

## Output
`templates/interaction-spec.md`, all headings present.

## Rules and red lines
- Confidence is shown only if calibrated.
- Every answer is correctable in one action.
- Refusals explain scope.
- Feedback feeds the eval set.

## Links
references/autonomy-ladder.md · build-evals · system-prompt-and-guardrails · ai-adoption-plan

## Sources
- ms-hax, google-pair: trust calibration and correction patterns, as references.
- own-assistant-ux: exception queue and edit-first patterns.
