# Проект "SkyPro - банковское приложение"
## Описание:
Проект "SkyPro - банковское приложение" - это учебная практика по курсу Python, включающая
в себя создание банковского приложения и отработку навыков. Проект постоянно дорабатывается,
улучшается и пополняется новыми функциями.
## Цель проекта:
 - научиться программированию на языке Python
 - научиться основным навыкам работы с основными приложениями и инструментами 
 - отработать практически теоретические навыки 
## Установка:
1. Клонируйте репозиторий с "Github":
```
git@github.com:KaizerWinx/Homework.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Для проверки работы программы, перейдите в файл и запустите его через командную 
строку или кнопку в вашем IDE 
```
MyProject1/src/main.py
```
## Тестирование
Для запуска тестов всех функция введите в терминал "pytest". Чтобы проверить, какой процент кода программы был протестирован, введите в терминал "pytest --cov"
## Описание функций проекта
### 1) Функция get_mask_card_number() 
Функция get_mask_card_number() принимает номер карты и возвращает ее маскированный вариант
```
Maestro 1596837868705199 - то что функция принимает
                         
Maestro 1596 83** **** 5199 - то что функция возвращает
```
### 2) Функция get_mask_account() 
Функция get_mask_account() принимает номер счёта и возвращает его маскированный вариант
```
Счет 64686473678894779589 - то что функция принимает
                         
Счет **9589 - то что функция возвращает
```
### 3) Функция filter_by_state() 
Функция filter_by_state() принимает список словарей и опционально значение для ключа 
state(по умолчанию 'EXECUTED'). Затем возвращает новый список словарей, содержащий только те словари,
у которых ключ state соответствует указанному значению.
```
Пример входных данных для проверки функции:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
Выход функции со статусом по умолчанию 'EXECUTED':                       
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
Выход функции, если вторым аргументов передано 'CANCELED':
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
### 4) Функция sort_by_date() 
Функция sort_by_date() принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый список, 
отсортированный по дате (date).
```
Пример входных данных для проверки функции:
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции):
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
### 5) Функция mask_account_card() 
Функция mask_account_card() принимает один аргумент — строку, содержащую тип и номер карты или счёта.
И возвращает строку с замаскированным номером. Для карты и счёта используются разные типы маскировки. 
```
Пример для карты:
Visa Platinum 7000792289606361 - входной аргумент
Visa Platinum 7000 79** **** 6361 - выход функции
Пример для счета:
Счет 73654108430135874305 - входной аргумент
Счет **4305 - выход функции
```
### 6) Функция get_date() 
Функция get_date() принимает на вход строку с датой в формате"2024-03-11T02:26:18.671407" и возвращает строку с датой в формате"ДД.ММ.ГГГГ" ("11.03.2024"). 
```
Пример для карты:
2024-03-11T02:26:18.671407 - входной аргумент
11.03.2024 - выход функции
```

### 7) Функция filter_by_currency()
Функция filter_by_currency() принимает на вход список словарей, представляющих транзакции. А затем возвращает итератор, который поочередно выводит транзакции, где валюта операции соответствует заданной (например, USD).
```
Пример выхода функции:
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
```

### 8) Функция transaction_descriptions()
Функция transaction_descriptions() принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```
Пример выхода функции:
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```

### 9) Функция card_number_generator()
Функция card_number_generator() выводит номера банковских карт в формате 
XXXX XXXX XXXX XXXX , где X — цифра номера карты. Функция может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Функция принимает начальное и конечное значения для генерации диапазона номеров.