import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("number_4, result_number_4", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11T02", "11.03.2024"),
    (" ", "некорректная дата"),
])
def test_reverse_string(number_4, result_number_4):
    assert get_date(number_4) == result_number_4


@pytest.mark.parametrize("number_3, result_number_3", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", "некорректный номер счета"),
])
def test_reverse_string_2(number_3, result_number_3):
    assert mask_account_card(number_3) == result_number_3
