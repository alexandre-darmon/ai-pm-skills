Use neither alone: route by confidence. The small model keeps the conversations where its confidence is above a threshold; the frontier model or a human takes the rest. Low-confidence cases go to human review or "unclassified", never forced into a class.

1. Split the agreement per dimension: 78% may hide 90% on use case and 60% on resolution.
2. On the 200 labelled conversations, find the threshold where the small model's kept cases reach the frontier's agreement. If it keeps 70% of the volume, the blended cost is 0.7 × 0.0004 + 0.3 × 0.012 ≈ 0.0039 EUR per conversation, about 233 EUR a month instead of 720 EUR.
3. Re-measure every month on a fresh labelled sample of 50–100 conversations to catch drift.
