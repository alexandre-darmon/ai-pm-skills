---
type: regex  # names the largest source of uncertainty: TPR on only 100 expert passes, not the 50 fails
pattern: '(largest|biggest|main|dominant|greatest|most of the|chief)[^.\n]{0,30}\b(source|share|part|term|contributor)?[^.\n]{0,15}(uncertainty|error|noise|variance|width)[^.\n]{0,50}\b(TPR|true positive|expert[- ]pass|analyst[- ]pass|labell?ed pass|100 (analyst|labell?ed|expert|memos|passes))|(uncertainty|error|noise)[^.\n]{0,30}\b(the )?(largest|biggest|main one|dominant one)\b[^.\n]{0,20}\b(TPR|true positive|expert[- ]pass|analyst[- ]pass)|\b(TPR|true positive rate|expert[- ]pass\w*|analyst[- ]pass\w*)[^.\n]{0,60}\b(dominat\w*|largest|biggest|main (source|driver)|most of the (uncertainty|width))'
flags: i
---
