# 03_r_first_steps_student.R
# Первый практический блок R на знакомом кейсе входного аудита данных.
# Задача: открыть те же данные, которые использовались в Python, и выполнить базовую проверку в R.

# 1. Подключение пакетов ---------------------------------------------------
# Если пакет не найден, сначала запустите r/03_setup_packages.R.

library(tidyverse)
library(readxl)
library(jsonlite)

# 2. Проверка рабочей папки ------------------------------------------------
# В RStudio желательно открыть файл data_quality_audit_case_v1.Rproj.
# Тогда рабочая папка автоматически станет корнем проекта.

cat("Рабочая папка:\n")
print(getwd())

# 3. Пути к исходным данным ------------------------------------------------

sales_path <- "data/raw/sales.csv"
products_path <- "data/raw/products.xlsx"
clients_path <- "data/raw/clients.csv"
regions_path <- "data/raw/regions.json"

required_files <- c(sales_path, products_path, clients_path, regions_path)

file_check <- tibble(
  file_path = required_files,
  exists = file.exists(required_files)
)

print(file_check)

# Контрольный вопрос:
# Что нужно исправить, если напротив какого-то файла стоит FALSE?

# 4. Загрузка данных -------------------------------------------------------
# В R read_csv обычно показывает, какие типы столбцов были определены автоматически.

sales <- read_csv(sales_path, show_col_types = FALSE)
products <- read_excel(products_path, sheet = "products")
clients <- read_csv(clients_path, show_col_types = FALSE)
regions <- fromJSON(regions_path) |> as_tibble()

# 5. Быстрый просмотр ------------------------------------------------------

cat("\nРазмеры таблиц:\n")
cat("sales:", nrow(sales), "строк,", ncol(sales), "столбцов\n")
cat("products:", nrow(products), "строк,", ncol(products), "столбцов\n")
cat("clients:", nrow(clients), "строк,", ncol(clients), "столбцов\n")
cat("regions:", nrow(regions), "строк,", ncol(regions), "столбцов\n")

cat("\nПервые строки sales:\n")
print(head(sales, 5))

cat("\nСтруктура sales:\n")
str(sales)

# 6. Сводка по источникам --------------------------------------------------
# В этом блоке мы повторяем рабочую идею первого Python-комплекта:
# сначала понимаем состав источников, потом принимаем решение о пригодности данных.

loaded_data_summary <- tibble(
  dataset = c("sales", "products", "clients", "regions"),
  rows = c(nrow(sales), nrow(products), nrow(clients), nrow(regions)),
  columns = c(ncol(sales), ncol(products), ncol(clients), ncol(regions)),
  missing_cells = c(
    sum(is.na(sales)),
    sum(is.na(products)),
    sum(is.na(clients)),
    sum(is.na(regions))
  )
)

print(loaded_data_summary)

# 7. Проверка дат ----------------------------------------------------------
# lubridate входит в tidyverse. ymd() пытается привести значения к формату год-месяц-день.

sales_checked <- sales |>
  mutate(
    order_date_parsed = lubridate::ymd(order_date, quiet = TRUE),
    invalid_order_date = is.na(order_date_parsed)
  )

invalid_dates_count <- sum(sales_checked$invalid_order_date)
cat("\nНераспознанных дат:", invalid_dates_count, "\n")

print(
  sales_checked |>
    filter(invalid_order_date) |>
    select(order_id, order_date) |>
    head(10)
)

# 8. Проверка дублей заказов ----------------------------------------------
# duplicated(order_id) показывает повторы после первого появления.
# Для поиска всех строк с повторяющимся order_id удобнее использовать add_count().

duplicated_orders <- sales_checked |>
  add_count(order_id, name = "order_id_count") |>
  filter(order_id_count > 1) |>
  arrange(order_id)

cat("\nСтрок с повторяющимися order_id:", nrow(duplicated_orders), "\n")
print(head(duplicated_orders, 10))

# 9. Проверка бизнес-правил ------------------------------------------------
# Правила:
# quantity > 0
# unit_price > 0
# discount от 0 до 1
# order_date должна быть распознана

quality_preview <- tibble(
  check_name = c(
    "invalid_order_date",
    "non_positive_quantity",
    "non_positive_unit_price",
    "discount_out_of_range",
    "duplicated_order_id_rows"
  ),
  rows_count = c(
    sum(sales_checked$invalid_order_date),
    sum(sales_checked$quantity <= 0, na.rm = TRUE),
    sum(sales_checked$unit_price <= 0, na.rm = TRUE),
    sum(sales_checked$discount < 0 | sales_checked$discount > 1, na.rm = TRUE),
    nrow(duplicated_orders)
  )
)

print(quality_preview)

# 10. Проверка связей со справочниками ------------------------------------
# Проверяем, есть ли ключи из sales в соответствующих справочниках.

missing_products <- setdiff(unique(na.omit(sales$product_id)), unique(na.omit(products$product_id)))
missing_clients <- setdiff(unique(na.omit(sales$client_id)), unique(na.omit(clients$client_id)))
missing_regions <- setdiff(unique(na.omit(sales$region_id)), unique(na.omit(regions$region_id)))

reference_preview <- tibble(
  check_name = c("unknown_product_id", "unknown_client_id", "unknown_region_id"),
  unique_keys_count = c(length(missing_products), length(missing_clients), length(missing_regions))
)

print(reference_preview)

# 11. Сохранение первых результатов ---------------------------------------

if (!dir.exists("outputs")) {
  dir.create("outputs", recursive = TRUE)
}

write_csv(loaded_data_summary, "outputs/r_loaded_data_summary.csv")
write_csv(quality_preview, "outputs/r_first_quality_preview.csv")
write_csv(reference_preview, "outputs/r_reference_preview.csv")

# 12. Итоговое текстовое решение ------------------------------------------
# Заполните файл своими словами после просмотра таблиц.

r_decision_text <- c(
  "# Первое решение аналитика после запуска R",
  "",
  "## Общий статус",
  "Данные открылись в R. Перед аналитическим отчётом требуется проверить и исправить найденные проблемы качества.",
  "",
  "## Что обнаружено",
  "- Проверьте таблицу outputs/r_first_quality_preview.csv.",
  "- Проверьте таблицу outputs/r_reference_preview.csv.",
  "",
  "## Следующий шаг",
  "Повторить нормализацию и стандартизацию данных в R на следующем практическом блоке."
)

writeLines(r_decision_text, "outputs/r_first_decision.md", useBytes = TRUE)

cat("\nГотово. Первые R-результаты сохранены в папке outputs.\n")
