---
type: regex  # the 9 wrong codings still cost accountant time: about 8.10 EUR on top of the API bill
pattern: '\b8[.,]10?\b|\b9 ?(×|x|\*|times) ?0[.,]90?\b|\b0[.,]9[45]\d*\b|\b39[.,]1\d*\b|\b0[.,]18 ?(×|x|\*) ?0[.,]90?\b|\b(9|nine) of 50\b[^\n]{0,80}\b(fix|rework|re-?cod|correct)\w*|(rework|re-?cod\w*|correct\w*|fix\w*)[^\n.]{0,60}\b(9|nine) (wrong|incorrect|miscoded|errors?|invoices)|\b(9|nine) (wrong|incorrect|miscoded)[^\n.]{0,60}(rework|accountant|cost|still)'
flags: i
---
