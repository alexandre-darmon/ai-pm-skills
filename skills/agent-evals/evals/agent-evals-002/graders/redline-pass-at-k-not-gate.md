---
type: regex  # red line: pass@k is refused as the gate for payments
pattern: '(?:^|[.!?\n])(?=[^.!?\n]*(pass@ ?(k|3)|at least once|best[- ]of|one (success )?(in|of) (3|three|k)))(?=[^.!?\n]*(\bnot\b|\bnever\b|n.t\b|\bcannot\b|\bwrong\b|misleading|\binstead\b|rather than|\bhides?\b|overstates?))(?=[^.!?\n]*(gate|payment|irreversible|undone|undo|approval|L4|reliab|go/no-go|decision))|pass@ ?(k|3)[^\n]{0,220}\b(wrong|misleading|not the right|not a)\b[^\n]{0,20}\b(metric|measure|gate|figure)\b[^\n]{0,40}(payment|irreversible|gate|approval)'
flags: i
weight: 3
---
