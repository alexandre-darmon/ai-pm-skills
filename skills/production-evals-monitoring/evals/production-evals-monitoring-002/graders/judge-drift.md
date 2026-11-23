---
type: regex  # an expert re-checks the judge on the failing traces (or its TPR/TNR is re-measured), not only a re-score of old weeks
pattern: '\bTPR\b|\bTNR\b|\b(experts?|reviewers?|humans?|adjusters?|handlers?|specialists?|yourself)\b[^\n]{0,80}(\b(fail(ing|ed|ures?)?|flagged)\b[^\n]{0,20}\b(traces?|conversations?|transcripts?|answers?|cases?)\b|\bjudge[’'']?s (failures|fails|fail verdicts))|\b(fail(ing|ed)|flagged)\s+(traces?|conversations?|transcripts?|answers?)\b[^\n]{0,80}\b(experts?|reviewers?|humans?|adjusters?|handlers?|specialists?)\b'
flags: i
---
