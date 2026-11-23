---
type: regex  # scores on real and synthetic cases reported apart, with the synthetic share declared next to them
pattern: '(separately|separated|apart|split|side by side)[^\n]{0,160}(synthetic share|share of synthetic|proportion of synthetic|synthetic proportion|\d+\s?% synthetic|percentage of synthetic|how many (of the cases )?are synthetic|(share|proportion|percentage|fraction) of (the )?(cases|set|items|questions)[^\n]{0,30}synthetic)|(synthetic share|share of synthetic|proportion of synthetic|synthetic proportion|\d+\s?% synthetic|percentage of synthetic)[^\n]{0,160}(separately|separated|apart|split|side by side)'
flags: i
---
