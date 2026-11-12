Before building anything, turn this into a spike that answers one question for the COO: can the approved model, at L2 (a handler confirms each route), sort claims emails into the four types and extract the policy number well enough, under a cost ceiling, to justify a project?

Fixed before the build, signed by the claims operations lead:
- Appetite: a time box of 5 working days, not a few weeks, and a maximum cost per correct answer of 0.10 EUR (4 minutes of handler time is worth about 2.70 EUR at 40 EUR an hour, so the ceiling is generous).
- Target and stop line per class: motor, home, liability 90% target, 75% stop line; bodily injury a stricter 97% target and 85% stop line, because a misroute delays a statutory letter. Bodily injury cannot be dropped.
- Cases per class, sized for the stop line: 19 each for motor, home and liability, 34 for bodily injury (fewer and even a perfect score could not read promising). About 90 emails in total.
- Kill date: Friday of next week. Past it, the spike stops by default.

Data and tool: the gateway model is an authorised asset, but a spike is not production. Use anonymised or synthetic emails only; real claims emails only under an approved, time-limited testing occasion reported to IT risk.

Lethal trifecta: emails are untrusted content, the inbox holds customer data, and forwarding is a way to send data out. Remove forwarding in code: the prototype only writes a suggested route, and the handler forwards.

Design: a fixed workflow, not an agent. One model call classifies and extracts; code checks the policy number format.

Report each class as n of N with a Wilson interval, and cost per correct answer against the ceiling. Decision: go to PRD, reshape, or stop. These numbers are not release evidence; build-evals samples real traffic later.
