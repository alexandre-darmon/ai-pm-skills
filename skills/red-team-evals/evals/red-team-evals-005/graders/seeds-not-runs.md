---
type: regex  # n is the attack (seed), not the run: the 5 runs of one attack are not independent; an attack counts as one success when any of its runs succeeds
pattern: 'best[- ]of[- ](5|k|five)|any of (its|the|their) (5|five) (runs|attempts|tries)|\bnot (2,?000|two thousand)\b|\b(runs|repeats|repetitions|re-?runs|attempts|samples)\b[^.!?\n]{0,60}(\bnot\b|n[''’]t\b|\bnever\b)[^.!?\n]{0,20}\b(independent|separate (trials|samples|tests|observations)|the unit|extra n|additional (evidence|samples|data))|(\bnot\b|n[''’]t\b) (\w+ ){0,3}independent[^.!?\n]{0,60}\b(runs|repeats|repetitions|attempts|samples|observations)|\b(runs|attempts|repeats)\b[^.!?\n]{0,60}correlated|correlated[^.!?\n]{0,60}\b(runs|attempts|repeats)\b|\bn ?= ?(70|80|100|150|240|400)\b|(denominator|unit)[^.!?\n]{0,60}\b(attacks?|seeds?)\b|\b(count|counted|counts|counting) (per|by|each|at the level of the) (attack|seed)|\bper[- ](attack|seed) (count|rate|basis|level)|independent (seeds|attack ideas)|(attack|seed) (counts|is counted|is scored) (as )?(one|a single) success'
flags: i
weight: 2
---
