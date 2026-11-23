---
type: regex  # workers' representatives informed before use, with the duty's start date (2 December 2027) on the same line
pattern: '(\b26\s*\(7\)|workers[’'']? representatives|works council|employee representatives)[^\n]{0,200}\b(2\s+)?Dec(ember|\.)?\s+2027\b|\b(2\s+)?Dec(ember|\.)?\s+2027\b[^\n]{0,200}(\b26\s*\(7\)|workers[’'']? representatives|works council|employee representatives)'
flags: i
---
