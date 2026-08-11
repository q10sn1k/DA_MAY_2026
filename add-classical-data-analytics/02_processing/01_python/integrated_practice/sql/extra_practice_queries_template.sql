-- Дополнительная практика на 90 минут
-- Файл для слушателя: SQL-шаблоны к мини-отчёту.
-- Выполняйте запросы в SQLite-базе sql/analytics_demo.sqlite.

-- Задача 1. Посмотрите первые строки таблицы sales.
SELECT *
FROM sales
LIMIT 5;

-- Задача 2. Рассчитайте выручку по группам скидок.
-- Подсказка: используйте CASE и GROUP BY.
SELECT
    CASE
        WHEN discount = 0 THEN 'без скидки'
        WHEN discount <= 0.10 THEN 'скидка до 10%'
        WHEN discount <= 0.25 THEN 'скидка 10-25%'
        ELSE 'скидка выше 25%'
    END AS discount_group,
    COUNT(DISTINCT order_id) AS orders_count,
    ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS total_revenue,
    ROUND(AVG(quantity * unit_price * (1 - discount)), 2) AS avg_order_revenue
FROM sales
WHERE quantity > 0
  AND unit_price > 0
  AND discount BETWEEN 0 AND 1
GROUP BY discount_group
ORDER BY total_revenue DESC;

-- Задача 3. Получите топ-5 регионов по выручке.
-- Подсказка: соедините sales и regions через LEFT JOIN.
SELECT
    r.region_name,
    COUNT(DISTINCT s.order_id) AS orders_count,
    ROUND(SUM(s.quantity * s.unit_price * (1 - s.discount)), 2) AS total_revenue
FROM sales AS s
LEFT JOIN regions AS r
    ON s.region_id = r.region_id
WHERE s.quantity > 0
  AND s.unit_price > 0
  AND s.discount BETWEEN 0 AND 1
GROUP BY r.region_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Задача 4. Через CTE подготовьте читаемый запрос по категориям и каналам.
-- Дополните запрос: проверьте, какие категории лидируют в каждом канале.
WITH sales_enriched AS (
    SELECT
        s.order_id,
        s.channel,
        p.category,
        s.quantity * s.unit_price * (1 - s.discount) AS revenue
    FROM sales AS s
    LEFT JOIN products AS p
        ON s.product_id = p.product_id
    WHERE s.quantity > 0
      AND s.unit_price > 0
      AND s.discount BETWEEN 0 AND 1
)
SELECT
    channel,
    category,
    COUNT(DISTINCT order_id) AS orders_count,
    ROUND(SUM(revenue), 2) AS total_revenue
FROM sales_enriched
GROUP BY channel, category
ORDER BY channel, total_revenue DESC;
