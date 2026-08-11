# Промтинг в аналитике данных / Prompting for Data Analytics

Комплект для слушателя по применению промтинга в задачах аналитики данных.

## Что открыть первым

1. [`presentation/prompting_data_analytics_webinar.pptx`](./presentation/prompting_data_analytics_webinar.pptx) — презентация.
2. [`materials/data_dictionary.md`](./materials/data_dictionary.md) — описание полей учебного датасета.
3. [`notebooks/prompting_practice_student.ipynb`](./notebooks/prompting_practice_student.ipynb) — основной notebook слушателя.
4. [`materials/prompt_constructor.md`](./materials/prompt_constructor.md) — конструктор рабочего промта.
5. [`materials/validation_checklist.md`](./materials/validation_checklist.md) и [`materials/security_checklist.md`](./materials/security_checklist.md) — проверка качества и безопасности.

## Данные

- [`data/sales_sample.csv`](./data/sales_sample.csv) — синтетический датасет продаж для основной практики.
- [`assessment/data/support_tickets.csv`](./assessment/data/support_tickets.csv) — отдельный датасет для контрольного задания.

## Контроль и самостоятельная работа

В [`assessment/`](./assessment/) находятся `mini_test_student.md`, `post_assignment_brief.md`, `post_assignment_rubric.md` и датасет задания.

## Запуск notebook

```bash
pip install -r requirements.txt
jupyter notebook notebooks/prompting_practice_student.ipynb
```

## Важно

Этот GitHub-комплект предназначен для слушателя. Преподавательские notebooks, teleprompter, эталонные решения и внутренние QA-файлы сюда намеренно не включены.

[← Общий навигатор](../../README.md)
