---
name: conversation-analysis-005
description: Quarterly classification of an IT helpdesk assistant shows one high-volume use case that mostly ends unresolved (source - synthetic scenario written for the skills review, 2026)
tags: [conversation-analysis, p1, nominal]
expected_outcome: Treats the high-volume unresolved use case as a finding, pulls a masked sample of it and hands those conversations over as candidate cases for the eval set, without redoing the classification or grading the answers itself.
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

We classified last quarter's 40,000 conversations of our IT helpdesk assistant by use case and resolution. The text is masked and human agreement is good on both dimensions.

The top of the table: "VPN setup" is 22% of the volume and 46% of those conversations end unresolved. Every other use case is below 15% unresolved.

We present this next week. Beyond showing the table, what should we do with this result?
