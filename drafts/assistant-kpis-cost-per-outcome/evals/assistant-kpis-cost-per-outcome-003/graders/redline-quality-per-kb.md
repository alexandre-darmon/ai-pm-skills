---
type: regex  # red line: one quality line per KB, never only the blended 84%
pattern: '(^|\n)[ \t>*#|\-\d.]*\**(quality|accuracy|correct(ness)?|% correct)\**((?!\b(not|no|never|without|instead)\b|n[''’]t\b)[^\n]){0,80}\b(per|by|for each|each|for every|separately for)[- ](KBs?|knowledge[- ]bases?|bases?|domains?)\b|\|\s*(KB|knowledge[- ]base|base)\b[^|\n]*\|[^\n]*(quality|correct|accuracy)|\|\s*(quality|accuracy)\b[^\n]*\|\s*(KB|knowledge[- ]base)\b|(quality|accuracy|correct)((?!\b(not|no|never)\b|n[''’]t\b)[^\n]){0,80}\b(separately|split|broken down)\b[^\n]{0,40}\bHR\b[^\n]{0,40}\bIT\b'
flags: i
weight: 2
---
