---
type: regex  # client-data leakage: its own stricter tolerance, or its upper bound near 8%
pattern: '\b7[.,][5-9] ?%|\b0[.,]077\b|\b8 ?%|(stricter|tighter|lower|own|separate|specific) (tolerance|threshold|bar|limit)s?[^\n]{0,200}(client|portfolio|leak|data)|(client|portfolio|leak|data)[^\n]{0,200}(stricter|tighter|lower|own|separate|specific) (tolerance|threshold|bar|limit)'
flags: i
---
