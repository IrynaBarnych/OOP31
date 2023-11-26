#Завдання 5
#Створіть клас Multiplier, який при ініціалізації
#отримує множник. Забезпечте можливість викликати
#цей об'єкт з аргументом та повертати множене значення.

class Multiplier:
    def __init__(self, ):
        self.name = name
        self.age = age

    def information(self):
        if not self.name.isalpha():
            raise ValueError("Ім'я має складатися лише з букв!")
        if not (0 <= self.age <= 120):
            raise ValueError("Вік має бути в діапазоні від 0 до 120 років")
        return f"Ім'я: {self.name}, Вік: {self.age}"


person_info = Person("Тарас", 33)
print(person_info.information())



