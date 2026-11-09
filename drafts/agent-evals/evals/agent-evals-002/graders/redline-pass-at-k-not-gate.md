---
type: regex  # red line: pass@k is refused as the gate for payments
pattern: '(?:^|[.!?\n])(?=[^.!?\n]*(pass@ ?(k|3)|at least once|best[- ]of|one (success )?(in|of) (3|three|k)))(?=[^.!?\n]*(\bnot\b|\bnever\b|n.t\b|\bcannot\b|\bwrong\b|misleading|\binstead\b|rather than|\bhides?\b|overstates?))(?=[^.!?\n]*(gate|payment|irreversible|undone|undo|approval|L4|reliab|go/no-go|decision))'
flags: i
weight: 3
---
