---
type: regex  # reads the class score with its interval, not as a point
pattern: 'lower (bound|limit|end)|wilson|confidence interval|95 ?% (confidence )?interval|interval[^.\n]{0,40}\b(from|of|runs?)\b'
flags: i
---
