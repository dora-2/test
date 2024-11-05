import logging
from decorators import log

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='masks.log',  # Запись логов в файл
                    filemode='w')

auth_logger = logging.getLogger('get_mask_card_number')
dl_logger = logging.getLogger('get_mask_account')


@log()
def get_mask_card_number(number_1: str, k=0) -> str:
    """возращает маску карты"""
    auth_logger.info(f'ввели номер карты: {number_1}')
    if len(number_1) == 16:
        for i in number_1:
            if i not in '1234567890':
                k += 1
        if k == 0:
            auth_logger.info('программа работает успешно')
            return (
                number_1[0:4] + " " + number_1[4:6] + "**" + " " + "****" + " " + number_1[-4:]
            )
    auth_logger.warning('неверный номер карты')
    return f'{'неверный номер карты'}'


@log(filename='mylog.txt')
def get_mask_account(number_0: str, k=0) -> str:
    dl_logger.info(f'ввели номер карты: {number_0}')
    """возращает последние четыре цифры счета"""
    if len(number_0) > 4:
        for i in number_0:
            if i not in '1234567890':
                k += 1
        if k == 0:
            dl_logger.info('программа работает успешно')
            return "**" + number_0[-4:]
    dl_logger.error('неверный формат счета')
    return f'{'неверный формат счета'}'


if __name__ == '__main__':
    assert (get_mask_card_number('1234567891234567'))
    assert (get_mask_account('46'))
