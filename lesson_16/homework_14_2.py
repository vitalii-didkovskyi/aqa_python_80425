# [GREEN] Завдання-2:
# '''
# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
# '''

# [BLUE] Рішення завдання-2:
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self._side = side
    def area(self):
        return self._side ** 2
    def perimeter(self):
        return self._side * 4

class Rectangle(Figure):
    def __init__(self, name, side_a, side_b):
        super().__init__(name)
        self._side_a = side_a
        self._side_b = side_b
    def area(self):
        return self._side_a * self._side_b
    def perimeter(self):
        return 2 * (self._side_a + self._side_b)

class Triangle(Figure):
    def __init__(self, name, side_a, side_b, side_c):
        super().__init__(name)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
    def area(self):
        return math.sqrt(self.perimeter() * (self.perimeter() - self._side_a) *
                         (self.perimeter() - self._side_b) * (self.perimeter() - self._side_c))
    def perimeter(self):
        return self._side_a + self._side_b + self._side_c

def test_figure_area_and_perimeter():
    square = Square("Square", 5)
    rectangle = Rectangle("Rectangle", 4, 6)
    triangle = Triangle("Triangle", 3, 4, 5)

    for test_figure_area_and_perimeter in [square, rectangle, triangle]:
        print(f"\n{'-' * 90}")
        print(f"Назва фігури: {test_figure_area_and_perimeter.name}\n"
              f"Площа фігури: {test_figure_area_and_perimeter.area()}\n"
              f"Периметр фігури: {test_figure_area_and_perimeter.perimeter()}\n")

test_figure_area_and_perimeter()