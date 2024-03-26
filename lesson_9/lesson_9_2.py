# Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)

# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад, "Коло" (Circle)
# та "Прямокутник" (Rectangle). Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи
# існуючі класи. Використовуйте принцип OCP для розширення функціональності.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class AreaCalculator:
    @staticmethod
    def calculate(shape):
        return shape.area()