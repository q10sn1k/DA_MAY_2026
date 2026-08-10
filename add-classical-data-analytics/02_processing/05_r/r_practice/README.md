# Обработка и анализ данных в R

Комплект для живого лекционно-практического вебинара продолжительностью 240 минут. Материал рассчитан на начинающих слушателей и объединяет краткую прикладную лекцию, демонстрацию преподавателя, управляемую практику и самостоятельный мини-кейс.

## Результат занятия

Слушатель создаёт воспроизводимый R-скрипт, загружает и проверяет CSV, очищает данные, рассчитывает показатели по регионам, категориям, месяцам и каналам, строит графики и экспортирует результаты.

## Структура

```text
r_data_processing_webinar/
├── data/
│   └── retail_sales.csv
├── scripts/
│   ├── environment_check.R
│   ├── install_packages.R
│   ├── student_practice.R
│   └── teacher_solution.R
├── materials/
│   ├── instructor_scenario.md
│   ├── slide_structure.md
│   ├── student_handout.md
│   ├── data_dictionary.md
│   ├── common_errors.md
│   ├── self_checklist.md
│   ├── knowledge_check.md
│   └── post_assignment.md
├── teacher/
│   ├── control_values.json
│   └── reference_outputs/
├── outputs/
└── r_data_basics.Rproj
```

## Быстрый старт

1. Установите R и RStudio Desktop.
2. Распакуйте архив без изменения структуры папок.
3. Откройте файл `r_data_basics.Rproj`.
4. Выполните `scripts/install_packages.R`.
5. Перезапустите RStudio при необходимости.
6. Откройте `scripts/student_practice.R` или `scripts/teacher_solution.R`.
7. Выполняйте код сверху вниз.

## Требования

- R 4.3 или новее; на 3 августа 2026 года официальный актуальный выпуск — R 4.6.1.
- RStudio Desktop либо браузерная среда, поддерживающая R-проект.
- Пакет `tidyverse`.

## Контрольные значения

- Исходная таблица: 726 строк, 10 столбцов.
- После нормализации, удаления дубликатов и применения бизнес-фильтров: 613 строк.
- Итоговая выручка: 25143394.52.
- Лидер среди регионов: Санкт-Петербург.
- Лидер среди категорий: Ноутбуки.
- Лидер среди каналов: online.

Полный набор контрольных значений находится в `teacher/control_values.json`.

## Официальные источники

- R Project: https://www.r-project.org/
- RStudio IDE User Guide: https://docs.posit.co/ide/user/
- RStudio Projects: https://docs.posit.co/ide/user/ide/guide/code/projects.html
- dplyr: https://dplyr.tidyverse.org/
- ggplot2: https://ggplot2.tidyverse.org/
- readr: https://readr.tidyverse.org/

## Ограничение проверки

В текущей среде сборки R не установлен, поэтому скрипты прошли статическую проверку структуры, путей и последовательности объектов. Контрольные значения рассчитаны независимой реализацией на Python по той же логике очистки и агрегации. Перед проведением рекомендуется один раз выполнить `scripts/teacher_solution.R` в целевой R-среде.
