# Работа с учебным проектом в VS Code

## 1. Назначение инструкции

Эта инструкция помогает открыть и запустить учебный проект по теме:

**«Загрузка и интеграция данных из различных форматов. Инструменты для сбора данных. Основы Python для обработки данных»**

В VS Code слушатель должен уметь:

- открыть папку проекта;
- выбрать Python-интерпретатор;
- открыть и запустить `.ipynb`-ноутбук;
- запускать ячейки;
- смотреть переменные;
- работать с терминалом;
- запускать `.py`-файлы;
- запускать R-скрипты из папки `r/`.

---

## 2. Что должно быть установлено

Перед началом желательно установить:

1. **VS Code**.
2. **Python 3.10+**.
3. **Расширение Python для VS Code**.
4. **Расширение Jupyter для VS Code**.
5. **R** — если планируется выполнять R-часть.
6. **Расширение R для VS Code** — если планируется работать с `.R`-файлами прямо в VS Code.

Полезные расширения VS Code:

| Расширение | Зачем нужно |
|---|---|
| Python | Выбор интерпретатора, запуск `.py`, работа с Python-окружениями |
| Jupyter | Открытие и запуск `.ipynb`-ноутбуков |
| R | Подсветка R-кода, запуск R-команд, работа с R-терминалом, просмотр переменных и графиков |
| Excel Viewer, CSV Viewer или аналог | Удобный просмотр CSV/Excel-файлов внутри VS Code, если установлен |

---

## 3. Рекомендуемая структура проекта

Проект должен быть открыт в VS Code именно как папка проекта, а не как отдельный файл.

Ожидаемая структура:

```text
data_loading_integration_python/
│
├── data/
│   ├── raw/
│   │   ├── sales.csv
│   │   ├── products.xlsx
│   │   ├── regions.json
│   │   ├── clients.csv
│   │   └── web_table_sample.html
│   │
│   ├── prepared/
│   │   └── sales_prepared.csv
│   │
│   └── output/
│
├── notebooks_student/
│   ├── 00_setup_and_check.ipynb
│   ├── 01_data_loading_formats.ipynb
│   ├── 02_dataframe_types_and_quality.ipynb
│   ├── 03_data_integration.ipynb
│   ├── 04_basic_analysis.ipynb
│   ├── 05_basic_visualization.ipynb
│   └── 06_python_to_r_bridge.ipynb
│
├── notebooks_teacher/
│
├── r/
│   ├── install_packages.R
│   ├── 01_read_python_result.R
│   ├── 02_duckdb_from_r.R
│   └── 03_basic_r_visualization.R
│
├── docs/
│   └── vscode_workflow.md
│
├── requirements.txt
├── environment_check.py
└── README.md
```

Если папки `data/prepared/` или `data/output/` пока нет, это нормально. Они появятся после запуска соответствующих ноутбуков.

---

## 4. Как открыть проект в VS Code

1. Откройте VS Code.
2. Выберите меню:

```text
File → Open Folder...
```

3. Выберите корневую папку проекта:

```text
data_loading_integration_python/
```

4. Убедитесь, что слева в панели Explorer видны папки:

```text
data/
notebooks_student/
r/
docs/
```

### Важно

Не открывайте отдельный файл `.ipynb` двойным кликом из проводника Windows.  
Лучше сначала открыть всю папку проекта, а уже потом открыть ноутбук из панели Explorer.

Так меньше проблем с относительными путями вида:

```python
data/raw/sales.csv
```

---

## 5. Как открыть терминал в VS Code

Откройте встроенный терминал:

```text
Terminal → New Terminal
```

Или горячими клавишами:

```text
Ctrl + `
```

На macOS:

```text
Control + `
```

В терминале проверьте, что вы находитесь в корне проекта:

```bash
pwd
```

На Windows PowerShell можно использовать:

```powershell
Get-Location
```

Посмотреть файлы в текущей папке:

```bash
ls
```

На Windows также можно:

```powershell
dir
```

---

## 6. Как создать Python-окружение

Если виртуальное окружение еще не создано, выполните в терминале из корня проекта:

```bash
python -m venv .venv
```

### Активация на Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Если PowerShell запрещает запуск скриптов, можно использовать обычный терминал Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Активация на macOS / Linux

```bash
source .venv/bin/activate
```

После активации в начале строки терминала обычно появляется:

```text
(.venv)
```

---

## 7. Установка Python-зависимостей

После активации окружения установите зависимости:

```bash
pip install -r requirements.txt
```

Проверить окружение:

```bash
python environment_check.py
```

Если все хорошо, скрипт должен вывести сообщение:

```text
ОКРУЖЕНИЕ ГОТОВО
```

---

## 8. Как выбрать Python-интерпретатор в VS Code

VS Code должен понимать, какой Python использовать.

1. Откройте Command Palette:

```text
Ctrl + Shift + P
```

На macOS:

```text
Cmd + Shift + P
```

2. Введите команду:

```text
Python: Select Interpreter
```

3. Выберите интерпретатор из папки проекта:

```text
.venv
```

Примеры путей:

```text
Windows: .venv\Scripts\python.exe
macOS/Linux: .venv/bin/python
```

### Как проверить выбранный Python

В терминале выполните:

```bash
python --version
```

И:

```bash
python -c "import sys; print(sys.executable)"
```

Путь должен указывать на `.venv`.

---

## 9. Как открыть `.ipynb`-ноутбук

1. В панели Explorer откройте папку:

```text
notebooks_student/
```

2. Откройте первый ноутбук:

```text
00_setup_and_check.ipynb
```

3. В правом верхнем углу ноутбука выберите Kernel.

Обычно нужно выбрать Python-окружение из проекта:

```text
.venv
```

или похожее имя интерпретатора.

### Если Kernel не выбран

Ноутбук откроется, но ячейки не будут выполняться.  
Нужно нажать на выбор Kernel в правом верхнем углу и выбрать Python из `.venv`.

---

## 10. Как запускать ячейки в `.ipynb`

В ноутбуке есть два типа ячеек:

| Тип ячейки | Что внутри |
|---|---|
| Markdown | Текст, объяснение, инструкции |
| Code | Python-код для выполнения |

### Запуск одной ячейки

Нажмите кнопку запуска слева от ячейки:

```text
▶
```

Или используйте клавиши:

```text
Shift + Enter
```

### Запуск всех ячеек

В верхней панели ноутбука выберите:

```text
Run All
```

### Рекомендуемый порядок

Для учебного занятия лучше запускать ячейки сверху вниз.

Не рекомендуется запускать ячейки в случайном порядке, потому что переменные создаются постепенно.

---

## 11. Как смотреть переменные в VS Code

После выполнения ячеек можно смотреть переменные, созданные в ноутбуке.

В Jupyter-ноутбуке VS Code обычно доступна панель переменных:

```text
Variables
```

Через нее можно увидеть:

- имя переменной;
- тип объекта;
- размер таблицы;
- значение или краткое представление.

Для таблиц `pandas` удобно открывать Data Viewer, если он доступен в интерфейсе.

Примеры переменных в нашем проекте:

```python
sales
products
regions
clients
sales_prepared
category_summary
```

### Если переменной нет

Возможные причины:

1. Ячейка, где переменная создается, еще не была запущена.
2. Kernel был перезапущен.
3. В ячейке была ошибка.
4. Переменная называется иначе.

---

## 12. Как работать с терминалом

Терминал нужен для команд:

- установка зависимостей;
- проверка окружения;
- запуск `.py`-файлов;
- запуск R-скриптов;
- проверка файлов и папок.

### Частые команды

Проверить Python:

```bash
python --version
```

Проверить pip:

```bash
pip --version
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить проверку окружения:

```bash
python environment_check.py
```

Посмотреть файлы:

```bash
ls
```

На Windows:

```powershell
dir
```

Создать папку:

```bash
mkdir data/output
```

---

## 13. Как запускать `.py`-файлы

В проекте есть файл:

```text
environment_check.py
```

Он проверяет, что нужные Python-библиотеки установлены.

### Способ 1. Через терминал

Из корня проекта выполните:

```bash
python environment_check.py
```

### Способ 2. Через интерфейс VS Code

1. Откройте файл:

```text
environment_check.py
```

2. Нажмите кнопку запуска Python-файла в правом верхнем углу редактора.

Обычно она называется:

```text
Run Python File
```

Результат появится в терминале VS Code.

---

## 14. Как запускать учебные ноутбуки по порядку

Рекомендуемый порядок:

```text
00_setup_and_check.ipynb
01_data_loading_formats.ipynb
02_dataframe_types_and_quality.ipynb
03_data_integration.ipynb
04_basic_analysis.ipynb
05_basic_visualization.ipynb
06_python_to_r_bridge.ipynb
```

### Почему порядок важен

Некоторые ноутбуки создают файлы, которые нужны следующим ноутбукам.

Например:

```text
03_data_integration.ipynb
```

создает:

```text
data/prepared/sales_prepared.csv
```

А этот файл затем используется в:

```text
04_basic_analysis.ipynb
05_basic_visualization.ipynb
06_python_to_r_bridge.ipynb
```

---

## 15. Как использовать R в VS Code

R-часть проекта находится в папке:

```text
r/
```

Там есть файлы:

```text
install_packages.R
01_read_python_result.R
02_duckdb_from_r.R
03_basic_r_visualization.R
```

### Что нужно установить

Для R-части нужен установленный R.

Также желательно установить расширение VS Code:

```text
R
```

Оно добавляет:

- подсветку R-кода;
- работу с R-терминалом;
- просмотр переменных;
- просмотр графиков;
- поддержку R Markdown.

---

## 16. Как установить R-пакеты

Сначала запустите скрипт установки пакетов:

```bash
Rscript r/install_packages.R
```

Или из R-консоли:

```r
source("r/install_packages.R")
```

Скрипт установит и проверит пакеты:

```text
tidyverse
readxl
jsonlite
DBI
duckdb
arrow
ggplot2
IRkernel
reticulate
```

### Если команда `Rscript` не найдена

Возможные причины:

1. R не установлен.
2. R установлен, но не добавлен в PATH.
3. Терминал VS Code был открыт до установки R.

Что сделать:

- перезапустить VS Code;
- проверить установку R;
- открыть RStudio/Positron как резервный вариант;
- выполнить `source("r/install_packages.R")` внутри R.

---

## 17. Как запускать R-скрипты

Перед запуском R-скриптов нужно выполнить ноутбук:

```text
06_python_to_r_bridge.ipynb
```

Он создает файлы:

```text
data/output/python_to_r/sales_prepared_for_r.csv
data/output/python_to_r/sales_prepared_for_r.xlsx
data/output/python_to_r/analytics.duckdb
```

После этого можно запускать R-скрипты.

### Чтение CSV и Excel из R

```bash
Rscript r/01_read_python_result.R
```

### Чтение DuckDB из R

```bash
Rscript r/02_duckdb_from_r.R
```

### Простая визуализация в R

```bash
Rscript r/03_basic_r_visualization.R
```

Графики R сохраняются в папку:

```text
data/output/r_figures/
```

---

## 18. Как запускать R-код из редактора VS Code

Если установлено R-расширение:

1. Откройте файл `.R`, например:

```text
r/01_read_python_result.R
```

2. Выделите нужную строку или блок кода.
3. Выполните команду запуска выделенного R-кода.

В зависимости от настроек расширения команда может быть доступна через:

```text
Ctrl + Enter
```

или через Command Palette.

Если запуск из VS Code не получается, используйте терминал:

```bash
Rscript r/01_read_python_result.R
```

---

## 19. Как использовать R в Jupyter

Скрипт:

```text
r/install_packages.R
```

пытается зарегистрировать R-kernel для Jupyter через `IRkernel`.

Если регистрация прошла успешно, в Jupyter/VS Code при выборе Kernel может появиться:

```text
R data-course
```

После этого можно создавать R-ноутбуки или запускать `.ipynb` с R-kernel.

### Важно

Для основной части занятия R-kernel не обязателен.  
Достаточно запускать R-скрипты через:

```bash
Rscript
```

---

## 20. Типовые проблемы и диагностика

### Проблема 1. VS Code не видит Python-окружение

Что проверить:

```bash
python -c "import sys; print(sys.executable)"
```

Решение:

1. Откройте Command Palette.
2. Выполните:

```text
Python: Select Interpreter
```

3. Выберите Python из `.venv`.

---

### Проблема 2. В ноутбуке ошибка `ModuleNotFoundError`

Пример:

```text
ModuleNotFoundError: No module named 'pandas'
```

Причина: выбран не тот Python или зависимости не установлены.

Что сделать:

```bash
pip install -r requirements.txt
```

Затем выбрать правильный Kernel в ноутбуке.

---

### Проблема 3. Файл данных не найден

Пример:

```text
FileNotFoundError: data/raw/sales.csv
```

Что проверить:

```python
from pathlib import Path
print(Path.cwd())
print(Path("data/raw/sales.csv").exists())
```

Частая причина: проект открыт не с корневой папки.

---

### Проблема 4. Ячейки ноутбука не запускаются

Проверьте:

1. выбран ли Kernel;
2. не завис ли Kernel;
3. установлены ли зависимости;
4. нет ли ошибки в предыдущей ячейке.

Можно перезапустить Kernel:

```text
Restart Kernel
```

---

### Проблема 5. Переменная не отображается

Причины:

- ячейка не была выполнена;
- Kernel перезапущен;
- переменная создана с другим именем;
- в коде выше была ошибка.

Решение: запустить ячейки сверху вниз.

---

### Проблема 6. R не видит файлы Python

Проверьте рабочую папку R:

```r
getwd()
list.files()
```

Проверьте существование файла:

```r
file.exists("data/output/python_to_r/sales_prepared_for_r.csv")
```

Если `FALSE`, сначала выполните:

```text
06_python_to_r_bridge.ipynb
```

---

### Проблема 7. DuckDB-файл занят

Если Python или R держит открытое подключение к DuckDB, другой процесс может не получить доступ к файлу.

В Python закрывайте соединение:

```python
connection.close()
```

В R закрывайте соединение:

```r
dbDisconnect(con, shutdown = TRUE)
```

---

## 21. Рекомендуемый сценарий для занятия

### Шаг 1. Открыть проект

```text
File → Open Folder...
```

Выбрать корневую папку проекта.

### Шаг 2. Выбрать Python

```text
Ctrl + Shift + P → Python: Select Interpreter → .venv
```

### Шаг 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### Шаг 4. Проверить окружение

```bash
python environment_check.py
```

### Шаг 5. Запустить первый ноутбук

```text
notebooks_student/00_setup_and_check.ipynb
```

### Шаг 6. Выполнять ноутбуки по порядку

```text
00 → 01 → 02 → 03 → 04 → 05 → 06
```

### Шаг 7. Запустить R-часть

```bash
Rscript r/install_packages.R
Rscript r/01_read_python_result.R
Rscript r/02_duckdb_from_r.R
Rscript r/03_basic_r_visualization.R
```

---

## 22. Мини-чек-лист слушателя

Перед началом работы проверьте:

- [ ] проект открыт как папка, а не как отдельный файл;
- [ ] выбран Python из `.venv`;
- [ ] `pip install -r requirements.txt` выполнен;
- [ ] `python environment_check.py` показывает, что окружение готово;
- [ ] первый ноутбук `00_setup_and_check.ipynb` запускается;
- [ ] файлы из `data/raw/` видны;
- [ ] после `03_data_integration.ipynb` появляется `data/prepared/sales_prepared.csv`;
- [ ] после `06_python_to_r_bridge.ipynb` появляются файлы в `data/output/python_to_r/`;
- [ ] R-скрипты запускаются через `Rscript`.

---

## 23. Полезные ссылки на официальную документацию

- Python environments in VS Code: https://code.visualstudio.com/docs/python/environments
- Jupyter Notebooks in VS Code: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
- Python in VS Code: https://code.visualstudio.com/docs/languages/python
- R in Visual Studio Code: https://code.visualstudio.com/docs/languages/r
- Jupyter kernel management in VS Code: https://code.visualstudio.com/docs/datascience/jupyter-kernel-management
