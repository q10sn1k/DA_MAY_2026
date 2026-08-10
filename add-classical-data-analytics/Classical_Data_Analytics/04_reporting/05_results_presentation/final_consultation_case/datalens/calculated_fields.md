# Справочник вычисляемых полей DataLens

```text
Orders = COUNTD([order_id])
Customers = COUNTD([customer_id])
Revenue = SUM([recognized_revenue])
Gross Profit = SUM([gross_profit])
Margin % = SUM([gross_profit]) / SUM([recognized_revenue])
Return Rate = SUM([is_returned]) / COUNTD([order_id])
Cancellation Rate = SUM([is_cancelled]) / COUNTD([order_id])
SLA Violation Rate = SUM([late_flag]) / SUM([sla_eligible])
Average Order Value = SUM([recognized_revenue]) / COUNTD_IF([order_id], [is_delivered] = 1)
Negative Margin Orders = COUNTD_IF([order_id], [negative_margin_flag] = 1)
```

## Правила проверки

1. Не смешивать агрегированные и неагрегированные выражения.
2. Процент маржи считать как отношение сумм, а не `AVG([margin_pct])`.
3. Для уникальных объектов использовать `COUNTD`.
4. После добавления фильтров перепроверять знаменатели долей.
5. Сверять итоговые KPI с `data/processed/monthly_kpi.csv` и контрольной таблицей.
