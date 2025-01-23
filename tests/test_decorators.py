import pytest

import src.decorators as decorators


# тест ошибки выполнения функции и записи лога в файл
def test_log_decorator_file_function_error() -> None:
    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    with pytest.raises(Exception):
        func(1, 1)


# тест успешного выполнения функции и записи лога в файл
def test_log_decorator_file() -> None:
    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    result = func(2, 1)
    assert result == 1


# тест ошибки выполнения функции и вывода лога в консоль
def test_log_decorator_console_func_error() -> None:
    @decorators.log()
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    with pytest.raises(Exception):
        func(1, 1)


# тест успешного выполнения функции и вывода лога в консоль
def test_log_decorator_console() -> None:
    @decorators.log()
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    result = func(2, 1)
    assert result == 1
