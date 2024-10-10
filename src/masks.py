
def get_mask_card_number(number_1: str) -> str:
    """возращает маску карты"""
    if len(number_1) == 16:
        return (
            number_1[0:4] + " " + number_1[4:6] + "**" + " " + "****" + " " + number_1[-4:]
        )
    return f'неверный номер карты'


def get_mask_account(number_0: str) -> str:
    """возращает последние четыре цифры счета"""
    if len(number_0) > 4:
        return "**" + number_0[-4:]
    return f'неверный номер счета'