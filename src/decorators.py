from functools import wraps
import time


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()

            try:
                result = func(*args, **kwargs)

                if filename is not None:
                    # Запись логов в файл
                    with open(filename, 'a') as f:
                        msg = f'{func.__name__}: Выполнена успешно. Результат: {result}. Время выполнения: {time.perf_counter() - start_time} сек.'
                        print(msg, file=f)
                else:
                    # Вывод логов в консоль
                    print(
                        f'{func.__name__}: Выполнена успешно. Результат: {result}. Время выполнения: {time.perf_counter() - start_time} сек.')
            except Exception as e:
                if filename is not None:
                    # Запись логов об ошибках в файл
                    with open(filename, 'a') as f:
                        msg = f'{func.__name__}: Возникла ошибка. Тип ошибки: {type(e).__name__}, Параметры: {args}, {kwargs}'
                        print(msg, file=f)
                else:
                    # Вывод логов об ошибках в консоль
                    print(
                        f'{func.__name__}: Возникла ошибка. Тип ошибки: {type(e).__name__}, Параметры: {args}, {kwargs}')
            finally:
                return result

        return wrapper

    return decorator