---
name: multi-turn-evals
description: 'Evaluate whole conversations. Use when a chat assistant forgets, contradicts itself or drifts over turns while one-shot tests pass, or a per-turn average or simulated-chat score is offered as ready.'
license: CC-BY-4.0
metadata:
  stage: "evaluate"
  version: "0.2.2"
  status: "tested"
  eval_threshold: "0.80"
  legal: "false"
  last_verified: "2026-11-12"
  autonomy_relevant: "true"
  depends_on: "build-evals, error-analysis, conversation-analysis, llm-judge-calibration"
  feeds: "release-to-production, production-evals-monitoring, model-card-ai-registry"
  sources: "laban-multi-turn, kwan-mt-eval, bai-mt-bench-101, dou-simulatorarena, zhou-sim2real-users, yao-tau-bench, anthropic-agent-evals, sierra-adlc, wilson-interval, miller-error-bars, husain-shankar-evals"
---

# multi-turn-evals

## When to use
- Users work with the assistant or copilot over several turns (they refine, correct, add facts, come back to an earlier point), and its evals score one question and one answer at a time.
- One-shot evals pass, yet users complain that it forgets what they said, contradicts an earlier answer, drifts off the task or ignores their correction.
- A team reports a per-turn average, or the pass rate of simulated conversations, as the reason a conversational assistant is ready.
- An assistant that only converses moves up the autonomy ladder (L1 → L2, L2 → L3 in references/autonomy-ladder.md): a human who used to read the whole exchange stops reading it.
- Do not use to build a one-shot eval set, its graders or the release gate itself: that is `build-evals`, which takes this skill's conversation-level results as one input.
- Do not use to generate one-shot test inputs when real cases are scarce: that is `synthetic-eval-data`. Simulated users that hold a whole conversation, and their validation, stay here.
- Do not use for an assistant that calls tools or writes to systems (books, pays, sends, updates a record), even for its level move: end state and forbidden events are `agent-evals`. A level move for an assistant that only talks, drafts or proposes comes here.
- Do not use to classify production conversations by use case at scale: that is `conversation-analysis`.
- Do not use to read traces and find failure modes for the first time: that is `error-analysis`.

## Inputs
Mandatory: what the assistant does and for whom; a sample of real conversations (anonymised) with their length; the facts and constraints users typically state, and when; the decision the eval feeds (release, ladder move, model change) and the monthly volume of conversations.
Ask if missing: the one-shot suite and its scores; complaints or reviewer notes about forgetting or contradiction; the length distribution of conversations (share past 4, 6, 10 turns); who reads conversations today and at which level; a user simulator if one exists, and how it was built.
No real conversations yet: simulate, but every score stays indicative until step 4 has been run on real ones. For the exposure, ask the business owner for the cost of one failed conversation (rework, complaint handling, remediation).

## Method
1. **Pick conversation-level outcomes, each a binary check on the whole transcript.** Goal reached (the user got what they came for, or a correct refusal). Facts and constraints given earlier kept to the end (each stated constraint, "budget 300 EUR", "I rent", "no equities", is listed and checked at every later turn that depends on it). No self-contradiction across turns. Recovery after a user correction (the correction is used from then on and never reverted). Correct hand-off (it escalates when it should and passes the context, so the user does not repeat it). No premature answer (it asks for the missing fact instead of guessing, references/multi-turn-method.md §1). A conversation passes only if every outcome holds. Never average per-turn scores into a readiness figure: turns that pass one by one still add up to failed conversations (98% per turn over 10 independent turns leaves about 82% of conversations clean), and a turn can be fine on its own while it breaks a constraint stated five turns earlier.
2. **Keep per-turn checks only where a turn has its own correct answer**: a rate quoted, an amount computed, a policy fact. Those turns are also one-shot cases in `build-evals`. Everything that depends on earlier turns is graded on the conversation.
3. **Build cases two ways, both from real use** (failure modes from `error-analysis`, use-case shares and lengths from `conversation-analysis`). Cover the patterns: recollection of an early fact, refinement, a correction, a fact revealed late, a topic switch and return.
   - **Scripted from real logs.** Take anonymised conversations, keep the user turns, regenerate the assistant's turns with the version under test, and mark the decisive turns: where the constraint is stated, where it must be applied, where the correction arrives. Grade at the decisive turns and at the end. When a scripted user turn no longer makes sense after a new reply, mark the case diverged, not failed. Scripted cases are the regression suite (references/eval-statistics.md §14); every conversation in a complaint becomes one.
   - **Simulated users.** A second model plays the user from a card: persona (expertise, patience, verbosity, language), a goal, and a hidden fact it reveals late or only when asked. Stop on goal reached, user gives up, or a turn cap. Simulated cases give coverage and repetitions; they are only as good as step 4.
4. **Validate the simulator against real conversations before trusting a score.** Take real conversations of the same use cases, derive a card from each, simulate them, and compare distributions with tolerances written before the comparison: turns per conversation (median and 90th percentile), share with a correction, share of vague or incomplete first messages, facts volunteered against facts given only when asked, abandonment, message length. Then compare outcomes, paired card by card: each simulated conversation against the real conversation its card came from, rated by people. Report the difference in pass rate with its paired interval (references/eval-statistics.md §5), about ±1.96 × √(d / n) with d the share of cards whose two verdicts disagree; the simulator passes only when the whole interval sits inside the tolerance, and a gap inside it with an interval that crosses it is not a pass. The same holds for every row; size the cards so the half-width is at most tolerance minus expected gap, or widen the tolerance and say so (references/multi-turn-method.md §4). Simulated users tend to be too cooperative, too clear and too alike, so assistants score higher with them than with people; a stronger model is not a more faithful simulator. Read 10 to 20 simulated transcripts by hand; a trial the simulator broke is invalid. Until it passes, a simulator score is indicative and gates nothing.
5. **Measure the one-shot to multi-turn drop on the same tasks.** Take tasks from the one-shot suite and give the same information over several turns (split the facts, add a correction, reveal one fact late). Run both versions, compare per task (references/eval-statistics.md §5), and report the one-shot rate, the multi-turn rate, the drop, and the spread across repeated runs (worst run, share of tasks whose verdict changes between runs). Most of the loss is unreliability, not lost ability: a mean hides it.
6. **Grade per conversation, repeated.** Run each scenario k times (3 to 5, fixed before the run). The unit is the scenario (references/eval-statistics.md §1): turns of one conversation, and runs of one scenario, are not independent cases, so 400 turn scores are not n = 400. Report the per-conversation pass rate with its Wilson interval on n = scenarios (average the k runs of each scenario first, or bootstrap by scenario), and the observed pass^k, the share of scenarios whose k runs all pass (references/eval-statistics.md §8). p^k is a planning projection only (0.92 per conversation gives about 0.78 over 3 runs); it is a floor when scenarios differ in difficulty, so the observed pass^k is usually higher. Size each gated class from the expected rate and the margin the decision needs (references/eval-statistics.md §3: about 113 scenarios for ±5 points at 92%). When the gate is on the lower bound (references/eval-statistics.md §4), size so the lower bound at the expected rate clears the bar: at 92% expected against a 90% bar, 140 scenarios give a lower bound near 86.5% and fail an assistant that is as good as the pilot; it takes about 830. Otherwise lower the bar with a reason, gate a narrower class, or keep the current level. Price the run: scenarios × k × turns × (assistant + simulator calls) + judge calls. Zero failures in n scenarios still allows about 3/n.
7. **Locate the first failing turn.** For each failed conversation, label the turn where it became unrecoverable (constraint dropped, early wrong assumption, contradiction, correction ignored) and its distance from the turn that gave the fact; later errors are consequences. Count by position and type: late starts point to context handling, turns 1 and 2 to premature answers, turns after a correction to correction handling.
8. **Choose graders per outcome.** A code check where the transcript allows it (the stated budget appears in the final offer, the hand-off was called). Otherwise a judge that reads the whole transcript on one binary criterion, calibrated against expert labels with `llm-judge-calibration` before it gates.
9. **Write the gate.** Dated and signed before the run (references/evals-as-evidence.md, rule 1): scenarios per class and k, the simulator validation result, the bar per outcome on the per-conversation rate (strictest on constraint kept and hand-off where an error costs money or a complaint), a separate pass^k bar, the maximum one-shot to multi-turn drop. Never copy the per-conversation bar onto pass^k: an assistant at 92% per conversation shows a pass^3 near 0.78, so a 90% pass^3 bar fails it. Start the pass^k bar from the per-conversation bar to the power k (0.90^3 ≈ 0.73) and raise it where a scenario that fails once in k runs is itself unacceptable. For a ladder move, start from what the human reader used to catch across turns: those outcomes carry the bar. State the exposure with its interval: failure rate × the monthly conversations of the population the test sample represents (if the sample holds only conversations past six messages, apply the rate to those, not to all traffic) × cost per failed conversation (rework, complaint, remediation), the cost given by the business owner (references/roi-model.md), never invented. If the interval is too wide for that cost, the answer is more scenarios or the current level.

## Output
`templates/multi-turn-eval-plan.md`, all headings present: conversation outcomes, per-turn checks kept, scripted cases, simulated users, simulator validation, one-shot to multi-turn drop, repetitions and pass^k, first failing turn, graders, gate and exposure, open questions. A section that cannot be filled says what is missing and who provides it.

## Rules and red lines
- Never declare a conversational assistant ready, or move it up a level, on an average of per-turn scores: the conversation is the unit, and a conversation that loses a stated constraint fails whatever its turns scored.
- Never gate on a user simulator that has not been compared with real conversations on length, corrections and vagueness, and on outcomes.
- Never treat turns or repeated runs of one scenario as independent cases.
- Never read a one-shot score as evidence for multi-turn use without the drop measured on the same tasks.
- Report the observed pass^k and the spread across runs, not only the mean; p^k is a projection, not a result.
- Failed conversations are located at their first failing turn before any fix is proposed.
- Scenarios, k, tolerances and bars are fixed before the run.

## Links
references/eval-statistics.md · references/evals-as-evidence.md · references/autonomy-ladder.md · references/multi-turn-method.md · references/roi-model.md · build-evals · agent-evals · synthetic-eval-data · error-analysis · conversation-analysis · llm-judge-calibration · release-to-production · production-evals-monitoring

## Sources
- laban-multi-turn: the same task given over several turns scores lower, mostly from unreliability; early assumptions are rarely recovered.
- kwan-mt-eval: the same queries scored one-shot and multi-turn to measure the drop; recollection, expansion, refinement and follow-up patterns; distance to the relevant turn.
- bai-mt-bench-101: multi-turn abilities drawn from real dialogues, scored per task and per turn.
- dou-simulatorarena: a simulator validated against real conversations on message behaviour and on agreement with human ratings.
- zhou-sim2real-users: simulated users are too cooperative and uniform, so scores run higher than with people.
- yao-tau-bench: pass^k over repeated conversations; a simulated user with hidden information; grading once per conversation.
- anthropic-agent-evals: trials per task and pass^k against pass@k.
- sierra-adlc: reviewed conversations turned into regression tests.
- wilson-interval: the interval on the per-conversation rate and the rule of three.
- miller-error-bars: clustered results, so the scenario is the unit, not the turn.
- husain-shankar-evals: binary criteria and the first upstream failure.
