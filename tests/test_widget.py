import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("number_4, result_number_4", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11T02", "11.03.2024"),
    (" ", "некорректная дата"),
])
def test_reverse_string(number_4, result_number_4):
    assert get_date(number_4) == result_number_4