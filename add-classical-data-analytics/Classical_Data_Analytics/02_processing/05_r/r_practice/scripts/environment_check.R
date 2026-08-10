# Проверка среды и файлов

cat("Версия R:", R.version.string, "\n")
cat("Рабочая папка:", getwd(), "\n")

required_file <- file.path("data", "retail_sales.csv")

if (file.exists(required_file)) {
  cat("OK: найден файл", required_file, "\n")
} else {
  stop(
    "Файл data/retail_sales.csv не найден. Откройте проект r_data_basics.Rproj и повторите запуск."
  )
}

if (requireNamespace("tidyverse", quietly = TRUE)) {
  cat("OK: пакет tidyverse доступен.\n")
} else {
  stop("Пакет tidyverse не установлен. Выполните scripts/install_packages.R")
}
