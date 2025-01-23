import src.decorators as decorators


@decorators.log(filename="log.txt")
def filter_by_state(list_of_dict: list = [], state: str = "EXECUTED") -> list:
    """
    Функция филтрует список банковских операций по параметру state
    :param list_of_dict: входной список словарей;
    :param state: параметр, по которому фильтруется список;
    :return: Возвращается отфильтрованный по параметру state список словарей;
    """
    filtered_list_of_dict = []  # отфильтрованный список
    for dictionary in list_of_dict:  # фильтрация списка по параметру state
        if dictionary["state"] == state:
            filtered_list_of_dict.append(dictionary)
    return filtered_list_of_dict


@decorators.log(filename="log.txt")
def sort_by_date(list_of_dict: list, _reverse: bool = True) -> list:
    """
    Функция сортирует банковские операции по дате
    :param list_of_dict: входной список словарей;
    :param _reverse: параметр сортировки True - по убыванию, False - по возрастанию;
    :return: возвращается отсортированный список;
    """
    return sorted(list_of_dict, key=lambda _dict: _dict["date"], reverse=_reverse)
