---
type: regex  # red line: the open "few weeks" becomes a time box in days (or one week) before anything is built
pattern: '(time[- ]?box|appetite|limit|cap)[^\n]{0,60}\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b[^\n]{0,15}(working )?days?\b|\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten)[- ](working[- ])?days?\b[^\n]{0,60}(time[- ]?box|appetite|maximum|max|cap|not (a few )?weeks)|(time[- ]?box|appetite|limit|cap)[^\n]{0,40}\b(one|1|a|single)[- ]week\b|\b(one|1|a|single)[- ]week\b[^\n]{0,40}(time[- ]?box|appetite|cap|kill date)'
flags: i
weight: 3
---
