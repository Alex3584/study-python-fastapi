# Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)

# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання.
# Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують
# лише ті методи, які їм потрібні. Переконайтеся, що жоден з класів не має пустого методу.

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Coppable(ABC):
    @abstractmethod
    def copy(self):
        pass

class Printer(Printable):
    def print(self):
        print("Printing document...")

class Scanner(Scanable):
    def scan(self):
        print("Scanning document...")

class NetworkPrinter(Printable, Scanable, Coppable):
    def print(self):
        print("Printing document...")

    def scan(self):
        print("Scanning document...")

    def copy(self):
        print("Copying document...")