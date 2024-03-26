# Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)

# Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг")
# може замінити базовий клас "Фігура" без порушення функціональності. Переконайтеся, що ці підкласи можуть
# використовуватися замість базового класу у всіх контекстах без проблем.

from  abc import  ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2