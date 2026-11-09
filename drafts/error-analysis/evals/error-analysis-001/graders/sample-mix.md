---
type: regex  # a random stream plus targeted signals, never only failures
pattern: 'random[^\n]{0,200}(thumbs|escalat|complain|abandon|low[- ]confidence|long|targeted|flagged)|(thumbs|escalat|complain|abandon|targeted|flagged)[^\n]{0,200}random'
flags: i
---
