# Карта учебных артефактов

| Этап | Вход | Выход | Проверка |
|---|---|---|---|
| Validation gate | `data/raw/*` | `data_validation_gate.csv` | raw `STOP`, clean `CONTINUE` |
| Очистка | сырые источники | `tickets_clean.csv`, `analysis_base.csv` | 23 922 строки |
| Прогноз | `daily_demand.csv` | `daily_forecast.csv`, `forecast_scenarios.csv` | сравнение с baseline |
| Кластеризация | `team_profiles.csv` | `cluster_profiles.csv` | silhouette + интерпретация |
| Классификация | model table | `sla_risk_predictions.csv` | временной test |
| Калибровка | validation probabilities | calibrated predictions | Brier score и cost curve |
| Сегментный анализ | test predictions | `segment_error_analysis.csv` | support и gaps |
| BI | объединённые результаты | `bi_export.csv` | 23 922 строки |
| Представление | графики и таблицы | `executive_summary.md` | факт + ограничение |
