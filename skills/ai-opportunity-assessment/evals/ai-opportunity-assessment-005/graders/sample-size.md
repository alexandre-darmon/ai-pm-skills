---
type: regex  # the evidence plan sizes the sampled answers for the precision of the read (margin or interval bound), not just a round number
pattern: '\b\d{2,4}\+?\s+(?:[\w-]+\s+){0,3}?(questions|cases|answers|conversations|searches)\b[^\n]{0,120}(±|\+/-|plus or minus|within (about )?\d+ (points|pts|%)|(lower|upper) bound|confidence interval|95\s?% (interval|CI)|\bCI\b|Wilson|margin of error)|(±|\+/-|plus or minus|(lower|upper) bound|confidence interval|95\s?% (interval|CI)|\bCI\b|Wilson|margin of error)[^\n]{0,120}\b\d{2,4}\+?\s+(?:[\w-]+\s+){0,3}?(questions|cases|answers|conversations)\b'
flags: i
---
