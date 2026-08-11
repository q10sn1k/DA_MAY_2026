# Раздатка: groupby для начинающих

## Тема

**Группировка данных в pandas: `groupby()`**

Эта раздатка предназначена для слушателей начального уровня.  
Цель — понять, как с помощью `groupby()` отвечать на бизнес-вопросы:

- какая категория дает больше выручки;
- какой регион лидирует по продажам;
- какой канал продаж приносит больше заказов;
- какой средний чек у разных групп;
- как посчитать несколько показателей сразу.

---

# 1. Зачем аналитику нужен groupby

Когда аналитик получает таблицу продаж, каждая строка обычно описывает отдельную продажу или заказ.

Пример:

| sale_id | category | region_name | channel | quantity | revenue |
|---:|---|---|---|---:|---:|
| 1 | электроника | Москва | online | 2 | 120000 |
| 2 | одежда | Казань | offline | 1 | 5000 |
| 3 | электроника | Москва | online | 1 | 60000 |
| 4 | мебель | Казань | marketplace | 1 | 30000 |
| 5 | одежда | Москва | offline | 3 | 15000 |

Но бизнес редко спрашивает:

> сколько принесла продажа № 1?

Чаще бизнес спрашивает:

- сколько выручки дала каждая категория;
- какой регион лидирует;
- какой канал продаж эффективнее;
- сколько заказов было по каждому направлению;
- где выше средний чек.

Чтобы ответить на такие вопросы, нужно не смотреть каждую строку отдельно, а **сгруппировать строки по нужному признаку**.

Для этого используется `groupby()`.

---

# 2. Бытовая аналогия

Представьте, что у вас есть стопка чеков из магазина.

На каждом чеке написано:

- категория товара;
- регион;
- канал продаж;
- сумма покупки.

Чтобы понять, сколько денег принесла каждая категория, вы делаете три действия:

```text
разделить чеки по категориям
↓
сложить суммы внутри каждой стопки
↓
записать итоговую таблицу
```

Например:

```text
электроника → сложили все чеки → 180000
одежда      → сложили все чеки → 20000
мебель      → сложили все чеки → 30000
```

Это и есть логика `groupby`.

---

# 3. Главный принцип groupby

`groupby()` работает по принципу:

```text
разделить → посчитать → собрать результат
```

В английской документации pandas эта идея называется:

```text
split → apply → combine
```

## 3.1. Разделить

pandas делит таблицу на группы по значениям одного или нескольких столбцов.

Например, по категории:

```text
электроника
одежда
мебель
```

## 3.2. Посчитать

Для каждой группы pandas применяет расчет:

- сумма;
- среднее;
- количество;
- минимум;
- максимум;
- несколько расчетов сразу.

## 3.3. Собрать результат

pandas собирает итоги в новую таблицу или Series.

---

# 4. Мини-пример на маленькой таблице

Создадим учебную таблицу:

```python
import pandas as pd

sales = pd.DataFrame({
    "sale_id": [1, 2, 3, 4, 5],
    "category": ["электроника", "одежда", "электроника", "мебель", "одежда"],
    "region_name": ["Москва", "Казань", "Москва", "Казань", "Москва"],
    "channel": ["online", "offline", "online", "marketplace", "offline"],
    "quantity": [2, 1, 1, 1, 3],
    "revenue": [120000, 5000, 60000, 30000, 15000],
})
```

Посмотрим таблицу:

```python
sales
```

---

# 5. Самый простой groupby

## 5.1. Выручка по категориям

Вопрос:

> сколько выручки принесла каждая категория?

Код:

```python
sales.groupby("category")["revenue"].sum()
```

Читается так:

```text
взять таблицу sales
↓
разделить строки по category
↓
в каждой группе взять revenue
↓
сложить revenue
```

Ожидаемый результат:

| category | revenue |
|---|---:|
| мебель | 30000 |
| одежда | 20000 |
| электроника | 180000 |

---

# 6. Почему результат иногда выглядит как Series

Команда:

```python
sales.groupby("category")["revenue"].sum()
```

часто возвращает `Series`, где категория становится индексом.

Для начинающих удобнее получить обычную таблицу.

Используйте:

```python
category_revenue = (
    sales
    .groupby("category", as_index=False)
    .agg(total_revenue=("revenue", "sum"))
)

category_revenue
```

Результат будет DataFrame:

| category | total_revenue |
|---|---:|
| мебель | 30000 |
| одежда | 20000 |
| электроника | 180000 |

---

# 7. groupby по категориям

## 7.1. Выручка по категориям

```python
category_revenue = (
    sales
    .groupby("category", as_index=False)
    .agg(total_revenue=("revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
)

category_revenue
```

Что делает код:

| Часть кода | Объяснение |
|---|---|
| `groupby("category")` | разделить таблицу по категориям |
| `agg(...)` | посчитать показатели |
| `total_revenue=("revenue", "sum")` | сложить выручку и назвать столбец `total_revenue` |
| `sort_values(...)` | отсортировать результат по выручке |

---

## 7.2. Количество заказов по категориям

```python
category_orders = (
    sales
    .groupby("category", as_index=False)
    .agg(orders_count=("sale_id", "count"))
    .sort_values("orders_count", ascending=False)
)

category_orders
```

Если `sale_id` уникален для каждого заказа, можно использовать:

```python
orders_count=("sale_id", "nunique")
```

`nunique` считает количество уникальных значений.

---

## 7.3. Несколько показателей по категориям

```python
category_summary = (
    sales
    .groupby("category", as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean"),
        min_revenue=("revenue", "min"),
        max_revenue=("revenue", "max"),
    )
    .sort_values("total_revenue", ascending=False)
)

category_summary
```

Такой вариант ближе к реальной аналитике.

---

# 8. groupby по регионам

## 8.1. Вопрос

> какие регионы дают максимальную выручку?

Код:

```python
region_revenue = (
    sales
    .groupby("region_name", as_index=False)
    .agg(total_revenue=("revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
)

region_revenue
```

---

## 8.2. Выручка и количество заказов по регионам

```python
region_summary = (
    sales
    .groupby("region_name", as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

region_summary
```

## Как объяснить слушателям

> Мы разложили все продажи по регионам. Внутри каждого региона посчитали количество заказов, количество товаров, общую выручку и средний чек.

---

# 9. groupby по каналам продаж

## 9.1. Вопрос

> какой канал продаж приносит больше выручки?

Код:

```python
channel_summary = (
    sales
    .groupby("channel", as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

channel_summary
```

## Пример интерпретации

Если `online` дает максимальную выручку, это не обязательно значит, что он самый прибыльный.  
Нужно дополнительно смотреть прибыль, скидки, возвраты и затраты.

---

# 10. groupby по нескольким столбцам

Иногда нужно сгруппировать данные сразу по двум признакам.

Например:

> сколько выручки дает каждый канал в каждом регионе?

Код:

```python
region_channel_summary = (
    sales
    .groupby(["region_name", "channel"], as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

region_channel_summary
```

Читается так:

```text
сначала разделить по региону
↓
внутри каждого региона разделить по каналу
↓
посчитать показатели
↓
собрать итоговую таблицу
```

---

# 11. groupby после объединения данных

В реальном кейсе `groupby` обычно применяется не к сырым данным, а к подготовленной таблице.

Например, после `merge` у нас есть таблица:

```text
sales_prepared.csv
```

В ней уже есть:

- продажи;
- товары;
- категории;
- регионы;
- клиенты;
- каналы;
- выручка;
- прибыль.

Пример:

```python
df = pd.read_csv("data/prepared/sales_prepared.csv")
```

Если дата нужна для анализа динамики:

```python
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
```

Если `revenue` еще нет:

```python
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount_percent"] / 100)
```

Теперь можно считать аналитику:

```python
df.groupby("category", as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

---

# 12. Типовые функции агрегации

| Функция | Что считает | Пример бизнес-вопроса |
|---|---|---|
| `sum` | сумма | какая общая выручка по категориям |
| `mean` | среднее | какой средний чек |
| `count` | количество непустых строк | сколько записей в группе |
| `nunique` | количество уникальных значений | сколько уникальных заказов |
| `min` | минимум | минимальный чек |
| `max` | максимум | максимальный чек |
| `median` | медиана | типичный чек без сильного влияния выбросов |

Пример:

```python
summary = (
    df
    .groupby("category", as_index=False)
    .agg(
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean"),
        median_revenue=("revenue", "median"),
        max_revenue=("revenue", "max"),
    )
)
```

---

# 13. Разница между count и nunique

## count

`count` считает количество непустых значений.

```python
orders_count=("sale_id", "count")
```

## nunique

`nunique` считает количество уникальных значений.

```python
orders_count=("sale_id", "nunique")
```

Если в таблице одна строка — одна продажа, результат может совпадать.  
Если один заказ может занимать несколько строк, лучше использовать `nunique`.

Пример:

| order_id | product_id | revenue |
|---:|---:|---:|
| 1 | 101 | 1000 |
| 1 | 102 | 500 |
| 2 | 103 | 700 |

`count` по `order_id` даст 3 строки.  
`nunique` по `order_id` даст 2 заказа.

---

# 14. Средний чек

Если каждая строка — отдельная продажа, можно посчитать средний чек так:

```python
avg_check=("revenue", "mean")
```

Если один заказ может занимать несколько строк, лучше сначала агрегировать до уровня заказа, а потом считать средний чек.

Упрощенный вариант для занятия:

```python
category_summary = (
    df
    .groupby("category", as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
    )
)

category_summary["avg_check"] = (
    category_summary["total_revenue"] / category_summary["orders_count"]
)
```

---

# 15. Связь groupby и графиков

`groupby` часто нужен перед графиком.

Например, чтобы построить график выручки по категориям, сначала нужно подготовить таблицу:

```python
category_revenue = (
    df
    .groupby("category", as_index=False)
    .agg(total_revenue=("revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
)
```

А потом построить график:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(category_revenue["category"], category_revenue["total_revenue"])
plt.title("Выручка по категориям")
plt.xlabel("Категория")
plt.ylabel("Выручка")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

# 16. Типовая структура кода groupby

Запомните шаблон:

```python
result = (
    df
    .groupby("столбец_группировки", as_index=False)
    .agg(
        новое_имя_показателя=("исходный_столбец", "функция")
    )
    .sort_values("новое_имя_показателя", ascending=False)
)
```

Пример:

```python
category_summary = (
    df
    .groupby("category", as_index=False)
    .agg(
        total_revenue=("revenue", "sum")
    )
    .sort_values("total_revenue", ascending=False)
)
```

---

# 17. Типовые ошибки начинающих

## Ошибка 1. Забыли выбрать числовой столбец

Непонятный или слишком большой результат:

```python
df.groupby("category").sum()
```

pandas может попытаться суммировать все числовые столбцы сразу.

Лучше явно указать столбцы:

```python
df.groupby("category")["revenue"].sum()
```

или:

```python
df.groupby("category", as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

---

## Ошибка 2. Столбец с выручкой не числовой

Ошибка или странный результат:

```python
df.groupby("category")["revenue"].sum()
```

Если `revenue` текстовый, сумма может не работать корректно.

Проверить:

```python
df["revenue"].dtype
```

Исправить:

```python
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
```

---

## Ошибка 3. Неверное имя столбца

Ошибка:

```text
KeyError: 'revenue'
```

Причина: такого столбца нет или он называется иначе.

Проверить:

```python
df.columns.tolist()
```

---

## Ошибка 4. Получили Series, а хотели таблицу

Код:

```python
df.groupby("category")["revenue"].sum()
```

Результат может быть Series.

Решения:

```python
df.groupby("category", as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

или:

```python
df.groupby("category")["revenue"].sum().reset_index()
```

---

## Ошибка 5. Не отсортировали результат

Без сортировки сложно увидеть лидеров:

```python
df.groupby("category", as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

Лучше:

```python
df.groupby("category", as_index=False).agg(
    total_revenue=("revenue", "sum")
).sort_values("total_revenue", ascending=False)
```

---

## Ошибка 6. Пропуски в группирующем столбце исчезли

По умолчанию группы с пропусками могут не попадать в результат.

Если нужно учитывать пропуски:

```python
df.groupby("category", dropna=False, as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

Так можно увидеть группу `NaN`.

---

## Ошибка 7. Путают `count` и `nunique`

```python
orders_count=("sale_id", "count")
```

считает строки.

```python
orders_count=("sale_id", "nunique")
```

считает уникальные продажи или заказы.

Если один заказ может занимать несколько строк, используйте `nunique`.

---

## Ошибка 8. Делают groupby до очистки данных

Например, в столбце `channel` есть значения:

```text
online
Online
 online
ONLINE
```

Если сгруппировать сразу, получится несколько разных групп.

Сначала очистить:

```python
df["channel"] = (
    df["channel"]
    .astype("string")
    .str.strip()
    .str.lower()
)
```

Потом группировать:

```python
df.groupby("channel", as_index=False).agg(
    total_revenue=("revenue", "sum")
)
```

---

## Ошибка 9. Делают вывод только по выручке

Высокая выручка не всегда означает высокую прибыль.

Лучше считать несколько показателей:

```python
category_summary = (
    df
    .groupby("category", as_index=False)
    .agg(
        total_revenue=("revenue", "sum"),
        total_profit=("gross_profit", "sum"),
        avg_check=("revenue", "mean"),
    )
)
```

---

# 18. Как проверить результат groupby

После группировки проверьте:

## 18.1. Количество групп

```python
category_summary.shape
```

## 18.2. Сумма до и после

Если вы считаете сумму выручки по категориям, общая сумма должна совпадать:

```python
df["revenue"].sum()
category_summary["total_revenue"].sum()
```

Если суммы сильно отличаются, нужно искать причину.

## 18.3. Пропуски

```python
category_summary.isna().sum()
```

## 18.4. Лидеры

```python
category_summary.head()
```

## 18.5. Аутсайдеры

```python
category_summary.tail()
```

---

# 19. Примеры для учебного кейса «РегионМаркет»

## 19.1. Выручка по категориям

```python
category_summary = (
    df
    .groupby("category", dropna=False, as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
        total_profit=("gross_profit", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

category_summary
```

## 19.2. Выручка по регионам

```python
region_summary = (
    df
    .groupby("region_name", dropna=False, as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
        total_profit=("gross_profit", "sum"),
    )
    .sort_values("total_revenue", ascending=False)
)

region_summary
```

## 19.3. Выручка по каналам продаж

```python
channel_summary = (
    df
    .groupby("channel", dropna=False, as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

channel_summary
```

## 19.4. Регионы и каналы вместе

```python
region_channel_summary = (
    df
    .groupby(["region_name", "channel"], dropna=False, as_index=False)
    .agg(
        orders_count=("sale_id", "nunique"),
        total_revenue=("revenue", "sum"),
        total_profit=("gross_profit", "sum"),
        avg_check=("revenue", "mean"),
    )
    .sort_values("total_revenue", ascending=False)
)

region_channel_summary
```

---

# 20. Как объяснить groupby за 1 минуту

> `groupby()` — это способ сгруппировать строки таблицы по какому-то признаку и посчитать показатель внутри каждой группы.  
> Например, мы можем разделить все продажи по категориям, внутри каждой категории сложить выручку и получить итоговую таблицу «категория → выручка».  
> Логика простая: разделить → посчитать → собрать результат.  
> Сначала выбираем, по чему группируем, потом выбираем, что считаем, потом выбираем функцию: сумма, среднее, количество, максимум или минимум.

---

# 21. Контрольные вопросы

1. Для чего нужен `groupby()`?
2. Что означает принцип «разделить → посчитать → собрать»?
3. Чем `sum` отличается от `mean`?
4. Что считает `count`?
5. Что считает `nunique`?
6. Почему перед `groupby` нужно проверить типы данных?
7. Почему перед `groupby` нужно очистить текстовые значения?
8. Как посчитать выручку по категориям?
9. Как посчитать выручку по регионам?
10. Как сгруппировать сразу по региону и каналу?
11. Что делать, если результат получился Series, а нужна таблица?
12. Как проверить, что сумма после группировки не потерялась?

---

# 22. Практическое задание

Используйте подготовленную таблицу `sales_prepared.csv`.

## Задание 1

Посчитайте выручку по категориям.

```python
category_revenue = (
    df
    .groupby("category", as_index=False)
    .agg(total_revenue=("revenue", "sum"))
    .sort_values("total_revenue", ascending=False)
)

category_revenue
```

## Задание 2

Посчитайте выручку и прибыль по регионам.

## Задание 3

Посчитайте количество заказов и средний чек по каналам продаж.

## Задание 4

Сгруппируйте данные по `region_name` и `channel`.

## Задание 5

Проверьте, совпадает ли общая сумма `revenue` до и после группировки по категориям.

---

# 23. Итог

`groupby()` — одна из главных команд аналитика в pandas.

Она нужна, когда вопрос звучит так:

```text
посчитать показатель по группам
```

Примеры:

```text
выручка по категориям
прибыль по регионам
заказы по каналам
средний чек по клиентским сегментам
продажи по месяцам
```

Главное правило:

> сначала понять бизнес-вопрос, потом выбрать группировку и функцию расчета.

---

# 24. Справочные источники

- pandas User Guide: Group by — split-apply-combine: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
- pandas `DataFrame.groupby`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
