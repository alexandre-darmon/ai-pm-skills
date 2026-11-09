---
type: regex
pattern: '(?:measur\w*|profil\w*|baseline)[^\n]{0,80}\b(?:unfiltered|uncleaned|uncurated|raw|as[- ]is|production|live|real)\b[^\n]{0,30}\b(?:sample|extract|data|rows?|snapshot|table|records)\b|\b(?:unfiltered|uncleaned|uncurated|raw|as[- ]is|production|live|real)\b[^\n]{0,30}\b(?:sample|extract|data|rows?|snapshot|table|records)\b[^\n]{0,80}(?:measur\w*|profil\w*|baseline)'
flags: i
---
