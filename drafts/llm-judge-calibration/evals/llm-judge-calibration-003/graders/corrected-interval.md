---
type: regex  # interval carrying TPR and TNR uncertainty: bootstrap 82% to 99.6%, delta method 82% to 99%
pattern: '(?<![\d.])(0?\.)?8[0-4](\.\d+)? ?%?\s*(to|–|—|-|,|;|and)\s*(0?\.)?(9[6-9]|100)(\.\d+)? ?%?|(?<![\d.])0?\.8[0-4]\d*\s*(to|–|—|-|,|;|and)\s*1(\.0+)?\b|(?<![\d.])90(\.\d+)? ?%? ?(±|\+/-) ?[7-9](\.\d+)?'
flags: i
---
