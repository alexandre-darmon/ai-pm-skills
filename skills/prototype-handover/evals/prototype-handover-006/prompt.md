---
name: prototype-handover-006
description: Release plan for a new prompt version of a triage service engineering already rebuilt and runs (source - anonymised insurance claims brief, 2026)
tags: [prototype-handover, negative]
expected_outcome: Plans the release without loading prototype-handover; the change is already built by engineering, so it belongs to release-to-production.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Engineering rebuilt our motor claims email triage last quarter and it is live for 90 handlers, about 4,000 emails a week. They now have a new prompt version that scores two points higher on our 400-case suite.

How should we roll it out: shadow run, canary, A/B test?
