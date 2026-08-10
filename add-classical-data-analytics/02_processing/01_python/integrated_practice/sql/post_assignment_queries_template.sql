-- post_assignment_queries_template.sql
-- Шаблон SQL-запросов для пост-задания.
-- Запросы можно выполнять через sqlite3 или из notebook через pandas.read_sql_query().

-- 1. Посмотреть первые строки продаж
SELECT *
FROM sales
LIMIT 5;

-- 2. Проверить количество строк
SELECT COUNT(*) AS rows_count
FROM sales;

-- 3. Рассчитать выручку по регионам
SELECT
    region_id,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(quantity * unit_price * (1 - discount)) AS total_revenue
FROM sales
WHERE quantity > 0
  AND unit_price > 0
  AND discount BETWEEN 0 AND 1
GROUP BY region_id
ORDER BY total_revenue DESC;

-- 4. Рассчитать выручку по категориям через JOIN
SELECT
    p.category,
    COUNT(DISTINCT s.order_id) AS orders_count,
    SUM(s.quantity * s.unit_price * (1 - s.discount)) AS total_revenue
FROM sales AS s
LEFT JOIN products AS p
    ON s.product_id = p.product_id
WHERE s.quantity > 0
  AND s.unit_price > 0
  AND s.discount BETWEEN 0 AND 1
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 5. Рассчитать выручку по регионам и категориям
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
