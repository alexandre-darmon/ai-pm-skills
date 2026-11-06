Action guardrails: cap of 150 EUR per refund, daily cap, approval by a supervisor above the cap. L4 is blocked until action guardrails pass the redteam set; the step stays at L3 meanwhile.

Enforcement point: the cap is a code check in the refund service, not a prompt line. It fails closed: on a timeout or crash the refund is denied, and an attempt above the cap alerts the support lead.

Three-leg check: private data yes (customer orders), untrusted content yes (customer messages, order notes), external path yes (the refund moves money out). All three present, so the external leg is broken by paying only to the original payment method, under the cap.
