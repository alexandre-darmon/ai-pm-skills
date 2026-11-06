You cannot compute cost per resolved request yet: the logs have no outcome. The thumbs are not a quality source either: given on 6% of conversations, self-selected.

1. Add an outcome event attached to each conversation id: `outcome_id`, `trace_id`, `use_case`, `result` (success, failure, escalated, abandoned), `value_eur`, `source`, `timestamp`.
2. Interim quality, until outcomes are logged: a weekly sampled review of 50 conversations, graded by IT agents against a rubric.
3. Cost per resolved request = monthly run cost ÷ (conversations × share resolved correctly), never all conversations.
4. A request closed by the assistant and later redone by a helpdesk agent does not count as resolved: leaving it in would make the KPI look too low.
5. Adoption: active users ÷ eligible employees per department, weekly.
