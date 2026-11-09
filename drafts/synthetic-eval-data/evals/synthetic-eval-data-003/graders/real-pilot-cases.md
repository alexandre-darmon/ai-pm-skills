---
type: regex  # masked pilot conversations sampled into the set
pattern: '(sample|pull|take|draw|add|bring)\w*[^\n]{0,60}(real|pilot|production)[^\n]{0,40}(conversations|questions|messages|cases)|(mask|pseudonymi|anonymi|redact)\w*[^\n]{0,80}(pilot|real|conversations|messages)'
flags: i
---
