def filter_by_currency(transactions, currency='USD'):
    def _is_matching_currency(transaction):
        operation_amount = transaction["operationAmount"]
        currency_details = operation_amount["currency"]
        return currency_details["name"].lower() == currency.lower()

    filtered = (transaction for transaction in transactions if _is_matching_currency(transaction))
    return filtered

# usd_transactions = filter_by_currency(transactions, 'USD')
# # for i in range(2):
# print(next(usd_transactions))


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield f"{transaction['description']}"


# descriptions = transaction_descriptions(transactions)
# # for _ in range(5):
# print(next(descriptions))


def card_number_generator(start=1, end=9999999999999999):
    for num in range(start, end + 1):
        s = f'{num:016d}'
        yield f'{s[:4]} {s[4:8]} {s[8:12]} {s[12:]}'


# for card_number in card_number_generator(1, 5):
#     print(card_number)
