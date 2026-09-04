# Импорт в GitHub

Целевой путь:

```text
groups/VNIIT_MSK5/2026-09-05_viz/
```

Существующий каталог `add-classical-data-analytics/` изменять не требуется.

## Рекомендуемый вариант через Git

Из корня локальной копии `q10sn1k/DA_MAY_2026`:

```bash
git switch main
git pull
git switch -c vniit-moscow-5-2026-09-05-visualization
```

Скопируйте каталог `groups/` из архива в корень репозитория, затем:

```bash
git add groups/VNIIT_MSK5/2026-09-05_viz
git commit -m "Add VNIIT Moscow 5 visualization practice for 2026-09-05"
git push -u origin vniit-moscow-5-2026-09-05-visualization
```

После проверки можно открыть Pull Request в `main`.

## Контроль после загрузки

1. Откройте GitHub-страницу нового каталога.
2. Проверьте отображение README и Markdown-файлов.
3. Скачайте/клонируйте ветку на чистую машину.
4. Выполните `python env_check.py`.
5. Запустите преподавательские ноутбуки сверху вниз.
