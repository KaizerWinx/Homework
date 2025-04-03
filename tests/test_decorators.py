import pytest
import src.decorators as decorators


# тест ошибки выполнения функции и записи лога в файл
def test_log_decorator_file_function_error() -> None:
    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    with pytest.raises(Exception):
        func(1, 1)
    file = open("log.txt", "r")
    line = file.readlines()
    file.close()
    assert line[-1] == f"func error: division by zero, inputs: (1, 1), {"{}"}\n"


# тест успешного выполнения функции и записи лога в файл
def test_log_decorator_filec() -> None:
    @decorators.log(filename="log.txt")
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    func(2, 1)
    file = open("log.txt", "r")
    line = file.readlines()
    file.close()
    assert line[-1] == "func ok\n"

    # тест ошибки выполнения функции и вывода лога в консоль
    def test_log_decorator_console_func_error(capsys) -> None:
        @decorators.log()
        def func(a: int, b: int) -> float:
            return 1 / (a - b)

        with pytest.raises(Exception):
            func(1, 1)
        captured = capsys.readouterr()
        assert captured.out == f"func error: division by zero, inputs: (1, 1), {"{}"}\n\n"


# тест успешного выполнения функции и вывода лога в консоль
def test_log_decorator_console(capsys) -> None:
    @decorators.log()
    def func(a: int, b: int) -> float:
        return 1 / (a - b)

    func(2, 1)
    captured = capsys.readouterr()
    assert captured.out == "func ok\n\n"
