---
type: regex  # the controller decides on the DPO's advice, with the factors the test turns on, not just "loop in the DPO"
pattern: 'DPO[''’]s advice|advice (?:of|from) the DPO|\bDPO advis\w*|(?:factors|facts)\b[^.\n]{0,30}\bfor the DPO|for the DPO\b[^.\n]{0,20}\bfactors|\bthe DPO\b[^.\n]{0,30}\b(?:these |the )?(?:factors|facts)\b|\bcontroller\b[^.\n]{0,30}\b(?:decides?|makes the (?:final )?call)\b|\b(?:decision|call)\b[^.\n]{0,30}\b(?:belongs to|is for|rests with|lies with|sits with) the (?:data )?controller\b'
flags: i
---
