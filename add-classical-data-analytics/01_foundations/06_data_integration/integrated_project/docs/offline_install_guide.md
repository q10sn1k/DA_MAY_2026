# Офлайн-установка и подготовка к занятию без Wi‑Fi

## 1. Назначение инструкции

Эта инструкция нужна для проведения занятия по теме:

**«Загрузка и интеграция данных из различных форматов. Инструменты для сбора данных. Основы Python для обработки данных»**

Сценарий: в аудитории может не быть стабильного Wi‑Fi, доступ к внешним сайтам может быть ограничен, API могут не открываться, а установка библиотек из интернета может не работать.

Цель подготовки:

- заранее установить нужное ПО;
- заранее скачать Python-зависимости;
- проверить окружение до занятия;
- запустить JupyterLab локально;
- заменить API и сайты локальными файлами;
- обеспечить резервный сценарий для слушателей.

---

## 2. Главный принцип офлайн-занятия

Для занятия без Wi‑Fi нельзя рассчитывать на команды, которые требуют интернета:

```bash
pip install pandas
pip install -r requirements.txt
install.packages("tidyverse")
```

Эти команды работают только при наличии доступа к репозиториям пакетов.

Правильный подход:

```text
До занятия, при наличии интернета:
скачать установщики, зависимости, датасеты и документацию
↓
В аудитории без Wi‑Fi:
устанавливать и запускать всё из локальных файлов
```

---

## 3. Что нужно подготовить заранее

### 3.1. Минимальный комплект на флешке или сетевой папке

Подготовьте папку:

```text
offline_course_bundle/
│
├── installers/
│   ├── python/
│   ├── vscode/
│   └── r/
│
├── wheels/
│   └── *.whl
│
├── project/
│   ├── data/
│   ├── notebooks_student/
│   ├── notebooks_teacher/
│   ├── r/
│   ├── docs/
│   ├── requirements.txt
│   ├── environment_check.py
│   └── README.md
│
└── docs_offline/
    ├── python_installation_notes.pdf
    ├── jupyter_notes.pdf
    └── troubleshooting.md
```

### 3.2. Что должно быть внутри

| Компонент | Зачем нужен |
|---|---|
| Установщик Python | Чтобы поставить Python без интернета |
| Установщик VS Code | Чтобы открыть проект и ноутбуки |
| Установщик R | Для R-части занятия |
| Python wheels | Для установки библиотек без интернета |
| Учебный проект | Ноутбуки, данные, скрипты, инструкции |
| Локальные датасеты | Замена API и сайтов |
| PDF/Markdown-инструкции | Резерв вместо онлайн-документации |

---

## 4. Что установить заранее на компьютеры

### 4.1. Python

Рекомендуется Python версии **3.10 или новее**.

Проверка:

```bash
python --version
```

или:

```bash
python3 --version
```

Если Python установлен корректно, команда покажет версию, например:

```text
Python 3.11.9
```

### 4.2. VS Code

VS Code нужен для:

- открытия проекта;
- запуска `.ipynb`;
- работы с терминалом;
- запуска `.py`;
- запуска R-скриптов.

Желательно заранее установить расширения:

```text
Python
Jupyter
R
```

### 4.3. R

R нужен только для части:

```text
06_python_to_r_bridge.ipynb
r/*.R
```

Проверка:

```bash
R --version
```

или:

```bash
Rscript --version
```

Если R не нужен на конкретном занятии, этот блок можно пропустить.

---

## 5. Подготовка Python-зависимостей заранее

### 5.1. Почему обычный `pip install` не подходит

В аудитории без Wi‑Fi команда:

```bash
pip install -r requirements.txt
```

может не сработать, потому что `pip` будет пытаться скачать пакеты из интернета.

Для офлайн-сценария нужно заранее скачать пакеты в папку `wheels/`.

---

## 6. Как скачать Python-пакеты заранее

Эти команды выполняются **до занятия** на компьютере с интернетом.

Перейдите в корень проекта, где лежит:

```text
requirements.txt
```

Создайте папку для wheels:

```bash
mkdir wheels
```

Скачайте зависимости:

```bash
python -m pip download -r requirements.txt -d wheels
```

После выполнения в папке `wheels/` должны появиться файлы:

```text
*.whl
*.tar.gz
```

Пример:

```text
wheels/
├── pandas-...
├── numpy-...
├── matplotlib-...
├── openpyxl-...
├── duckdb-...
├── pyarrow-...
├── jupyterlab-...
└── ...
```

### Важно

Скачивать wheels лучше на той же операционной системе и архитектуре, что и компьютеры в аудитории.

Например:

| Где будет занятие | Где лучше скачивать wheels |
|---|---|
| Windows 64-bit | Windows 64-bit |
| macOS ARM | macOS ARM |
| Linux x86_64 | Linux x86_64 |

Некоторые пакеты имеют платформенно-зависимые бинарные сборки.

---

## 7. Как проверить, что wheelhouse готов

На компьютере с интернетом можно протестировать установку в чистое окружение.

Создайте тестовое окружение:

```bash
python -m venv .venv_test
```

Активируйте его.

Windows PowerShell:

```powershell
.venv_test\Scripts\Activate.ps1
```

Windows cmd:

```cmd
.venv_test\Scripts\activate.bat
```

macOS / Linux:

```bash
source .venv_test/bin/activate
```

Установите зависимости **только из локальной папки wheels**:

```bash
python -m pip install --no-index --find-links wheels -r requirements.txt
```

Проверьте:

```bash
python environment_check.py
```

Если проверка успешна, папку `wheels/` можно переносить на компьютеры без Wi‑Fi.

---

## 8. Установка на компьютере без Wi‑Fi

### 8.1. Открыть проект

Скопируйте проект на компьютер слушателя, например:

```text
C:\data_course\data_loading_integration_python\
```

или:

```text
./data_loading_integration_python/
```

Откройте терминал в корне проекта.

Проверьте, что рядом есть:

```text
requirements.txt
environment_check.py
wheels/
data/
notebooks_student/
```

---

## 9. Создание виртуального окружения

Создайте окружение:

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Если PowerShell блокирует запуск скриптов, используйте cmd:

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source .venv/bin/activate
```

После активации в терминале обычно появляется:

```text
(.venv)
```

---

## 10. Установка зависимостей без интернета

Установите зависимости из локальной папки `wheels/`:

```bash
python -m pip install --no-index --find-links wheels -r requirements.txt
```

Расшифровка команды:

| Фрагмент | Что означает |
|---|---|
| `python -m pip install` | запустить pip через выбранный Python |
| `--no-index` | не обращаться в интернет-репозиторий |
| `--find-links wheels` | искать пакеты в локальной папке `wheels` |
| `-r requirements.txt` | установить список пакетов из файла requirements |

Если установка прошла успешно, переходите к проверке окружения.

---

## 11. Проверка Python-окружения

Выполните:

```bash
python environment_check.py
```

Скрипт должен проверить:

```text
pandas
numpy
matplotlib
openpyxl
duckdb
pyarrow
jupyterlab
```

Успешный результат:

```text
ОКРУЖЕНИЕ ГОТОВО
```

Если есть ошибки, смотрите раздел диагностики ниже.

---

## 12. Проверка Python вручную

Если нужно быстро проверить Python без скрипта:

```bash
python --version
```

Проверить путь к Python:

```bash
python -c "import sys; print(sys.executable)"
```

Проверить ключевые библиотеки:

```bash
python -c "import pandas, numpy, matplotlib, openpyxl, duckdb, pyarrow; print('OK')"
```

Проверить JupyterLab:

```bash
python -m jupyter lab --version
```

---

## 13. Запуск JupyterLab без интернета

Из корня проекта выполните:

```bash
python -m jupyter lab
```

Или:

```bash
jupyter lab
```

Если команда `jupyter` не находится, используйте более надежный вариант:

```bash
python -m jupyter lab
```

После запуска JupyterLab обычно откроет браузер с локальным адресом:

```text
http://localhost:8888/lab
```

или похожим.

### Важно

JupyterLab работает локально.  
Интернет для запуска ноутбуков не нужен, если все библиотеки уже установлены и все данные лежат в проекте.

---

## 14. Как запускать ноутбуки офлайн

Откройте папку:

```text
notebooks_student/
```

Запускайте ноутбуки по порядку:

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

Ноутбук:

```text
03_data_integration.ipynb
```

создает файл:

```text
data/prepared/sales_prepared.csv
```

Этот файл нужен для:

```text
04_basic_analysis.ipynb
05_basic_visualization.ipynb
06_python_to_r_bridge.ipynb
```

---

## 15. Что делать без доступа к API и сайтам

В этом учебном комплекте интернет не обязателен.

### 15.1. Чем заменить API

Если в программе занятия обсуждается сбор данных через API, в офлайн-сценарии используйте заранее подготовленные файлы:

```text
data/raw/regions.json
data/raw/clients.csv
data/raw/sales.csv
```

Объяснение для слушателей:

> В реальном проекте данные могли бы прийти из API. На занятии без интернета мы используем заранее сохраненный JSON/CSV как снимок ответа внешней системы.

### 15.2. Чем заменить сайт

Для демонстрации HTML-таблицы используйте локальный файл:

```text
data/raw/web_table_sample.html
```

Вместо:

```python
pd.read_html("https://example.com/table")
```

используйте:

```python
pd.read_html("data/raw/web_table_sample.html")
```

Объяснение для слушателей:

> Это локальная копия HTML-страницы. Принцип чтения таблицы тот же, но нам не нужен интернет.

### 15.3. Чем заменить онлайн-ноутбуки

Если нет доступа к Google Colab, Kaggle или облачным ноутбукам, используйте локальный JupyterLab:

```bash
python -m jupyter lab
```

### 15.4. Чем заменить онлайн-подсказки

Если нет доступа к ChatGPT/Qwen/поиску, используйте:

```text
README.md
docs/
notebooks_teacher/
environment_check.py
```

Для лектора лучше заранее подготовить PDF-версии ключевых инструкций.

---

## 16. Офлайн-сценарий для R

R-пакеты тоже нужно установить заранее.

### 16.1. Простой вариант

Если интернет был доступен до занятия, на каждом компьютере заранее выполните:

```bash
Rscript r/install_packages.R
```

### 16.2. Если R-пакеты нельзя скачать в аудитории

Подготовьте R-библиотеки заранее на компьютерах или используйте переносимый образ/установленную аудиторию.

Минимально для занятия нужны:

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

### 16.3. Проверка R

```bash
Rscript --version
```

Проверить загрузку пакетов:

```bash
Rscript r/install_packages.R
```

Запустить R-скрипты:

```bash
Rscript r/01_read_python_result.R
Rscript r/02_duckdb_from_r.R
Rscript r/03_basic_r_visualization.R
```

Перед этим должен быть выполнен ноутбук:

```text
06_python_to_r_bridge.ipynb
```

Он создает файлы:

```text
data/output/python_to_r/sales_prepared_for_r.csv
data/output/python_to_r/sales_prepared_for_r.xlsx
data/output/python_to_r/analytics.duckdb
```

---

## 17. Что проверить за день до занятия

### 17.1. На компьютере лектора

Проверьте:

```bash
python --version
python -m pip --version
python environment_check.py
python -m jupyter lab --version
```

Запустите JupyterLab:

```bash
python -m jupyter lab
```

Откройте и выполните:

```text
00_setup_and_check.ipynb
03_data_integration.ipynb
06_python_to_r_bridge.ipynb
```

Проверьте появление файлов:

```text
data/prepared/sales_prepared.csv
data/output/python_to_r/sales_prepared_for_r.csv
data/output/python_to_r/sales_prepared_for_r.xlsx
data/output/python_to_r/analytics.duckdb
```

### 17.2. На компьютере слушателя

Проверьте хотя бы один типовой компьютер аудитории:

```bash
python -m venv .venv
```

Активируйте окружение и установите зависимости:

```bash
python -m pip install --no-index --find-links wheels -r requirements.txt
```

Проверьте:

```bash
python environment_check.py
python -m jupyter lab --version
```

---

## 18. Быстрая диагностика проблем

### Проблема 1. `python` не найден

Проверить:

```bash
python --version
```

или:

```bash
py --version
```

На Windows иногда работает:

```bash
py -3 --version
```

Решение:

- установить Python;
- добавить Python в PATH;
- перезапустить терминал;
- использовать полный путь к `python.exe`.

---

### Проблема 2. `pip` пытается выйти в интернет

Если команда выглядит так:

```bash
pip install -r requirements.txt
```

она может пытаться скачать пакеты из интернета.

Для офлайн-установки используйте:

```bash
python -m pip install --no-index --find-links wheels -r requirements.txt
```

---

### Проблема 3. Не хватает пакета в `wheels/`

Ошибка может выглядеть так:

```text
No matching distribution found for ...
```

Возможные причины:

- пакет не был скачан заранее;
- скачан wheel не для той операционной системы;
- скачан wheel не для той версии Python;
- нет зависимого пакета.

Что сделать до занятия:

```bash
python -m pip download -r requirements.txt -d wheels
```

На той же ОС и версии Python, что будут в аудитории.

---

### Проблема 4. `ModuleNotFoundError`

Пример:

```text
ModuleNotFoundError: No module named 'pandas'
```

Причина:

- зависимости не установлены;
- активировано не то окружение;
- Jupyter использует другой Python.

Проверить:

```bash
python -c "import sys; print(sys.executable)"
```

В ноутбуке:

```python
import sys
sys.executable
```

Путь должен указывать на `.venv`.

---

### Проблема 5. JupyterLab не запускается

Проверьте:

```bash
python -m jupyter lab --version
```

Если команда не работает, проверьте установку:

```bash
python -m pip show jupyterlab
```

Если пакета нет:

```bash
python -m pip install --no-index --find-links wheels jupyterlab
```

Если браузер не открылся автоматически, скопируйте URL из терминала и откройте его вручную.

---

### Проблема 6. Ноутбук не видит файлы данных

Проверьте текущую папку в ноутбуке:

```python
from pathlib import Path

print(Path.cwd())
print(Path("data/raw/sales.csv").exists())
```

Если `False`, значит проект открыт не из корневой папки или данные лежат не там.

---

### Проблема 7. Нет доступа к внешнему API

Используйте локальные данные:

```text
data/raw/regions.json
data/raw/web_table_sample.html
```

Формулировка для аудитории:

> Сегодня мы работаем с локальным снимком данных. В реальном проекте эти данные могли бы быть получены через API или сайт.

---

## 19. Резервный план для лектора

Если установка у части слушателей не удалась:

1. Продолжить демонстрацию на компьютере лектора.
2. Раздать готовую папку `.venv`, если ОС и пути совместимы.
3. Использовать заранее подготовленный ноутбук с выполненными ячейками.
4. Дать слушателям смотреть код и результаты на экране.
5. После занятия дать инструкцию для локальной установки.

Если не запускается JupyterLab:

1. Использовать VS Code + Jupyter extension.
2. Использовать классический Jupyter Notebook, если установлен.
3. Запускать `.py`-фрагменты через терминал.
4. Показывать готовые HTML/PNG/Excel-результаты.

Если нет R:

1. Пропустить R-практику.
2. Показать R-код как демонстрационный.
3. Сосредоточиться на Python → CSV/Excel/Parquet/DuckDB.

---

## 20. Итоговый чек-лист офлайн-подготовки

### До занятия

- [ ] Скачан установщик Python.
- [ ] Скачан установщик VS Code.
- [ ] Скачан установщик R, если нужна R-часть.
- [ ] Скачаны расширения VS Code или подготовлена аудитория с установленными расширениями.
- [ ] Подготовлена папка `wheels/`.
- [ ] Проверена офлайн-установка через `--no-index --find-links wheels`.
- [ ] Подготовлена папка проекта.
- [ ] В проекте есть `data/raw/`.
- [ ] В проекте есть все ноутбуки.
- [ ] В проекте есть `requirements.txt`.
- [ ] В проекте есть `environment_check.py`.
- [ ] Подготовлены R-скрипты.
- [ ] Скопирована инструкция `docs/offline_install_guide.md`.

### В аудитории

- [ ] Открыть проект.
- [ ] Создать `.venv`.
- [ ] Активировать `.venv`.
- [ ] Установить зависимости из `wheels/`.
- [ ] Запустить `python environment_check.py`.
- [ ] Запустить `python -m jupyter lab`.
- [ ] Открыть `00_setup_and_check.ipynb`.
- [ ] Проверить чтение `data/raw/sales.csv`.
- [ ] Перейти к основным ноутбукам.

---

## 21. Краткая версия команд

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --no-index --find-links wheels -r requirements.txt
python environment_check.py
python -m jupyter lab
```

### Windows cmd

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --no-index --find-links wheels -r requirements.txt
python environment_check.py
python -m jupyter lab
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --no-index --find-links wheels -r requirements.txt
python environment_check.py
python -m jupyter lab
```

---

## 22. Официальные справочные ссылки

- Python `venv`: https://docs.python.org/3/library/venv.html
- Python tutorial: virtual environments: https://docs.python.org/3/tutorial/venv.html
- pip requirements files: https://pip.pypa.io/en/stable/reference/requirements-file-format.html
- pip download: https://pip.pypa.io/en/stable/cli/pip_download/
- Jupyter install: https://jupyter.org/install
