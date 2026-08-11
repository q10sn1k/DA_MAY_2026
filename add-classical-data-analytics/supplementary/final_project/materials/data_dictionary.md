# Словарь данных

## orders_big.csv

| Поле | Тип | Назначение |
|---|---|---|
| order_id | string | идентификатор заказа |
| order_date | date | дата заказа |
| client_id | string | идентификатор клиента |
| product_id | string | идентификатор товара |
| region | string | регион продажи |
| channel | string | канал продажи |
| category | string | категория товара |
| quantity | integer | количество товаров в заказе |
| unit_price | float | цена за единицу |
| discount | float | скидка от 0 до 1 |
| delivery_days | integer | срок доставки в днях |
| rating | float | оценка клиента |
| is_returned | integer | факт возврата: 1 — возврат, 0 — нет возврата |
| revenue | float | выручка по заказу |

## clients.csv

| Поле | Тип | Назначение |
|---|---|---|
| client_id | string | идентификатор клиента |
| client_segment | string | сегмент клиента |
| loyalty_level | string | уровень лояльности |
| registration_date | date | дата регистрации клиента |

## products.csv

| Поле | Тип | Назначение |
|---|---|---|
| product_id | string | идентификатор товара |
| product_name | string | название товара |
| category | string | категория товара |
| brand | string | бренд |
| base_price | float | базовая цена |
| cost | float | себестоимость |

## Контролируемые проблемы качества

В данных специально заложены учебные проблемы:

- пропуски в `rating`;
- пропуски в `region`;
- дубликаты `order_id`;
- отрицательные значения `quantity`;
- некорректные скидки больше 1;
- выбросы в `delivery_days`;
- разный регистр и пробелы в `channel`.

Эти проблемы нужны для отработки ETL, preprocessing и проверки качества данных.
