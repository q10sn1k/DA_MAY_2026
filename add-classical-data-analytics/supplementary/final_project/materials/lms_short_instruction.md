# Материалы к практическому занятию и итоговой работе

## Что нужно скачать

Скачайте и распакуйте архив:

```text
capstone_big_sales_project_v3_final.zip
```

Не запускайте notebook прямо из архива. Сначала распакуйте ZIP в обычную папку.

## Что открыть первым

Откройте notebook:

```text
notebooks/capstone_draft_student_template.ipynb
```

Выполняйте ячейки сверху вниз.

Этот notebook поможет пройти основной маршрут итоговой аналитической работы:

```text
загрузка данных → консолидация → очистка → preprocessing → EDA → статистика → анализ взаимосвязей → подготовка BI-датасета → предварительные выводы
```

## Какие данные уже есть в проекте

В папке `data/raw` уже лежат учебные CSV-файлы:

```text
orders_big.csv
clients.csv
products.csv
```

Сначала выполните работу на учебных данных. После занятия эту же структуру нужно будет перенести на собственный или выбранный открытый датасет.

## Что должно получиться после первого notebook

В папке `outputs` должны появиться:

```text
data_quality_report.csv
descriptive_statistics.csv
group_summary.csv
correlation_matrix.csv
bi_dataset.csv
preliminary_conclusions.md
```

Главный файл для дальнейшего BI-блока:

```text
outputs/bi_dataset.csv
```

## Что открыть вторым

После создания `bi_dataset.csv` откройте notebook:

```text
notebooks/02_abc_xyz_rfm_student.ipynb
```

Он нужен для обогащения данных:

```text
ABC-анализ → XYZ-анализ → ABC-XYZ-матрица → RFM-анализ → segmented_bi_dataset.csv
```

## Что должно получиться после второго notebook

В папке `outputs` должны появиться:

```text
abc_analysis.csv
xyz_analysis.csv
abc_xyz_matrix.csv
rfm_analysis.csv
rfm_segment_summary.csv
segmented_bi_dataset.csv
abc_xyz_rfm_conclusions.md
```

## Что показать по итогам занятия

Минимально:

1. выполненный первый notebook;
2. файл `outputs/bi_dataset.csv`;
3. файл `outputs/preliminary_conclusions.md`;
4. понимание, как заменить учебный датасет на свой.

Дополнительно, если прошли второй notebook:

1. `outputs/abc_analysis.csv`;
2. `outputs/xyz_analysis.csv`;
3. `outputs/rfm_analysis.csv`;
4. `outputs/segmented_bi_dataset.csv`.

## Что делать после занятия

1. Выбрать собственный датасет.
2. Скопировать структуру учебного проекта.
3. Заменить учебные CSV на свои данные.
4. Повторить маршрут первого notebook.
5. Подготовить `bi_dataset.csv`.
6. Построить BI-дашборд.
7. Выполнить ABC-XYZ/RFM.
8. Написать итоговые выводы.

## Где смотреть дополнительные инструкции

В папке `materials`:

```text
student_quick_start.md
capstone_roadmap.md
capstone_post_assignment.md
capstone_bi_dashboard_guide.md
abc_xyz_rfm_guide.md
dataset_selection_guide.md
final_submission_instruction.md
capstone_assessment_rubric.md
```

## Если Jupyter не запускается

Можно работать в Google Colab. В этом случае загрузите notebook и CSV-файлы в среду Colab и проверьте пути к данным.