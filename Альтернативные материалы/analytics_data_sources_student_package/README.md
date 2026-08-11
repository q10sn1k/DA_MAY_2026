# Аналитика данных в бизнесе и других сферах. Типы и источники данных

Этот комплект предназначен для самостоятельной работы с материалами занятия и вводной практики по Python, Jupyter Notebook, pandas и первичному анализу данных.

## Что есть в комплекте

```text
analytics_data_sources_student_package/
├── docs/
│   ├── ipynb_opening_guide.docx
│   └── lecture_data_analytics_sources.pdf
├── notebooks/
│   ├── 01_python_basics_for_analytics.ipynb
│   ├── 02_strings_collections_cycles.ipynb
│   ├── 03_cycles_functions_for_analytics.ipynb
│   ├── 04_pandas_dataframe_visualization.ipynb
│   └── 05_final_practice_intro_data_analysis.ipynb
├── outputs/
├── requirements.txt
└── README.md
```

## Рекомендуемый порядок работы

1. Откройте `docs/ipynb_opening_guide.docx`, если раньше не работали с `.ipynb`.
2. Прочитайте `docs/lecture_data_analytics_sources.pdf` как вводный материал.
3. Выполните notebooks по порядку из папки `notebooks/`:
   - `01_python_basics_for_analytics.ipynb` — переменные, типы данных, ввод/вывод, условия;
   - `02_strings_collections_cycles.ipynb` — строки, списки, кортежи, множества, словари, циклы;
   - `03_cycles_functions_for_analytics.ipynb` — управление циклом, генераторы списков, функции;
   - `04_pandas_dataframe_visualization.ipynb` — DataFrame, группировки, сводные таблицы, графики;
   - `05_final_practice_intro_data_analysis.ipynb` — итоговая вводная практика по первичному анализу данных.

## Как запускать notebooks

Можно использовать Google Colab или локальный Jupyter Notebook. Внутри notebooks запускайте ячейки сверху вниз. В некоторых базовых упражнениях есть `input()` — в таком случае введите значение в поле под ячейкой и продолжайте выполнение.

## Локальный запуск

Если вы запускаете материалы локально, установите зависимости:

```bash
pip install -r requirements.txt
```

Затем откройте нужный `.ipynb` в Jupyter Notebook, JupyterLab или VS Code.

## Самопроверка

Перед завершением работы проверьте:

- notebooks открываются без ошибки;
- ячейки выполняются сверху вниз;
- графики отображаются;
- в итоговой практике есть таблицы, расчёты и краткие выводы;
- созданные в процессе файлы не нужно переносить вручную, если этого явно не требует задание.

## Что делать при типовых ошибках

| Ошибка | Что проверить |
|---|---|
| `NameError` | Запущены ли предыдущие ячейки, где создаётся переменная |
| `ModuleNotFoundError` | Установлены ли зависимости из `requirements.txt` |
| Не отображается график | Выполнена ли ячейка построения графика и импортирован ли `matplotlib.pyplot` |
| Notebook не видит файл | Проверьте текущую папку и имя файла |
| После перезапуска среды всё пропало | Запустите notebook заново сверху вниз |
```
