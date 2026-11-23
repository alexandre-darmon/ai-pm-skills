---
type: regex  # personal data is masked before anyone reads a trace, internal readers included, not only before an external model or labeller sees it
pattern: '\b(mask|pseudonymi[sz]|redact|anonymi[sz])\w*\b[^\n]{0,80}\bbefore (any ?one|any ?body|any (human|person|reviewer)|a (person|human|reviewer)|the (expert|reader|reviewer|team)|people|humans?|we|you|reading)\b|\bbefore (any ?one|any ?body|any (human|person)|a (person|human)|the (expert|team)|people|humans?) (reads?|reviews?|looks? at|opens?)\b[^\n]{0,80}\b(mask|pseudonymi[sz]|redact|anonymi[sz])'
flags: i
---
