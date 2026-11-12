---
type: regex  # logs the retrieved ids
flags: i
---
(document|doc|chunk|passage|transaction|source|record)[ _-]?ids?\b|retriev\w*[^\n]{0,40}\bids?\b|ids? of (the )?(retrieved|documents|transactions|chunks)
