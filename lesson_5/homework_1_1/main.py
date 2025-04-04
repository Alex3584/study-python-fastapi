# **Завдання 1: Робота з функціями**
# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:

# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

import calculator

a = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
b = float(input("Введите второе число: "))


operators = {
"+":calculator.add,
"-":calculator.subtract,
"*":calculator.multiply,
"/":calculator.divide
}

if operator in operators:
    result = operators[operator] (a, b)
    print("Результат: ", result)
else:
    print("Ошибка операции, введите нужный оператор!")
