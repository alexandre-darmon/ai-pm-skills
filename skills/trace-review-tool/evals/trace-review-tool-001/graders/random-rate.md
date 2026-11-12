---
type: regex  # the rate comes from the random stream only (table row or prose)
flags: i
---
random[^\n]{0,120}\b(only|alone|solely)\b[^\n]{0,60}(rate|estimate|prevalence)|random[^\n]{0,60}\bthe only (stream|sample|part|draw|one)\b|(rate|estimate|prevalence)[^\n]{0,80}\b(only|alone|solely)\b[^\n]{0,40}random|(rate|estimate|prevalence)[^\n]{0,40}\bfrom (the )?random[^\n]{0,30}\b(only|alone)\b
