---
type: regex  # computes the interval width more labels would give (about ±6 points), not a promise they will decide
pattern: '(label\w*|passes|fails|memos|cases)[^.\n]{0,60}\b(narrow|shrink|tighten|cut|bring)\w*[^.\n]{0,40}(±\s?\d|plus or minus \d|to (about |roughly |around )?\d+([.,]\d)? ?(%|points?))'
flags: i
---
