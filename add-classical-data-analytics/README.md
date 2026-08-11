# Classical Data Analytics / Классическая аналитика данных

> **Главный навигатор по материалам для слушателей.**  
> Папки и технические имена файлов стандартизированы на английском, чтобы пути стабильно работали в GitHub, Windows, VS Code, Jupyter и других инструментах. Содержимое материалов при этом может оставаться на русском языке. Ниже для каждого английского имени указано, что именно это за материал и где его искать.

## С чего начать

1. Найдите нужную тему в таблице **«Карта 22 тем»**.
2. Перейдите в папку темы и сначала откройте ее `README.md`.
3. Для практики ищите `notebooks/`, `notebooks_student/` или `practice/`.
4. Для исходных данных ищите `data/raw/`.
5. Если в проекте есть свой `requirements.txt`, используйте именно его.
6. Не переименовывайте технические файлы без необходимости: notebooks используют относительные пути.
7. Если папка темы содержит только `README.md`, это **навигационная тема**, а не пустой раздел: README указывает на каноническое место большого сквозного кейса.

Полный технический список файлов находится в [`FILE_INDEX.md`](./FILE_INDEX.md), короткая двуязычная карта тем — в [`TOPIC_MAP.md`](./TOPIC_MAP.md).

---

## Основная структура каталога

```text
Classical_Data_Analytics/
├── 01_foundations/      # основы аналитики, источники, сбор, SQL, интеграция
├── 02_processing/       # Python, очистка, преобразование, R, Big Data
├── 03_analysis/         # статистика, гипотезы, временные ряды, ML
├── 04_reporting/        # визуализация, BI, интерпретация, презентация
├── shared/              # сквозные кейсы для нескольких тем
├── supplementary/       # промтинг, AI workflows, итоговая работа
├── README.md            # этот навигатор
├── TOPIC_MAP.md         # карта 22 тем
├── FILE_INDEX.md        # полный индекс файлов
├── SOURCE_MANIFEST.csv  # техническая трассировка исходников
├── QA_REPORT.md         # отчет о проверке комплекта
└── requirements.txt     # общее Python-окружение
```

## Словарь английских названий папок

| Папка | По-русски | Что там находится |
|---|---|---|
| `materials/` | материалы | презентации, методички, памятки, PDF/DOCX/MD/HTML |
| `notebooks/` | notebooks | практические Jupyter `.ipynb` |
| `notebooks_student/` | notebooks слушателя | версии без преподавательских решений |
| `practice/` | практика | задания, инструкции и датасеты |
| `integrated_project/` | интегрированный проект | законченный многошаговый кейс |
| `integrated_practice/` | интегрированная практика | связанная практика Python/SQL/данные |
| `data/raw/` | исходные данные | входные CSV/XLSX/JSON и др. |
| `data/processed/` | обработанные данные | подготовленные таблицы и результаты |
| `data/bi/` | данные для BI | готовые витрины для DataLens/BI |
| `docs/` | документация | словари данных, пояснения, чек-листы |
| `scripts/` | скрипты | служебные Python/R-скрипты |
| `sql/` | SQL | запросы и SQLite-базы |
| `datalens/` | DataLens | инструкции, расчетные поля, спецификации |
| `assets/figures/` | иллюстрации | графики, схемы, mockup'ы |
| `assessment/` | контроль | тесты, диагностика, самостоятельные задания, рубрики |
| `report/` | отчет | пример итогового отчета |
| `extensions/` | расширение | дополнительные упражнения |

## Что означают расширения

| Расширение | Что это |
|---|---|
| `.ipynb` | Jupyter Notebook / Google Colab / VS Code Notebook |
| `.md` | Markdown-инструкция, читается прямо на GitHub |
| `.csv` | табличный датасет |
| `.xlsx` | Excel |
| `.json` | JSON-данные |
| `.sql` | SQL-скрипт |
| `.sqlite` | SQLite-база |
| `.py` | Python-скрипт |
| `.R` | R-скрипт |
| `.Rproj` | проект RStudio |
| `.pptx` | презентация PowerPoint |
| `.docx` | документ Word |
| `.pdf` | документ для чтения/печати |
| `.html` | HTML-презентация или локальная страница, открывается браузером |
| `.png` | изображение/график |
| `.gitkeep` | служебный файл для сохранения пустой папки в Git |

---

# Карта 22 тем

| № | Тема на русском | Техническая папка | Что открыть первым |
|---:|---|---|---|
| 1 | Аналитика данных в бизнесе и других сферах | [`01_foundations/01_business_analytics`](./01_foundations/01_business_analytics/) | [`data_analytics_foundations_complete.ipynb`](./01_foundations/01_business_analytics/notebooks/data_analytics_foundations_complete.ipynb) |
| 2 | Типы и источники данных | [`01_foundations/02_data_sources`](./01_foundations/02_data_sources/) | [`student_practice_instruction.md`](./01_foundations/02_data_sources/practice/data_sources_practice_csv/student_practice_instruction.md) |
| 3 | Сбор данных с различных источников | [`01_foundations/03_data_collection`](./01_foundations/03_data_collection/) | локальный `README.md` — навигация |
| 4 | Основы работы с SQL | [`01_foundations/04_sql`](./01_foundations/04_sql/) | [`01_mysql_start_crud_beginner.md`](./01_foundations/04_sql/materials/01_mysql_start_crud_beginner.md) |
| 5 | Инструменты для сбора данных | [`01_foundations/05_collection_tools`](./01_foundations/05_collection_tools/) | [`data_collection_tools_presentation.html`](./01_foundations/05_collection_tools/materials/data_collection_tools_presentation.html) |
| 6 | Загрузка и интеграция данных из различных форматов | [`01_foundations/06_data_integration`](./01_foundations/06_data_integration/) | [`integrated_project/README.md`](./01_foundations/06_data_integration/integrated_project/README.md) |
| 7 | Основы Python для обработки данных | [`02_processing/01_python`](./02_processing/01_python/) | [`integrated_practice/README.md`](./02_processing/01_python/integrated_practice/README.md) |
| 8 | Очистка данных | [`02_processing/02_cleaning`](./02_processing/02_cleaning/) | [`practice_instruction.md`](./02_processing/02_cleaning/materials/practice_instruction.md) |
| 9 | Преобразование данных | [`02_processing/03_transformation`](./02_processing/03_transformation/) | [`transformation_practice/README.md`](./02_processing/03_transformation/transformation_practice/README.md) |
| 10 | Нормализация и стандартизация данных | [`02_processing/04_scaling`](./02_processing/04_scaling/) | [`normalization_standardization_guide.md`](./02_processing/04_scaling/normalization_case/docs/normalization_standardization_guide.md) |
| 11 | Основы работы с R для обработки данных | [`02_processing/05_r`](./02_processing/05_r/) | [`r_practice/README.md`](./02_processing/05_r/r_practice/README.md) |
| 12 | Работа с большими данными | [`02_processing/06_big_data`](./02_processing/06_big_data/) | [`big_data_student_kit/README.md`](./02_processing/06_big_data/big_data_student_kit/README.md) |
| 13 | Основы статистического анализа данных | [`03_analysis/01_statistics`](./03_analysis/01_statistics/) | [`support_service_case/README.md`](./03_analysis/01_statistics/support_service_case/README.md) |
| 14 | Анализ взаимосвязей | [`03_analysis/02_relationships`](./03_analysis/02_relationships/) | [`relationships_and_hypothesis_testing.ipynb`](./03_analysis/02_relationships/notebooks/relationships_and_hypothesis_testing.ipynb) |
| 15 | Тестирование гипотез | [`03_analysis/03_hypotheses`](./03_analysis/03_hypotheses/) | [`hypothesis_timeseries_case/README.md`](./03_analysis/03_hypotheses/hypothesis_timeseries_case/README.md) |
| 16 | Анализ временных рядов и прогнозирование | [`03_analysis/04_time_series`](./03_analysis/04_time_series/) | локальный `README.md` — ссылки на кейсы |
| 17 | Методы кластеризации и классификации | [`03_analysis/05_ml_clustering_classification`](./03_analysis/05_ml_clustering_classification/) | локальный `README.md` — ссылки на `shared` |
| 18 | Интерпретация и представление результатов анализа | [`04_reporting/01_interpretation`](./04_reporting/01_interpretation/) | локальный `README.md` |
| 19 | Первичная визуализация данных | [`04_reporting/02_visualization`](./04_reporting/02_visualization/) | локальный `README.md` |
| 20 | Визуализация данных в Python и R | [`04_reporting/03_python_r_visualization`](./04_reporting/03_python_r_visualization/) | локальный `README.md` |
| 21 | Визуализация данных в BI-инструментах | [`04_reporting/04_bi_visualization`](./04_reporting/04_bi_visualization/) | [`datalens_student_package/README.md`](./04_reporting/04_bi_visualization/datalens_student_package/README.md) |
| 22 | Презентация аналитических результатов для руководства и заинтересованных сторон | [`04_reporting/05_results_presentation`](./04_reporting/05_results_presentation/) | [`README.md`](./04_reporting/05_results_presentation/README.md) |

---

# 1. `01_foundations` — основы аналитики и сбор данных

## `01_business_analytics` — Аналитика данных в бизнесе

- `materials/data_analytics_lecture.pdf` — лекционный материал;
- `materials/jupyter_notebook_quick_guide.docx` — памятка по Jupyter;
- `notebooks/data_analytics_foundations_complete.ipynb` — основной практический notebook.

**Порядок:** лекция → памятка → notebook.

## `02_data_sources` — Типы и источники данных

- `materials/data_sources_webinar_presentation.pptx` — презентация;
- `materials/data_sources_student_handout.docx` — раздаточный материал;
- `practice/data_sources_practice_csv/student_practice_instruction.md` — инструкция к практике;
- `practice/data_sources_practice_csv/README_practice_dataset.md` — описание датасета;
- `practice/data_sources_practice_csv/data_sources_templates.xlsx` — Excel-шаблон;
- `practice/data_sources_practice_csv/csv/` — `products.csv`, `sales.csv`, `clients.csv`, `regions.csv`, `customer_reviews.csv`, `marketing_channels.csv`, `site_events_log.csv`, `source_catalog.csv`, `external_source_links.csv`, `data_dictionary.csv`, `business_questions.csv`.

## `03_data_collection` — Сбор данных с различных источников

Папка содержит только навигационный `README.md`. Материалы физически находятся в практикуме `02_data_sources` и в `05_collection_tools`. Это сделано специально, чтобы не хранить дубли.

## `04_sql` — Основы SQL

- `materials/01_mysql_start_crud_beginner.md` и `.pdf` — MySQL, старт и CRUD;
- `materials/02_mysql_relations_joins_beginner.md` и `.pdf` — связи и JOIN;
- `materials/sql_mysql_pandas_student_guide.docx` — руководство слушателя;
- `materials/sql_web_presentation.html` — HTML-презентация;
- `materials/sqlite_backup_instruction.md` — SQLite/backup;
- `notebooks/03_sql_result_as_dataframe_intro.ipynb` — SQL → DataFrame;
- `notebooks/04_assignment_sql_pandas_bridge.ipynb` — задание SQL → pandas;
- `notebooks/sqlite_backup_student.ipynb` — практика SQLite.

## `05_collection_tools` — Инструменты для сбора данных

- `materials/data_collection_tools_presentation.html` — презентация;
- `materials/jupyter_colab_secrets_security_guide.pdf` — безопасная работа с секретами в Jupyter/Colab.

## `06_data_integration` — Загрузка и интеграция данных

Главный проект: [`integrated_project/`](./01_foundations/06_data_integration/integrated_project/).

Внутри:

- `README.md` — инструкция;
- `environment_check.py` — проверка окружения;
- `requirements.txt` — зависимости;
- `data/raw/` — `clients.csv`, `products.xlsx`, `regions.json`, `sales.csv`, `web_table_sample.html`;
- `data/prepared/`, `data/output/` — каталоги результатов;
- `docs/` — словарь данных и пояснения по форматам, `merge/join`, `groupby`, `pivot_table`, визуализации, VS Code и offline-установке;
- `notebooks_student/00_setup_and_check*.ipynb` — подготовка;
- `01_data_loading_formats.ipynb` — загрузка форматов;
- `02_dataframe_types_and_quality.ipynb` — типы/качество;
- `03_data_integration.ipynb` — интеграция;
- `04_basic_analysis.ipynb` — анализ;
- `05_basic_visualization.ipynb` — визуализация;
- `06_python_to_r_bridge.ipynb` — Python → R;
- `07_final_practice_case.ipynb` — итоговый кейс.

---

# 2. `02_processing` — обработка данных

## `01_python` — Python для обработки данных

Основной каталог: [`integrated_practice/`](./02_processing/01_python/integrated_practice/).

- `README.md` — порядок работы;
- `notebooks/student_practice.ipynb` — основная практика;
- `notebooks/extra_practice_analytics_report.ipynb` — дополнительная практика;
- `notebooks/post_assignment_template.ipynb` — шаблон самостоятельной работы;
- `data/raw/` — `clients.csv`, `products.xlsx`, `regions.json`, `sales.csv`;
- `sql/analytics_demo.sqlite` — готовая SQLite-база;
- `sql/create_database.sql`, `practice_queries.sql`, `*_template.sql` — SQL;
- `docs/` — словарь данных, glossary, post-assignment, checklist и rubric;
- `scripts/check_sqlite.py` — проверка SQLite;
- `requirements.txt` — зависимости.

## `02_cleaning` — Очистка данных

- `materials/practice_instruction.md` — инструкция;
- `notebooks/data_cleaning_full_practice_beginner.ipynb` — полный практикум по очистке.

## `03_transformation` — Преобразование данных

В `transformation_practice/`:

- `README.md`;
- `notebooks/data_transformation_demo.ipynb`;
- `data/raw/clients.csv`, `products.xlsx`, `regions.json`, `sales.csv`;
- `requirements.txt`.

## `04_scaling` — Нормализация и стандартизация

В `normalization_case/`:

- `docs/normalization_standardization_guide.md` — основная методичка;
- `docs/data_dictionary.md` — словарь;
- `docs/final_integration_student_instruction.md` — инструкция;
- `docs/final_post_assignment.md` — самостоятельная работа;
- `docs/final_seminar_checklist.md` — чек-лист;
- `notebooks/02_normalization_standardization_datamart.ipynb` — практика;
- `data/raw/` — учебные данные;
- `requirements.txt`.

## `05_r` — R для обработки данных

- `materials/r_data_processing_presentation.pptx` — презентация;
- `r_practice/README.md` — основная инструкция;
- `r_practice/r_data_basics.Rproj` — RStudio Project;
- `r_practice/data/retail_sales.csv` — датасет;
- `r_practice/scripts/student_practice.R` — практика;
- `r_practice/scripts/environment_check.R` и `install_packages.R` — настройка;
- `r_practice/extensions/` — дополнительные `.R` и инструкции;
- `r_practice/materials/` — common errors, словарь, knowledge check, post-assignment, self-check, handout;
- `r_practice/MANIFEST.md` — состав комплекта.

## `06_big_data` — Работа с большими данными

В `big_data_student_kit/`:

- `README.md`, `practice_instruction.md`;
- `data/raw/events_lite.csv` — основной датасет;
- `notebooks/student_practice.ipynb` — практика;
- `materials/data_dictionary.md`, `self_checklist.md`;
- `assessment/` — диагностика, итоговый тест, самостоятельная работа и rubric;
- `scripts/generate_events.py` — генератор данных;
- `requirements.txt`.

---

# 3. `03_analysis` — анализ и моделирование

## `01_statistics` — Статистический анализ

Кейс `support_service_case/`:

- `data/raw/support_tickets.csv`, `customers.csv`, `regions.csv`;
- `materials/data_dictionary.md`, `student_instruction.md`, `hypothesis_cards.md`, `self_checklist.md`;
- `notebooks/student_practice.ipynb`;
- `requirements.txt`.

## `02_relationships` — Анализ взаимосвязей

Основной файл: `notebooks/relationships_and_hypothesis_testing.ipynb`. Локальный README также ведет к статистическому и сквозному кейсам.

## `03_hypotheses` — Тестирование гипотез

Кейс `hypothesis_timeseries_case/`:

- `data/raw/support_tickets.csv`;
- `materials/data_dictionary.md`, `student_assignment_brief.md`;
- `notebooks/hypothesis_timeseries_student_template.ipynb`;
- `notebooks/hypothesis_timeseries_arima_extension.ipynb`;
- `scripts/generate_support_tickets.py`;
- `requirements.txt`.

## `04_time_series` — Временные ряды и прогнозирование

Навигационная тема. Практические notebooks находятся в `03_hypotheses/hypothesis_timeseries_case/` и в `shared/cases/support_analytics/notebooks/student/`.

## `05_ml_clustering_classification` — Кластеризация и классификация

Навигационная тема. Основные notebooks в `shared/cases/support_analytics/notebooks/student/`:

- `03_entity_clustering_student.ipynb` — кластеризация;
- `04_sla_classification_student.ipynb` — классификация;
- `04b_probability_calibration_threshold_student.ipynb` — калибровка/порог;
- `04c_segment_error_analysis_student.ipynb` — анализ ошибок.

---

# 4. `04_reporting` — визуализация, BI и представление результатов

## `01_interpretation` — Интерпретация результатов

Навигационная тема. Основной notebook: `shared/cases/support_analytics/notebooks/student/05_results_interpretation_student.ipynb`.

## `02_visualization` — Первичная визуализация

Навигация на:

- `01_foundations/06_data_integration/integrated_project/notebooks_student/05_basic_visualization.ipynb`;
- `shared/cases/support_analytics/notebooks/student/01_data_quality_eda_student.ipynb`.

## `03_python_r_visualization` — Визуализация в Python и R

Навигация на Python-визуализацию в интегрированном проекте и на R-комплект `02_processing/05_r/`.

## `04_bi_visualization` — BI / DataLens

Главный комплект: `datalens_student_package/`:

- `README.md`;
- `student_practice_180min.md` — практика на 180 минут;
- `data/raw/` — `support_tickets.csv`, `customers.csv`, `regions.csv`;
- `data/bi/` — `support_service_datalens.csv`, `daily_forecast_datalens.csv`, `forecast_metrics_datalens.csv`, `hypothesis_summary_datalens.csv`;
- `materials/dataset_design_handout.md`;
- `materials/relationships_and_joins_handout.md`;
- `materials/final_self_checklist.md`.

Отдельно: `materials/multiple_tables_granularity_answer.pdf` — ответ по нескольким таблицам и разной гранулярности.

## `05_results_presentation` — Презентация аналитических результатов

Кейс `final_consultation_case/`:

- `notebooks/02_student_consultation_template.ipynb` — основной шаблон;
- `notebooks/03_optional_ml_extension.ipynb` — дополнительный ML-блок;
- `data/raw/` — `customers.csv`, `orders.csv`, `products.csv`, `regions.csv`;
- `data/processed/` — витрина, KPI, summaries, гипотезы, ABC/XYZ, RFM, ML-метрики;
- `datalens/datalens_build_guide.md`, `calculated_fields.md`, `datalens_dashboard_specification.xlsx`;
- `materials/data_dictionary.xlsx`, `defense_questions.md`;
- `report/example_final_report.docx` и `.pdf`;
- `assets/figures/01_...png`–`09_...png` — примеры графиков/макета;
- `requirements.txt`.

---

# 5. `shared` — сквозные кейсы

## `shared/cases/support_analytics` — аналитика службы поддержки

Кейс хранится один раз и используется в нескольких темах: прогнозирование, кластеризация, классификация, интерпретация и визуализация.

### Данные `data/raw/`

`tickets.csv`, `ticket_events.csv`, `teams.xlsx`, `regions.json`, `team_capacity_daily.csv`, `calendar_events.csv`, `load_log.csv`.

### Notebooks `notebooks/student/`

1. `00_data_validation_gate_student.ipynb` — входная валидация;
2. `01_data_quality_eda_student.ipynb` — качество и EDA;
3. `02_timeseries_forecast_student.ipynb` — прогнозирование;
4. `02b_forecast_uncertainty_scenarios_student.ipynb` — сценарии неопределенности;
5. `03_entity_clustering_student.ipynb` — кластеризация;
6. `04_sla_classification_student.ipynb` — классификация;
7. `04b_probability_calibration_threshold_student.ipynb` — калибровка;
8. `04c_segment_error_analysis_student.ipynb` — ошибки по сегментам;
9. `05_results_interpretation_student.ipynb` — интерпретация.

Дополнительно:

- `docs/` — словарь данных, правила качества, карта артефактов, ссылки;
- `materials/student/` — задания и self-check;
- `datalens/` — расчетные поля, mapping чартов, спецификация и acceptance checklist;
- `scripts/validate_support_analytics_data.py` — проверка данных;
- `requirements.txt`.

---

# 6. `supplementary` — дополнительные материалы

## `prompting` — Промтинг в аналитике данных

- `presentation/prompting_data_analytics_webinar.pptx` — презентация;
- `data/sales_sample.csv` — учебные продажи;
- `materials/data_dictionary.md` — словарь;
- `materials/prompt_constructor.md` — конструктор промта;
- `materials/validation_checklist.md` — валидация;
- `materials/security_checklist.md` — безопасность;
- `notebooks/prompting_practice_student.ipynb` — практика слушателя;
- `assessment/` — мини-тест, post-assignment, rubric и `support_tickets.csv`;
- `requirements.txt`.

## `ai_workflows` — AI-процессы аналитика

- `universal_analytics_pipeline_steps.md` — универсальный pipeline;
- `analytical_pipeline_movies_example.md` — пример на фильмах;
- `ai_analysis_prompt_series_a_to_z_revised.md` — серия промтов;
- `AI_assist/AI_assist_preprompt.md` и `instruct.md` — настройка AI-ассистента;
- `MoviesOnStreamingPlatforms/MoviesOnStreamingPlatforms.csv` — датасет;
- `MoviesOnStreamingPlatforms/example.ipynb` — пример notebook.

## `final_project` — Итоговая работа

Сначала откройте `supplementary/final_project/README.md`.

Главные файлы:

- `notebooks/01_capstone_draft_student_template.ipynb` — основной шаблон;
- `notebooks/02_abc_xyz_rfm_student.ipynb` — ABC/XYZ/RFM;
- `data/raw/orders_big.csv`, `clients.csv`, `products.csv` — учебные данные;
- `materials/capstone_roadmap.md` — маршрут;
- `materials/data_dictionary.md` — словарь;
- `materials/dataset_selection_guide.md` — выбор датасета;
- `materials/abc_xyz_rfm_guide.md` — ABC/XYZ/RFM;
- `materials/capstone_bi_dashboard_guide.md` — BI;
- `materials/final_submission_instruction.md` — сдача;
- остальные `materials/` — rubric, FAQ, post-assignment и инструкции СДО.

`data/processed/.gitkeep` — это пустая папка для будущих результатов, а не потерянные данные.

---

# Служебные файлы в корне

| Файл | Назначение |
|---|---|
| `README.md` | основной навигатор для слушателя |
| `TOPIC_MAP.md` | короткое соответствие русских тем и английских путей |
| `FILE_INDEX.md` | полный список физических файлов |
| `SOURCE_MANIFEST.csv` | трассировка происхождения материалов |
| `QA_REPORT.md` | технический QA-комплекта |
| `ARCHIVE_VERIFICATION.txt` | контроль архива |
| `requirements.txt` | общее Python-окружение |
| `.gitignore` | исключения Git |

Обычному слушателю в первую очередь нужны `README.md`, папки тем, notebooks и данные. `SOURCE_MANIFEST.csv`, `QA_REPORT.md` и `ARCHIVE_VERIFICATION.txt` нужны для сопровождения и контроля комплекта.

---

# Запуск Python-практики

Находясь в папке конкретного кейса:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установка библиотек:

```bash
pip install -r requirements.txt
```

Запуск Jupyter:

```bash
jupyter lab
```

Если в текущем кейсе нет своего `requirements.txt`, можно использовать корневой.

# Запуск R

Откройте `02_processing/05_r/r_practice/README.md`. Для RStudio используйте `r_data_basics.Rproj`; основная практика — `scripts/student_practice.R`.

# Правила работы с данными

- исходники в `data/raw/` лучше не редактировать;
- результаты сохраняйте в предусмотренные `processed`, `output`, `outputs`;
- не переносите notebook отдельно от его проекта;
- не меняйте имена входных файлов, если на них ссылается notebook;
- `data/bi/` обычно содержит уже подготовленные витрины для BI.

# Почему английские имена не переводятся физически

Русские названия приведены в этом README и `TOPIC_MAP.md`, а физические пути оставлены компактными английскими. Это уменьшает риск проблем с длинными Windows-путями и не ломает относительные ссылки внутри notebooks и Markdown.

Если нужно найти **любой конкретный файл**, откройте [`FILE_INDEX.md`](./FILE_INDEX.md).
