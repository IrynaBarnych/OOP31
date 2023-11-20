#функтори
#метод __call__
class MyFunctor():
    def __init__(self):
        self.counter = 0
        self.suma = 0
        print("Я ініціалізувався")

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.suma = sum(args)
        print("Сума аргументів", self.suma)
        print(f"Екземпляр класу викликався {self.counter} разів")
obj = MyFunctor()
obj(1, 4, 6, 8, 6)
obj()
obj()