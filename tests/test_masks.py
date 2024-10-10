from src.masks import get_mask_account, get_mask_card_number


def test_up_first():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('7000792289') == 'неверный номер карты'
    assert get_mask_card_number('') == 'неверный номер карты'
    assert get_mask_card_number('fsdghdfghjkloip;') == 'неверный номер карты'


def test_up_first_2():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73654108445857895892400230135874305') == '**4305'
    assert get_mask_account('74305') == '**4305'
    assert get_mask_account('gnb') == 'неверный номер счета'
    assert get_mask_account('736541084301mjnh') == 'неверный номер счета'
