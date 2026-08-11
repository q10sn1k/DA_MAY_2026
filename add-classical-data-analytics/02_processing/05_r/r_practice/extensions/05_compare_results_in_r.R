# Финальная сверка Python- и R-результатов средствами R

library(readr)
library(dplyr)

outputs_dir <- 'outputs'

python_datamart <- read_csv(file.path(outputs_dir, 'sales_datamart.csv'), show_col_types = FALSE)
r_datamart <- read_csv(file.path(outputs_dir, 'r_expected_sales_datamart.csv'), show_col_types = FALSE)

python_report <- read_csv(file.path(outputs_dir, 'report_by_region_channel.csv'), show_col_types = FALSE)
r_report <- read_csv(file.path(outputs_dir, 'r_expected_report_by_region_channel.csv'), show_col_types = FALSE)

python_datamart <- python_datamart |> arrange(order_id)
r_datamart <- r_datamart |> arrange(order_id)
python_report <- python_report |> arrange(macro_region, region_name, channel)
r_report <- r_report |> arrange(macro_region, region_name, channel)

comparison <- tibble(
  check_name = c(
    'datamart_rows',
    'datamart_columns',
    'report_rows',
    'total_revenue',
    'total_margin',
    'unique_orders'
  ),
  python_value = c(
    nrow(python_datamart),
    ncol(python_datamart),
    nrow(python_report),
    round(sum(python_datamart$revenue), 2),
    round(sum(python_datamart$margin), 2),
    n_distinct(python_datamart$order_id)
  ),
  r_value = c(
    nrow(r_datamart),
    ncol(r_datamart),
    nrow(r_report),
    round(sum(r_datamart$revenue), 2),
    round(sum(r_datamart$margin), 2),
    n_distinct(r_datamart$order_id)
  )
) |>
  mutate(
    difference = as.numeric(python_value) - as.numeric(r_value),
    status = if_else(abs(difference) <= 0.01, 'pass', 'fail')
  )

write_csv(comparison, file.path(outputs_dir, 'r_final_python_r_comparison.csv'))

cat('Файл сверки сохранён:', file.path(outputs_dir, 'r_final_python_r_comparison.csv'), '\n')
print(comparison)

# Для полной проверки объектов можно использовать base::all.equal после явной сортировки.
# Пример:
# isTRUE(all.equal(python_report, r_report, tolerance = 0.01, check.attributes = FALSE))
