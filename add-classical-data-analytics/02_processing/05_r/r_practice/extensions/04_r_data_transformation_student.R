# 04_r_data_transformation_student.R
# Практика для слушателя: нормализация, стандартизация и сборка аналитической витрины в R.
# Запускайте из корневой папки проекта или через файл data_quality_audit_case_v1.Rproj.

library(tidyverse)
library(readxl)
library(jsonlite)

# 1. Проверяем структуру проекта -------------------------------------------------
required_files <- c(
  "data/raw/sales.csv",
  "data/raw/products.xlsx",
  "data/raw/clients.csv",
  "data/raw/regions.json"
)

if (!all(file.exists(required_files))) {
  missing <- required_files[!file.exists(required_files)]
  stop(paste("Не найдены файлы:", paste(missing, collapse = ", "), "\nОткройте .Rproj или запустите скрипт из корня проекта."))
}

if (!dir.exists("outputs")) {
  dir.create("outputs", recursive = TRUE)
}

cat("Рабочая папка:", getwd(), "\n")
cat("Все исходные файлы найдены.\n\n")

# 2. Загружаем данные -------------------------------------------------------------
sales <- read_csv("data/raw/sales.csv", show_col_types = FALSE)
products <- read_excel("data/raw/products.xlsx", sheet = "products")
clients <- read_csv("data/raw/clients.csv", show_col_types = FALSE)
regions <- fromJSON("data/raw/regions.json") |> as_tibble()

cat("Размеры исходных таблиц:\n")
print(tibble(
  dataset = c("sales", "products", "clients", "regions"),
  rows = c(nrow(sales), nrow(products), nrow(clients), nrow(regions)),
  columns = c(ncol(sales), ncol(products), ncol(clients), ncol(regions))
))

# 3. Вспомогательные функции ------------------------------------------------------
clean_text <- function(x) {
  x |>
    as.character() |>
    str_trim() |>
    na_if("")
}

clean_key <- function(x) {
  clean_text(x) |> str_to_upper()
}

normalize_label <- function(x) {
  clean_text(x) |>
    str_to_lower() |>
    str_replace_all("\\s+", " ")
}

# 4. Нормализуем основную таблицу продаж -----------------------------------------
sales_work <- sales |>
  mutate(
    order_id = clean_key(order_id),
    client_id = clean_key(client_id),
    product_id = clean_key(product_id),
    region_id = clean_key(region_id),
    channel_raw = channel,
    channel = normalize_label(channel),
    order_date_raw = order_date,
    order_date = lubridate::ymd(order_date, quiet = TRUE),
    quantity = as.numeric(quantity),
    unit_price = as.numeric(unit_price),
    discount = as.numeric(discount)
  )

cat("Каналы после нормализации:\n")
print(sort(unique(na.omit(sales_work$channel))))

# 5. Нормализуем справочники ------------------------------------------------------
products_work <- products |>
  mutate(
    product_id = clean_key(product_id),
    product_name = clean_text(product_name),
    category = normalize_label(category),
    category = recode(
      category,
      "electronics" = "Electronics",
      "accessories" = "Accessories",
      "furniture" = "Furniture",
      "office supplies" = "Office Supplies",
      "appliances" = "Appliances",
      .default = category
    ),
    status = normalize_label(status),
    cost = as.numeric(cost)
  )

products_dedup <- products_work |>
  distinct(product_id, .keep_all = TRUE)

clients_work <- clients |>
  mutate(
    client_id = clean_key(client_id),
    segment = normalize_label(segment),
    segment = recode(
      segment,
      "b2c" = "B2C",
      "b2b" = "B2B",
      "enterprise" = "Enterprise",
      "smb" = "SMB",
      .default = segment
    ),
    loyalty_level = str_to_title(clean_text(loyalty_level)),
    registration_date = lubridate::ymd(registration_date, quiet = TRUE)
  )

clients_dedup <- clients_work |>
  distinct(client_id, .keep_all = TRUE)

regions_work <- regions |>
  mutate(
    region_id = clean_key(region_id),
    region_name = clean_text(region_name),
    macro_region = clean_text(macro_region)
  )

regions_dedup <- regions_work |>
  distinct(region_id, .keep_all = TRUE)

cat("Категории после нормализации:\n")
print(sort(unique(na.omit(products_dedup$category))))

# 6. Флаги качества ---------------------------------------------------------------
valid_product_ids <- products_dedup |> filter(!is.na(product_id)) |> pull(product_id)
valid_client_ids <- clients_dedup |> filter(!is.na(client_id)) |> pull(client_id)
valid_region_ids <- regions_dedup |> filter(!is.na(region_id)) |> pull(region_id)

sales_work <- sales_work |>
  mutate(
    is_duplicate_order = duplicated(order_id),
    invalid_date = is.na(order_date),
    invalid_quantity = is.na(quantity) | quantity <= 0,
    invalid_price = is.na(unit_price) | unit_price <= 0,
    invalid_discount = is.na(discount) | discount < 0 | discount > 1,
    missing_key = is.na(product_id) | is.na(client_id) | is.na(region_id),
    unknown_product = !(product_id %in% valid_product_ids),
    unknown_client = !(client_id %in% valid_client_ids),
    unknown_region = !(region_id %in% valid_region_ids),
    exclude_from_report = is_duplicate_order | invalid_date | invalid_quantity | invalid_price |
      invalid_discount | missing_key | unknown_product | unknown_client | unknown_region,
    quality_status = if_else(exclude_from_report, "excluded", "ready_for_report")
  )

flag_summary <- sales_work |>
  summarise(
    is_duplicate_order = sum(is_duplicate_order, na.rm = TRUE),
    invalid_date = sum(invalid_date, na.rm = TRUE),
    invalid_quantity = sum(invalid_quantity, na.rm = TRUE),
    invalid_price = sum(invalid_price, na.rm = TRUE),
    invalid_discount = sum(invalid_discount, na.rm = TRUE),
    missing_key = sum(missing_key, na.rm = TRUE),
    unknown_product = sum(unknown_product, na.rm = TRUE),
    unknown_client = sum(unknown_client, na.rm = TRUE),
    unknown_region = sum(unknown_region, na.rm = TRUE),
    exclude_from_report = sum(exclude_from_report, na.rm = TRUE)
  ) |>
  pivot_longer(everything(), names_to = "check", values_to = "rows_count")

cat("Сводка флагов качества:\n")
print(flag_summary)

# 7. Готовим строки для отчёта ----------------------------------------------------
sales_valid <- sales_work |>
  filter(!exclude_from_report) |>
  mutate(
    gross_revenue = quantity * unit_price,
    revenue = gross_revenue * (1 - discount)
  )

cat("Строк в исходной таблице продаж:", nrow(sales), "\n")
cat("Строк в готовой части для отчёта:", nrow(sales_valid), "\n")
cat("Исключено строк:", sum(sales_work$exclude_from_report), "\n\n")

# 8. Собираем аналитическую витрину ----------------------------------------------
sales_datamart <- sales_valid |>
  left_join(products_dedup |> select(product_id, product_name, category, cost), by = "product_id", relationship = "many-to-one") |>
  left_join(clients_dedup |> select(client_id, segment, loyalty_level, registration_date), by = "client_id", relationship = "many-to-one") |>
  left_join(regions_dedup |> select(region_id, region_name, macro_region), by = "region_id", relationship = "many-to-one") |>
  mutate(
    margin = revenue - quantity * cost,
    order_month = format(order_date, "%Y-%m")
  )

# 9. Стандартизация и min-max нормализация выручки -------------------------------
revenue_mean <- mean(sales_datamart$revenue, na.rm = TRUE)
revenue_std <- sqrt(mean((sales_datamart$revenue - revenue_mean)^2, na.rm = TRUE))
revenue_min <- min(sales_datamart$revenue, na.rm = TRUE)
revenue_max <- max(sales_datamart$revenue, na.rm = TRUE)

sales_datamart <- sales_datamart |>
  mutate(
    revenue_zscore = (revenue - revenue_mean) / revenue_std,
    revenue_minmax = (revenue - revenue_min) / (revenue_max - revenue_min)
  )

# 10. Сводка для отчёта -----------------------------------------------------------
report_by_region_channel <- sales_datamart |>
  group_by(macro_region, region_name, channel) |>
  summarise(
    orders_count = n_distinct(order_id),
    total_quantity = sum(quantity, na.rm = TRUE),
    total_revenue = sum(revenue, na.rm = TRUE),
    avg_order_revenue = mean(revenue, na.rm = TRUE),
    total_margin = sum(margin, na.rm = TRUE),
    .groups = "drop"
  ) |>
  arrange(desc(total_revenue))

# 11. Лог трансформаций -----------------------------------------------------------
transformation_log <- tibble(
  step = c(
    "raw_sales_rows",
    "duplicate_orders_excluded",
    "invalid_dates_excluded",
    "invalid_quantity_excluded",
    "invalid_price_excluded",
    "invalid_discount_excluded",
    "missing_or_unknown_reference_excluded",
    "sales_ready_for_report",
    "products_unique_after_dedup",
    "clients_unique_after_dedup"
  ),
  value = c(
    nrow(sales),
    sum(sales_work$is_duplicate_order, na.rm = TRUE),
    sum(sales_work$invalid_date, na.rm = TRUE),
    sum(sales_work$invalid_quantity, na.rm = TRUE),
    sum(sales_work$invalid_price, na.rm = TRUE),
    sum(sales_work$invalid_discount, na.rm = TRUE),
    sum(sales_work$missing_key | sales_work$unknown_product | sales_work$unknown_client | sales_work$unknown_region, na.rm = TRUE),
    nrow(sales_datamart),
    nrow(products_dedup),
    nrow(clients_dedup)
  ),
  comment = c(
    "Строк в исходной таблице продаж",
    "Повторные order_id исключены из витрины",
    "Строки с нераспознанной датой исключены",
    "Строки с некорректным количеством исключены",
    "Строки с некорректной ценой исключены",
    "Строки с некорректной скидкой исключены",
    "Строки с отсутствующими или неизвестными ключами исключены",
    "Строк готовой витрины",
    "Уникальных товаров после разрешения дублей справочника",
    "Уникальных клиентов после разрешения дублей справочника"
  )
)

# 12. Сохраняем результат ---------------------------------------------------------
write_csv(sales_work, "outputs/r_sales_prepared_with_quality_flags.csv")
write_csv(sales_datamart, "outputs/r_sales_datamart.csv")
write_csv(report_by_region_channel, "outputs/r_report_by_region_channel.csv")
write_csv(transformation_log, "outputs/r_transformation_log.csv")

r_decision_text <- c(
  "# Решение аналитика после подготовки витрины в R",
  "",
  "## Что сделано",
  "1. Ключевые поля приведены к единому регистру и очищены от лишних пробелов.",
  "2. Каналы продаж и категории товаров нормализованы.",
  "3. Даты заказов преобразованы в тип Date.",
  "4. Критичные строки исключены из отчётной витрины.",
  "5. Справочники товаров, клиентов и регионов присоединены к продажам.",
  "6. Рассчитаны выручка, маржа, z-score и min-max нормализация выручки.",
  "",
  "## Итог",
  paste0("В готовой витрине осталось ", nrow(sales_datamart), " строк из ", nrow(sales), " исходных строк продаж."),
  "",
  "## Ограничение",
  "Исключённые строки нельзя использовать в итоговом управленческом отчёте без уточнения у владельца данных.",
  "",
  "## Следующий шаг",
  "Использовать r_sales_datamart.csv и r_report_by_region_channel.csv для сверки результатов R с Python и подготовки финального вывода."
)
writeLines(r_decision_text, "outputs/r_normalization_decision.md", useBytes = TRUE)

cat("\nФайлы R-комплекта сохранены в outputs.\n")
cat("Строк в r_sales_datamart.csv:", nrow(sales_datamart), "\n")
cat("Итоговая выручка:", round(sum(sales_datamart$revenue), 2), "\n")
cat("Итоговая маржа:", round(sum(sales_datamart$margin), 2), "\n")
