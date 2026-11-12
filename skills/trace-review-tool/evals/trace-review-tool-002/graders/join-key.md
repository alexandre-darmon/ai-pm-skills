---
type: regex  # a key that joins the trace to the loan outcome
flags: i
---
join[ _-]?key|(loan|application|credit|case|decision|outcome)[ _-]?(id|identifier|number|reference)\b|link\w*[^\n]{0,40}(business )?outcome
