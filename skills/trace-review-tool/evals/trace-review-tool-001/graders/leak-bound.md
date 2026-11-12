---
type: regex  # sizes the residual-leak check: zero leaks in n bounds the rate at about 3/n, 1% for 300
flags: i
---
rule of three|3 ?/ ?(n|300)\b|\b1 ?%[^\n]{0,80}leak|leak[^\n]{0,120}\b1 ?%|(all|every|each of the|the full) 300\b[^\n]{0,80}(leak|mask|residual)|(leak|residual)[^\n]{0,80}(all|every|each of the|the full) 300\b
