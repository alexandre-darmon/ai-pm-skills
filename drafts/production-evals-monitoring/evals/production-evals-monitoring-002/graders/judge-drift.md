---
type: regex  # the judge itself is re-checked against experts on production traces
pattern: '\bTPR\b|\bTNR\b|true (positive|negative) rate|judge[^\n]{0,100}\b(drift\w*|re-?check\w*|re-?label\w*|re-?validat\w*|re-?calibrat\w*)|\b(re-?label|re-?score|re-?grade|re-?check|re-?validat)\w*[^\n]{0,80}\bjudge'
flags: i
---
