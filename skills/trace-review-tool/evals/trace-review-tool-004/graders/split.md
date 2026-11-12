---
type: regex  # dev and test split so later judge calibration is honest
flags: i
---
\bdev\b[^\n]{0,40}\btest\b|development[^\n]{0,20}test (set|split)|held[- ]out|test (set|split)
