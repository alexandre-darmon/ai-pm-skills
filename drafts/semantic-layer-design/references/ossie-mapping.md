# Mapping the semantic spec to Apache Ossie

[Apache Ossie](https://ossie.apache.org/) (incubating, formerly Open Semantic Interchange) is a vendor-neutral format to exchange metrics, dimensions and joins between BI, analytics and AI tools. [Specification](https://github.com/apache/ossie/blob/main/core-spec/spec.md), read 2026-11-05. [Converters](https://github.com/apache/ossie-converters) exist for tools such as dbt and Snowflake.

**Version.** The last release is 0.1.1 (2025-12-11). The current spec, 0.2.0.dev0, is marked as a draft whose schema may change, not for production dependency, and it has breaking changes: one model at the document root (no `semantic_model` array), and metric expressions, keys and relationships refer to dataset fields rather than source columns. State the version in the file, and check which one the target tool reads. The shapes below follow 0.2.0.dev0.

**What it does not cover.** Ossie describes meaning, not governance. Its core has no field for owner, status, test, grain or conflict. It stays the exchange format; this skill's spec stays the source for governance.

| Semantic spec | Ossie | Note |
| --- | --- | --- |
| Domain | model: `version`, `name`, `datasets` (required) | one model per document |
| Source table | dataset: `name`, `source`, `primary_key`, `unique_keys` | fact or dimension table |
| Allowed dimension | field: `name`, `expression`, `dimension.is_time`, `datatype` | field expressions are scalar, no aggregation |
| Join | relationship: `from` (many side), `to` (one side), `from_columns`, `to_columns` | column order must match in both arrays |
| Metric on one table | `datasets[].metrics` | dataset-scoped |
| Metric across tables | root `metrics`, written `dataset.field` | model-scoped |
| Formula | `expression.sql` (portable `OSSIE_SQL_2026`), `expression.dialects` for vendor variants | at least one of the two; `sql` wins over an `OSSIE_SQL_2026` dialect entry |
| Business definition | `description` | |
| Terms users really say | `ai_context`: `synonyms`, `examples`, `instructions` | take them from the question inventory |
| Owner, status, test, grain | `custom_extensions`: `vendor_name` plus `data` as a JSON string | carried, not interpreted, by consumers |

```yaml
version: 0.2.0.dev0
name: billing
datasets:
  - name: invoices
    source: finance.billing.invoices
    primary_key: [invoice_id]
    fields:
      - name: invoice_id
        expression:
          sql: invoice_id
      - name: amount
        expression:
          sql: amount_eur
        datatype: Decimal
      - name: paid_at
        expression:
          sql: paid_at
        dimension:
          is_time: true
    metrics:
      - name: revenue
        expression:
          sql: SUM(amount)
        description: Invoiced amount paid, in EUR, per calendar month.
        datatype: Decimal
        ai_context:
          synonyms: ["paid revenue", "billed and paid"]
        custom_extensions:
          - vendor_name: ACME_GOVERNANCE
            data: '{"owner": "finance-controlling", "status": "certified", "grain": "month", "test": "reconcile with ledger"}'
```
