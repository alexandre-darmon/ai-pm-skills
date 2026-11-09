---
type: regex  # red line: expected answers from experts or procedures, not the model under test
pattern: '(expected|gold|reference|correct) (answers?|outputs?|labels?)[^\n]{0,150}(experts?|claims handlers?|specialists?|adjusters?|from the procedures|(written|validated|checked|reviewed|approved|signed off) by)|(experts?|claims handlers?|adjusters?)[^\n]{0,80}(write|writes|approve|validate)[^\n]{0,40}(expected|gold|reference) answers?'
flags: i
weight: 3
---
