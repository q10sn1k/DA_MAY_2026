# Словарь данных

## Общие соглашения

- технические имена полей — на английском языке;
- временные метки исходных событий хранятся в UTC;
- пустые значения в целевом признаке означают, что обращение ещё не решено;
- идентификаторы синтетические и не связаны с реальными системами;
- CSV-файлы записаны в UTF-8 с разделителем `,`.

## `tickets.csv`

Гранулярность: одна строка — одна версия карточки обращения. После дедупликации должна остаться одна строка на `ticket_id`.

| Поле | Тип | Доступность | Описание |
|---|---|---|---|
| `ticket_id` | string | сразу | Идентификатор обращения |
| `source_system` | category | сразу | Система-источник: CRM, портал или чат-платформа |
| `source_record_id` | string | сразу | Идентификатор записи в источнике |
| `schema_version` | string | при загрузке | Версия схемы источника |
| `load_ts` | datetime | при загрузке | Время попадания записи в аналитический контур |
| `source_updated_at` | datetime | при загрузке | Последнее изменение карточки в источнике |
| `created_at_utc` | datetime | сразу | Время создания обращения в UTC |
| `first_response_at_utc` | datetime | после ответа | Время первого ответа |
| `resolved_at_utc` | datetime | после решения | Время решения |
| `closed_at_utc` | datetime | после закрытия | Время закрытия |
| `created_date` | date | производное | Календарная дата создания |
| `created_hour_local` | integer | производное | Локальный час создания |
| `created_weekday` | integer | производное | День недели: 0 — понедельник, 6 — воскресенье |
| `channel` | category | сразу | Канал поступления: email, chat, phone, portal |
| `category` | category | сразу | Основная категория обращения |
| `subcategory` | category | сразу | Подкатегория |
| `priority` | ordinal | сразу | low, medium, high, critical |
| `customer_segment` | category | сразу | SMB, Enterprise, Public |
| `product` | category | сразу | Продукт или сервис |
| `product_version` | string | сразу | Версия продукта |
| `language` | category | сразу | Язык обращения |
| `initial_team_id` | string | сразу | Первоначально назначенная команда |
| `team_id` | string | сразу | Рабочая команда |
| `region_id` | string | сразу | Регион обращения |
| `description_length` | integer | сразу | Длина описания обращения |
| `attachment_count` | integer | сразу | Число вложений |
| `is_vip` | integer | сразу | Признак приоритетного клиента: 0/1 |
| `customer_tenure_days` | integer | сразу | Длительность отношений с клиентом |
| `prior_tickets_30d` | integer | сразу | Число обращений клиента за 30 дней |
| `prior_tickets_90d` | integer | сразу | Число обращений клиента за 90 дней |
| `previous_sla_breaches_90d` | integer | сразу | Прошлые нарушения SLA за 90 дней |
| `requested_callback` | integer | сразу | Запрошен обратный звонок: 0/1 |
| `status` | category | текущая | Текущий или итоговый статус |
| `first_response_min` | float | после ответа | Время первого ответа в минутах |
| `resolution_min` | float | после решения | Время решения в минутах |
| `sla_target_min` | integer | сразу | Норматив SLA в минутах |
| `sla_breached` | integer/null | после решения | 1 — SLA нарушен, 0 — выполнен, null — исход неизвестен |
| `reopen_count` | integer | после решения | Число повторных открытий |
| `escalation_count` | integer | после обработки | Число эскалаций |
| `csat` | float/null | после закрытия | Оценка удовлетворённости от 1 до 5 |

### Признаки с утечкой для классификации SLA

Нельзя использовать при прогнозе в момент регистрации:

- `first_response_at_utc` и `first_response_min`;
- `resolved_at_utc`, `closed_at_utc`, `resolution_min`;
- `sla_breached` как входной признак;
- `reopen_count`, `escalation_count`, `csat`;
- любой результат события, произошедшего после момента прогноза.

## `ticket_events.csv`

Гранулярность: одна строка — одно событие обращения.

| Поле | Тип | Описание |
|---|---|---|
| `event_id` | string | Идентификатор события |
| `ticket_id` | string | Идентификатор обращения |
| `event_ts_utc` | datetime | Время события в UTC |
| `event_type` | category | created, assigned, agent_response, customer_response и другие |
| `status_from` | category | Статус до события |
| `status_to` | category | Статус после события |
| `team_from` | string | Команда до события |
| `team_to` | string | Команда после события |
| `actor_type` | category | customer, agent, system |
| `queue_name` | category | Очередь обработки |
| `comment_length` | integer | Длина комментария |
| `source_system` | category | Источник события |
| `load_ts` | datetime | Время загрузки |

Перед объединением с `tickets` агрегировать по `ticket_id`, например рассчитывать число событий, переводов, эскалаций, клиентских сообщений и время первого назначения.

## `team_capacity_daily.csv`

Гранулярность: одна команда за один календарный день.

| Поле | Тип | Доступность | Описание |
|---|---|---|---|
| `date` | date | сразу | Дата |
| `team_id` | string | сразу | Команда |
| `planned_agents` | integer | заранее | Плановое число сотрудников |
| `active_agents` | integer | начало дня | Активные сотрудники |
| `absence_count` | integer | начало дня | Отсутствующие сотрудники |
| `shift_hours` | float | начало дня | Доступные человеко-часы |
| `backlog_start` | integer | начало дня | Очередь на начало дня |
| `backlog_end` | integer | конец дня | Очередь на конец дня |
| `incoming_tickets` | integer | конец дня | Новые обращения за день |
| `resolved_tickets` | integer | конец дня | Решённые обращения за день |
| `avg_handle_time_min` | float | конец дня | Среднее время обработки |
| `overtime_hours` | float | конец дня | Сверхурочные часы |
| `load_ts` | datetime | при загрузке | Время загрузки |

Для классификации риска при регистрации допустимы `active_agents`, `absence_count`, `shift_hours`, `backlog_start`. Показатели конца текущего дня использовать нельзя.

## `calendar_events.csv`

Гранулярность: один календарный день.

| Поле | Тип | Описание |
|---|---|---|
| `date` | date | Дата |
| `weekday` | integer | День недели |
| `is_weekend` | integer | Выходной: 0/1 |
| `holiday_flag` | integer | Праздничный день: 0/1 |
| `pre_holiday_flag` | integer | Предпраздничный день: 0/1 |
| `release_flag` | integer | Выпуск версии: 0/1 |
| `promo_flag` | integer | Маркетинговая активность: 0/1 |
| `outage_flag` | integer | Технический сбой: 0/1 |
| `outage_minutes` | integer | Продолжительность сбоя |
| `month_end_flag` | integer | Конец месяца: 0/1 |
| `quarter_end_flag` | integer | Конец квартала: 0/1 |

## `load_log.csv`

Гранулярность: одна загрузка одного источника.

| Поле | Тип | Описание |
|---|---|---|
| `batch_id` | string | Идентификатор загрузки |
| `source_system` | category | Источник |
| `load_date` | date | Дата загрузки |
| `extracted_at` | datetime | Начало извлечения |
| `loaded_at` | datetime | Окончание загрузки |
| `expected_rows` | integer | Ожидаемое число строк |
| `loaded_rows` | integer | Загруженное число строк |
| `rejected_rows` | integer | Отклонённые строки |
| `freshness_minutes` | integer | Задержка поступления данных |
| `schema_version` | string | Версия схемы |
| `checksum_match` | integer | Совпадение контрольной суммы: 0/1 |
| `load_status` | category | success, warning, failed |
| `error_code` | string/null | Код ошибки |

## `teams.xlsx`

Гранулярность: одна команда.

| Поле | Тип | Описание |
|---|---|---|
| `team_id` | string | Ключ команды |
| `team_name` | string | Техническое название |
| `region_id` | string | Регион |
| `specialization` | category | Специализация |
| `support_level` | category | L1 или L2 |
| `supports_24x7` | integer | Круглосуточная поддержка: 0/1 |
| `opened_date` | date | Дата запуска команды |
| `target_utilization` | float | Целевая загрузка |
| `target_csat` | float | Целевой CSAT |
| `target_sla_rate` | float | Целевая доля выполнения SLA |
| `manager_alias` | string | Синтетический псевдоним руководителя |
| `is_active` | integer | Активность команды: 0/1 |

## `regions.json`

Гранулярность: один регион.

| Поле | Тип | Описание |
|---|---|---|
| `region_id` | string | Ключ региона |
| `city_name` | string | Город |
| `macro_region` | string | Макрорегион |
| `utc_offset_hours` | integer | Смещение относительно UTC |
| `latitude` | float | Широта |
| `longitude` | float | Долгота |
| `geo_available` | integer | Допуск на карту: 0/1 |
| `support_model` | category | Модель поддержки |
| `population_tier` | category | Условный размер города |
