import json


# with open('operations.json') as f:
#     data = json.load(f)
from pathlib import Path


def load_financial_transactions(file_path: str) -> list:

    if not Path(file_path).exists():
        print(f"Файл {file_path} не найден")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        else:
            print(f"Данные в файле {file_path} имеют неверный формат")
            return []
    except json.JSONDecodeError as e:
        print(f"Произошла ошибка при разборе JSON: {e}")
        return []


transactions = load_financial_transactions('operations.json')
if transactions:
    for transaction in transactions:
        if len(transaction) > 1:
            print(transaction['date'], transaction["operationAmount"]["amount"], transaction['description'])
else:
    print("Список транзакций пуст")
