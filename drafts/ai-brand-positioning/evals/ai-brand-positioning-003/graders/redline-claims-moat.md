---
type: regex
pattern: '(?<!(?:\bnot?\b|\bnever\b|\bnothing\b|\bneither\b|\bwithout\b|n[\x27’]t\b|\bremov|\bdrop|\bcut\b|\bdelet|\binstead\b|\bbefore\b|\bbanned\b|\bavoid|\bout\b)[^\n]{0,60})(?<!["“‘«\x27])\b(?:(?:this|it|the assistant|the product|you|your (?:product|assistant)|we)\s+(?:is|are|has|have|own|owns)\s+(?:a |an |the |real |strong |genuine |defensible |clear )*(?:moat|defensible|category of one|unique category|competitive advantage)|your (?:moat|defensible advantage|unfair advantage|category of one) is|(?:your|the) (?:prompts?|models?|interface) (?:is|are|gives? you)[^\n.]{0,20}(?:moat|defensible|advantage))\b(?![^\n.]{0,60}\b(?:if|once|until|when)\b)'
flags: i
match: not_contains
weight: 5
---
