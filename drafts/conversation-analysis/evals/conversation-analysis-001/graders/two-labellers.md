---
type: regex  # human agreement measured on a shared subset
pattern: '(both|two) (labell?ers|annotators|HR assistants)[^\n]{0,100}(same|overlap|agreement|double|50|subset)|double[- ]label|inter[- ](annotator|rater|labell?er)[^\n]{0,80}(same|shared|overlap|\d+ conversations|subset|kappa)|(same|shared|overlapping) (\d+|subset|set|sample)[^\n]{0,60}(conversations|agreement|kappa)|(labell?er|annotator|human) agreement[^\n]{0,80}(same|shared|overlap|\d+|subset|ceiling)'
flags: i
---
