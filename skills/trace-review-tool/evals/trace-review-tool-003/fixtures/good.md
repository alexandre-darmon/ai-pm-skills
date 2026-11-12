# Brief: alert-summary review app

I cannot write this one as asked. Two of the requirements cross lines a bank tool cannot cross: raw names and IBANs on a laptop app, and labels with no reviewer identity.

**ICT asset first.** Masked data is pseudonymised, so still personal data. Before the app loads anything derived from production, even masked, it is identified as an ICT asset, documented and approved at its end-user computing tier; until then it runs on synthetic alerts.

**Masking.** Names, IBANs and addresses are pseudonymised in the export step, before the app loads anything, with consistent placeholders: `<PARTY_1>` sends to `<PARTY_2>`, `<IBAN_1>` stays `<IBAN_1>` across the alert. The analyst can still judge whether the summary followed the money. A second person reads all 200 masked alerts for residual leaks before grading starts, free-text fields first: zero leaks in 200 still allows a leak rate up to about 1.5%.

**When the real name matters.** Checking that the summary names the right counterparty against the sanctions hit is done in the source system, the case-management tool, under its access rights, or by code against the system of record. It never goes into the app.

**Who labels.** Each label carries the analyst id from the bank login (SSO) and a UTC timestamp; the app refuses to save without one. Four people is exactly when "who said pass" matters to an auditor.

**Storage.** Labels go to approved storage with an access list, not the laptop.

**Questions for the DPO and IT risk.** Financial-crime data is sensitive: the DPO decides on masking and access. A tool built outside IT is an ICT asset under DORA whatever data it holds: it is identified and risk-managed like any other.
