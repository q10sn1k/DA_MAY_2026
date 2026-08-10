#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
environment_check.py

Проверка Python-окружения для занятия:
"Загрузка и интеграция данных из различных форматов.
Инструменты для сбора данных. Основы Python для обработки данных".

Что проверяет:
- pandas
- numpy
- matplotlib
- openpyxl
- duckdb
- pyarrow
- jupyterlab

Как запускать:
    python environment_check.py
"""

from __future__ import annotations

import importlib
import importlib.metadata as metadata
import platform
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class PackageCheck:
    """Описание проверяемой зависимости."""

    display_name: str
    import_name: str
    distribution_name: str
    purpose: str


PACKAGES: list[PackageCheck] = [
    PackageCheck(
        display_name="pandas",
        import_name="pandas",
        distribution_name="pandas",
        purpose="таблицы, CSV, Excel, JSON, HTML, объединение данных",
    ),
    PackageCheck(
        display_name="numpy",
        import_name="numpy",
        distribution_name="numpy",
        purpose="числовые операции и базовые вычисления",
    ),
    PackageCheck(
        display_name="matplotlib",
        import_name="matplotlib",
        distribution_name="matplotlib",
        purpose="базовые графики и визуализация",
    ),
    PackageCheck(
        display_name="openpyxl",
        import_name="openpyxl",
        distribution_name="openpyxl",
        purpose="чтение и запись Excel-файлов .xlsx",
    ),
    PackageCheck(
        display_name="duckdb",
        import_name="duckdb",
        distribution_name="duckdb",
        purpose="локальная аналитическая база и SQL-запросы",
    ),
    PackageCheck(
        display_name="pyarrow",
        import_name="pyarrow",
        distribution_name="pyarrow",
        purpose="формат Parquet и обмен аналитическими данными",
    ),
    PackageCheck(
        display_name="jupyterlab",
        import_name="jupyterlab",
        distribution_name="jupyterlab",
        purpose="запуск учебных ноутбуков в JupyterLab",
    ),
]


def get_distribution_version(distribution_name: str) -> str:
    """Вернуть версию установленного пакета по имени distribution package."""
    try:
        return metadata.version(distribution_name)
    except metadata.PackageNotFoundError:
        return "не установлено"


def check_package(package: PackageCheck) -> dict[str, str | bool]:
    """Проверить, что пакет установлен и импортируется."""
    version = get_distribution_version(package.distribution_name)

    if version == "не установлено":
        return {
            "name": package.display_name,
            "installed": False,
            "imported": False,
            "version": version,
            "purpose": package.purpose,
            "error": "пакет не найден в текущем Python-окружении",
        }

    try:
        importlib.import_module(package.import_name)
        return {
            "name": package.display_name,
            "installed": True,
            "imported": True,
            "version": version,
            "purpose": package.purpose,
            "error": "",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "name": package.display_name,
            "installed": True,
            "imported": False,
            "version": version,
            "purpose": package.purpose,
            "error": f"пакет найден, но не импортируется: {exc}",
        }


def print_header() -> None:
    """Вывести информацию о Python и системе."""
    print("=" * 78)
    print("ПРОВЕРКА PYTHON-ОКРУЖЕНИЯ ДЛЯ ЗАНЯТИЯ")
    print("=" * 78)
    print(f"Python:       {sys.version.split()[0]}")
    print(f"Исполняемый:  {sys.executable}")
    print(f"Платформа:    {platform.platform()}")
    print("-" * 78)


def print_result(row: dict[str, str | bool]) -> None:
    """Печать результата проверки одного пакета."""
    status = "OK" if row["installed"] and row["imported"] else "FAIL"

    print(f"[{status}] {row['name']}")
    print(f"      Версия:     {row['version']}")
    print(f"      Назначение: {row['purpose']}")

    if row["error"]:
        print(f"      Ошибка:     {row['error']}")

    print()


def print_install_hint(missing_packages: list[str]) -> None:
    """Вывести подсказку по установке недостающих пакетов."""
    if not missing_packages:
        return

    print("-" * 78)
    print("Нужно установить или переустановить следующие пакеты:")
    print(" ".join(missing_packages))
    print()
    print("Команда для установки всего комплекта:")
    print("    pip install -r requirements.txt")
    print()
    print("Команда для установки только отсутствующих пакетов:")
    print(f"    pip install {' '.join(missing_packages)}")


def main() -> int:
    """Основная функция проверки окружения."""
    print_header()

    results = [check_package(package) for package in PACKAGES]

    for row in results:
        print_result(row)

    failed = [row for row in results if not (row["installed"] and row["imported"])]
    missing_packages = [str(row["name"]) for row in failed]

    print("=" * 78)

    if not failed:
        print("ОКРУЖЕНИЕ ГОТОВО")
        print("Все необходимые библиотеки установлены и успешно импортируются.")
        print("Можно запускать учебные ноутбуки.")
        print("=" * 78)
        return 0

    print("ОКРУЖЕНИЕ НЕ ГОТОВО")
    print("Часть библиотек отсутствует или не импортируется.")
    print_install_hint(missing_packages)
    print("=" * 78)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
