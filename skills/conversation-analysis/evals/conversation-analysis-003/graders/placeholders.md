---
type: regex  # a typed placeholder per identifier type found (name, IBAN, email, phone, customer id...), not one or two examples: at least four types named together
pattern: '(\[[A-Z][A-Z_]{1,20}\]|<[A-Z][A-Z_]{1,20}>)([^\n]{0,40}(\[[A-Z][A-Z_]{1,20}\]|<[A-Z][A-Z_]{1,20}>)){3}'
flags: i
---
