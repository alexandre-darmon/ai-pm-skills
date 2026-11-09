---
type: regex  # the 88% bar is read against the interval: neither shown missed nor met
pattern: '88 ?%[^\n]{0,150}\b(inside|within|in)\b (the |its |this |that )?(\d+ ?% )?(interval|range|CI|confidence)|(interval|range|CI)\b[^\n]{0,100}\b(includes?|contains?|spans?|straddles?|covers?|overlaps?)\b[^\n]{0,30}88|(cannot|can[’'']?t|can not|does not|doesn[’'']?t|do not|don[’'']?t)\s+(\w+\s+){0,4}?(say|conclude|tell|claim|show|establish|prove|demonstrate)\w*[^\n]{0,80}(below|under|above|breach|miss)\w*|neither (met|demonstrated|shown|proven)|not (demonstrably|significantly|clearly|statistically) (below|under|above)|inconclusive|not (yet )?(proven|demonstrated|shown) (either way|in either direction)'
flags: i
---
