# Сообщение для группы

Коллеги, к занятию подготовлен комплект материалов для практической работы и дальнейшей итоговой аналитической работы.

## Что нужно скачать

Скачайте архив:

```text
capstone_big_sales_project_v3_final.zip
```

Распакуйте архив в удобную папку на компьютере. Важно: не запускайте notebook прямо из архива, сначала архив нужно распаковать.

## Что открыть первым

После распаковки откройте файл:

```text
notebooks/capstone_draft_student_template.ipynb
```

Работайте с ним сверху вниз. Этот notebook ведёт по основному маршруту итоговой работы:

```text
данные → загрузка → консолидация → очистка → preprocessing → EDA → статистика → взаимосвязи → BI-датасет → предварительные выводы
```

## Какие данные уже есть в архиве

В архиве уже есть учебные данные:

```text
data/raw/orders_big.csv
data/raw/clients.csv
data/raw/products.csv
```

На них можно выполнить всю практику. Потом эту же структуру нужно будет перенести на свой датасет для итоговой работы.

## Что должно получиться после первого notebook

В папке `outputs` должны появиться файлы:

```text
data_quality_report.csv
descriptive_statistics.csv
group_summary.csv
correlation_matrix.csv
bi_dataset.csv
preliminary_conclusions.md
```

Главный файл для перехода к BI:

```text
outputs/bi_dataset.csv
```

## Что открыть вторым

После выполнения первого notebook откройте:

```text
notebooks/02_abc_xyz_rfm_student.ipynb
```

Он нужен для блока обогащения данных:

```text
ABC-анализ → XYZ-анализ → ABC-XYZ-матрица → RFM-анализ → segmented_bi_dataset.csv
```

После выполнения второго notebook в `outputs` должны появиться:

```text
abc_analysis.csv
xyz_analysis.csv
abc_xyz_matrix.csv
rfm_analysis.csv
rfm_segment_summary.csv
segmented_bi_dataset.csv
abc_xyz_rfm_conclusions.md
```

## Какие инструкции лежат в архиве

В папке `materials` есть вспомогательные материалы:

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

## Что показать в конце занятия

К концу занятия нужно показать:

1. выполненный первый notebook;
2. файл `outputs/bi_dataset.csv`;
3. предварительные выводы;
4. понимание, как заменить учебные данные на свой датасет.

Если успеваем перейти ко второму notebook, дополнительно показываем:

1. ABC-анализ;
2. XYZ-анализ;
3. RFM-анализ;
4. файл `outputs/segmented_bi_dataset.csv`.

## Важное замечание

Если локальный Jupyter не запускается, можно работать в Google Colab. В Colab нужно загрузить notebook и CSV-файлы заново, потому что файлы должны быть доступны среде выполнения.