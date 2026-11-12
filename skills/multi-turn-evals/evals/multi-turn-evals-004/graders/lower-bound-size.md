---
type: regex  # sees that about 140 scenarios at 92% cannot clear a 90% bar on the lower bound (about 830 needed, or move the bar, or stay)
pattern: '\b(7\d\d|8\d\d|9[0-4]\d)\b[^\n]{0,40}(scenarios|conversations|cases)|lower (bound|limit|end)[^\n.]{0,80}\b8[5-7]([.,]\d)? ?%|\b8[5-7]([.,]\d)? ?%[^\n.]{0,80}lower (bound|limit|end)|(?=[^.!?\n]*lower (bound|limit|end))[^.!?\n]*\b(cannot|can.t|won.t|will not|would not|never|unlikely to|too (small|few))\b[^.!?\n]{0,60}(clear|pass|reach|exceed|above|90)'
flags: i
weight: 2
---
