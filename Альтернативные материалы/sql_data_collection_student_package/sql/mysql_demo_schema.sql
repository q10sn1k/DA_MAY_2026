CREATE DATABASE IF NOT EXISTS my_database;
USE my_database;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    country VARCHAR(50) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users (name, email, age, country, balance) VALUES
('Ivan', 'ivan@example.com', 25, 'RUS', 100000.00),
('Gleb', 'gleb@example.com', 26, 'RUS', 90000.00),
('Sergey', 'sergey@example.com', 28, 'RUS', 90000.00),
('Andrew', 'andrew@example.com', 24, 'RUS', 95000.00),
('Bob', 'bob@example.com', 25, 'USA', 100000.00),
('Tom', 'tom@example.com', 29, 'USA', 110000.00);

CREATE TABLE orders (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO orders (user_id, product_name, price, quantity, order_date) VALUES
(1, 'Product A', 10.00, 2, '2023-02-22'),
(2, 'Product B', 20.00, 1, '2023-02-20'),
(2, 'Product C', 15.00, 3, '2023-02-23'),
(1, 'Product D', 12.00, 2, '2023-02-25'),
(2, 'Product E', 25.00, 1, '2023-02-26');
