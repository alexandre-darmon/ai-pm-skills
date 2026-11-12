---
type: regex  # red line: the summary never recommends moving to the PRD on this spike (only a negation that directly governs the recommend or the go verb exempts it: "reshape, not go to PRD"); nor declares the go ("so we go to the PRD") unless negated, conditional ("if the re-run clears the ceiling, we go to PRD") or restating the user's ask
pattern: '(?<!\b(not|n.t|never) )(?<!\b(not|n.t|never) \w+ )\b(recommend\w*|propose\w*)\b[^\n.]{0,40}(?<!(\bnot|\bnever|n.t) (yet )?)\b(go|move|proceed)\b[^\n.]{0,15}\b(to|into) (the )?PRD|(?<!\b(if|unless|once|when)\b(?:[^\n.]|\.\d){0,150})(?<!\b(not|never|no(?![- ]go)|\w+n.t|you)\b[^\n.;:]{0,30})\b(we|I|let.s|so)\b(?:(?!\b(not|never|\w+n.t)\b)[^\n.]){0,20}\b(go|move|proceed)\b[^\n.]{0,10}\b(to|into) (the )?PRD'
flags: i
match: not_contains
weight: 4
---
