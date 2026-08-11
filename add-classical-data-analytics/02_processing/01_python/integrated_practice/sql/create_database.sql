-- Скрипт создания учебных таблиц SQLite
-- Данные уже загружены в файл sql/analytics_demo.sqlite.
-- Этот файл нужен как справочная схема для слушателей.

DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS clients;

CREATE TABLE sales (
    order_id TEXT,
    order_date TEXT,
    client_id TEXT,
    product_id TEXT,
    region_id TEXT,
    channel TEXT,
    quantity INTEGER,
    unit_price REAL,
    discount REAL
);

CREATE TABLE products (
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    cost REAL
);

CREATE TABLE regions (
    region_id TEXT,
    region_name TEXT,
    macro_region TEXT
);

CREATE TABLE clients (
    client_id TEXT,
    segment TEXT,
    registration_date TEXT,
    loyalty_level TEXT
);
