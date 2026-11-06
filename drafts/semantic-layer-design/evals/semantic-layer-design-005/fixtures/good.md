churn_rate stays draft and is excluded from the export.

Standing filter on revenue: none known, finance controlling to confirm, since users say paid revenue and the formula sums every invoice.

```yaml
version: 0.2.0.dev0
name: billing
relationships:
  - name: invoice_customer
    from: invoices
    to: customers
metrics:
  - name: arpu
    ai_context:
      synonyms: ["average revenue per user"]
    custom_extensions:
      - vendor_name: ACME
        data: '{"owner": "finance controlling", "status": "certified"}'
```
