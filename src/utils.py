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
        auth_logger.warning(f"Произошла ошибка при разборе JSON: {e}")
        return []


transactions = load_financial_transactions('operations.json')
if transactions:
    for transaction in transactions:
        if len(transaction) > 1:
            print(transaction['date'], transaction["operationAmount"]["amount"], transaction['description'])
else:
    print("Список транзакций пуст")
