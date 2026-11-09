---
name: ai-opportunity-assessment-002
description: 'Contract-clause extraction with scanned, unlabelled data (source - anonymised insurance brief, 2026)'
tags: [ai-opportunity-assessment, p1, nominal, red-line]
expected_outcome: 'Explore: data readiness below 2/5 blocks a go; a data task comes first.'
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Legal ops want to extract 30 clauses (termination, liability cap, renewal) from our supplier contracts. We have about 8,000 contracts: most are scanned PDFs from 2005-2018, some are photos of signed pages, around a third are missing annexes. Nobody has ever labelled a clause. Access needs approval from each business unit, which has taken months in the past.

Can an LLM do this for us?
