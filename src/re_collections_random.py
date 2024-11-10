from src.csv_pandas import excel_read
from collections import Counter


def filter_operations(tra: list, search_string: str, s=[]) -> list:
    """возращает список словарей, у которых в описании есть данная строка"""
    for i in tra:
        if i['description'] == search_string:
            s.append(i)
    return s


d = excel_read('transactions_excel.xlsx')
print(filter_operations(d, 'Перевод с карты на карту'))


def filter_operations_2(tra: list, operation: list) -> dict:
    """возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    counter = Counter()

    for i in tra:
        if 'description' in i and i['description'] in operation:
            counter.update([i['description']])

    return dict(counter)


# d = excel_read('transactions_excel.xlsx')
print(filter_operations_2(d, ['Перевод с карты на карту', 'Открытие вклада', 'Перевод со счета на счет']))
