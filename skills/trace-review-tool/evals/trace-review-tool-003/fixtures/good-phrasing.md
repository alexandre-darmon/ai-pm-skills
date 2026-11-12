# Brief: alert-summary review app

The app is entered in the ICT asset register and approved at its end-user computing tier before it loads anything.

Masking happens upstream.
The app only ever reads the masked file.
The export script replaces names and IBANs with placeholders (PERSON_1, IBAN_1) before writing the file the app reads. The app reads only the pseudonymised file, never the raw export.

A second person reads all 200 masked alerts for leaks. Sanctions name checks stay in the case-management system.

Each label stores `labelled_by` (the logged-in user) and the time; the authenticated user is stored with each label. The head of compliance asked for "no accounts or passwords, whoever is free just opens it": not acceptable, an app anyone can open would lose the audit trail.

Labels go to approved storage, not the laptop.
