---
type: regex  # the quality rate comes from the random stream only
flags: i
---
(rate|share|percentage|estimate|prevalence)[^\n]{0,120}\brandom|\brandom[^\n]{0,120}(rate|share|estimate|percentage|prevalence)
