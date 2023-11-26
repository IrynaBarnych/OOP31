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

    def to_upper(self):
        self.text = self.text.upper()

    def to_lower(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = self.text.replace(" ", "")

    def encrypt_shift_left(self, shift):
        result = ""
        for char in self.text:
            if char.isalpha():  # шифрувати тільки літери
                encrypted_char = chr((ord(char) - shift) % 3 + ord('a'))
                result += encrypted_char
            else:
                result += char
        self.text = result

    def get_result(self):
        return self.text


# Створення об'єкта класу TextModifier
text_modifier = TextModifier("H e l l o, W o r l d!")

# Верхній регістр.
text_modifier.to_upper()
result_text = text_modifier.get_result()
print("Результат у верхньому регістрі:", result_text)

# Нижній регістр.
text_modifier.to_lower()
result_text = text_modifier.get_result()
print("Результат у нижньому регістрі:", result_text)

# видалення пробілів.
text_modifier.remove_spaces()
result_text = text_modifier.get_result()
print("Результат після видалення пробілів:", result_text)

# Операція шифрування тексту за допомогою зсуву вліво на 3 символи.
text_modifier.encrypt_shift_left(3)
result_text = text_modifier.get_result()
print("Результат шифрування:", result_text)


