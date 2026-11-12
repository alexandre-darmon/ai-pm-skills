---
type: regex  # trials and bars fixed before the run
pattern: '(k|trials|runs|tasks|bars?|thresholds?)\b[^\n]{0,80}\b(fixed|set|decided|chosen|written|declared|signed|pre-?registered)\b[^\n]{0,40}\b(before|ahead of|prior to|in advance|up ?front)\b|\b(before|ahead of|prior to)\b (any|the first|the) (trial|run|results?)'
flags: i
---
