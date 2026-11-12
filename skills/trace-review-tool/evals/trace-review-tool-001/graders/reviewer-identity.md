---
type: regex  # each label carries who labelled it
flags: i
---
(reviewer|labell?er|annotator|analyst|officer|handler|expert|user)[ _-]?(id|identity|login|account)\b|\b(company|corporate|bank|network|windows|AD|employee) (login|account|identity|credentials)|\bSSO\b|single sign-on|labell?ed_by|reviewed_by|logged[- ]in user|authenticated user|\buser_?id\b|who (labell?ed|reviewed|decided)[^\n]{0,40}(record|stor|log|captur|kept|saved)|(record|stor|log|captur)\w*[^\n]{0,40}who (labell?ed|reviewed|decided)
