# Обработка и анализ данных в R
# Студенческая версия практикума

# 0. Подключение пакета -----------------------------------------------------
library(tidyverse)

# 1. Проверка окружения ----------------------------------------------------
source(file.path("scripts", "environment_check.R"))

# 2. Загрузка данных -------------------------------------------------------
sales_raw <- read_csv(
  file.path("data", "retail_sales.csv"),
  show_col_types = FALSE
)

# Контрольная точка: размер исходной таблицы
# Ожидается 726 строк и 10 столбцов.
dim(sales_raw)
glimpse(sales_raw)
head(sales_raw)

# 3. Первичная проверка качества ------------------------------------------
# Задание: посчитайте пропуски по столбцам.
missing_by_column <- ...
missing_by_column

# Задание: посчитайте количество полных дубликатов.
duplicate_rows <- ...
duplicate_rows

# 4. Очистка и преобразование ---------------------------------------------
# Выполните следующие действия:
# - приведите дату к типу Date;
# - удалите лишние пробелы в текстовых полях;
# - приведите channel и status к нижнему регистру;
# - удалите полные дубликаты;
# - оставьте завершённые заказы с корректными значениями;
# - рассчитайте revenue.

sales_clean <- sales_raw |>
  mutate(
    order_date = ...,
    region = ...,
    channel = ...,
    category = ...,
    product = ...,
    status = ...
  ) |>
  distinct() |>
  filter(
    ...
  ) |>
  mutate(
    revenue = ...
  )

# Контрольная точка: проверьте размер и итоговую выручку.
dim(sales_clean)
sum(sales_clean$revenue)

# 5. Анализ по регионам ----------------------------------------------------
region_summary <- sales_clean |>
  group_by(...) |>
  summarise(
    orders = ...,
    units = ...,
    revenue = ...,
    .groups = "drop"
  ) |>
  mutate(average_order = ...) |>
  arrange(desc(...))

region_summary

# 6. Анализ по категориям -------------------------------------------------
category_summary <- sales_clean |>
  group_by(...) |>
  summarise(
    orders = ...,
    units = ...,
    revenue = ...,
    .groups = "drop"
  ) |>
  mutate(average_order = ...) |>
  arrange(desc(...))

category_summary

# 7. Динамика по месяцам ---------------------------------------------------
monthly_summary <- sales_clean |>
  mutate(month = format(order_date, "%Y-%m")) |>
  group_by(...) |>
  summarise(
    orders = ...,
    revenue = ...,
    .groups = "drop"
  ) |>
  mutate(average_order = ...) |>
  arrange(month)

monthly_summary

# 8. Визуализация ----------------------------------------------------------
# График 1: выручка по регионам.
region_plot <- ggplot(
  region_summary,
  aes(x = reorder(..., ...), y = ...)
) +
  geom_col() +
  coord_flip() +
  labs(
    title = "Выручка по регионам",
    x = "Регион",
    y = "Выручка"
  ) +
  theme_minimal()

region_plot

# График 2: динамика выручки по месяцам.
monthly_plot <- ggplot(
  monthly_summary,
  aes(x = ..., y = ..., group = 1)
) +
  geom_line(linewidth = 1) +
  geom_point(size = 2) +
  labs(
    title = "Динамика выручки по месяцам",
    x = "Месяц",
    y = "Выручка"
  ) +
  theme_minimal()

monthly_plot

# 9. Самостоятельный мини-кейс --------------------------------------------
# Рассчитайте показатели по каналам продаж:
# orders, units, revenue, average_order.
channel_summary <- ...

# Постройте столбчатую диаграмму выручки по каналам.
channel_plot <- ...

# 10. Экспорт --------------------------------------------------------------
dir.create("outputs", showWarnings = FALSE)

write_csv(region_summary, file.path("outputs", "region_summary.csv"))
write_csv(monthly_summary, file.path("outputs", "monthly_summary.csv"))
write_csv(channel_summary, file.path("outputs", "channel_summary.csv"))

ggsave(
  filename = file.path("outputs", "region_revenue.png"),
  plot = region_plot,
  width = 9,
  height = 5,
  dpi = 150
)

# 11. Итоговый вывод -------------------------------------------------------
# Сформулируйте 3–5 предложений:
# 1. Какой регион лидирует по выручке?
# 2. Какая категория лидирует?
# 3. Как менялась выручка по месяцам?
# 4. Какое ограничение есть у анализа?
