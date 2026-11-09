---
type: regex  # leave and expenses are classes of different risk: one threshold each
pattern: 'thresholds?\b[^.;]{0,25}\b(per|for each|for every|by)[- ](question[- ])?(class|type|category|kind|topic)|\b(per|each)[- ](question[- ])?(class|type|category|kind|topic)[- ]thresholds?|class[- ](level|specific) thresholds?|(separate|distinct|different) thresholds? (for|per|by)|\bper[- ](question[- ])?class (gates?|bars?)\b'
flags: i
---
