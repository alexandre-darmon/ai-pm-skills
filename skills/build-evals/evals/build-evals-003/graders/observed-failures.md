---
type: regex  # outputs exist here, so graders come from reading them and grouping what went wrong
pattern: 'error analysis|failure taxonomy|\b(read|review|inspect|go through|look at|sample|annotate)[^\n.]{0,80}(outputs?|answers?|traces?|transcripts?|conversations?|failures?|failed cases|responses)[^\n]{0,200}(cluster|group|categori[sz]e|taxonomy|failure (modes?|types?|categor)|error (types?|categor)|recurring)|(cluster|group|categori[sz]e)[^\n.]{0,50}(failures|errors|failed|what went wrong)'
flags: i
---
