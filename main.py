#Завдання 3
#Створіть клас для представлення відомостей про
#замовлення. Забезпечте, щоб номер замовлення був
#тільки для читання за допомогою керованих атрибутів,
#але його можна було переглядати.

class Order:
    def __init__(self, order_number, customer_name, total_amount):
        self._order_number = order_number
        self.customer_name = customer_name
        self.total_amount = total_amount

    @property
    def order_number(self):
        return self._order_number

order_instance = Order(12345, "John Doe", 100.0)
print(order_instance.order_number)




