# Завдання 3
# Завдання для функторів. Створіть клас TextModifier,
# який може здійснювати різні операції над текстом:
# • Операція перетворення тексту у верхній регістр.
# • Операція перетворення тексту у нижній регістр.
# • Операція видалення пробілів у тексті.
# • Операція шифрування тексту за допомогою зсуву
# вліво на задану кількість символів.


class TextModifier:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        self.text = self.text.upper()

    def get_result(self):
        return self.text

