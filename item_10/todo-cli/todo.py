"""Консольное Todo-приложение для управления списком задач.

Приложение работает с JSON-файлом todo.json, предоставляет команды
add, list, done, delete через argparse.
"""

import argparse
import json
import os
import sys
from typing import Any


# Путь к файлу хранения задач — вынесен как константа,
# чтобы не дублировать строку и легко менять при необходимости
TODO_FILE: str = "todo.json"


def load_tasks(file_path: str) -> list[dict[str, Any]]:
    """Загрузить задачи из JSON-файла.

    Если файл отсутствует или повреждён — возвращает пустой список,
    чтобы приложение могло работать с чистого листа.

    Args:
        file_path: Путь к JSON-файлу с задачами.

    Returns:
        Список задач (словарей).
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Файл повреждён или не читается — начинаем с пустого списка
        return []


def save_tasks(tasks: list[dict[str, Any]], file_path: str) -> None:
    """Сохранить список задач в JSON-файл.

    Args:
        tasks: Список задач для сохранения.
        file_path: Путь к JSON-файлу.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def generate_task_id(tasks: list[dict[str, Any]]) -> int:
    """Сгенерировать уникальный числовой ID для новой задачи.

    Используем максимальный существующий ID + 1, чтобы гарантировать
    уникальность даже после удаления задач из середины списка.

    Args:
        tasks: Текущий список задач.

    Returns:
        Уникальный числовой ID.
    """
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(tasks: list[dict[str, Any]], text: str) -> list[dict[str, Any]]:
    """Добавить новую задачу в список.

    Args:
        tasks: Текущий список задач.
        text: Текст новой задачи.

    Returns:
        Обновлённый список задач.
    """
    task_id = generate_task_id(tasks)
    new_task = {
        "id": task_id,
        "text": text,
        "done": False,
    }
    return tasks + [new_task]


def find_task_by_id(tasks: list[dict[str, Any]], task_id: int) -> int | None:
    """Найти индекс задачи по её ID.

    Args:
        tasks: Список задач.
        task_id: Искомый ID задачи.

    Returns:
        Индекс задачи в списке или None, если задача не найдена.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return index
    return None


def mark_task_done(tasks: list[dict[str, Any]], task_id: int) -> list[dict[str, Any]]:
    """Отметить задачу как выполненную.

    Args:
        tasks: Текущий список задач.
        task_id: ID задачи для отметки.

    Returns:
        Обновлённый список задач.

    Raises:
        ValueError: Если задача с указанным ID не найдена.
    """
    index = find_task_by_id(tasks, task_id)
    if index is None:
        raise ValueError(f"Задача с ID {task_id} не найдена")
    # Создаём копию словаря, чтобы не мутировать оригинальный список
    updated_task = {**tasks[index], "done": True}
    return tasks[:index] + [updated_task] + tasks[index + 1:]


def delete_task(tasks: list[dict[str, Any]], task_id: int) -> list[dict[str, Any]]:
    """Удалить задачу по ID.

    Args:
        tasks: Текущий список задач.
        task_id: ID задачи для удаления.

    Returns:
        Обновлённый список задач.

    Raises:
        ValueError: Если задача с указанным ID не найдена.
    """
    index = find_task_by_id(tasks, task_id)
    if index is None:
        raise ValueError(f"Задача с ID {task_id} не найдена")
    return tasks[:index] + tasks[index + 1:]


def format_task(task: dict[str, Any]) -> str:
    """Отформатировать задачу для вывода в консоль.

    Args:
        task: Словарь задачи.

    Returns:
        Строка вида "[x] Текст задачи" или "[ ] Текст задачи".
    """
    status = "x" if task["done"] else " "
    return f"[{status}] {task['id']}. {task['text']}"


def print_tasks(tasks: list[dict[str, Any]]) -> None:
    """Вывести список задач в консоль.

    Args:
        tasks: Список задач для вывода.
    """
    if not tasks:
        print("Список задач пуст.")
        return
    for task in tasks:
        print(format_task(task))


def build_parser() -> argparse.ArgumentParser:
    """Создать и настроить парсер аргументов командной строки.

    Returns:
        Настроенный объект ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        description="Todo-приложение для управления списком задач"
    )
    subparsers = parser.add_subparsers(dest="command", help="Команда")

    # Подкоманда add — добавление задачи
    add_parser = subparsers.add_parser("add", help="Добавить новую задачу")
    add_parser.add_argument("text", help="Текст задачи")

    # Подкоманда list — вывод всех задач
    subparsers.add_parser("list", help="Показать все задачи")

    # Подкоманда done — отметка задачи как выполненной
    done_parser = subparsers.add_parser("done", help="Отметить задачу как выполненную")
    done_parser.add_argument("id", type=int, help="ID задачи")

    # Подкоманда delete — удаление задачи
    delete_parser = subparsers.add_parser("delete", help="Удалить задачу")
    delete_parser.add_argument("id", type=int, help="ID задачи")

    return parser


def handle_add(args: argparse.Namespace, file_path: str) -> None:
    """Обработать команду add — добавление задачи.

    Args:
        args: Разобранные аргументы командной строки.
        file_path: Путь к файлу хранения задач.
    """
    tasks = load_tasks(file_path)
    updated_tasks = add_task(tasks, args.text)
    save_tasks(updated_tasks, file_path)
    print(f"Задача добавлена с ID {generate_task_id(tasks)}")


def handle_list(args: argparse.Namespace, file_path: str) -> None:
    """Обработать команду list — вывод всех задач.

    Args:
        args: Разобранные аргументы командной строки.
        file_path: Путь к файлу хранения задач.
    """
    tasks = load_tasks(file_path)
    print_tasks(tasks)


def handle_done(args: argparse.Namespace, file_path: str) -> None:
    """Обработать команду done — отметка задачи как выполненной.

    Args:
        args: Разобранные аргументы командной строки.
        file_path: Путь к файлу хранения задач.

    Raises:
        SystemExit: Если задача не найдена.
    """
    tasks = load_tasks(file_path)
    try:
        updated_tasks = mark_task_done(tasks, args.id)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    save_tasks(updated_tasks, file_path)
    print(f"Задача {args.id} отмечена как выполненная")


def handle_delete(args: argparse.Namespace, file_path: str) -> None:
    """Обработать команду delete — удаление задачи.

    Args:
        args: Разобранные аргументы командной строки.
        file_path: Путь к файлу хранения задач.

    Raises:
        SystemExit: Если задача не найдена.
    """
    tasks = load_tasks(file_path)
    try:
        updated_tasks = delete_task(tasks, args.id)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    save_tasks(updated_tasks, file_path)
    print(f"Задача {args.id} удалена")


def main() -> None:
    """Точка входа — разбор аргументов и вызов соответствующей команды."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    # Словарь маппинга команд на обработчики — позволяет избежать цепочки if/elif
    handlers = {
        "add": handle_add,
        "list": handle_list,
        "done": handle_done,
        "delete": handle_delete,
    }
    handlers[args.command](args, TODO_FILE)


if __name__ == "__main__":
    main()
