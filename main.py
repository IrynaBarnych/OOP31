#Завдання 5
#Створіть клас Multiplier, який при ініціалізації
#отримує множник. Забезпечте можливість викликати
#цей об'єкт з аргументом та повертати множене значення.

class Multiplier:
    def __init__(self, coefficient):
        self.coefficient = coefficient

    def multiply(self, number):
        return number * self.coefficient


multiplier_obj = Multiplier(5)
result = multiplier_obj.multiply(10)
print(result)



