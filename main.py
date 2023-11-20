#функтори
#метод __call__

import time
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        print(f"Викликаємо функцію {self.func.__name__}")
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"Функція виконувалася {end - start:.5f}" )
        return result

@Timer
def summa():
    return sum(range(1, 100000))

print(summa())