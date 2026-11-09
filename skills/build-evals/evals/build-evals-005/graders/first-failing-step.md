---
type: regex  # label where each failed case first went wrong
pattern: '(first|earliest|upstream)[^.\n]{0,30}\b(failing|failed|broken|wrong|faulty)\b[^.\n]{0,15}\b(step|stage|component)|(step|stage|component)[^.\n]{0,40}\b(went|goes|first) wrong'
flags: i
---
