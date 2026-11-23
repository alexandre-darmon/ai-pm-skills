---
type: regex  # the interval on 82% of 200 (about 76% to 87%) carried into the gain as its low and high quality values, not only quoted
pattern: '\b(low|conservative|pessimistic|worst)\b[^\n]{0,60}\b7[67](?:[.,]\d+)?\s?%|\b7[67](?:[.,]\d+)?\s?%(?!\s*(to|–|-|and)\s*8)[^\n]{0,80}\d[\d,.]*\s?(h|hours|EUR|€|k|M)\b|\|\s*7[67](?:[.,]\d+)?\s?%\s*\|\s*8[678](?:[.,]\d+)?\s?%\s*\|'
flags: i
---
