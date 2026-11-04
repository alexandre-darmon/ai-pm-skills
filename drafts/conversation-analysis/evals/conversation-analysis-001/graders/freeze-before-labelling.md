---
type: regex  # freeze, then label
pattern: '(freez|frozen|lock)[^\n]{0,100}(before|prior to|until)[^\n]{0,60}(label|annotat)|(before|prior to) (any |the )?(labell?ing|annotat)[^\n]{0,100}(freez|frozen|lock)|(label|annotat)[^\n]{0,80}(before|until|once)[^\n]{0,60}(freez|frozen|lock)|frozen version|(freeze|lock) (it|the (list|taxonomy|classes))\b|(change|edit)s?[^\n]{0,40}after labell?ing (begins|starts|has started)[^\n]{0,60}relabel'
flags: i
---
