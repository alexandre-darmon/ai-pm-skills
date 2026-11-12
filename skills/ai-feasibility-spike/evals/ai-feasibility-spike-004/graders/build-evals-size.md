---
type: regex  # what the real suite needs per class: sized for the margin to the bar, sampled from production (a count with an expected rate counts only after the class is named; "expected rate close to the bar" counts only with a size direction)
pattern: '\b([2-9]\d\d|1[34]\d)\b[^\n]{0,50}(cases|documents|per (class|type|document type)|each)|\b(margin|gap|distance)\b[^\n.]{0,60}(bar|threshold)|(sampl\w*|drawn)[^\n.]{0,50}(production|live|real)[^\n.]{0,25}(traffic|onboarding|files|flows?|documents|cases)|per (gated |each )?(category|class|type|document type)[^\n.]{0,60}\b(if|when|at|assuming) (you |we )?(an? |the )?expect\w*|\b(more|larger|bigger|\d{2,3})\b[^\n.]{0,40}\bexpected (rate|accuracy)\b[^\n.]{0,60}\b(closer|nearer|near|close) (to )?the (bar|threshold|target)|\b(categor(y|ies)|class(es)?|type|passport|registry)\w*\b[^\n]{0,120}?\b\d{2,3}\b (or more )?(cases|documents|complaints|emails)\b[^\n.]{0,30}\b(at|if|assuming) (you |we )?(an? |the )?expect\w*'
flags: i
---
