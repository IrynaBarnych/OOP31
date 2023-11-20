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

    @property
    def radius(self):
        print("get_radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("set_radius")
        if value < 0:
            raise ValueError("Значення радіусу не може бути меньше 0")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("delete_radius")
        del self._radius

    #radius = property(get_radius, set_radius, delete_radius)
    #radius = radius.getter(get_radius)

circle = Circle(10)
#print(circle.get_radius())
#circle.set_radius(100)
#print(circle.get_radius())
print(circle.radius) #fget=get_radius
radius = 100
print(circle.radius)
del circle.radius
#print(circle.radius)
class MyClass:
    _x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        else:
            self._x = value

obj = MyClass()
obj.x = 10  # Виведе: 10
print(obj.x)
obj.x = -5  # Виведе: 0
print(obj.x)