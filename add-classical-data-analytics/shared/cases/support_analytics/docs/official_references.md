# Официальные источники по используемым инструментам

Проверено 17.07.2026. Перед повторным проведением занятия рекомендуется сверить актуальный интерфейс и версии библиотек.

## scikit-learn

- Probability calibration: https://scikit-learn.org/stable/modules/calibration.html
- `CalibratedClassifierCV`: https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html
- Decision threshold tuning: https://scikit-learn.org/stable/modules/classification_threshold.html
- `ColumnTransformer`: https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html
- Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html

## statsmodels

- Forecasting with state-space models: https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_forecasting.html
- `SARIMAXResults.get_forecast`: https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAXResults.get_forecast.html
- Time-series analysis: https://www.statsmodels.org/stable/tsa.html

## Great Expectations

- Checkpoint API: https://docs.greatexpectations.io/docs/reference/api/checkpoint_class/
- Run a Checkpoint: https://docs.greatexpectations.io/docs/core/trigger_actions_based_on_results/run_a_checkpoint/

Учебный notebook реализует прозрачный validation gate на pandas. Great Expectations приводится как вариант промышленного развития, а не как обязательная зависимость комплекта.

## DataLens

- Dashboard widgets and links: https://datalens.tech/docs/en/dashboard/widget
- Navigator: https://datalens.tech/docs/en/operations/chart/config-chart-navigator
- `GEOPOINT`: https://datalens.tech/docs/en/function-ref/GEOPOINT
- `COUNTD_IF`: https://datalens.tech/docs/en/function-ref/COUNTD_IF
- `CASE`: https://datalens.tech/docs/en/function-ref/CASE
