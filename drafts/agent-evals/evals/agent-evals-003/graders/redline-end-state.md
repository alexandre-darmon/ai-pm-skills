---
type: regex  # red line: success is read in the CRM after the run, not in the final message
pattern: '(end|final|resulting)[- ]state|state of the (sandbox|system|ledger|database|crm|record|opportunity|order|payment)|(query|queries|read|reads|check|checks|verify|verifies|assert|asserts|inspect|compare|diff)\w*( back)?[^\n.]{0,50}\b(ledger|database|sandbox|test double|payment (system|record)|refund (row|record|table)|crm (record|field)|record in the crm|opportunity record|fields? in the crm)|before[- ]and[- ]after'
flags: i
weight: 3
---
