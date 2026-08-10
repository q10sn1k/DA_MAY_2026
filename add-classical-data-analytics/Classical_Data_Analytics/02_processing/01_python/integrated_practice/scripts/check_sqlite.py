"""Проверка SQLite-базы для учебного комплекта.

Запуск из корня проекта:
python scripts/check_sqlite.py
"""
from pathlib import Path
import sqlite3

project_root = Path.cwd()
db_path = project_root / 'sql' / 'analytics_demo.sqlite'

if not db_path.exists():
    raise FileNotFoundError(f'База не найдена: {db_path}')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

for table in ['sales', 'products', 'regions', 'clients']:
    cursor.execute(f'SELECT COUNT(*) FROM {table}')
    rows_count = cursor.fetchone()[0]
    print(f'{table}: {rows_count} rows')

connection.close()
print('SQLite-проверка завершена.')
