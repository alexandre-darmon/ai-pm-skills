---
type: regex
pattern: '(?:\bagents?\b[^\n]{0,40}\b(?:no|not|unnecessary|overkill|unjustified)\b|\b(?:no|not an?) agents?\b)[^\n]{0,120}\b(?:workflow|single [\w -]{0,20}call|fixed|drawn in advance|no (?:actions?|branch\w*))\b|\b(?:workflow|single [\w -]{0,20}call|fixed|drawn in advance|no (?:actions?|branch\w*))\b[^\n]{0,120}\b(?:no|not an?|rather than an?|instead of an?) agents?\b'
flags: i
---
