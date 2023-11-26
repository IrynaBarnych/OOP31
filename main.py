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


#Варіант 2

class Person:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Ім'я має складатися лише з букв!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("Вік має бути в діапазоні від 0 до 120 років")
        self._age = value

    def information(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


person_info = Person("Віктор", 33)
print(person_info.information())



