Stop before any model sees these transcripts: they contain names, IBANs, emails, phone numbers and customer ids. Masking comes first, and nothing else starts until it is done and checked.

1. Mask the 45,000 conversations before any model call: patterns for IBANs, emails, phones and customer ids, named-entity recognition for names and places. Replace them with placeholders: [NAME], [IBAN], [EMAIL], [PHONE], [ID].
2. Check by hand a sample of 100 masked conversations and report the residual leak rate. GDPR data minimisation: raw text stays in the source system.
3. Then draft the taxonomy from the masked text. From the three examples: change of salary account, lost or retained card, fee or charge question.
