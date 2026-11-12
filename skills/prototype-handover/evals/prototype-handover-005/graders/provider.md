---
type: regex  # the company itself may be the provider of an in-house system
pattern: '(?:\bwe\b|the insurer|the company|the (?:bank|firm|group)|\bitself\b)[^.\n]{0,60}(?<!(?:model|API|cloud|LLM|vendor|service|third[- ]party)\s)\bprovider\b|(?<!(?:model|API|cloud|LLM|vendor|service|third[- ]party)\s)\bprovider\b[^.\n]{0,60}(?:own use|3\s*\(3\)|3\s*\(11\)|in-house|not (?:only|just) (?:a )?deployer|rather than (?:a |just a )?deployer)'
flags: i
---
