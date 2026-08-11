# Словарь данных

## sales.csv

| Поле | Тип | Назначение |
|---|---|---|
| order_id | string | идентификатор заказа |
| order_date | string/date | дата заказа, требует проверки преобразования |
| client_id | string | ключ клиента |
| product_id | string | ключ товара |
| region_id | string | ключ региона |
| channel | string | канал продаж, содержит разные варианты написания |
| quantity | integer | количество товара |
| unit_price | float | цена за единицу |
| discount | float | скидка в долях от 0 до 1 |
| comment | string | служебный комментарий к строке |

## products.xlsx

| Поле | Тип | Назначение |
|---|---|---|
| product_id | string | ключ товара |
| product_name | string | название товара |
| category | string | категория товара, содержит текстовые расхождения |
| cost | float | себестоимость |
| status | string | статус товара |

## clients.csv

| Поле | Тип | Назначение |
|---|---|---|
| client_id | string | ключ клиента |
| segment | string | клиентский сегмент |
| registration_date | string/date | дата регистрации клиента |
| loyalty_level | string | уровень лояльности |

## regions.json

| Поле | Тип | Назначение |
|---|---|---|
| region_id | string | ключ региона |
| region_name | string | название региона |
| macro_region | string | макрорегион |
