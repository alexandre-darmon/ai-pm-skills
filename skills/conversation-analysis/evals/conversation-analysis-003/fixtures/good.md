Stop before any model sees these transcripts: they contain names, IBANs, emails, phone numbers and customer ids. Masking comes first, and nothing else starts until it is done and checked.

1. Mask the 45,000 conversations before any model call: patterns for IBANs, emails, phones and customer ids, named-entity recognition for names and places. Replace them with placeholders: [NAME], [IBAN], [EMAIL], [PHONE], [ID].
2. Check by hand a sample of 100 masked conversations and report the residual leak rate. GDPR data minimisation: raw text stays in the source system.
3. Three conversations are too few for a taxonomy. Take a masked sample of about 50 conversations, write a free-form note on what each user wanted, and cluster the notes into candidate classes. The three examples only give a seed: change of salary account, lost or swallowed card, fee or charge question.
4. Set a retention period for the masked text and the classifier logs, 12 months for example, because masked chat can still identify someone.
