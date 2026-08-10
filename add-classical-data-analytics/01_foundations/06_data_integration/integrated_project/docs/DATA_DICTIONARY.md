# Data Dictionary — «РегионМаркет»

## sales.csv

| Поле | Назначение | Проблемы |
|---|---|---|
| sale_id | ID продажи | Есть дубликат `1007` |
| order_date | Дата заказа | Разные форматы и `bad_date` |
| client_id | ID клиента | Есть `999`, отсутствующий в clients.csv |
| product_id | ID товара | Есть `999`, отсутствующий в products.xlsx |
| region_id | ID региона | Есть `999`, отсутствующий в regions.json |
| quantity | Количество | Есть отрицательное значение |
| unit_price | Цена | Есть `price_error` |
| discount_percent | Скидка | Есть пустое значение, `five`, 150% |
| channel | Канал | Пробелы и разный регистр |
| payment_method | Метод оплаты | Категориальное поле |
| order_status | Статус заказа | completed, cancelled, returned |
| manager_id | ID менеджера | Дополнительный признак |

## products.xlsx

| Поле | Назначение | Проблемы |
|---|---|---|
| product_id | ID товара | Дубликат `106` |
| product_name | Название | — |
| category | Категория | Пробелы и разный регистр |
| subcategory | Подкатегория | — |
| brand | Бренд | — |
| supplier | Поставщик | Есть пропуск |
| purchase_price | Закупочная цена | Есть `cost_error` |
| is_active | Активность товара | Есть неактивный товар |

## regions.json

Есть разные регистры и пробелы в `federal_district`, а также пропуск `population_group`.

## clients.csv

Есть разные форматы дат, `bad_date`, дубликат клиента `507`, пропуски `loyalty_level`, разные регистры и пробелы в `client_type`.

## web_table_sample.html

Есть разные форматы месяца, пробел в `channel`, `sales_plan = plan_error`, планы по регионам/каналам без факта.
