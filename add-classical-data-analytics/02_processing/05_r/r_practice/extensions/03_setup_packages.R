# 03_setup_packages.R
# Установка и проверка пакетов для практики в R.
# Запускайте этот файл один раз после установки R и RStudio.

required_packages <- c(
  "tidyverse",  # readr, dplyr, tidyr, stringr, ggplot2 и другие пакеты ежедневной аналитики
  "readxl",     # чтение Excel-файлов
  "jsonlite"    # чтение JSON-файлов
)

installed <- rownames(installed.packages())
missing <- setdiff(required_packages, installed)

if (length(missing) > 0) {
  message("Будут установлены пакеты: ", paste(missing, collapse = ", "))
  install.packages(missing)
} else {
  message("Все необходимые пакеты уже установлены.")
}

message("Проверяем подключение пакетов...")
library(tidyverse)
library(readxl)
library(jsonlite)

message("Готово. Версия R:")
print(R.version.string)
message("Рабочая папка:")
print(getwd())


# После проверки окружения переходите к r/04_r_data_transformation_student.R.
