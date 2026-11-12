---
type: regex  # adds simulated users with a fact revealed late, not just a persona
pattern: 'hidden (fact|detail|information|constraint|preference)s?|reveal\w*[^\n.]{0,40}(late|later|only (when|if) asked|when asked)|(late|later)[- ](revealed|stated|given|disclosed)|withh(o|e)ld\w*[^\n.]{0,30}(fact|detail|information|constraint)|(fact|constraint|detail)s? (given|stated|revealed|disclosed) (only )?(late|later|when asked)'
flags: i
---
