---
type: regex  # the vendor may have tuned on its own benchmark or graded itself
pattern: '(tuned|trained|optimi[sz]ed|fit\w*|patched) (on|against|to) (its|their|that|this|the) (own |internal )?(benchmark|test|attacks?|prompts?|set)|(set|benchmark|prompts?|attacks?) (they|it|the vendor) (have |has |may have |probably |likely )?(tuned|trained|optimi[sz]ed|fit\w*|patched)|contaminat\w*|teach\w* to the test|own homework|conflict of interest|(marks?|grades?|grading|marking) (its|their) own|self[- ](graded|reported|assessed)|not independent\w*|\b(vendor|vendor[''’]s team|they|provider)\b[^.!?\n]{0,20}\b(may|might|could|probably|likely)\b[^.!?\n]{0,15}(tuned|trained|optimi[sz]ed|patched) (on|against) (them|those|these|it)\b|\b(whether|if)\b (the vendor|the provider|they|it|the model|their model) (has |had |have |was |were |has been |had been )?(tuned|trained|optimi[sz]ed|patched) (on|against) (them|those|these|it)\b|\b(were|was|been|being|are)\b[^.!?\n]{0,25}\b(tuned|trained|optimi[sz]ed|fitted)\b (on|against|to)\b|\b(benchmark|prompts?|attacks?|set)\b[^.!?\n]{0,40}\binformed (the )?(training|tuning)\b'
flags: i
weight: 2
---
