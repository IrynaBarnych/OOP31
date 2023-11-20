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

#property()

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        print("get_radius")
        return self._radius

    def set_radius(self, value):
        print("set_radius")
        if value < 0:
            raise ValueError("Значення радіуса не може бути меньше нуля")
        self._radius = value

    def delete_radius(self):
        print("delete_radius")
        del self._radius
    radius = property(fget=get_radius, fset=set_radius, fdel=delete_radius)

circle = Circle(10)
#print(circle.get_radius())
#circle.set_radius(100)
#print(circle.get_radius())
print(circle.radius) #fget=get_radius
circle.radius = 100
print(circle.radius)
del circle.radius
#print(circle.radius)