---
type: regex  # the swap is gated like a release with a stated decision rule on the paired re-run: count the questions where exactly one version hits (d); a gap under 2√d ÷ n is a tie, not a win
pattern: '2 ?(√|sqrt|\\sqrt|×? ?root)|\b(exactly|only) one (of the )?(model|index|indexe?s|version|system)s?\b[^\n]{0,30}\b(hits?|finds?|retrieves?|gets?|returns?|is right|succeeds?)|\bdiscordant\b|mcnemar|\b(sign|binomial|exact) test\b'
flags: i
---
