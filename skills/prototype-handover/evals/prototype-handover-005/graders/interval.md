---
type: regex  # Wilson interval on 221 of 250 (about 84% to 92%), and the baseline read per class with its own n and interval
pattern: '^(?=[\s\S]*?\b8[34](?:\.\d+)?\s?%?\s?(?:to|-|–|—|and|,|;)\s?9[12](?:\.\d+)?\b)[\s\S]*?(?:(?:per|each|every|by)[- ](?:risk )?(?:class|category)\b[^.\n]{0,80}\b(?:intervals?|n of N|k of n|\d+ of \d+)|\b(?:intervals?|k of n|n of N)\b[^\n]{0,60}\b(?:per|each|every|by)[- ](?:risk )?(?:class|category)|\b(?:rare|small|few)\b[^.\n]{0,60}\bwide\w* intervals?|lower bound)'
flags: i
---
