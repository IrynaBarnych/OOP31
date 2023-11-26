# Завдання 2
# Створіть клас температурного датчика, де обмежується
# температура в межах прийнятних для датчика значень, за
# допомогою property().

class TemperatureDevice:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if -50 <= value <= 150:
            self._temperature = value
        else:
            print('Неприпустима температура')


sensor = TemperatureDevice()

sensor.temperature = 25
print(sensor.temperature)

sensor.temperature = 260
print(sensor.temperature)

