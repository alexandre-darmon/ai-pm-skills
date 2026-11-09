---
type: regex  # adoption read on correct outcomes, not logins
pattern: '(correct|accepted|usable|validated|right)\b[^\n]{0,40}\b(outcomes?|notes?|summaries|answers?|outputs?)\b[^\n]{0,40}\bper (active |weekly )?(user|adviser|advisor|person)\b|\b(logins?|log-ins?|sessions?|opens?|active users?)\b[^\n]{0,80}(\bnot\b|\bnever\b|n[’'']t\b)[^\n]{0,40}\b(adoption|proof|prove|evidence|enough|success)\b'
flags: i
---
