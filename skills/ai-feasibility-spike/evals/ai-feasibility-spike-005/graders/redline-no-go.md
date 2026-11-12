---
type: regex  # red line: over appetite means reshape or stop, not a go to PRD; the decision is anchored, a stray "reshape" or "no-go" does not count, nor a decision line that says go to PRD before it, nor a "reads as reshape/stop" with an un-negated, unconditional go to PRD on the same line
pattern: '\b(decision|decide|recommend\w*|verdict)\b(?:(?!\bgo (to|into) (the )?PRD)[^\n]){0,30}\b(reshape|stop|no[- ]go)\b|\breshape (it|the spike|into|as)\b|(?<!(?<!\b(if|unless|once|when)\b(?:[^\n.]|\.\d){0,150})(?<!\b(not|never|no(?![- ]go)|\w+n.t|you)\b[^\n.;:]{0,30})\b(go|move|proceed)\b[^\n.]{0,10}\b(to|into) (the )?PRD[^\n]*)\b(reads|counts|lands) as (an? )?\**(reshape|stop(?![- ]gap|s? sign)|no[- ]go)\b(?![^\n]*(?<!\b(if|unless|once|when)\b(?:[^\n.]|\.\d){0,150})(?<!\b(not|never|no(?![- ]go)|\w+n.t|you)\b[^\n.;:]{0,30})\b(go|move|proceed)\b[^\n.]{0,10}\b(to|into) (the )?PRD)|\b(not|never|cannot|can.t|isn.t|don.t|won.t)\b(?! an? no[- ]go)[^\n.]{0,30}\b(go|move|proceed|ready)\b'
flags: i
weight: 4
---
