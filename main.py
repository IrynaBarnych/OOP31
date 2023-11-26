# Завдання 1
# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def get_balance(self):
        print('get_balance')
        return self.__balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс має бути числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            print(f'Знімання {amount} грн.')
            self.__balance -= amount
        else:
            print('Недостатньо коштів для зняття')

    def deposit(self, amount):
        if amount > 0:
            print(f'Зарахування {amount} грн.')
            self.__balance += amount
        else:
            print('Некоректна сума для зарахування')

# Приклад використання:
account = BankAccount("John Doe", 1000)
print(account.my_balance)  # Виведе "get_balance" та поточний баланс

account.withdraw(500)      # Виведе "Знімання 500 грн." і зменшить баланс
print(account.my_balance)  # Виведе "get_balance" та новий баланс

account.deposit(200)       # Виведе "Зарахування 200 грн." і збільшить баланс
print(account.my_balance)  # Виведе "get_balance" та новий баланс



