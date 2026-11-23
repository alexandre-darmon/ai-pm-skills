---
type: regex  # a thumbs-down sample gives no rate; the random draw that would is sized (a number of conversations, or what a zero count still allows)
pattern: '\brandom\w*\b[^\n]{0,40}(?<![\d,.])\b\d{2,3}\b(\s*(to|-|–)\s*\d{2,3})?\s*(or more\s+)?(\w+\s+)?(conversations?|traces?|chats?|answers?)\b|(?<![\d,.])\b\d{2,3}\b(\s*(to|-|–)\s*\d{2,3})?\s*(or more\s+)?random\w*|(?<![\d,.])\b\d{2,3}\b(\s*(to|-|–)\s*\d{2,3})?\s*(or more\s+)?(\w+\s+)?(conversations?|traces?|chats?)\b[^\n]{0,30}\b(drawn |picked |selected )?at random\b|\brule of three\b|\bnever (seen|appears?)\b[^\n]{0,60}\bup to (about )?\d+\s?%'
flags: i
---
