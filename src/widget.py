from src.masks import get_mask_account, get_mask_card_number

def get_date(number_4: str) -> str:
    """формат даты"""
    if len(number_4) >= 10:
        return number_4[8:10] + '.' + number_4[5:7] + '.' + number_4[0:4]
    return f'некорректная дата'

def mask_account_card(number_3: str) -> str:
    """проверка карт по сущ функциям"""
    for i in number_3:
        if i in 'С':
            return 'Счет ' + get_mask_account(number_3)
        else:
            number_5 = number_3[-16:]
            df = len(number_3) - 16
            return number_3[:df] + get_mask_card_number(number_5)
