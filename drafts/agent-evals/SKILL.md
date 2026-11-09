---
name: agent-evals
description: 'Test an agent that calls tools or acts on systems and gate its autonomy on measured reliability. Use for "how do we test our agent?", a level change, a new tool, or "it says done, nothing changed".'
stage: evaluate
version: 0.2.0
legal: false
depends_on: [agent-design-and-tooling, build-evals]
feeds: [release-to-production, production-evals-monitoring, assistant-kpis-cost-per-outcome, model-selection]
autonomy_relevant: true
sources: [anthropic-agent-evals, yao-tau-bench, agentdojo, laban-multi-turn, anthropic-agents, wilson-interval, husain-shankar-evals, repo-lenny, repo-chanmeng, own-nanoagent]
eval_threshold: 0.80
status: draft
---

# agent-evals

## When to use
- "How do we test our agent?": an agent that calls tools, writes records, pays or sends needs its suite before it acts.
- A step moves up the autonomy ladder (L2 → L3, L3 → L4 in references/autonomy-ladder.md), or the agent gets a new tool, a higher cap or a new permission.
- Agent failures in production, or transcripts that say "done" while the system shows nothing changed.
- A prompt, tool description, model or provider model update must not break what the agent already does.
- An agent that reads emails, files or pages written by outsiders is about to act alone: injected instructions must be measured first.
- Do not use to design the agent's loop, tools, permission matrix or write protocol: that is `agent-design-and-tooling`.
- Do not use for an assistant that only retrieves and answers, with no tool that acts: retrieval quality is `retrieval-evaluation`, the answer set and thresholds are `build-evals`.

## Inputs
Mandatory: the agent's tools, each with its side effect and whether it can be undone; the step with its current and target level; the caps and approval rules (the permission matrix from `agent-design-and-tooling`); an isolated environment, sandbox or test doubles of every system the agent writes to.
Ask if missing: 20 or more real requests or transcripts (anonymised), production failures, monthly volume per action, cost per trial, who signs the gate.
No isolated environment: the first deliverable is the environment, not the suite. Trials never run against production systems with real side effects.

## Method
1. **Write tasks, not prompts.** A task is an instruction, a starting state, a success check on the end state and a list of forbidden events. The starting state is a fixture loaded before each trial: records, balances, permissions, approvals already given, past actions (a refund already issued). Draw tasks from real requests and production failures. Cover every tool, each cap at its boundary (just under, at, just over), lookups that return nothing and lookups that fail, and requests that span two tools. A transcript without its starting state cannot be replayed. Worked example and catalogue: references/agent-eval-method.md.
2. **Grade the end state first, the path only where it matters.** The success check queries the sandbox after the run: the refund row and its amount, the CRM field's new value, the outbox. The agent's final message is never the success check: a judge reading "Done" passes a run that changed nothing. Then check the trajectory only where the business requires it: calls that must happen (read before write, approval before commit), calls that must not, arguments (amount, target id), order. Where several paths reach the same valid end state, accept them all: a grader pinned to one reference path fails good runs.
3. **List forbidden events per task.** Approval skipped, write before read, duplicate write or send, amount over the cap, action on a record outside scope or on one the lookup did not find. One occurrence fails the trial, whatever the end state and the final message. When a level change is gated, start from what the higher level removes: the events a human used to catch at the lower level are the ones the suite must now catch.
4. **Seed false success.** For each write tool, add tasks where the last write fails, times out or the lookup before it comes back empty. The trial passes only if the agent says it did not finish (or that the result is unknown), hands over, and does not blindly retry a write that timed out (the reconcile rule is `agent-design-and-tooling`'s): a hand-off is a pass, a confident "done" the worst outcome (references/eval-statistics.md §12). A run that ends "done" with an unchanged end state is labelled **false success** and counted apart: it is the failure nobody goes looking for.
5. **Fix trials and bars before the run.** Write down, dated and signed, the tasks, the trials per task k and the bar per task class before any trial runs (references/evals-as-evidence.md, rule 1). One trial per task measures luck. Reset the environment between trials. Report:
   - **pass@1**, the mean per-trial success rate, averaged per task then over tasks, with its interval (references/eval-statistics.md §2): the average quality.
   - **pass^k**, the share of tasks whose k trials all succeed (references/eval-statistics.md §8): the reliability users meet, because they meet every trial. With per-trial rate p, pass^k ≈ p^k: 0.90 per trial gives 0.73 over 3 trials.
   - **pass@k** (at least one success in k) only on the capability suite, where a human picks among attempts. Never gate an action that cannot be undone (payment, refund, deletion, external send) on pass@k or best-of-k: production gets every attempt, not the best one.
   - **Forbidden events and false successes**, as counts with their bound. Zero in n trials still allows a rate up to about 3/n (rule of three): zero in 30 allows 10%, zero in 300 allows 1%. Multiply the bound by the monthly volume to show the exposure the gate accepts: 1% of 9,000 refunds a month is up to 90 bad refunds. When trials of the same task tend to fail together, the effective n is nearer the number of tasks: give both bounds when the gate is tight.
   Compute them with `python3 scripts/agent_reliability.py --k <k> --events <e> --volume <monthly> c/n c/n …` (one c/n per task); `--pass-at-k 0.9 --k 3` shows what a pass@k figure hides.
6. **Keep two suites.** The capability suite holds hard tasks with a low pass rate: it shows progress and gates nothing. The regression suite holds tasks the agent already passes, must stay near 100% on pass^k, and runs on every change: prompt, tool description, model and the provider's model updates. A capability task that passes reliably moves to regression; every production failure becomes a regression task with its starting state (references/eval-statistics.md §14).
7. **Simulate the user only where needed.** For tasks that need a clarification (missing order number, ambiguous request), a second model plays the user from a persona, a goal and hidden information it gives only when asked. It makes its own mistakes: spot-check 10 to 20 simulated conversations by hand, and mark a trial the simulator broke as invalid, not as an agent failure. Where users state a request over several messages, also run tasks with the facts given one per turn and report the spread across repeated runs (worst run, share of tasks whose verdict changes), not only the mean: in multi-turn use most of the loss is unreliability, which a one-message suite never shows.
8. **Run the same tasks under attack** when the agent reads anything an outsider can write (inbound email, attachments, web pages, third-party API results). Plant instructions inside the tool outputs of real suite tasks, each aimed at one forbidden action (change the payee, send a file outside, update a contact). A pack of malicious messages with no legitimate request measures attack success, never utility. Report three numbers on the same tasks: benign utility (clean pass rate), utility under attack (the user's task done and the injected goal not reached) and attack success rate per forbidden action, with its upper bound (references/eval-statistics.md §2; zero in n still allows about 3/n). Gate on the upper bound, never on the point rate. Keep the attack test set apart from the attacks used to write or tune the prompt, filter or guardrail: a rate measured on the attacks a defence was tuned on proves nothing. Attacks and defences are written in `system-prompt-and-guardrails`; detail in references/agent-eval-method.md.
9. **Locate the break, starting with the failed runs you already have.** Before any new task or fix, take the failures in hand (a hand review, incidents, complaints), then every failed trial: label the first failing step (wrong tool, wrong argument, skipped read, result misread, failed write reported as done); later errors are often its consequences. Count them in a matrix of last successful step × first failing step, even for a handful of runs. The busiest cell says which seeds to write first and what to fix: a tool contract or protocol fix goes to `agent-design-and-tooling`, an attack path to `system-prompt-and-guardrails`.
10. **Track cost and latency per task.** Log steps, tool calls, tokens and time per trial. Report cost per successful task = cost of all trials ÷ successful trials, never ÷ all trials, and the 95th percentile of steps and latency. A version that passes more tasks with three times the steps is a trade-off the sponsor sees.
11. **Write the level gate.** For a level move, state: tasks and k, the pass^k bar per task class (strictest on actions that cannot be undone), zero forbidden events with the bound and the monthly exposure it implies, the false-success rate, the attack-success bound per forbidden action where outsiders write what the agent reads, and the other gate facts the target level requires in references/autonomy-ladder.md (shadow run, redteam, canary, rollback). Bars per class and the baseline follow `build-evals`. If the bound is too wide for the cost of one event, the answer is more trials or the current level, never a looser reading. Online monitoring after the move is `production-evals-monitoring`.

## Output
`templates/agent-eval-plan.md`, all headings present: environment, tasks, false-success seeds, simulated users, under attack, suites, trials and bars, metrics with intervals and bounds, where runs break, cost and latency, level gate, open questions. A section that cannot be filled says what is missing and who provides it.
When the brief brings failed runs, the answer labels each one's first failing step and shows them in the last-success × first-failure matrix, whatever its length.

## Rules and red lines
- Never grade or gate an agent on its final message alone: success is the end state, read in the system.
- Never gate an action that cannot be undone (payment, refund, deletion, external send) on pass@k or best-of-k: report the per-trial rate and pass^k.
- Never claim zero risk from zero observed failures: state the bound (about 3/n) and the monthly exposure it allows.
- Never run trials against production systems with real side effects: sandbox or test doubles, reset between trials.
- Tasks, k and bars are fixed before the run.
- One forbidden event fails the trial, whatever the final message says.
- Failed runs in hand are located at their first failing step, in the matrix, before any fix is proposed.
- Attack success is read per forbidden action on attacks kept apart from tuning, and gated on its upper bound.

## Links
references/autonomy-ladder.md · references/eval-statistics.md · references/evals-as-evidence.md · references/agent-eval-method.md · agent-design-and-tooling · build-evals · system-prompt-and-guardrails · production-evals-monitoring · release-to-production · assistant-kpis-cost-per-outcome

## Sources
- anthropic-agent-evals: tasks, trials, outcome and transcript graders; pass@k against pass^k; capability and regression suites.
- yao-tau-bench: pass^k as the reliability measure; grading on the database end state; a simulated user with hidden information.
- agentdojo: the same tasks run clean and with injected tool outputs, read as benign utility, utility under attack and attack success rate.
- laban-multi-turn: a task revealed over several turns loses mostly to unreliability across runs, so the spread is reported.
- anthropic-agents: agent errors compound, so agents are tested in sandboxed environments first.
- wilson-interval: the interval on pass@1 and the rule of three on zero observed failures.
- husain-shankar-evals: label the first failure upstream; the matrix of last success × first failure.
- repo-lenny: locating the breaking step of an agent run, as an idea.
- repo-chanmeng: false success seeded at the last step and the starting state kept as a fixture (ideas, own words).
- own-nanoagent: the per-step trace (tool, arguments, result, cost) that the break matrix and the cost per task read, from the author's raw agent loop.
