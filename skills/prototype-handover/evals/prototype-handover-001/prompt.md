---
name: prototype-handover-001
description: 'Motor claims email triage app built by a PM, engineering offers to take it over (source - anonymised insurance claims brief, 2026)'
tags: [prototype-handover, p0, nominal]
expected_outcome: 'Places it at tier 3 (business-critical, complaints and fraud signals touch customer outcomes) and proposes a rebuild by engineering against the suite and a frozen baseline with its Wilson interval (about 88% to 93%) per category, marks the judge as not validated without TPR and TNR, puts prompts and model version under change control, lists row-level access and secrets to rebuild, drafts the ICT asset entry with questions for IT risk, and never says approved.'
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

I built a triage tool for our motor claims inbox with a coding agent over three weeks. It reads each incoming claim email, puts it in one of six categories (new claim, document sent, complaint, payment chase, fraud signal, other) and drafts the acknowledgement; a handler reviews and sends it. I tested it on 400 anonymised emails from last year: 364 were put in the right category. An LLM judge rated 88% of the drafts as good.

It runs as a Python app on a VM in our innovation sandbox. The API key sits in a config file, the prompts are in the code, and anyone with the link sees every email loaded. So far it has only run on the 400 anonymised emails; twelve handlers tried it in demo sessions and want it. The claims director wants it for all 90 handlers by January, and engineering says they can take it over.

What should we hand over, and what happens to the tool now?
