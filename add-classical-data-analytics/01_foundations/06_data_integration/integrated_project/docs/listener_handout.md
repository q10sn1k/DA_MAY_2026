# Раздатка для слушателя

## Занятие

**Тема:**  
**«Загрузка и интеграция данных из различных форматов. Инструменты для сбора данных. Основы Python для обработки данных»**

**Программа:** профессиональная переподготовка / повышение квалификации  
**Направление:** аналитик данных  
**Уровень:** начальный

---

# 1. Цель занятия

На занятии вы научитесь проходить базовый путь аналитика данных:

```text
получить данные
↓
загрузить их в Python
↓
проверить качество
↓
объединить несколько источников
↓
посчитать показатели
↓
построить графики
↓
сохранить результат
```

В учебном кейсе используется компания **«РегионМаркет»**.

Компания продает товары в разных регионах.  
Данные приходят из разных источников:

- продажи — CSV;
- товары — Excel;
- регионы — JSON;
- клиенты — CSV;
- план продаж — HTML-таблица.

Главная задача занятия:

> собрать данные из разных файлов в единую аналитическую таблицу и получить первые бизнес-выводы.

---

# 2. Что вы должны уметь после занятия

После занятия вы должны уметь:

- открыть учебный проект;
- запустить Jupyter Notebook / JupyterLab / VS Code;
- загрузить CSV, Excel, JSON и HTML-таблицу;
- посмотреть структуру таблицы;
- понять, что такое `DataFrame` и `Series`;
- проверить типы данных;
- найти пропуски и дубликаты;
- объединить таблицы через `merge`;
- склеить таблицы через `concat`;
- посчитать группировки через `groupby`;
- построить сводную таблицу через `pivot_table`;
- построить базовые графики;
- сохранить результат в CSV, Excel, Parquet или DuckDB;
- понять, как результат Python можно передать в R.

---

# 3. Структура учебного проекта

Ожидаемая структура проекта:

```text
data_loading_integration_python/
│
├── data/
│   ├── raw/
│   │   ├── sales.csv
│   │   ├── products.xlsx
│   │   ├── regions.json
│   │   ├── clients.csv
│   │   └── web_table_sample.html
│   │
│   ├── prepared/
│   │   └── sales_prepared.csv
│   │
│   └── output/
│
├── notebooks_student/
│   ├── 00_setup_and_check.ipynb
│   ├── 01_data_loading_formats.ipynb
│   ├── 02_dataframe_types_and_quality.ipynb
│   ├── 03_data_integration.ipynb
│   ├── 04_basic_analysis.ipynb
│   ├── 05_basic_visualization.ipynb
│   └── 06_python_to_r_bridge.ipynb
│
├── r/
│   ├── install_packages.R
│   ├── 01_read_python_result.R
│   ├── 02_duckdb_from_r.R
│   └── 03_basic_r_visualization.R
│
├── docs/
│   ├── vscode_workflow.md
│   ├── offline_install_guide.md
│   ├── software_alternatives_ru.md
│   └── listener_handout.md
│
├── requirements.txt
├── environment_check.py
└── README.md
```

---

# 4. Назначение основных папок

| Папка | Назначение |
|---|---|
| `data/raw/` | Исходные учебные данные |
| `data/prepared/` | Подготовленные данные после объединения |
| `data/output/` | Результаты анализа, отчеты, графики |
| `notebooks_student/` | Ноутбуки для самостоятельной работы слушателя |
| `notebooks_teacher/` | Версии ноутбуков для лектора |
| `r/` | R-скрипты для чтения результатов Python |
| `docs/` | Инструкции и раздаточные материалы |

---

# 5. Учебные файлы данных

| Файл | Формат | Что внутри |
|---|---|---|
| `sales.csv` | CSV | Основная таблица продаж |
| `products.xlsx` | Excel | Справочник товаров |
| `regions.json` | JSON | Справочник регионов |
| `clients.csv` | CSV | Справочник клиентов |
| `web_table_sample.html` | HTML | Таблица планов продаж |

Главная таблица — `sales.csv`.

Остальные таблицы нужны, чтобы дополнить продажи:

```text
sales.csv
   │
   ├── product_id → products.xlsx
   ├── region_id  → regions.json
   └── client_id  → clients.csv
```

План продаж соединяется по нескольким полям:

```text
region_id + channel + month
```

---

# 6. Как открыть проект

## Вариант 1. Через VS Code

1. Откройте VS Code.
2. Выберите:

```text
File → Open Folder...
```

3. Выберите корневую папку проекта.
4. Убедитесь, что слева видны папки:

```text
data/
notebooks_student/
r/
docs/
```

5. Откройте нужный ноутбук из папки:

```text
notebooks_student/
```

## Вариант 2. Через JupyterLab

Откройте терминал в корне проекта и выполните:

```bash
python -m jupyter lab
```

Затем в браузере откройте папку:

```text
notebooks_student/
```

---

# 7. Как проверить Python-окружение

В терминале из корня проекта выполните:

```bash
python environment_check.py
```

Если окружение готово, вы увидите сообщение вида:

```text
ОКРУЖЕНИЕ ГОТОВО
```

Если появилась ошибка `ModuleNotFoundError`, значит не установлена библиотека или выбран не тот Python-интерпретатор.

---

# 8. Как запускать ноутбуки

Рекомендуемый порядок:

```text
00_setup_and_check.ipynb
01_data_loading_formats.ipynb
02_dataframe_types_and_quality.ipynb
03_data_integration.ipynb
04_basic_analysis.ipynb
05_basic_visualization.ipynb
06_python_to_r_bridge.ipynb
```

## Почему порядок важен

Ноутбук:

```text
03_data_integration.ipynb
```

создает файл:

```text
data/prepared/sales_prepared.csv
```

Этот файл нужен для следующих ноутбуков:

```text
04_basic_analysis.ipynb
05_basic_visualization.ipynb
06_python_to_r_bridge.ipynb
```

---

# 9. Как запускать ячейки

В Jupyter Notebook / JupyterLab / VS Code ноутбук состоит из ячеек.

| Тип ячейки | Что внутри |
|---|---|
| Markdown | Текст, инструкция, пояснение |
| Code | Python-код |

Запустить ячейку:

```text
Shift + Enter
```

Или нажать кнопку:

```text
▶
```

Лучше запускать ячейки сверху вниз.

Если запускать ячейки в случайном порядке, переменные могут быть не созданы.

---

# 10. Мини-шпаргалка: импорт библиотек

Обычно в начале ноутбука пишем:

```python
import pandas as pd
from pathlib import Path
```

Для графиков:

```python
import matplotlib.pyplot as plt
```

Для DuckDB:

```python
import duckdb
```

---

# 11. Мини-шпаргалка: пути к файлам

Используем `Path`, чтобы аккуратно работать с путями:

```python
from pathlib import Path

DATA_DIR = Path("data/raw")
sales_path = DATA_DIR / "sales.csv"
```

Проверить, существует ли файл:

```python
sales_path.exists()
```

Посмотреть текущую рабочую папку:

```python
Path.cwd()
```

---

# 12. pandas: что такое DataFrame и Series

## DataFrame

`DataFrame` — это таблица в pandas.

Пример:

```python
sales = pd.read_csv("data/raw/sales.csv")
```

`sales` — это `DataFrame`.

## Series

`Series` — это один столбец таблицы.

Пример:

```python
sales["channel"]
```

---

# 13. Шпаргалка: первичный осмотр таблицы

После загрузки таблицы всегда выполните несколько проверок.

```python
df.head()
```

Первые 5 строк.

```python
df.tail()
```

Последние 5 строк.

```python
df.shape
```

Количество строк и столбцов.

```python
df.columns
```

Названия столбцов.

```python
df.info()
```

Общая информация: типы, пропуски, память.

```python
df.dtypes
```

Типы данных по столбцам.

```python
df.isna().sum()
```

Количество пропусков.

```python
df.duplicated().sum()
```

Количество полных дубликатов строк.

---

# 14. Загрузка CSV

Основная команда:

```python
sales = pd.read_csv("data/raw/sales.csv")
```

С явным указанием кодировки:

```python
sales = pd.read_csv("data/raw/sales.csv", encoding="utf-8")
```

С указанием разделителя:

```python
sales = pd.read_csv("data/raw/sales.csv", sep=",")
```

Если файл разделен точкой с запятой:

```python
df = pd.read_csv("file.csv", sep=";")
```

---

# 15. Загрузка Excel

Прочитать Excel-файл:

```python
products = pd.read_excel("data/raw/products.xlsx")
```

Прочитать конкретный лист:

```python
products = pd.read_excel(
    "data/raw/products.xlsx",
    sheet_name="products"
)
```

Посмотреть список листов:

```python
excel_file = pd.ExcelFile("data/raw/products.xlsx")
excel_file.sheet_names
```

---

# 16. Загрузка JSON

Прочитать JSON:

```python
regions = pd.read_json("data/raw/regions.json")
```

Проверить результат:

```python
regions.head()
regions.info()
```

---

# 17. Загрузка HTML-таблицы

Прочитать таблицы из HTML:

```python
tables = pd.read_html("data/raw/web_table_sample.html")
```

`read_html()` возвращает список таблиц.

Взять первую таблицу:

```python
plans = tables[0]
```

---

# 18. Шпаргалка: типовые ошибки загрузки файлов

## FileNotFoundError

Файл не найден.

Что проверить:

```python
from pathlib import Path

print(Path.cwd())
print(Path("data/raw/sales.csv").exists())
```

Частая причина: проект открыт не из корневой папки.

## UnicodeDecodeError

Python не смог прочитать кодировку файла.

Попробуйте:

```python
pd.read_csv("file.csv", encoding="utf-8")
pd.read_csv("file.csv", encoding="utf-8-sig")
pd.read_csv("file.csv", encoding="cp1251")
```

## ParserError

CSV имеет неожиданную структуру.

Проверьте разделитель:

```python
pd.read_csv("file.csv", sep=",")
pd.read_csv("file.csv", sep=";")
pd.read_csv("file.csv", sep="\t")
```

---

# 19. Преобразование типов данных

## Числа

Если столбец должен быть числом:

```python
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
```

`errors="coerce"` означает:

> если значение нельзя преобразовать, заменить его на `NaN`.

## Даты

Если столбец должен быть датой:

```python
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
```

Создать месяц:

```python
df["month"] = df["order_date"].dt.to_period("M").astype(str)
```

## Строки

Убрать пробелы:

```python
df["channel"] = df["channel"].str.strip()
```

Привести к нижнему регистру:

```python
df["channel"] = df["channel"].str.lower()
```

Сразу оба действия:

```python
df["channel"] = (
    df["channel"]
    .astype("string")
    .str.strip()
    .str.lower()
)
```

---

# 20. Пропуски

Посчитать пропуски:

```python
df.isna().sum()
```

Посмотреть строки с пропуском в столбце:

```python
df[df["unit_price"].isna()]
```

Заполнить пропуски нулем:

```python
df["discount_percent"] = df["discount_percent"].fillna(0)
```

Важно:

> Заполнять пропуски можно только тогда, когда это логично по бизнес-смыслу.

---

# 21. Дубликаты

Посчитать полные дубликаты:

```python
df.duplicated().sum()
```

Посмотреть дубликаты:

```python
df[df.duplicated(keep=False)]
```

Дубликаты по ключу:

```python
df.duplicated(subset=["sale_id"]).sum()
```

Удалить дубликаты по ключу:

```python
df = df.drop_duplicates(subset=["sale_id"], keep="first")
```

---

# 22. Создание расчетных столбцов

Пример: выручка без учета скидки:

```python
df["gross_revenue"] = df["quantity"] * df["unit_price"]
```

Сумма скидки:

```python
df["discount_amount"] = (
    df["gross_revenue"] * df["discount_percent"] / 100
)
```

Выручка после скидки:

```python
df["net_revenue"] = df["gross_revenue"] - df["discount_amount"]
```

Валовая прибыль:

```python
df["gross_profit"] = df["net_revenue"] - df["purchase_cost"]
```

---

# 23. Фильтрация строк

## Одно условие

```python
df[df["channel"] == "online"]
```

## Числовое условие

```python
df[df["net_revenue"] > 50000]
```

## Несколько условий

```python
df[
    (df["channel"] == "online") &
    (df["net_revenue"] > 50000)
]
```

Важно:

> Каждое условие нужно брать в скобки.

## Несколько значений через `isin`

```python
df[df["channel"].isin(["online", "marketplace"])]
```

---

# 24. Сортировка

По одному столбцу:

```python
df.sort_values("net_revenue", ascending=False)
```

По нескольким столбцам:

```python
df.sort_values(
    by=["region_name", "net_revenue"],
    ascending=[True, False]
)
```

Топ-10 продаж:

```python
df.sort_values("net_revenue", ascending=False).head(10)
```

---

# 25. Объединение таблиц: merge

`merge()` нужен, чтобы соединить таблицы по ключу.

Пример:

```python
sales_products = sales.merge(
    products,
    on="product_id",
    how="left"
)
```

## Основные виды join

| Вид join | Что делает |
|---|---|
| `left` | оставляет все строки из левой таблицы |
| `inner` | оставляет только совпавшие строки |
| `outer` | оставляет все ключи из обеих таблиц |

## left join

```python
sales.merge(products, on="product_id", how="left")
```

Используем, когда продажи — главная таблица, и мы не хотим потерять строки продаж.

## inner join

```python
sales.merge(products, on="product_id", how="inner")
```

Оставит только продажи, где товар найден в справочнике.

## outer join

```python
sales.merge(products, on="product_id", how="outer")
```

Покажет все ключи из обеих таблиц.

---

# 26. Проверка результата после merge

Количество строк до и после:

```python
rows_before = sales.shape[0]

merged = sales.merge(
    products,
    on="product_id",
    how="left"
)

rows_after = merged.shape[0]

print(rows_before)
print(rows_after)
```

Диагностика через `_merge`:

```python
merged = sales.merge(
    products,
    on="product_id",
    how="left",
    indicator=True
)

merged["_merge"].value_counts()
```

Контроль связи:

```python
sales.merge(
    products,
    on="product_id",
    how="left",
    validate="many_to_one"
)
```

`many_to_one` означает:

> в продажах одному товару может соответствовать много строк, но в справочнике один `product_id` должен быть только один раз.

---

# 27. Почему после merge появляются NaN

Если после объединения появились `NaN`, это часто означает:

> ключ есть в основной таблице, но не найден в справочнике.

Пример:

```python
missing_products = merged[merged["product_name"].isna()]
```

Что проверить:

```python
set(sales["product_id"]) - set(products["product_id"])
```

---

# 28. Склейка таблиц: concat

`concat()` нужен, когда нужно склеить таблицы по строкам.

Пример:

```python
sales_all = pd.concat(
    [sales_january, sales_february],
    ignore_index=True
)
```

Когда использовать:

- есть несколько файлов с одинаковой структурой;
- нужно соединить продажи за разные месяцы;
- нужно добавить новые строки под старые.

Отличие:

| Команда | Для чего |
|---|---|
| `merge` | соединить таблицы по ключу |
| `concat` | склеить таблицы по строкам или столбцам |

---

# 29. Группировка: groupby

`groupby()` нужен, чтобы посчитать показатели по группам.

Пример:

```python
df.groupby("category")["net_revenue"].sum()
```

Читается так:

> сгруппировать строки по категории и сложить выручку внутри каждой категории.

## Выручка по категориям

```python
category_revenue = (
    df
    .groupby("category")["net_revenue"]
    .sum()
    .sort_values(ascending=False)
)
```

## Выручка по регионам

```python
region_revenue = (
    df
    .groupby("region_name")["net_revenue"]
    .sum()
    .sort_values(ascending=False)
)
```

---

# 30. Несколько показателей: agg

`agg()` нужен, чтобы посчитать несколько показателей сразу.

```python
category_summary = (
    df
    .groupby("category")
    .agg(
        orders_count=("sale_id", "nunique"),
        total_quantity=("quantity", "sum"),
        total_revenue=("net_revenue", "sum"),
        avg_revenue=("net_revenue", "mean"),
        total_profit=("gross_profit", "sum"),
    )
    .reset_index()
    .sort_values("total_revenue", ascending=False)
)
```

---

# 31. Сводная таблица: pivot_table

`pivot_table()` похожа на сводную таблицу в Excel.

Пример:

```python
revenue_pivot = pd.pivot_table(
    df,
    values="net_revenue",
    index="region_name",
    columns="category",
    aggfunc="sum",
    fill_value=0
)
```

Расшифровка:

| Параметр | Что означает |
|---|---|
| `values` | какой показатель считаем |
| `index` | что будет в строках |
| `columns` | что будет в столбцах |
| `aggfunc` | как считаем |
| `fill_value` | чем заменить пустые значения |

---

# 32. Первичная статистика: describe

По числовым столбцам:

```python
df[["quantity", "unit_price", "net_revenue"]].describe()
```

По текстовым столбцам:

```python
df.describe(include="object")
```

`describe()` помогает быстро увидеть:

- количество значений;
- среднее;
- минимум;
- максимум;
- квартили;
- наиболее частые текстовые значения.

---

# 33. Корреляция: corr

Корреляция показывает связь между числовыми показателями.

```python
df[[
    "quantity",
    "unit_price",
    "discount_percent",
    "net_revenue",
    "gross_profit"
]].corr()
```

Важно:

> Корреляция не доказывает причинно-следственную связь.

---

# 34. Визуализация: базовые графики

Для графиков используем:

```python
import matplotlib.pyplot as plt
```

## Динамика продаж

```python
daily_revenue = (
    df
    .groupby("order_date", as_index=False)
    .agg(total_revenue=("net_revenue", "sum"))
    .sort_values("order_date")
)

plt.figure(figsize=(10, 5))
plt.plot(daily_revenue["order_date"], daily_revenue["total_revenue"], marker="o")
plt.title("Динамика выручки по датам")
plt.xlabel("Дата")
plt.ylabel("Выручка")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
```

## Продажи по категориям

```python
category_revenue = (
    df
    .groupby("category", as_index=False)
    .agg(total_revenue=("net_revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
)

plt.figure(figsize=(10, 5))
plt.bar(category_revenue["category"], category_revenue["total_revenue"])
plt.title("Выручка по категориям")
plt.xlabel("Категория")
plt.ylabel("Выручка")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## Топ регионов

```python
top_regions = (
    df
    .groupby("region_name", as_index=False)
    .agg(total_revenue=("net_revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
    .head(10)
)

top_regions_for_plot = top_regions.sort_values("total_revenue")

plt.figure(figsize=(10, 6))
plt.barh(top_regions_for_plot["region_name"], top_regions_for_plot["total_revenue"])
plt.title("Топ регионов по выручке")
plt.xlabel("Выручка")
plt.ylabel("Регион")
plt.tight_layout()
plt.show()
```

## Распределение чеков

```python
plt.figure(figsize=(10, 5))
plt.hist(df["net_revenue"].dropna(), bins=15)
plt.title("Распределение суммы заказа")
plt.xlabel("Сумма заказа")
plt.ylabel("Количество заказов")
plt.tight_layout()
plt.show()
```

## Boxplot по категориям

```python
boxplot_data = []
boxplot_labels = []

for category, group in df.groupby("category"):
    values = group["net_revenue"].dropna()
    if not values.empty:
        boxplot_data.append(values)
        boxplot_labels.append(str(category))

plt.figure(figsize=(10, 5))
plt.boxplot(boxplot_data, labels=boxplot_labels)
plt.title("Распределение суммы заказа по категориям")
plt.xlabel("Категория")
plt.ylabel("Сумма заказа")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

## Scatter plot

```python
plt.figure(figsize=(8, 5))
plt.scatter(df["unit_price"], df["quantity"])
plt.title("Связь цены и количества")
plt.xlabel("Цена за единицу")
plt.ylabel("Количество")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---

# 35. Какой график выбрать

| Вопрос | График |
|---|---|
| Как меняется показатель во времени? | `plt.plot()` |
| Какая категория больше? | `plt.bar()` |
| Какие регионы в топе? | `plt.barh()` |
| Как распределены чеки? | `plt.hist()` |
| Где есть выбросы? | `plt.boxplot()` |
| Есть ли связь двух числовых показателей? | `plt.scatter()` |

---

# 36. Сохранение результатов

## В CSV

```python
df.to_csv(
    "data/output/result.csv",
    index=False,
    encoding="utf-8"
)
```

## В Excel

```python
df.to_excel(
    "data/output/result.xlsx",
    index=False,
    sheet_name="result"
)
```

## Несколько листов Excel

```python
with pd.ExcelWriter("data/output/report.xlsx", engine="openpyxl") as writer:
    category_summary.to_excel(writer, sheet_name="category", index=False)
    region_summary.to_excel(writer, sheet_name="regions", index=False)
```

## В Parquet

```python
df.to_parquet(
    "data/output/result.parquet",
    index=False,
    engine="pyarrow"
)
```

## В DuckDB

```python
import duckdb

connection = duckdb.connect("data/output/analytics.duckdb")

connection.register("df_view", df)
connection.execute("CREATE TABLE sales_prepared AS SELECT * FROM df_view")
connection.unregister("df_view")

connection.close()
```

---

# 37. Сохранение графика

Важно: `savefig()` вызывается до `show()`.

```python
plt.figure(figsize=(10, 5))
plt.bar(category_revenue["category"], category_revenue["total_revenue"])
plt.title("Выручка по категориям")
plt.xlabel("Категория")
plt.ylabel("Выручка")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/output/figures/category_revenue.png", dpi=150)

plt.show()
```

---

# 38. Python → R: что нужно запомнить

Python может подготовить данные и сохранить их:

```text
CSV
Excel
Parquet
DuckDB
```

R может прочитать эти файлы:

| Формат | R-пакет | Команда |
|---|---|---|
| CSV | `readr` | `read_csv()` |
| Excel | `readxl` | `read_excel()` |
| Parquet | `arrow` | `read_parquet()` |
| DuckDB | `DBI` + `duckdb` | `dbConnect()`, `dbGetQuery()` |

Пример R-кода для CSV:

```r
library(readr)

sales <- read_csv("data/output/python_to_r/sales_prepared_for_r.csv")

head(sales)
```

Пример R-кода для DuckDB:

```r
library(DBI)
library(duckdb)

con <- dbConnect(
  duckdb::duckdb(),
  dbdir = "data/output/python_to_r/analytics.duckdb",
  read_only = TRUE
)

result <- dbGetQuery(con, "
  SELECT category, SUM(net_revenue) AS total_revenue
  FROM sales_prepared
  GROUP BY category
  ORDER BY total_revenue DESC
")

result

dbDisconnect(con, shutdown = TRUE)
```

---

# 39. Типовые ошибки и что делать

## Ошибка: файл не найден

Проверьте:

```python
from pathlib import Path

print(Path.cwd())
print(Path("data/raw/sales.csv").exists())
```

## Ошибка: нет библиотеки

Пример:

```text
ModuleNotFoundError: No module named 'pandas'
```

Что сделать:

```bash
pip install -r requirements.txt
```

Или проверить выбранный Python / Kernel.

## Ошибка: переменная не определена

Пример:

```text
NameError: name 'sales' is not defined
```

Причина: не была выполнена ячейка, где создается переменная.

Решение: запустить ноутбук сверху вниз.

## Ошибка: график не отображается

Проверьте, что написано:

```python
plt.show()
```

а не:

```python
plt.show
```

## Ошибка: после merge стало больше строк

Возможная причина: дубликаты в справочнике.

Проверьте:

```python
products.duplicated(subset=["product_id"]).sum()
```

Используйте:

```python
validate="many_to_one"
```

## Ошибка: после merge появились NaN

Проверьте ключи:

```python
set(sales["product_id"]) - set(products["product_id"])
```

---

# 40. Мини-чек-лист перед сдачей результата

Перед тем как считать задачу выполненной, проверьте:

- [ ] данные загружены без ошибок;
- [ ] `df.head()` показывает нормальную таблицу;
- [ ] `df.shape` соответствует ожиданиям;
- [ ] типы данных проверены через `df.info()`;
- [ ] даты преобразованы через `pd.to_datetime()`;
- [ ] числовые поля преобразованы через `pd.to_numeric()`;
- [ ] пропуски проверены через `isna().sum()`;
- [ ] дубликаты проверены через `duplicated()`;
- [ ] после `merge` количество строк проверено;
- [ ] после `merge` проверены `NaN`;
- [ ] итоговая таблица сохранена;
- [ ] аналитические таблицы сохранены;
- [ ] графики имеют заголовки и подписи осей.

---

# 41. Мини-глоссарий

| Термин | Простое объяснение |
|---|---|
| DataFrame | Таблица pandas |
| Series | Один столбец pandas |
| CSV | Текстовый файл с таблицей |
| Excel | Табличный файл `.xlsx` |
| JSON | Формат обмена данными, часто используется в API |
| HTML-таблица | Таблица внутри веб-страницы |
| merge | Объединение таблиц по ключу |
| concat | Склейка таблиц по строкам или столбцам |
| left join | Сохраняет все строки из левой таблицы |
| inner join | Оставляет только совпавшие строки |
| groupby | Группировка данных для расчета показателей |
| agg | Расчет нескольких показателей сразу |
| pivot_table | Сводная таблица |
| NaN | Пропуск в данных |
| dtype | Тип данных столбца |
| correlation | Связь между числовыми показателями |

---

# 42. Краткая последовательность работы аналитика

```text
1. Открыть проект
2. Проверить окружение
3. Загрузить данные
4. Посмотреть head, shape, columns, info
5. Проверить типы
6. Исправить даты, числа и строки
7. Проверить пропуски и дубликаты
8. Объединить таблицы
9. Проверить результат merge
10. Посчитать revenue, profit и другие показатели
11. Сделать groupby / agg / pivot_table
12. Построить графики
13. Сохранить результаты
14. Сформулировать выводы
```

---

# 43. Что можно использовать как итог занятия

Итогом занятия могут быть файлы:

```text
data/prepared/sales_prepared.csv
data/output/basic_analysis_report.xlsx
data/output/figures/category_revenue.png
data/output/figures/daily_revenue.png
data/output/python_to_r/sales_prepared_for_r.csv
data/output/python_to_r/analytics.duckdb
```

---

# 44. Источники и справочные материалы

Официальная документация:

- pandas I/O tools: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
- pandas `read_csv`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- pandas `merge`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
- pandas `groupby`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
- pandas pivot tables: https://pandas.pydata.org/docs/user_guide/reshaping.html
- pandas visualization: https://pandas.pydata.org/docs/user_guide/visualization.html
- Jupyter documentation: https://docs.jupyter.org/
