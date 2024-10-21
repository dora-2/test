from decorators import log


@log()
def get_mask_card_number(number_1: str, k=0) -> str:
    """возращает маску карты"""
    if len(number_1) == 16:
        for i in number_1:
            if i not in '1234567890':
                k += 1
        if k == 0:
            return (
                number_1[0:4] + " " + number_1[4:6] + "**" + " " + "****" + " " + number_1[-4:]
            )
    return f'{'неверный номер карты'}'


@log(filename='mylog.txt')
def get_mask_account(number_0: str, k=0) -> str:
    """возращает последние четыре цифры счета"""
    if len(number_0) > 4:
        for i in number_0:
            if i not in '1234567890':
                k += 1
        if k == 0:
            return "**" + number_0[-4:]
    return f'{'неверный номер счета'}'


if __name__ == '__main__':
    assert (get_mask_card_number('1234567891234567'))
    assert (get_mask_account('46'))