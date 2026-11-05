---
type: regex  # monthly drift check on fresh labels
pattern: '(re-?measur|re-?check|re-?evaluat|drift)[\s\S]{0,80}?(month|fresh|new)[^\n]{0,30}(sample|batch|conversations)|(monthly|every month|each month)[^\n]{0,100}(fresh|new|re-?label|hand-label)|fresh (labell?ed )?sample[^\n]{0,60}(month|drift)'
flags: i
---
