# Комплект для слушателя

## Назначение

Этот комплект нужен для практического занятия и подготовки итоговой аналитической работы.

Вы пройдёте маршрут:

```text
данные → загрузка → консолидация → очистка → preprocessing → EDA → статистика → взаимосвязи → BI-датасет → ABC-XYZ/RFM → выводы
```

## Что открыть первым

Откройте notebook:

```text
notebooks/01_capstone_draft_student_template.ipynb
```

Выполняйте ячейки сверху вниз.

## Что открыть вторым

После создания файла:

```text
outputs/bi_dataset.csv
```

откройте:

```text
notebooks/02_abc_xyz_rfm_student.ipynb
```

## Какие данные уже есть

```text
data/raw/orders_big.csv
data/raw/clients.csv
data/raw/products.csv
```

Сначала выполните практику на учебных данных. После занятия замените их на собственный датасет и повторите тот же маршрут.

## Что должно получиться после первого notebook

```text
outputs/data_quality_report.csv
outputs/descriptive_statistics.csv
outputs/group_summary.csv
outputs/correlation_matrix.csv
outputs/bi_dataset.csv
outputs/preliminary_conclusions.md
```

## Что должно получиться после второго notebook

```text
outputs/abc_analysis.csv
outputs/xyz_analysis.csv
outputs/abc_xyz_matrix.csv
outputs/rfm_analysis.csv
outputs/rfm_segment_summary.csv
outputs/segmented_bi_dataset.csv
outputs/abc_xyz_rfm_conclusions.md
```

## Как запустить локально

1. Распакуйте архив.
2. Откройте терминал в папке `capstone_student_project`.
3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите Jupyter:

```bash
jupyter notebook
```

5. Откройте первый notebook.

## Как работать в Google Colab

1. Загрузите notebook в Colab.
2. Загрузите CSV-файлы из `data/raw`.
3. Проверьте пути к файлам.
4. Выполняйте ячейки сверху вниз.

## Где смотреть инструкции

```text
materials/student_quick_start.md
materials/capstone_roadmap.md
materials/capstone_post_assignment.md
materials/capstone_bi_dashboard_guide.md
materials/abc_xyz_rfm_guide.md
materials/jupyter_colab_troubleshooting_faq.md
materials/final_submission_instruction.md
materials/capstone_assessment_rubric.md
```

## Важно

В комплекте нет преподавательских notebook, QA-отчётов и внутренних методических материалов.