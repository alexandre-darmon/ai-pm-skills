# Failure modes — <feature>, taxonomy v<n>, <date>

Feature version read: <model, prompt version, KB version>. Spec it runs on: <system prompt or PRD, version>.

## Sampling plan
| Stream | Selection rule | Traces | Period | Classes covered |
| --- | --- | --- | --- | --- |
| random | | | | |
| targeted: <signal> | | | | |

Monthly volume: <n traces / month, source>.
Masking: <method, placeholders, checked on n traces by whom>. Raw text stays in <source system>.
Reader: <name and role, the person who owns quality for this domain>. Second reader: <name, n traces, kappa per mode> or none.

## Reading log summary
| Stream | Traces read | Traces with a failure |
| --- | --- | --- |
| random | | |
| targeted | | |

Last new mode found at trace <k>. Traces read since: <m>. Saturation: <reached / not reached>. Taxonomy status: <provisional / stable>.

Taxonomy versions:
| Version | Date | Change | Notes re-checked |
| --- | --- | --- | --- |

## Failure modes
| # | Mode | Definition (fails when…) | Pass example | Fail example | Count | Share of random [95% interval] | Classes affected | Cost per occurrence (source) | Expected monthly cost | Priority | Action (fix / evaluate / accept) and why | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Modes with legal, privacy, financial or irreversible effects: <list; question for counsel>.

## Steps where runs break (agents and pipelines only)
| Last step that succeeded ↓ / first step that failed → | <step 1> | <step 2> | <step 3> |
| --- | --- | --- | --- |
| <step 1> | | | |

## Decisions
- Fix now: <mode, fix, owner, date; failing traces kept as regression cases>.
- Evaluate: <mode, evaluator, owner>.
- Accept: <mode, rationale, owner, re-check date>.

## Handovers
| To | What | Owner |
| --- | --- | --- |
| `build-evals` | | |
| `llm-judge-calibration` | | |
| `synthetic-eval-data` | | |
| `agent-evals` | | |
| `system-prompt-and-guardrails` / KB owner | | |

## Next run
Triggers: <model, prompt, KB or provider change; complaint spike>. Cadence: <monthly / quarterly>, on <n> fresh production traces.

## Open questions
| Question | Owner | Due |
| --- | --- | --- |
