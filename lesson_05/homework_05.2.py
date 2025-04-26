# [BLUE] ДЗ 5.2. Лист кортежiв ( List of tuples)
'''Заданий список кортежів (ім'я, прізвище, вік, професія, місце проживання):

Додайте свій новий запис на початок даного списку.
У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат.
Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки
'''

# [GREEN] Завдання:
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
print('Issue №1')
# new_record_04_25 = ('Maryna', 'Mezentseva', 31, 'QA - Engineer', 'Kyiv') # HACK: тимчасове рішення
# people_records.insert(0, new_record_04_25)
people_records.insert(0, ('Maryna', 'Mezentseva', 31, 'QA - Engineer', 'Kyiv'))
print(f"Додали свій запис до даного списку в комірку з індексом 0:\n{people_records}\n")
# print(people_records[0]) # HACK: w-check

print('Issue №2')
# print(people_records[1])
# print(people_records[5])
people_records[1] , people_records[5] = people_records[5], people_records[1]
# print(people_records[1])
# print(people_records[5])
print(f"Оміняли елементи місцям та оновили список:\n{people_records}\n")

print('Issue №3')
some_records = people_records[6] , people_records[10] , people_records[13]
print(f"Записи у списку з індексами 6, 10, 13:\n{some_records}")
for records in some_records:
    age = records[2]
    name = records[0]
    if age >= 30:
        print(f"Дана персона {name} - старша 30 років")
    else:
        print(f"Дана персона {name} - молодша 30 років")
