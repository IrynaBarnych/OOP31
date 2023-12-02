#Завдання 3
#Створіть клас для представлення відомостей про
#замовлення. Забезпечте, щоб номер замовлення був
#тільки для читання за допомогою керованих атрибутів,
#але його можна було переглядати.

class Order:
    def __init__(self, order_number, customer_name, total_amount):
        self._order_number = order_number
        self._customer_name = customer_name
        self._total_amount = total_amount

    @property
    def order_number(self):
        return self._order_number

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value < 0:
            raise ValueError("Total amount cannot be negative")
        self._total_amount = value


order_instance = Order(12345, "John Doe", 100.0)


print(order_instance.order_number)
print(order_instance.customer_name)
print(order_instance.total_amount)

order_instance.total_amount = 150.0
print(order_instance.total_amount)




