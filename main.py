# Завдання 1
# Створіть клас Calculator, який може виконувати
# операції додавання, віднімання, множення та ділення.
# Кожна операція буде реалізована як метод класу.
# Об'єкт класу Calculator буде функтором, що може
# викликатися для виконання обраної операції.

class Calculator:
    def dodavannya(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Додавати нуль не рекомендовано")
        return a + b
    def vidnimannya(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Віднімати нуль не рекомендовано")
        return a - b

    def mnojennya(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Множети на нуль не можна")
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Ділити на нуль не можна")
        return a / b

    def __call__(self, *args, **kwargs):
        match args[0]:
            case "+": return self.dodavannya(args[1], args[2])
            case "-": return self.vidnimannya(args[1], args[2])
            case "*": return self.mnojennya(args[1], args[2])
            case "/": return self.divide(args[1], args[2])
            case _  : return "такої  операції немає"

calcutate = Calculator()
print(calcutate("+", 4, 2))
print(calcutate("-", 4, 2))
print(calcutate("*", 4, 2))
print(calcutate("/", 4, 2))
