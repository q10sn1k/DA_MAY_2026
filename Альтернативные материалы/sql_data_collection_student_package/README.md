# Комплект для слушателей: сбор данных и основы SQL

Комплект предназначен для самостоятельной и аудиторной работы по темам:

- сбор данных с различных источников;
- основы работы с SQL;
- MySQL, связи таблиц и JOIN;
- резервный вариант SQL без Docker/MySQL на SQLite;
- переход от SQL-результата к pandas DataFrame;
- первичный анализ данных в pandas;
- работа с CSV, Excel и JSON.

## Структура комплекта

```text
sql_data_collection_student_package/
├── README.md
├── requirements.txt
├── docs/
│   ├── lecture_sql_mysql_pandas_for_students.docx
│   ├── 01_mysql_start_crud_beginner_student.md
│   ├── 02_mysql_relations_joins_beginner_student.md
│   └── 00_sqlite_backup_instruction_student.md
├── notebooks/
│   ├── 00_sqlite_backup_no_docker_no_mysql_student.ipynb
│   ├── 03_sql_result_as_dataframe_intro.ipynb
│   ├── 04_assignment_sql_pandas_bridge_student.ipynb
│   ├── 05_after_sql_basic_analysis_in_pandas_student.ipynb
│   ├── 06_extra_data_formats_csv_json_excel_student.ipynb
│   └── 07_extra_assignment_data_cleaning_and_formats_student.ipynb
├── sql/
│   ├── docker-compose.yml
│   ├── mysql_demo_schema.sql
│   └── README_sql.md
└── outputs/
```

## Рекомендуемый порядок работы

1. Прочитайте `docs/lecture_sql_mysql_pandas_for_students.docx`.
2. Пройдите `docs/01_mysql_start_crud_beginner_student.md`: запуск MySQL, база данных, таблица `users`, базовые SQL-команды.
3. Пройдите `docs/02_mysql_relations_joins_beginner_student.md`: таблица `orders`, внешний ключ, подзапросы, `UNION`, `INNER JOIN`, `LEFT JOIN`.
4. Если Docker или MySQL недоступны, используйте `docs/00_sqlite_backup_instruction_student.md` и ноутбук `notebooks/00_sqlite_backup_no_docker_no_mysql_student.ipynb`.
5. Откройте `notebooks/03_sql_result_as_dataframe_intro.ipynb` и посмотрите, как SQL-результат связан с pandas DataFrame.
6. Выполните `notebooks/04_assignment_sql_pandas_bridge_student.ipynb`.
7. Выполните `notebooks/05_after_sql_basic_analysis_in_pandas_student.ipynb`.
8. Выполните `notebooks/06_extra_data_formats_csv_json_excel_student.ipynb`.
9. Выполните дополнительную практику `notebooks/07_extra_assignment_data_cleaning_and_formats_student.ipynb`.

## Установка зависимостей для локального запуска

```bash
pip install -r requirements.txt
```

Для Google Colab обычно достаточно открыть notebook и запускать ячейки сверху вниз. Если библиотека отсутствует, установите её в отдельной ячейке через `!pip install имя_библиотеки`.

## Основной и резервный сценарии

Основной сценарий использует MySQL через Docker Compose. Резервный сценарий использует SQLite через Python и не требует Docker, MySQL и прав администратора.

## Что должно получиться в результате

После прохождения комплекта слушатель должен уметь:

- понимать базовые сущности SQL: база, таблица, строка, столбец, ключ;
- создавать таблицы `users` и `orders`;
- выполнять `SELECT`, `WHERE`, `ORDER BY`, `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`;
- безопасно использовать `UPDATE` и `DELETE` с `WHERE`;
- объяснять связь `users.id = orders.user_id`;
- использовать подзапросы, `UNION`, `INNER JOIN`, `LEFT JOIN`;
- получать SQL-результат как pandas DataFrame;
- выполнять первичный анализ и простую визуализацию;
- читать и сохранять CSV, Excel и JSON.
