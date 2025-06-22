# [GREEN] Завдання:
'''
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
'''

# [BLUE] Рішення завдання:
class FigureRhombus:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("довжина сторони 'a' повинна бути більше 0")
        elif name == 'angle_a':
            if not 0 < value < 180:
                raise ValueError("кут повинен бути між 0 та 180 градусів")

        super().__setattr__(name, value)


rhombus = FigureRhombus(side_a = 5, angle_a = 60)
print(f"{'-' * 10}Позитивний тест{'-' * 90}")
print(f"Сторона 'a': {rhombus.side_a}\n"
      f"Кут 'a': {rhombus.angle_a}\n"
      f"Кут 'b': {rhombus.angle_b}\n"
      f"Сума кутів 'a' та 'b': {rhombus.angle_a + rhombus.angle_b}\n")

print(f"{'-' * 10}Негативний тест{'-' * 90}")
side_a = -6
angle_a = 190
try:
    incorrect_rhombus = FigureRhombus(side_a, angle_a)
except ValueError as error:
    print(f"Помилка при значеннях атрибутів {side_a} та {angle_a}:\n"
          f"    - {error}")



