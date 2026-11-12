---
type: regex  # names the user behaviours a simulator must reproduce
pattern: 'user corrections?|correct(s|ing)? (themselves|itself|a fact|an earlier|the assistant)|change[sd]? (their|his|her) (mind|story|answer)|corrections? (share|rate)|share[^\n.]{0,20}corrections?|vague|underspecified|incomplete (first )?(message|request|opening)|missing (detail|information|fact)s?|hidden (fact|detail|information)|reveal\w*[^\n.]{0,20}late|only when asked'
flags: i
---
