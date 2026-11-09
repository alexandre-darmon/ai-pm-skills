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

Exposure: <events a month the gate accepts>

## Where runs break
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
