---
type: regex  # red line: component scores locate the failure; the release stays gated end to end
pattern: '(end[- ]to[- ]end|overall|full[- ]pipeline)[^.\n]{0,80}\b(gat(e|es|ed|ing)|decides?|release|ship|go/no-go|still|remains?|stays?)\b|\b(gate|release|ship)\w*[^.\n]{0,60}(end[- ]to[- ]end|full[- ]pipeline)'
flags: i
weight: 3
---
