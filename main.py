#Завдання 4
#Створіть клас для представлення користувача з
#атрибутами: ім'я та вік. Додайте властивості для
#валідації віку користувача. Наприклад, вік повинен
#бути у межах від 0 до 120.

class Person:
    def __init__(self, name, age):
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





