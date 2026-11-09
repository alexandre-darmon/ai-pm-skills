# Data requirements: <feature>

## Blockers
Ownerless sources, thresholds missed, fields without a lawful basis, mixed-sensitivity index. Each with who decides and by when.

# Part A: fields and flows

## Fields (source | field | step | volume | personal data? | lawful basis | owner)
One sentence per source: does it hold personal data?

## Data flows (field | prompt | retrieved context | logs and traces | eval set | vendor | training)
Each cell: no, or masked/clear and retention as a number.

## Quality thresholds (source | completeness | freshness | duplication | measured today)
Sample: <how drawn, size, date, nothing cleaned> or "not measured".

## Pseudonymisation plan (destination | what is masked | where the key lives)

## Lineage, refresh and retention

# Part B: documents retrieved (when the feature retrieves)

## Source register (source | owner | refresh | expiry | effective from-to | sensitivity | users allowed)

## Excluded or escalated sources

## Inclusion, exclusion and dated versions

## Segregation and access control at retrieval

## Chunk metadata

## No-source behaviour and uncovered question classes

## Labelled queries handed to build-evals and retrieval-evaluation

## Retirement path and monthly review

## Stale-answer and untraceable-claim KPIs
