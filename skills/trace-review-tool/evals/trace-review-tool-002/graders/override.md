---
type: regex  # logs the analyst's overrides
flags: i
---
(officer|human|user|analyst|handler|reviewer)s?.?[^\n]{0,30}overrid|overrid\w*[^\n]{0,40}(rate|field|who|logged|captured|capture|recorded|signal|record|reason)
