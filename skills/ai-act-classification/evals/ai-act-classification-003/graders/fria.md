---
type: regex  # fundamental rights impact assessment for Annex III 5(b), timed: before first use or from 2 December 2027
pattern: '(\bart(icle|\.)?s?\s*27\b|\|\s*27\s*\||fundamental[- ]rights impact|\bFRIA\b)(?![^\n]{0,80}((?<!\bnot )only (applies |required |needed )?(to|for) public|\bnot (required|needed|applicable)|\b(do|does)(n[''’]t| not) apply))[^\n]{0,200}(before (its |the )?first use|before (go(ing)?[- ]live|deploy\w*|launch\w*|(it is )?put into (use|service))|\b(2\s+)?Dec(ember|\.)?\s+2027\b)|(before (its |the )?first use|before (go(ing)?[- ]live|deploy\w*|launch\w*))[^\n]{0,100}(\bart(icle|\.)?s?\s*27\b|fundamental[- ]rights impact|\bFRIA\b)'
flags: i
---
