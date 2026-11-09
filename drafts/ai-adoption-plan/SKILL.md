---
name: ai-adoption-plan
description: 'Plan and prove adoption of an AI tool on outcomes: correct results per user, overrides, over-trust test, training by role and level, art. 4 evidence. Use when go-live nears or use stalls.'
stage: prove
version: 0.3.1
depends_on: [assistant-kpis-cost-per-outcome, process-ai-redesign, ai-interaction-patterns, build-evals, ai-act-classification]
feeds: [model-card-ai-registry, build-evals, ai-data-requirements, ai-roi-quantification]
autonomy_relevant: true
sources: [eu-ai-act, eu-digital-omnibus-ai, google-pair, wilson-interval, own-coaching, own-pedagogy, repo-chanmeng, repo-lenny]
eval_threshold: 0.80
status: draft
---

# ai-adoption-plan

## When to use
- An AI go-live approaches, a process redesign was approved, or a new population joins a live tool.
- Use is below target, a sponsor asks how to get people to use it, or someone proposes a fix before the cause is known.
- People over-trust a tool, accept its output unread, or must review or supervise it: they need training and a way to show they can catch its errors.
- The AI Act literacy measures (art. 4) need a concrete, dated plan.
- Do not use to set eval thresholds or a release gate: that is `build-evals`.
- Do not use to design what the interface shows (sources, scores, correction): that is `ai-interaction-patterns`.
- Do not use to define KPI formulas or the dashboard: that is `assistant-kpis-cost-per-outcome`; for a tool with no model in it, generic change management is enough.

## Inputs
Mandatory: populations and their sizes, what each population uses for this task today, the tool and the autonomy level of each step people touch (references/autonomy-ladder.md), the adoption and outcome data if live.
Ask if missing: sampled quality per use case, the override, redo and bypass data (`assistant-kpis-cost-per-outcome`), failed eval cases and incident records for the tool, time available for training per person, known objections.
Logins, sessions and satisfaction ratings are not adoption data: if they are all there is, outcome data is missing and the plan says who instruments it.

## Method
1. **Map populations and their rival.** Per population: size, role towards the tool (user, reviewer of outputs, sponsor), the level of the steps it touches, and its current workaround (the old tool, a personal chatbot account) as the real rival. State what the tool must beat it on: if the personal account stays easier, the wave moves nobody and the data leaves unseen.
2. **Define adoption as outcomes, per population, before any wave.** Four metrics, each with a target per wave, a source and an owner:
   - correct outcomes per active user per week: successes from the sampled review or outcome events, redone ones excluded, divided by active users. Use without correct outcomes is not adoption;
   - override and bypass rates, as `assistant-kpis-cost-per-outcome` defines them: outputs changed or rejected by users, in-scope work that goes around the tool;
   - wrong-answer acceptance, the over-trust signal: of the outputs the sampled review grades wrong, the share users accepted unchanged. Its mirror, sound outputs rewritten or rejected, is under-trust;
   - for populations that review outputs, the calibration result (step 5).
   Rates carry their counts and interval (references/eval-statistics.md). Wrong outputs are rare in a sample, so production acceptance of wrong answers stays indicative; the calibration test fills the gap.
3. **Diagnose before prescribing when use is low.** Split the funnel per population: awareness, access, first use, repeat use, then depth and trust. High satisfaction with low use points to awareness or access, not quality. Regular use with high override or bypass points to trust or quality: the fix is in `build-evals` or `ai-interaction-patterns`, not more communication. High use with high wrong-answer acceptance is over-trust: training and interface, not promotion. Each check gets a named owner, and any proposed fix waits for its result.
4. **Size training by role and level.** Per population, from the levels in references/autonomy-ladder.md:
   - every user: what this tool cannot do, the data rules (no client data in personal accounts), how to report a wrong output; short, hands-on, on their real tasks;
   - anyone who reviews or validates outputs (L2 and above): this tool's failure modes, built from its own failed eval cases (`build-evals`) and incidents (`ai-incident-playbook`); the pull to accept output unread as errors get rare; how to override, intervene and stop;
   - sponsors: about an hour on limits, governance and the decisions only they take (stop conditions), with no technical course.
   A generic e-learning may be a base layer, never the sole measure.
5. **Test reviewers before they take up the duty.** A calibration test on real outputs of this tool, mixing sound ones and seeded errors from its own failures, unmarked; scored per population on errors caught out of errors seeded and on sound outputs wrongly flagged out of sound ones (references/calibration-test.md). The team sets the pass mark, not this skill. Completion never stands as proof that someone can catch a wrong output. Individual scores are personal data about employees: before the first test, decide with the DPO who sees them and what for.
6. **Sequence waves.** Managers before their teams. The pilot population is chosen for learning, not for ease: include hard cases and sceptics. At least one champion per team or branch, with time allocated. A wave opens when the previous one meets its outcome targets, not on a calendar date.
7. **Handle objections.** An objection table, each objection with its answer and an owner. Sceptics get a seat in the pilot or the steering group, not a memo. Where staff fear the tool rates them, list what is logged and who sees it, and take it to the DPO and HR before any wave; whether employee representatives must be informed or consulted is a question for counsel.
8. **Record the literacy measures as dated evidence.** As amended by Regulation (EU) 2026/1744, art. 4 asks providers and deployers to take measures to support the AI literacy of staff and others operating AI systems on their behalf, with no required level. Per population: the measure, its date, completion, the latest calibration result, the next refresh. Checklist, not verdict: whether the measures suffice goes to counsel through `ai-act-classification`.
9. **Refresh and close the loop.** Retrain and retest with fresh errors at each change of level or major release, and after an incident. Wrong outputs that users catch become cases in `build-evals`; missing knowledge goes to `ai-data-requirements`. Training and support hours go to the change-cost line of `ai-roi-quantification`.

## Output
`templates/adoption-plan.md`, all headings present.

## Rules and red lines
- Adoption is measured per population on correct outcomes, never on logins, sessions or ratings alone.
- Every population that acts on outputs has an override or acceptance metric beside its usage.
- Diagnose before prescribing: no fix before the funnel check it depends on.
- Training is role- and level-specific; a generic e-learning is never the sole measure.
- Anyone with oversight duties is trained on this tool's failure modes and sits a calibration test; completion is never proof.
- Pass marks come from the team, never from this skill.
- Every objection has an owner; sceptics get a seat, not a memo.
- Never state that the plan makes the company compliant.

## Links
references/autonomy-ladder.md · references/eval-statistics.md · references/calibration-test.md · assistant-kpis-cost-per-outcome · build-evals · ai-interaction-patterns · ai-incident-playbook · ai-act-classification · model-card-ai-registry · ai-data-requirements · ai-roi-quantification

## Sources
- eu-ai-act: art. 4 on literacy; art. 14(4)(b) on awareness of over-reliance, for high-risk systems.
- eu-digital-omnibus-ai: the rewritten art. 4 (measures to support literacy, no required level).
- google-pair: trust calibration, over-trust and under-trust as two failures.
- wilson-interval: rates read with their counts and interval.
- own-coaching: populations and their workaround, managers first, sceptics at the table, waves opened on results.
- own-pedagogy: training on real tasks; the calibration test is our own proposal.
- repo-chanmeng: low use as a possible trust problem; errors nobody can see lead users to re-check everything or to trust blindly (ideas only).
- repo-lenny: staff already on personal AI accounts as the real alternative (idea only, no guest quote reused).
