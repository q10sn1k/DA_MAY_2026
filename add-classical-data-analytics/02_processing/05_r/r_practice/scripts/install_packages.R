# Установка пакетов для практикума
# Выполните этот файл один раз перед занятием.

required_packages <- c("tidyverse")

missing_packages <- required_packages[
  !required_packages %in% rownames(installed.packages())
]

if (length(missing_packages) > 0) {
  install.packages(missing_packages)
} else {
  message("Все необходимые пакеты уже установлены.")
}
