import time
from functools import wraps


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
                        msg = (f'{func.__name__} ok')
                               # f'Результат: {result}. Время выполнения: {time.perf_counter() - start_time} сек.')
                        print(msg, file=f)
                else:
                    # Вывод логов в консоль
                    print(f'{func.__name__} ok')
                        # f'Результат: {result}. Время выполнения: {time.perf_counter() - start_time} сек.')
            except Exception as e:
                if filename is not None:
                    # Запись логов об ошибках в файл
                    with open(filename, 'a') as f:
                        msg = (f'{func.__name__} '
                               f'error: {type(e).__name__}, Inputs: {args}, {kwargs}')
                        print(msg, file=f)
                else:
                    # Вывод логов об ошибках в консоль
                    print(
                        f'{func.__name__} '
                        f'error: {type(e).__name__}, Inputs: {args}, {kwargs}')
            finally:
                return result

        return wrapper

    return decorator
