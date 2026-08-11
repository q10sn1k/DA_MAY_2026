# Практическая работа в Yandex DataLens

Комплект предназначен для самостоятельной работы слушателей во время 180-минутного практического вебинара. Все действия выполняются непосредственно в Yandex DataLens; Python и Jupyter Notebook не требуются.

## Результат работы

В ходе практики вы создадите:

1. файловое подключение к CSV;
2. датасет из трёх связанных таблиц;
3. отдельный BI-датасет на подготовленной витрине;
4. вычисляемые показатели и KPI;
5. аналитические чарты;
6. дашборд с селекторами;
7. секцию визуальной проверки гипотезы;
8. итоговый чек-лист качества.

## Состав комплекта

```text
student_practice_180min.md
materials/
  dataset_design_handout.md
  relationships_and_joins_handout.md
  final_self_checklist.md
data/
  raw/
    support_tickets.csv
    customers.csv
    regions.csv
  bi/
    support_service_datalens.csv
    hypothesis_summary_datalens.csv
    daily_forecast_datalens.csv
    forecast_metrics_datalens.csv
```

## С чего начать

1. Распакуйте архив в отдельную папку.
2. Откройте `student_practice_180min.md`.
3. Убедитесь, что все CSV-файлы находятся в папках `data/raw` и `data/bi`.
4. Войдите в Yandex DataLens и создайте отдельный воркбук для практики.
5. Выполняйте шаги инструкции последовательно.
6. После завершения используйте `materials/final_self_checklist.md`.

## Основные файлы

- `student_practice_180min.md` — полная пошаговая практика;
- `materials/dataset_design_handout.md` — проектирование датасетов и гранулярность;
- `materials/relationships_and_joins_handout.md` — ключи, связи и JOIN;
- `materials/final_self_checklist.md` — самопроверка результата;
- `data/raw` — таблицы для изучения связей;
- `data/bi` — подготовленные витрины для чартов и дашборда.

## Официальная документация

- Обзор и быстрый старт: https://yandex.cloud/ru/docs/datalens/quickstart
- Работа с датасетом: https://yandex.cloud/ru/docs/datalens/dataset/create-dataset
- Создание дашборда из CSV: https://yandex.cloud/ru/docs/tutorials/datalens/data-from-csv-visualization
- Чарты: https://yandex.cloud/ru/docs/datalens/concepts/chart/

## Важно

Не публикуйте учебный воркбук в открытом доступе без отдельной необходимости. Для передачи результата используйте скриншоты ключевых объектов или ссылку с корректно настроенными правами доступа.
