from collections.abc import Callable


def log(filename: str = "") -> object:
    """
    :rtype: object
    :param filename: имя файла с логами
    Декоратор, записывающий результаты работы функции в файл или в консоль.
    """

    def decorator(func: Callable) -> object:
        def wrapper(*args: str, **kwargs: int) -> object:
            try:
                # попытка выполнения декорируемой функции
                result = func(*args, **kwargs)
            except Exception as err:
                # обработка исключения при выполнении декорируемой функции
                try:
                    # попытка открытия файла для записи лога
                    file = open(filename, "a")
                except FileNotFoundError:
                    # обработка исключения при ошибке открытия файла
                    # вывод ошибки выполнения декорируемой функции в консоль
                    print(f"{func.__name__} error: {err}, inputs: {args}, {kwargs}\n")
                else:
                    # вывод лога ошибки выполнения декорируемой функции в файл
                    file.write(
                        f"{func.__name__} error: {err}, inputs: {args}, {kwargs}\n"
                    )  # вывод лога в файл при ошибке
                    file.close()
                # исключение выбрасываемое при ошибке выполнения декорируемой функции
                raise Exception(f"Function error: {err}")
            else:
                # код, выполняемый при успешном выполнении декорируемой функции
                try:
                    # попытка открытия файла для вывода лога
                    file = open(filename, "a")
                except FileNotFoundError:
                    # обработка исключения при ошибке открытия файла
                    # вывод лога в консоль при ошибке открытия файла
                    print(f"{func.__name__} ok\n")
                else:
                    # вывод лога в файл при успешном открытии
                    file.write(f"{func.__name__} ok\n")
                    file.close()
                return result

                return wrapper
            return decorator
