---
type: regex  # a model version change invalidates the prototype score
pattern: '(?:(?:new|newer|different|gateway|another) (?:model(?: version)?|version)|\bnewer one|\bmodel (?:version )?(?:change|update|swap)s?)[^.\n]{0,120}(?<!(?:\b(?:not?|nothing|without)|n.t)(?:\s+\w+){0,3}\s+)(?:invalidat\w*|new (?:run|release|baseline)|re-?run(?!\w*\s+(?:nothing|not\b|is not|isn.t))|does not carry|doesn.t carry|not (?:valid|transfer|carry|apply))|(?:invalidat\w*|no longer (?:valid|holds|applies))[^.\n]{0,80}(?:baseline|score|result|95|38)'
flags: i
---
