
def get_mask_card_number(number_1: str) -> str:
    """возращает маску карты"""
    return (
        number_1[0:4] + " " + number_1[4:6] + "**" + " " + "****" + " " + number_1[-4:]
    )


def get_mask_account(number_0: str) -> str:
    """возращает последние четыре цифры счета"""
    return "**" + number_0[-4:]
