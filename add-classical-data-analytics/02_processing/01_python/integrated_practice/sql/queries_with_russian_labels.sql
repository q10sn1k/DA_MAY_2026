-- SQL-запросы с русскими подписями столбцов
-- Этот файл нужен для чтения результатов на русском языке.
-- Имена исходных таблиц и полей остаются техническими: sales, products, regions, clients.

-- 1. Первые строки продаж с русскими названиями столбцов
SELECT
    order_id AS "Номер заказа",
    order_date AS "Дата заказа",
    client_id AS "Код клиента",
    product_id AS "Код товара",
    region_id AS "Код региона",
    channel AS "Канал продаж",
    quantity AS "Количество",
    unit_price AS "Цена за единицу",
    discount AS "Скидка"
FROM sales
LIMIT 5;

-- 2. Выручка по регионам
SELECT
    r.region_name AS "Регион",
    COUNT(DISTINCT s.order_id) AS "Количество заказов",
    ROUND(SUM(s.quantity * s.unit_price * (1 - s.discount)), 2) AS "Общая выручка",
    ROUND(AVG(s.quantity * s.unit_price * (1 - s.discount)), 2) AS "Средняя выручка на заказ"
FROM sales AS s
LEFT JOIN regions AS r
    ON s.region_id = r.region_id
WHERE s.quantity > 0
  AND s.unit_price > 0
  AND s.discount BETWEEN 0 AND 1
GROUP BY r.region_name
ORDER BY "Общая выручка" DESC;

-- 3. Выручка по категориям и каналам продаж
SELECT
    p.category AS "Категория",
    s.channel AS "Канал продаж",
    COUNT(DISTINCT s.order_id) AS "Количество заказов",
    ROUND(SUM(s.quantity * s.unit_price * (1 - s.discount)), 2) AS "Общая выручка"
FROM sales AS s
LEFT JOIN products AS p
    ON s.product_id = p.product_id
WHERE s.quantity > 0
  AND s.unit_price > 0
  AND s.discount BETWEEN 0 AND 1
GROUP BY p.category, s.channel
ORDER BY "Общая выручка" DESC;

-- 4. Группы скидок с русскими подписями
WITH sales_with_discount_group AS (
    SELECT
        order_id,
        quantity,
        unit_price,
        discount,
        CASE
            WHEN discount = 0 THEN 'без скидки'
            WHEN discount <= 0.10 THEN 'скидка до 10%'
            WHEN discount <= 0.25 THEN 'скидка 10-25%'
            ELSE 'скидка выше 25%'
        END AS discount_group
    FROM sales
    WHERE quantity > 0
      AND unit_price > 0
      AND discount BETWEEN 0 AND 1
)
SELECT
    discount_group AS "Группа скидки",
    COUNT(DISTINCT order_id) AS "Количество заказов",
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS "Общая выручка",
    ROUND(AVG(quantity * unit_price * (1 - discount)), 2) AS "Средняя выручка на заказ"
FROM sales_with_discount_group
GROUP BY discount_group
ORDER BY "Общая выручка" DESC;
