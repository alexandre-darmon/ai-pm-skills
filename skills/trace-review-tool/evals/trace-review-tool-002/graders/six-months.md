---
type: regex  # the six-month floor with its qualifier: unless other law, in particular data protection law, provides otherwise
flags: i
---
(six|6)[ -]months?[^\n]{0,300}(data[- ]protection|GDPR)[^\n]{0,60}(provides?|says?|requires?|sets?) otherwise|(six|6)[ -]months?[^\n]{0,250}\b(unless|except\w*)\b[^\n]{0,80}(data[- ]protection|GDPR)
