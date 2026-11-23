---
type: regex
flags: i
---
(train|fine-?tun|improv)\w*[^\n|]{0,120}(feedback|eval(uation)? (set|cases|data)|test (set|cases|data))|(feedback|eval(uation)? (set|cases|data)|test (set|cases|data))[^\n|]{0,60}(never|not)[^\n|]{0,40}(train|fine-?tun|improv)
