---
type: regex  # a random stream plus targeted signals, never only failures (the two streams may sit on two bullet lines)
pattern: 'random[^\n]{0,200}(thumbs|escalat|complain|abandon|low[- ]confidence|long|targeted|flagged)|(thumbs|escalat|complain|abandon|targeted|flagged)[^\n]{0,200}random|random (sample|stream|draw|set)[\s\S]{0,400}targeted (sample|stream|draw|set)'
flags: i
---
