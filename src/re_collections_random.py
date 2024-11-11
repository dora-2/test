from src.csv_pandas import excel_read
from collections import Counter
import re

def filter_operations(tra: list, search_string: str) -> list:
    """возращает список словарей, у которых в описании есть данная строка"""
    s = []
    for i in tra:
        # print(i['description'])
        if re.findall(str(search_string), str(i['description'])):
            s.append(i)
    return s


# d = excel_read('transactions_excel.xlsx')
# print(filter_operations(d, ['Открытие вклада']))

# print(filter_operations(d, 'Перевод с карты на карту'))


def filter_operations_2(tra: list, operation: list) -> dict:
    """возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    counter = Counter()

    for i in tra:
        if 'description' in i and i['description'] in operation:
            counter.update([i['description']])

    return dict(counter)


d = excel_read('transactions_excel.xlsx')
