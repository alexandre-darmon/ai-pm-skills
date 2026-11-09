---
type: regex  # masked pilot conversations sampled into the set
pattern: '(sample|pull|take|draw|add|bring)\w*[^\n]{0,60}(real|pilot|production)[^\n]{0,40}(conversations|questions|messages|cases)|(mask|pseudonymi|anonymi|redact)\w*[^\n]{0,80}(pilot|real|conversations|messages)|(conversations|messages)[^\n]{0,10}(mask|pseudonymi|anonymi|redact|scrub)\w*|build\w*[^\n]{0,40}(real|pilot)[^\n]{0,30}(conversations|traffic|messages)'
flags: i
---
