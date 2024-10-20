import pytest
import time
from src.decorators import log
from src.masks import get_mask_account


@log(filename="mylog.txt")
def get_mask_account():
    return f'Выполнена успешно. Результат: **4567. Время выполнения:{time.perf_counter() - start_time} сек.'


def test_get():
    @log()
    def get_long_text():
        return "339394567"

    assert get_long_text() == "**4567"