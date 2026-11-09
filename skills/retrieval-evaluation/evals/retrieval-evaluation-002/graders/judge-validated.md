---
type: regex  # any judge is validated against expert labels
pattern: 'calibrat|\bTPR\b|\bTNR\b|true (positive|negative) rate|sensitivity|specificity|(validat|check)\w*[^\n]{0,40}judge[^\n]{0,60}(expert|human|label)|judge[^\n]{0,80}(against|with) (expert|human|the procedure owners.?) (labels|grades|judg)'
flags: i
---
