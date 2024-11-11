from src.csv_pandas import excel_read, scl
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.re_collections_random import filter_operations
from src.utils import cl
from src.widget import get_date, mask_account_card


def main(s=0):
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')

    x = int(input('Выберите необходимый пункт меню: '))
    while s == 0:
        if x == 1:
            print('Для обработки выбран JSON-файл.')
            transactions_data = cl()
            s += 1
        elif x == 2:
            print('Для обработки выбран CSV-файл.')
            transactions_data = scl()
            s += 1
        elif x == 3:
            print('Для обработки выбран XLSX-файл.')
            transactions_data = excel_read('transactions_excel.xlsx')
            s += 1
        else:
            print('некорректный выбор. попробуйте еще раз')

    s = 0
    while s == 0:
        print('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        d = input('Введите статус, по которому необходимо выполнить фильтрацию: ')
        if d.upper() not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции "{d}" недоступен.')
        elif d.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу {d}')
            transactions_data = filter_by_state(transactions_data, d)
            s += 1

    print('Отсортировать операции по дате? Да/Нет')
    q = input()
    if q.lower() == 'да':
        print('Отсортировать по возрастанию или по убыванию? ')
        w = input()
        if w == 'по возрастанию':
            transactions_data = sort_by_date(transactions_data, False)
        else:
            transactions_data = sort_by_date(transactions_data)
    print('Выводить только рублевые транзакции? Да/Нет')
    e = input()
    if e.lower() == 'да':
        transactions_data = list(filter_by_currency(transactions_data))
    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    r = input()
    if r.lower() == 'да':
        search_string = input("Введите слово для фильтрации: ")
        transactions_data = filter_operations(transactions_data, search_string)
    print('Распечатываю итоговый список транзакций...')

    if len(transactions_data) == 0:
        return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'

    print(f'Всего банковских операций в выборке: {len(transactions_data)}')

    for i in transactions_data:
        print(' ')
        print(f'{get_date(i['date']), i['description']}')
        if type(i['from']) is float:
            print(mask_account_card(i['to']))
        else:
            print(mask_account_card(i['from']), '->', mask_account_card(i['to']))
        print(f'Сумма: {i['amount']} {i['currency_code']} ')
    # return transactions_data


print(main())
