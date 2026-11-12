---
type: regex  # the judge itself is re-checked against experts on production traces (drift, re-check, or an expert/reviewer checking whether the judge is right on the failures)
pattern: '\bTPR\b|\bTNR\b|true (positive|negative) rate|judge[^\n]{0,100}\b(drift\w*|re-?check\w*|re-?label\w*|re-?validat\w*|re-?calibrat\w*)|\b(re-?label|re-?score|re-?grade|re-?check|re-?validat)\w*[^\n]{0,80}\bjudge|\b(experts?|reviewers?|humans?|adjusters?|handlers?)\b[^\n]{0,60}\b(whether|if|check|confirm|verify)\w*[^\n]{0,30}\bjudge\b[^\n]{0,20}\b(is |was |were )?(right|wrong|correct|mistaken|agrees?|agreed)\b'
flags: i
---
