---
type: regex  # reports unreliability across repeated runs, not only the mean
pattern: '(across|between|over) (the )?(repeated |several |multiple |\d+ |k )?(runs|trials|repetitions|seeds)|worst[- ](case )?run|run[- ]to[- ]run|(verdicts?|answers?|recommendations?|outcomes?|results?)[^\n.]{0,30}(change|flip|differ|vary)\w*[^\n.]{0,30}(between|across|from one) (repeated )?(runs?|trials?)|(repeat|rerun|re-run|run)\w*[^\n.]{0,40}\b(\d|k|three|five|several)\b[^\n.]{0,20}(times|runs)[^\n.]{0,60}(spread|varian|unreliab|consisten|worst)'
flags: i
---
