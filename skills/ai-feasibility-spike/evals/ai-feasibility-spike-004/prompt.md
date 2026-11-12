---
name: ai-feasibility-spike-004
description: KYC extraction spike where both classes sit at or above the 90% bar on their point estimate, 28 of 30 and 9 of 10, and the PM wants the go note (source - anonymised private bank onboarding brief, 2026)
tags: [ai-feasibility-spike, p1, edge-case]
expected_outcome: Reads each class with its Wilson interval (passports about 79% to 98%, registry extracts about 60% to 98%), says neither demonstrates 90% and that 9 of 10 falls under the 75% stop line at its lower bound, so registry extracts are undecided; goes to PRD for passports only with the class flagged as not demonstrated, reshapes registry extracts (more cases under a new appetite, or out of scope), and names the size build-evals needs.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our onboarding team spends 20 minutes per new corporate client keying data from two kinds of documents: the directors' passports and the company registry extract. We ran a one-week spike on the approved model to see if it can extract the fields.

Before the run, our head of onboarding signed a 90% bar per document type (all fields correct), and a 75% line under which we would drop the idea. We used anonymised documents from our test environment.

Results: passports 28 of 30 correct (93%), registry extracts 9 of 10 correct (90%). Model cost was 0.03 EUR per document, well under our ceiling.

Both document types meet the 90% bar. Write the go note for Thursday's steering committee so we can move on to the PRD.
