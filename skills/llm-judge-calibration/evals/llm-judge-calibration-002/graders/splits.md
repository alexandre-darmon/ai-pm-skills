---
type: regex  # the labels used to write or tune the prompt are named as tuning/dev data (or split into few-shot, dev and test), not a test of the judge
pattern: '\bdev(elopment)?\b[^\n]{0,120}\btest\b|\btest\b[^\n]{0,120}\bdev(elopment)?\b|(few[- ]shot|example)s?\s+(pool|split)|\bvalidation (set|split)\b[^\n]{0,120}\btest\b|\btest\b[^\n]{0,120}\bvalidation (set|split)\b|\b(tun(ed|ing)|dev(elopment)?)[- ](data|set|split|labels|figures?)\b|\bdescrib\w* (only )?(the )?tuning\b|\b(data|labels|set|summaries) (you|we) (tuned|iterated|fitted)\b|\btuned on the (test set|same)\b|\b(fitted|fitting|fit) (to|on) (them|those|these)\b|\b(measured|scored) on (the )?(data|labels|summaries) used to (build|tune|write)'
flags: i
---
