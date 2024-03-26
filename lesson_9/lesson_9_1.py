# Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)

# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. В цьому класі повинні бути
# методи для створення користувача, оновлення даних користувача та видалення користувача. Переконайтеся,
# що кожен метод відповідає за одну конкретну функцію.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_user(self, new_name=None, new_email=None):
        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email

    def delete_user(self):
        self.name = None
        self.email = None