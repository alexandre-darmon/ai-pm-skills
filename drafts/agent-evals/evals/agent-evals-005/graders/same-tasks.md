---
type: regex  # attacks planted inside the real client tasks, run clean and attacked on the same tasks
pattern: 'benign utility|(plant|inject|embed|insert|hid|seed)\w*[^\n.]{0,60}\b(into|in|inside) (the |those |these |each of the |copies of the )?(300|real|legitimate|genuine|normal|benign|actual|anonymi[sz]ed)\b|\b(same|those|these) (300 )?(tasks|emails|cases|requests)[^\n.]{0,80}\b(clean|attacked|injected|poisoned|with and without)|\b(300|real|client) (client )?(emails|tasks|requests)[^\n.]{0,40}\b(clean|unattacked)\b[^\n.]{0,60}(attack|inject|planted|poison)|(clean|unattacked|benign) and (attacked|injected|poisoned)|with and without (an? |the )?(injection|attack|planted)'
flags: i
---
