---
type: regex  # art. 50(1) listed with its start date, 2 August 2026, on the same line
pattern: '(\bart(icle|\.)?s?\s*50\b|\b50\s*\(1\))[^\n]{0,160}\b((2\s+)?Aug(ust|\.)?\s+2026|August 2,? 2026|2026-08-02)\b|\b((2\s+)?Aug(ust|\.)?\s+2026|August 2,? 2026)\b[^\n]{0,100}(\bart(icle|\.)?s?\s*50\b|\b50\s*\(1\))'
flags: i
---
