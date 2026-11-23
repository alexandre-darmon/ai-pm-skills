---
type: regex  # managers go first and are trained and tested (calibration on real outputs) before their teams, not only briefed
pattern: 'managers?\b[^\n]{0,80}\b(calibration|tested|test)\b[^\n]{0,60}\b(before|first)\b|\b(calibration|tested|test)\b[^\n]{0,60}\bmanagers?\b[^\n]{0,30}\b(before|first)\b'
flags: i
---
