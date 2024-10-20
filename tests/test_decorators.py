import pytest
from src.decorators import log

@pytest.fixture
def capsys():
    return log().patch('builtins.print').start()

def test_decorator_with_successful_function(capsys):
    # Проверка выполнения функции без ошибок
    # @timer
    def add(a, b):
        return a + b

    assert add(1, 2) == 3
    captured = capsys.readouterror()
    expected_output = 'Функция add выполнена за 0.0000 секунд\n'
    assert captured == expected_output

def test_decorator_with_exceptions(capsys):
    # Проверка обработки исключений
    # @timer
    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        else:
            return a / b

    with pytest.raises(ValueError):
        divide(1, 0)
    captured = capsys.readouterror()
    expected_output = 'Функция divide выполнена за 0.0000 секунд\n'
    assert captured == expected_output

def test_decorator_with_invalid_arguments(capsys):
    # Проверка работы с неправильными аргументами
    # @timer
    def subtract(a, b):
        return a - b

    with pytest.raises(TypeError):
        subtract(1, 'a')
    captured = capsys.readouterror()
    expected_output = 'Функция subtract выполнена за 0.0000 секунд\n'
    assert captured == expected_output

def test_decorator_multiple_calls(capsys):
    # Проверка нескольких вызовов одной функции
    # @timer
    def multiply(a, b):
        return a * b

    for _ in range(5):
        multiply(2, 3)
    captured = capsys.readouterror()
    expected_output = f'Функция multiply выполнена за {5*0.0000:.4f} секунд\n'
    assert captured == expected_output


