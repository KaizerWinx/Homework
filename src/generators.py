from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """
    :param transactions: список транзакций
    :param currency: валюта
    Функция получает на вход список транзакций и возвращает отфильтрованные значения ввиде генератора
    """
    result = list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions))
    yield result


def transaction_descriptions(transactions: list) -> Generator:
    """
    :param transactions: список транзакций
    Функция получает на вход список транзакций и возвращает описание каждой транзакции ввиде генератора
    """
    result = map(lambda description: description["description"], transactions)
    for i in result:
        yield i


def card_number_generator(start: int, end: int) -> Generator:
    """
    :param start: начальное значение
    :param end: конечное значение (на 1 больше фактического)
    Функция принимает на вход начальное и конечное значение диапазона и генерирует номера карт в этом диапазоне.
    На выход подается генератор.
    """
    card_number = ""
    for i in range(start, end):
        card_number = "0" * (16 - len(str(i))) + str(i)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:17]}"