from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs) :
          # captured = capsys.readouterr()
          print(f'Function {func} started')
          result = func(*args, **kwargs)
          print(f'Function {func} finished')
          return result
    return wrapper