from unittest.mock import Mock
from src.utils import load_financial_transactions


def test_load_financial_transactions():
    mock_random = Mock(return_value='Список транзакций пуст')
    # random.randint = mock_random
    assert test_load_financial_transactions() == mock_random
    # mock_random.assert_called_once_with(0, 10)