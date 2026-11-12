# Release plan: <version>

## Version bundle (what changed | pinned prompt, model snapshot, parameters, tools, KB snapshot)
## Autonomy level (level per step | gate facts if raised or above L2)
## Acceptance of the build (engineering rebuild only | pre-declared scenarios and frozen suite per class | handover baseline as the floor | failing cases sent back)
## Offline gate result
## Shadow (duration | comparison metric)
## Canary (share | guardrails | rollback triggers)
## Rollback (to which bundle | how long | who | data and actions written meanwhile | last rehearsal)
## A/B feasibility (n per arm | eligible units | verdict)
## Decision
Decision: release | hold | release after shadow. Owner, post-release review date.
