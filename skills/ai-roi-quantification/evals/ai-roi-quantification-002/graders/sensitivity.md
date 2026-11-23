---
type: regex  # sensitivity on the weakest assumptions, with the value at which the case stops paying
pattern: '\|[^\n]*(stops? paying|break[- ]?even|breaks even|no longer pays|turns negative|threshold|flips?)[^\n]*\|[ \t]*\n(?:[^\n]*\n){0,4}?\|[^\n|]*\b(quality|volume|uses|usage|adoption)\b[^\n]*\|[ \t]*\**[ \t]*((≈|~|about|below|under|at|roughly)[ \t]*)*\d[\d,.]* ?(%|uses)\**[^\n|%]{0,20}\|[ \t]*(\d[\d,.]* ?(%|uses)[ \t]*\|[ \t]*)?(?=\n|$)|\b(quality|volume|usage)\b[^\n|]{0,60}(stops? paying|break[- ]?even|breaks even|no longer pays|turns negative)[^\n|]{0,30}\d[\d,.]* ?(%|uses)|(stops? paying|break[- ]?even|breaks even|no longer pays|turns negative)[^\n|]{0,40}\b(quality|accuracy|correct|volume|usage)\w*[^\n|]{0,30}\d[\d,.]* ?(%|uses)'
flags: i
---
