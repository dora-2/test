import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')

def currency_api(to_api: str, from_api: str, amount_api: int) -> dict:
    """ конвертирует валюту """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_api}&from={from_api}&amount={amount_api}"

    payload = {}
    headers = {
        "apikey": os.getenv('apikey')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.text

    print(f'Result: {result}')


currency_api('RUB', 'EUR', 500)
