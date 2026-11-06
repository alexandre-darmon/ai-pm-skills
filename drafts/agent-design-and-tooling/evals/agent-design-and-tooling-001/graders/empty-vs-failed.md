---
type: regex
pattern: '(not[ _]found|no (match|result|invoice|record)\w*|empty (result|list))[^\n.]{0,80}\b(distinct|apart|separate\w*|differ\w*|not the same|rather than|never|vs\.?|versus|not an?|is a valid|is not)[^\n.]{0,80}(\berror\b|fail\w*|time[sd]?[- ]?outs?|outage|unavailable|\bdown\b)|(\berror\b|fail\w*|time[sd]?[- ]?outs?|outage|unavailable|\bdown\b)[^\n.]{0,80}\b(distinct|apart|separate\w*|differ\w*|not the same|rather than|never|vs\.?|versus|not an?|is a valid|is not)[^\n.]{0,80}(not[ _]found|no (match|result|invoice|record)\w*|empty (result|list))'
flags: i
---
