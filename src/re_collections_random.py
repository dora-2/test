from src.csv_pandas import excel_read


def filter_operations(tra: list, search_string: str, s=[]) -> list:
    """возращает список словарей, у которых в описании есть данная строка"""
    for i in tra:
        if i['description'] == search_string:
            s.append(i)
    return s


d = excel_read('transactions_excel.xlsx')
print(filter_operations(d, 'Перевод с карты на карту'))


def filter_operations_2(tra: list, operation: list, a=0, w={}) -> dict:
    """возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    for i in operation:
        for j in tra:
            if j['description'] == i:
                a += 1
        w[i] = a
        a = 0
    return w


# d = excel_read('transactions_excel.xlsx')
print(filter_operations_2(d, ['Перевод с карты на карту', 'Открытие вклада', 'Перевод со счета на счет'])) #587
