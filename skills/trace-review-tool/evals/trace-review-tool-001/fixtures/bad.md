# Brief for the coding agent

Build a Flask app that loads the JSONL export of the conversations, including complaint text and customer details, so the officers have full context. Show the complaint and the draft side by side.

Each officer types their name in a box at the top, then rates each draft 1 to 5 for accuracy, tone and completeness. Save ratings to a SQLite file next to the app. Add a "next" button that shows the next draft in file order.

At the end, export a CSV with the average score per complaint type so the head of complaints can see where quality is lowest.
