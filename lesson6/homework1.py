# **Завдання 1: Створення класу і об'єктів**

# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == "cat":
            print("Meow")
        elif self.species == "dog":
            print("Woof")
        else:
            print("Unknown sound")

    def info(self):
        print(f"Hello, I am a {self.species}. My name is {self.name} and I am {self.age} years old.")


animal1 = Animal("Murzik", "cat", 2)
animal2 = Animal("Barbos", "dog", 4)

animal1.make_sound()
animal1.info()
animal2.make_sound()
animal2.info()
