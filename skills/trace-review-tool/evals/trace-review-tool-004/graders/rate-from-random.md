---
type: regex  # the quality rate comes from the random stream only
flags: i
---
random[^\n]{0,120}\b(only|alone|solely)\b[^\n]{0,60}(rate|estimate|prevalence)|random[^\n]{0,80}\bthe only (stream|sample|part|draw|one)\b|(rate|estimate|prevalence)[^\n]{0,80}\b(only|alone|solely)\b[^\n]{0,40}random|(rate|estimate|prevalence)[^\n]{0,40}\bfrom (the )?random[^\n]{0,30}\b(only|alone)\b|\b(main|random|representative) (sample|stream|draw)s? only\b|\b(never|not|don.t)\b[^\n]{0,30}\b(enter|count toward|go into|feed|blend|mix)\w*[^\n]{0,25}\b(headline|quality rate|reported rate|the rate)
