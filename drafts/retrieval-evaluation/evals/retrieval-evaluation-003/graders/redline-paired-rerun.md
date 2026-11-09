---
type: regex  # red line: re-run old and new on the same questions
pattern: 'paired|same (\d+ )?(questions|queries|test set|set)[^\n]{0,80}(both|old and new|current and new|two (models|indexes|versions))|(both|old and new|current and new|two) (models|indexes|indices|versions|embeddings)[^\n]{0,80}same (\d+ )?(questions|queries|set)|side[- ]by[- ]side'
flags: i
weight: 3
---
