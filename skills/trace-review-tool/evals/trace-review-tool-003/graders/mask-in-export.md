---
type: regex  # personal data replaced in the export step, before the app reads it
flags: i
---
(replac|substitut|mask|pseudonymi[sz]|redact|anonymi[sz]|tokeni[sz]|scrub)\w*[^\n]{0,120}(export|extract|before|upstream|placeholder|(app|tool) (only )?(ever )?(reads|sees|loads|gets))|(export|extract|upstream)[^\n]{0,80}(replac|substitut|mask|pseudonymi[sz]|redact|anonymi[sz]|tokeni[sz])
