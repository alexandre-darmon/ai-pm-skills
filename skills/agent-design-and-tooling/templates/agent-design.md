# Agent design: <agent>

Trigger: <request | batch | event | schedule>
Done: <state of the world that proves success>
Exits: <success | error | escalation | paused for approval | policy denied | budget exhausted, and what follows each>
Loop type: <single step | plan-execute | multi-agent, with justification>

## Tools (name | schema | side effect | reversible? | use over nearest neighbour when | returns on no result | returns on failed call)
## Permission matrix (tool | level | data scope, from session or case | approval, by whom | cap: given, or proposed and marked as an assumption | rule until the owner confirms it)
## Write protocol (from L3: tool | prepare and commit | approval bound to, expiry | cap checked on | idempotency key | on timeout), or "none: no write tool at L3 or above"
## Stop conditions
## Memory policy
## Trace schema (personal data redacted, with outcome field)
## Prototype check (tasks run | tools misused or looping | fixes to names, descriptions, response sizes), or "not yet run"
## Framework (only for a named need: need and candidate, or none)
