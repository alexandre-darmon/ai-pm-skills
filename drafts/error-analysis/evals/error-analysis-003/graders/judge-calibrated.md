---
type: regex  # a judge per mode is checked against expert labels before scoring the 5,000
pattern: 'calibrat\w*|\bTPR\b|\bTNR\b|true[- ]positive|sensitivity|specificity|agree\w*[^\n]{0,40}(expert|human)(\x27s)?[- ]?(labels?)|(check|compar|validat|test|measur)\w*[^\n]{0,60}\bagainst (the |an? )?(domain )?(expert|human)(\x27s|’s)?[- ](labels?|coding|codes|notes|verdicts?|judge?ments?|reading)|\bexpert\b[^\n]{0,20}\blabel\w*[^\n]{0,60}\b(compare|agreement)'
flags: i
---
