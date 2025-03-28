# **Завдання 2: Створення та імпорт власних модулів**

# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:

# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.

# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

import utilities

numbers = [10, 22, 13, 44, 5]

average = utilities.calculate_average(numbers)
max_number = utilities.find_max(numbers)

print(f"The average is: {average}")
print(f"The maximum number is: {max_number}")