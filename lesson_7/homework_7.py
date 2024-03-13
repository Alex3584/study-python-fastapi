# **Завдання 1: Наслідування**

# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:

# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)

# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.

# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

# **Завдання 2: Поліморфізм**

# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").

# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.

# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Starting the engine!")

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def drive(self):
        print("Car is driving.")
        print("<------------------------------------------------------>")

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def wheelie(self):
        print("Motorcycle is doing a wheelie.")
        print("<------------------------------------------------------>")

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, frame_material):
        super().__init__(make, model, year)
        self.frame_material = frame_material

    def ring_bell(self):
        print("Ding! Ding!")

    def display_info(self):
        super().display_info()
        print(f"Frame Material: {self.frame_material}")

car = Car("Toyota", "Camry", 2022, "petrol")
motorcycle = Motorcycle("Honda", "CBR600RR", 2021, "inline-four")
bicycle = Bicycle("Giant", "Defy", 2020, "carbon")

car.start_engine()
car.display_info()
car.drive()

motorcycle.start_engine()
motorcycle.display_info()
motorcycle.wheelie()

bicycle.start_engine()
bicycle.display_info()
bicycle.ring_bell()