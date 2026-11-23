---
type: regex  # the sample is sized to the 5-point drop that matters (about 300 or more), not just "score more"
pattern: '(?<![\d,.])\b(29\d|3\d\d|4\d\d|5\d\d)\b(?![,.]\d)[^\n]{0,120}((?<![\d,.])\b(5|five)[- ]?(points?|pts?|pp|percentage[- ]points?)\b|\b86\s?%?\s*(from|and|vs\.?|versus)\s*91\b|\b91\s?%?\s*(from|and|vs\.?|versus)\s*86\b)|(?<![\d,.])\b(5|five)[- ]?(points?|pts?|pp|percentage[- ]points?)\b[^\n]{0,120}(?<![\d,.])\b(29\d|3\d\d|4\d\d|5\d\d)\b(?![,.]\d)'
flags: i
---
