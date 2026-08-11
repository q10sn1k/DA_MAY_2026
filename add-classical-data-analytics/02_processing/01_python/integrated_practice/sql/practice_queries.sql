-- Практические SQL-запросы для сквозного кейса

-- 1. Посмотреть первые строки продаж
SELECT *
FROM sales
LIMIT 5;

-- 2. Выбрать нужные поля и отфильтровать строки
SELECT 
    order_id,
    order_date,
    region_id,
    channel,
    quantity,
    unit_price
FROM sales
WHERE quantity > 0
ORDER BY order_date;

-- 3. Рассчитать выручку по region_id
SELECT
    region_id,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(quantity * unit_price * (1 - discount)) AS total_revenue,
    AVG(quantity * unit_price * (1 - discount)) AS avg_order_revenue
FROM sales
WHERE quantity > 0
  AND unit_price > 0
  AND discount BETWEEN 0 AND 1
GROUP BY region_id
ORDER BY total_revenue DESC;

-- 4. JOIN продаж с товарами и регионами
SELECT
    r.region_name,
    p.category,
    COUNT(DISTINCT s.order_id) AS orders_count,
    SUM(s.quantity * s.unit_price * (1 - s.discount)) AS total_revenue
FROM sales AS s
LEFT JOIN products AS p
    ON s.product_id = p.product_id
LEFT JOIN regions AS r
    ON s.region_id = r.region_id
WHERE s.quantity > 0
  AND s.unit_price > 0
  AND s.discount BETWEEN 0 AND 1
GROUP BY r.region_name, p.category
ORDER BY total_revenue DESC;

-- 5. Диагностика не найденных товаров при JOIN
SELECT
    s.product_id,
    COUNT(*) AS rows_count
FROM sales AS s
LEFT JOIN products AS p
    ON s.product_id = p.product_id
WHERE p.product_id IS NULL
GROUP BY s.product_id;

-- 6. Диагностика не найденных регионов при JOIN
SELECT
    s.region_id,
    COUNT(*) AS rows_count
FROM sales AS s
LEFT JOIN regions AS r
    ON s.region_id = r.region_id
WHERE r.region_id IS NULL
GROUP BY s.region_id;
