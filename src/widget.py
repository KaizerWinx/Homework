import src.decorators as decorators
from src.masks import get_mask_account, get_mask_card_number


@decorators.log(filename="log.txt")
def mask_account_card(input: str) -> str:
    """
    :param input: строка с типом данных и номером карты или счета (например Visa Platinum 7000792289606361)
    Функция принимает на вход строку, содержащую тип данных (название карты или счет) и номер карты или счета
    и возвращает замаскированный номер с типом данных
        # Пример для карты
        Visa Platinum 7000792289606361 # входной аргумент
        Visa Platinum 7000 79** **** 6361 # выход функции
        # Пример для счета
        Счет 73654108430135874305 # входной аргумент
        Счет **4305 # выход функции
    """
    if "Счет" in input:
        return f"{input[0:len(input) - 20]}{get_mask_account(input[-20:])}"
    else:
        return f"{input[0:len(input) - 16]}{get_mask_card_number(input[-16:])}"


@decorators.log(filename="log.txt")
def get_date(input_date: str) -> str:
    """
    функция принимаемает на вход строку даты в формате "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    splited_date = input_date.split("-")
    splited_date.reverse()
    splited_date[0] = splited_date[0][0:2]
    formated_date = ".".join(splited_date)
    return formated_date
