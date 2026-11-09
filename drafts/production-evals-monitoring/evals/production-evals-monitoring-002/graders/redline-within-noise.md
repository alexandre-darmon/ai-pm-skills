---
type: regex  # red line: the dip is read against its control limits and found inside them, not taken as a shift
pattern: '\b(within|inside)\b[^\n]{0,40}\b(the )?(control |3[- ]?sigma |three[- ]sigma |3\s?σ |±\s?3\s?σ |noise |expected |normal |statistical )?(limits?|band|noise|range|variation)\b|\b(not|isn[’'']t|is no)\b[^\n]{0,30}\b(outside|beyond|below) the (lower )?(control )?(limit|band)|\b(consistent with|explained by|compatible with|indistinguishable from)\b[^\n]{0,30}\b(noise|chance|sampling (variation|error|noise))|\b(above|over) the lower (control )?limit'
flags: i
weight: 3
---
