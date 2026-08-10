# SQL-файлы

- `docker-compose.yml` - быстрый запуск MySQL 8.0 для учебного занятия.
- `mysql_demo_schema.sql` - создание базы, таблиц `users` и `orders`, а также загрузка демонстрационных данных.

Базовый запуск:

```bash
docker compose up -d
```

Подключение к MySQL:

```bash
docker exec -it mysql_container mysql -u root -p
```

Пароль: `root`.

Загрузка готового SQL-сценария из папки `sql`:

```bash
docker exec -i mysql_container mysql -u root -proot < mysql_demo_schema.sql
```
