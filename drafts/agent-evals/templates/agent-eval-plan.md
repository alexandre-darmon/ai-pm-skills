# Agent eval plan — <agent>, step <step>

Level: <current> → <target> (references/autonomy-ladder.md)
Tools: <tool | side effect | can it be undone?>

## Environment
<Sandbox or test double per system written to; how the starting state is loaded; reset between trials; outbound channels captured.>

## Tasks
| Task | Instruction | Starting state (fixture) | End-state check | Trajectory checks, where required | Forbidden events | Class | Trials k |
| --- | --- | --- | --- | --- | --- | --- | --- |

## False-success seeds
| Task | Tool | Seeded failure (error, timeout, empty result) | Pass means |
| --- | --- | --- | --- |

## Simulated users
<Tasks that need one: persona, goal, hidden information, stop rule; spot-check size; rule for invalid trials. Or "none".>
<Requests given over several turns: tasks run with one fact per turn; mean, worst run and spread across runs. Or "single-message use only".>

## Under attack
<Content an outsider can write that the agent reads, or "none: not applicable".>
Attack test set: <n attacks, written by whom> · never used to tune <prompt, filter, guardrail> · dev set: <where>

| Forbidden action | Planted in (tool output) | Attacked trials n | Attacks that succeeded | Rate | Upper bound (95%) | Exposure a month (assumption) |
| --- | --- | --- | --- | --- | --- | --- |

Benign utility: <clean pass rate, interval> · Utility under attack: <same tasks attacked, interval>

## Suites
| Suite | Tasks | Expected pass rate | Runs on | Gates |
| --- | --- | --- | --- | --- |
| Capability | | | | |
| Regression | | | | |

## Trials and bars
Tasks: <n> · trials per task k: <k> · set on <date> · signed by <who>

| Task class | Can be undone? | Metric gated | Bar | Who may relax |
| --- | --- | --- | --- | --- |

## Metrics
| Metric | Result | n | Interval or bound |
| --- | --- | --- | --- |
| pass@1 | | | |
| pass^k | | | |
| Forbidden events | | | |
| False successes | | | |
| Attack success, per forbidden action | | | |

Exposure: <events a month the gate accepts>

## Where runs break
<Failed runs in hand first (hand review, incidents), then failed trials: first failing step of each.>

| Last successful step ↓ / first failing step → | | | |
| --- | --- | --- | --- |

<Busiest cell, the fix, its owner.>

## Cost and latency
| Measure | Value |
| --- | --- |
| Cost per successful task | |
| Steps, tool calls, tokens per trial (median, p95) | |
| Latency (median, p95) | |

## Level gate
<Gate facts the target level requires, each with its measured value or "missing"; decision owner; decision.>

## Open questions
| Question | Owner |
| --- | --- |
