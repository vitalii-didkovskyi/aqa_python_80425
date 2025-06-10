# [GREEN] Завдання:
'''Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент",який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.'''

# [BLUE] Рішення завдання:

class Student():

    def __init__(self, name, surname, age, average):
        self.name = name
        self.surname = surname
        self.age = age
        self.average = average

    def change_average(self, new_average):
        self.average = new_average

    def __str__(self):
        return f'{tom.name, tom.surname, tom.age, tom.average}'

# Створюємо об'єкт класу "Студент"
tom = Student('Tom', 'Jery', 23, 95)

print(f'Інформація про студента до зміни середнього балу:\n'
      f'{tom}')
print(f"{'-' * 90}")

# Вводимо новий середній бал студента
while True:
    try:
        typing_of_average = int(input('Введіть новий середній бал студента: '))
        break
    except ValueError:
        print("Некоректне значення середнього балу.")

# Змінюємо середній бал студента
tom.change_average(typing_of_average)

print(f"{'-' * 90}")

print(f'Інформація про студента після зміни середнього балу:\n'
      f'{tom}')