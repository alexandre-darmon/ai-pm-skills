# System prompt and guardrails: <feature>

## System prompt (role, scope, refusal policy, format)
## Input guardrails (mechanism | latency | cost | failure action)
## Output guardrails (mechanism | latency | cost | failure action)
## Action guardrails (tool | scope | caps | approvals | enforcement point | on failure)
## Three-leg check (answer per leg, then leg broken or level lowered)
## Level allowed per step and why
## Redteam set (≥ 20 injections, ≥ 5 of them indirect if it reads content, ≥ 10 out-of-scope, ≥ 5 action-limit, never fewer than the last run; held-out part; pass criteria set before the run)
## False-positive budget and tuning plan
## Human oversight (who can stop it; log redaction, access, retention)
## Assumptions to confirm (figure or rule | owner)
