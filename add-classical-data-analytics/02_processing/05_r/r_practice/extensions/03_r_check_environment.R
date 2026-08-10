# 03_r_check_environment.R
# Проверка R, рабочей папки, пакетов и исходных файлов.
# Цель: убедиться, что среда готова к практической работе.

cat("Версия R:\n")
print(R.version.string)

cat("\nРабочая папка:\n")
print(getwd())

required_packages <- c("tidyverse", "readxl", "jsonlite")

cat("\nПроверяем пакеты:\n")
for (pkg in required_packages) {
  if (requireNamespace(pkg, quietly = TRUE)) {
    cat("OK:", pkg, "\n")
  } else {
    cat("НЕ УСТАНОВЛЕН:", pkg, "\n")
  }
}

required_files <- c(
  "data/raw/sales.csv",
  "data/raw/products.xlsx",
  "data/raw/clients.csv",
  "data/raw/regions.json"
)

cat("\nПроверяем исходные файлы:\n")
file_check <- data.frame(
  file_path = required_files,
  exists = file.exists(required_files),
  stringsAsFactors = FALSE
)
print(file_check)

if (!dir.exists("outputs")) {
  dir.create("outputs", recursive = TRUE)
}

write.csv(file_check, "outputs/r_environment_check.csv", row.names = FALSE, fileEncoding = "UTF-8")
cat("\nРезультат проверки сохранён: outputs/r_environment_check.csv\n")
