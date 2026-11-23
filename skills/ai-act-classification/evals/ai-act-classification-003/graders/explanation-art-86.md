---
type: regex  # art. 86, the right to an explanation, with its start date given or sent to counsel as an open point
pattern: '(\bart(icle)?s?\.?\s*([\d–-]+\s*(,|and|&)\s*)*86\b|\|\s*86\s*\|)(?![^;\n]{0,30}\b(not|n[''’]t|never)\b)[^\n]{0,80}(counsel|to confirm|open point|\b20\d\d\b)|\bwhen\b[^\n]{0,30}\barts?\.?\s*([\d–-]+\s*(,|and|&)\s*)*86\b[^\n]{0,20}\b(appl|bite|start|take effect)'
flags: i
---
