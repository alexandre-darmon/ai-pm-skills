---
name: prototype-handover-005
description: 'In-house underwriting agent proposing risk class and premium loading, head of underwriting wants 40 users then autonomous simple files (source - anonymised life insurance brief, 2026)'
tags: [prototype-handover, p0, nominal]
expected_outcome: 'Places it at tier 3 now and tier 4 at the wanted autonomous level, proposes a rebuild, gives the baseline with its Wilson interval (about 84% to 92%), flags a possible provider role for an in-house system put into service for own use (art. 3(3), 3(11)) and a possible Annex III point 5(c) use for ai-act-classification, raises the health data question for the DPO, and never says approved or compliant.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our life insurance underwriting team asked me to speed up the review of medical questionnaires. With a coding agent I built an agent that reads the applicant's questionnaire and the attached medical reports, proposes a risk class and a premium loading, and writes its rationale. An underwriter reviews every proposal before it goes out.

We built it in-house on a general-purpose model called through an API, and tested it on 250 anonymised past files with two senior underwriters: it matched their decision on 221.

The head of underwriting wants to put it in front of all 40 underwriters in Q1, and later let it issue standard-class decisions on its own for simple files. Write the handover.
