---
type: regex  # sizes the residual-leak check: zero leaks in 200 bounds the rate at about 1.5%
flags: i
---
rule of three|3 ?/ ?(n|200)\b|\b1[.,]5 ?%|(all|every|each of the|the full) 200\b[^\n]{0,80}(leak|mask|residual)|(leak|residual)[^\n]{0,80}(all|every|each of the|the full) 200\b
