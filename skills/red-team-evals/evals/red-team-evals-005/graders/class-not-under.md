---
type: regex  # read per class on the interval: no class can be read as under its tolerance (undecided, or the lookup class over), with the per-attack Wilson bounds (0 of 100 about 3.7%, 0 of 70 about 5.2%, 2 of 80 up to about 8.7%)
pattern: 'undecided|inconclusive|straddl\w*|(interval|bound|range)[^.!?\n]{0,60}(spans?|includes?|contains?|crosses|covers?|above|over|exceeds?)[^.!?\n]{0,30}(toleran\w*|\b1 ?%|0[.,]5 ?%)|(cannot|can[''’]t|does not|doesn[''’]t|do not|don[''’]t|\bnot\b|\bnone\b|\bno class)[^.!?\n]{0,30}\b(show|shown|read|claim\w*|say|support\w*|demonstrat\w*|establish\w*|prove\w*|is|are)\b[^.!?\n]{0,50}\bunder (its |their |the |each |any )?(signed )?toleran|lower (bound|end|limit)(?:[^.!?\n]|\.(?=\d)){0,60}(above|over|exceeds?)|\bmay (already )?be (over|above)|\b(3[.,]7|5[.,]7|8[.,]7|5[.,]2|6[.,]7) ?%'
flags: i
weight: 2
---
