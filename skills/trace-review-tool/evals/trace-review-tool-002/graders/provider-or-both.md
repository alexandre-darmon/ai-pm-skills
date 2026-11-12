---
type: regex  # asks whether an in-house build makes the bank provider, deployer or both
flags: i
---
(provider|deployer)[^\n]{0,60}\bor both\b|\bboth (a |the )?(provider|deployer)|in[- ]house[^\n]{0,80}provider|provider[^\n]{0,80}in[- ]house
