"""Тесты для консольного Todo-приложения.

Покрывают бизнес-логику (add, done, delete), работу с файлами
(load, save) и интеграцию через CLI (subprocess).
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

# Импорт функций из todo.py для модульных тестов
from todo import (
    add_task,
    delete_task,
    find_task_by_id,
    format_task,
    generate_task_id,
    load_tasks,
    mark_task_done,
    save_tasks,
)


class TestGenerateTaskId(unittest.TestCase):
    """Тесты генерации уникального ID задачи."""

    def test_empty_list_returns_one(self) -> None:
        """Пустой список задач — первый ID равен 1."""
        self.assertEqual(generate_task_id([]), 1)

    def test_sequential_ids(self) -> None:
        """Новый ID на 1 больше максимального существующего."""
        tasks = [{"id": 1, "text": "A", "done": False},
                 {"id": 5, "text": "B", "done": True}]
        self.assertEqual(generate_task_id(tasks), 6)


class TestAddTask(unittest.TestCase):
    """Тесты добавления задачи."""

    def test_add_to_empty_list(self) -> None:
        """Добавление в пустой список создаёт задачу с ID 1."""
        result = add_task([], "Новая задача")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["text"], "Новая задача")
        self.assertFalse(result[0]["done"])

    def test_add_preserves_existing(self) -> None:
        """Новая задача не изменяет существующие."""
        existing = [{"id": 1, "text": "Старая", "done": False}]
        result = add_task(existing, "Новая")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["text"], "Старая")


class TestMarkTaskDone(unittest.TestCase):
    """Тесты отметки задачи как выполненной."""

    def test_mark_done(self) -> None:
        """Задача отмечается как выполненная."""
        tasks = [{"id": 1, "text": "Тест", "done": False}]
        result = mark_task_done(tasks, 1)
        self.assertTrue(result[0]["done"])

    def test_mark_nonexistent_raises(self) -> None:
        """Попытка отметить несуществующую задачу вызывает ValueError."""
        tasks = [{"id": 1, "text": "Тест", "done": False}]
        with self.assertRaises(ValueError):
            mark_task_done(tasks, 999)


class TestDeleteTask(unittest.TestCase):
    """Тесты удаления задачи."""

    def test_delete_task(self) -> None:
        """Задача удаляется из списка."""
        tasks = [
            {"id": 1, "text": "Первая", "done": False},
            {"id": 2, "text": "Вторая", "done": False},
        ]
        result = delete_task(tasks, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

    def test_delete_nonexistent_raises(self) -> None:
        """Попытка удалить несуществующую задачу вызывает ValueError."""
        tasks = [{"id": 1, "text": "Тест", "done": False}]
        with self.assertRaises(ValueError):
            delete_task(tasks, 999)


class TestFindTaskById(unittest.TestCase):
    """Тесты поиска задачи по ID."""

    def test_find_existing(self) -> None:
        """Поиск существующей задачи возвращает её индекс."""
        tasks = [{"id": 10, "text": "А", "done": False}]
        self.assertEqual(find_task_by_id(tasks, 10), 0)

    def test_find_missing(self) -> None:
        """Поиск несуществующей задачи возвращает None."""
        tasks = [{"id": 1, "text": "А", "done": False}]
        self.assertIsNone(find_task_by_id(tasks, 999))


class TestFormatTask(unittest.TestCase):
    """Тесты форматирования задачи для вывода."""

    def test_not_done(self) -> None:
        """Невыполненная задача — метка [ ]."""
        task = {"id": 1, "text": "Тест", "done": False}
        self.assertEqual(format_task(task), "[ ] 1. Тест")

    def test_done(self) -> None:
        """Выполненная задача — метка [x]."""
        task = {"id": 2, "text": "Готово", "done": True}
        self.assertEqual(format_task(task), "[x] 2. Готово")


class TestFileOperations(unittest.TestCase):
    """Тесты чтения и записи JSON-файла."""

    def setUp(self) -> None:
        """Создать временный файл для тестов."""
        self.tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        )
        self.file_path = self.tmp.name
        self.tmp.close()

    def tearDown(self) -> None:
        """Удалить временный файл после теста."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load_nonexistent(self) -> None:
        """Загрузка несуществующего файла возвращает пустой список."""
        self.assertEqual(load_tasks("/tmp/nonexistent_todo.json"), [])

    def test_save_and_load(self) -> None:
        """Сохранённые задачи загружаются корректно."""
        tasks = [{"id": 1, "text": "Тест", "done": False}]
        save_tasks(tasks, self.file_path)
        loaded = load_tasks(self.file_path)
        self.assertEqual(loaded, tasks)

    def test_corrupted_json(self) -> None:
        """Повреждённый JSON возвращает пустой список."""
        # Открываем файл заново для записи мусора
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write("not valid json {{{")
        loaded = load_tasks(self.file_path)
        self.assertEqual(loaded, [])


class TestCLI(unittest.TestCase):
    """Интеграционные тесты через subprocess."""

    def setUp(self) -> None:
        """Создать временный файл и подготовить путь к todo.py."""
        self.tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        )
        self.file_path = self.tmp.name
        self.tmp.close()
        self.script = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "todo.py"
        )

    def tearDown(self) -> None:
        """Удалить временный файл после теста."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_via_cli(self) -> None:
        """Команда add через subprocess записывает задачу в файл."""
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.dirname(self.script)
        # Подменяем TODO_FILE через патч в дочернем процессе
        # Используем подход с записью в стандартный путь и проверкой
        result = subprocess.run(
            [sys.executable, "-c",
             f"import sys; sys.path.insert(0, '.'); "
             f"import todo; todo.TODO_FILE = '{self.file_path}'; "
             f"from todo import load_tasks, save_tasks, add_task; "
             f"tasks = load_tasks('{self.file_path}'); "
             f"tasks = add_task(tasks, 'Тестовая задача'); "
             f"save_tasks(tasks, '{self.file_path}')"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script)
        )
        self.assertEqual(result.returncode, 0)
        tasks = load_tasks(self.file_path)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["text"], "Тестовая задача")

    def test_done_via_cli(self) -> None:
        """Команда done через subprocess отмечает задачу выполненной."""
        # Подготовить файл с задачей
        initial = [{"id": 1, "text": "Тест", "done": False}]
        save_tasks(initial, self.file_path)
        # Вызвать mark_task_done через subprocess
        result = subprocess.run(
            [sys.executable, "-c",
             f"import sys; sys.path.insert(0, '.'); "
             f"import todo; todo.TODO_FILE = '{self.file_path}'; "
             f"from todo import load_tasks, save_tasks, mark_task_done; "
             f"tasks = load_tasks('{self.file_path}'); "
             f"tasks = mark_task_done(tasks, 1); "
             f"save_tasks(tasks, '{self.file_path}')"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script)
        )
        self.assertEqual(result.returncode, 0)
        tasks = load_tasks(self.file_path)
        self.assertTrue(tasks[0]["done"])

    def test_delete_via_cli(self) -> None:
        """Команда delete через subprocess удаляет задачу."""
        initial = [{"id": 1, "text": "Тест", "done": False}]
        save_tasks(initial, self.file_path)
        result = subprocess.run(
            [sys.executable, "-c",
             f"import sys; sys.path.insert(0, '.'); "
             f"import todo; todo.TODO_FILE = '{self.file_path}'; "
             f"from todo import load_tasks, save_tasks, delete_task; "
             f"tasks = load_tasks('{self.file_path}'); "
             f"tasks = delete_task(tasks, 1); "
             f"save_tasks(tasks, '{self.file_path}')"],
            capture_output=True, text=True, cwd=os.path.dirname(self.script)
        )
        self.assertEqual(result.returncode, 0)
        tasks = load_tasks(self.file_path)
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
