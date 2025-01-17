# Обработка информации банка, карт, счетов

## Описание
Разработка данного проекта проходит в рамках курса "Профессия Python-разработчик" от Skypro.

Данный проект обрабатывает информацию, полученную от клиента банка. 
Алгоритм обрабатывает информацию и засекречивает полученную информацию о картах и счетах.

## Цели проекта:
- Научиться программировать на Python
- Изучить основные инструменты Python-разработчика
- Освоить профессию разработчика на Python
# Установка и запуск проекта
## Для установки и запуска проекта у вас должны быть установлены IDE, Python 3 и GitHub

- Клонируйте репозиторий 
- Запустите проект в своей IDE
- В корне проекта вам нужно найти модуль main.py
- Запустите файл main.py в вашей IDE
На данном этапе разработки не предусмотрен ввод команд. 
Все функции имеют заданные значения и запускаются автоматически.

# Описание функций
## Функция get_mask_card_number()
Функция принимает на вход номер карты и возвращает ее маску. 
Номер карты замаскирован и отображается в формате ```XXXX XX** **** XXXX``` где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.

### Пример работы функции:
    7000792289606361 - входной аргумент
    7000 79** **** 6361 - выход функции
## Функция get_mask_account()
Функция принимает на вход номер счета и возвращает его маску.
Номер счета замаскирован и отображается в формате ```**XXXX``` где X — это цифра номера.
То есть видны только последние 4 цифры номера, а перед ними — две звездочки.

### Пример работы функции:
    73654108430135874305 - входной аргумент
    **4305 - выход функции
## Функция mask_account_card()
Функция принимает на вход строку, содержащую тип данных (номер, название карты или номерБ название счета).
Возвращает замаскированный номер с названием карты или названием счета

### Пример для карты
    Visa Platinum 7000792289606361 - входной аргумент
    Visa Platinum 7000 79** **** 6361 - выход функции

### Пример для счета
    Счет 73654108430135874305 - входной аргумент
    Счет **4305 - выход функции
## Функция get_date()
Функция принимает на вход строку с датой в формате
```"2024-03-11T02:26:18.671407"```
и возвращает строку с датой в формате
```"ДД.ММ.ГГГГ" ("11.03.2024").```
## Функция filter_by_state()
Функция принимает список словарей и опционально значение для ключа ```state``` (по умолчанию ```'EXECUTED'```).
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ ```state``` соответствует указанному значению.

### Пример работы функции:
    Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    Выход функции со статусом по умолчанию 'EXECUTED'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    
    Выход функции, если вторым аргументов передано 'CANCELED'
    [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

## Функция sort_by_date
Функция принимает список словарей и сортирует списки по значению ```bool``` для ключа ```date``` (по умолчанию ```True```).
При значении ```True``` сортируется список и производится по убыванию.
### Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    
    Выход функции со статусом по умолчанию 'True'
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

При значении ```False``` сортировка списка производится по убыванию.
### Входные данные
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    Выход функции со статусом по умолчанию 'False'
    [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

## Тестирование
Для запуска тестов всех функция введите в терминал "pytest". Чтобы проверить, 
какой процент кода программы был протестирован, введите в терминал "pytest --cov"
