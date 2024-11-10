import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='utils.log',  # Запись логов в файл
                    filemode='w')

auth_logger = logging.getLogger('load_financial_transactions')


def load_financial_transactions(file_path: str) -> list:
    auth_logger.info(f'файл: {file_path} попытались открыть')
    if not Path(file_path).exists():
        print(f"Файл {file_path} не найден")
        auth_logger.warning(f'Файл {file_path} не найден')
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            auth_logger.info('программа работает успешно')
            return data
        else:
            print(f"Данные в файле {file_path} имеют неверный формат")
            auth_logger.warning(f"Данные в файле {file_path} имеют неверный формат")
            return []
    except json.JSONDecodeError as e:
        print(f"Произошла ошибка при разборе JSON: {e}")
        auth_logger.error(f"Произошла ошибка при разборе JSON: {e}")
        return []

def cl(k=[], dictionary = {}):
    transactions = load_financial_transactions('operations.json')
    if transactions:
        for transaction in transactions:
            if len(transaction) > 1:

                # k.append(transaction)
                if transaction['description'] == 'Перевод организации' or transaction['description'] == 'Перевод со счета на счет' or transaction['description'] == 'Перевод с карты на карту' or transaction['description'] == 'Перевод с карты на счет':
                    # print(transaction['date'], transaction['state'], transaction["operationAmount"]["amount"],
                    #       transaction["operationAmount"]["currency"]["name"], transaction['description'],
                    #       transaction['from'], transaction['to'])

                    dictionary['date'] = transaction['date']
                    dictionary['state'] = transaction['state']
                    dictionary['amount'] = transaction["operationAmount"]["amount"]
                    dictionary['currency'] = transaction["operationAmount"]["currency"]["code"]
                    dictionary['description'] = transaction['description']
                    dictionary['from'] = transaction['from']
                    dictionary['to'] = transaction['to']

                    # for key, value in transaction.items():
                    #     s = f'{key}: {value}'
                    k.append(dictionary)

                else:
                    dictionary['date'] = transaction['date']
                    dictionary['state'] = transaction['state']
                    dictionary['amount'] = transaction["operationAmount"]["amount"]
                    dictionary['currency'] = transaction["operationAmount"]["currency"]["code"]
                    dictionary['description'] = transaction['description']
                    dictionary['to'] = transaction['to']
                    # print(transaction['date'], transaction['state'], transaction["operationAmount"]["amount"],
                    #       transaction["operationAmount"]["currency"]["name"], transaction['description'],
                    #                      transaction['to'])
        return k
    else:
        print("Список транзакций пуст")

print(cl())