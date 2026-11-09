---
type: regex  # red line: the raw judge rate is corrected, (0.85 + 0.80 - 1) / (0.92 + 0.80 - 1) = 90.3%
pattern: '(?<![\d.])(90(\.[0-4]\d*)?|89\.[5-9]\d*) ?(%|per ?cent)|(?<![\d.])0\.90\d*\b|(?<![\d.])0\.89[5-9]\d*\b'
flags: i
weight: 2
---
