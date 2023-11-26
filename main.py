# Завдання 1
# Іноді ви можете використати property() для створення
# доступу до атрибутів через геттери та сеттери для
# забезпечення певних перевірок або операцій перед
# отриманням або зміною атрибутів. Створіть клас для
# роботи з банківським рахунком, щоб гроші знялися або
# зарахувалися тільки при виконанні певних умов
# (наприклад, якщо гроші на рахунку є).

class BankAccount:
    def __int__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get_balance')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        is not isinstance(value, (int, float)):
            raise ValueError('Баланс має бути числом')
        self.__balance == value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)
    balance = property(fget_balance,
                       fset=set_balance,
                       sdel=delete_balance)

