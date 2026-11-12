---
type: regex  # logs the prompt version
flags: i
---
prompt[^\n]{0,25}version|version\w*[^\n]{0,25}prompt|prompt[ _-]?(id|hash)
