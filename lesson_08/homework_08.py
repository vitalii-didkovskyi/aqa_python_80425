# [GREEN] Завдання:
'''Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try/except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”'''

# [BLUE] Рішення завдання №1:

def calculate_numbers_of_list():
    try:
        list_of_numbers = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
        for numbers in list_of_numbers:
            numbers_list = numbers.split(',')
            sum_of_numbers = sum(int(number) for number in numbers_list)
            print(sum_of_numbers)
    except ValueError:
        print('Не можу це зробити')

calculate_numbers_of_list()

# [BLUE] Рішення завдання №2 (трішки покращене):

# def calculate_numbers_of_list():
#     # NOTE: спочатку створимо масив, який потім будемо рахувати (наповнюємо через input)
#     list_of_numbers = []
#     count_objects = int(input(f"Введіть кількість об'єктів в масиві: "))
#     for k in range(count_objects):
#         object_of_list = input(f"Введіть ваш {k + 1} об'єкт через кому: ")
#         list_of_numbers.append(object_of_list)
#     print(f"Ваш масив з введених об'єктів:\n{list_of_numbers}\n")
#
#     # NOTE: тепер обчислимо об'єкти в масиві та виведемо результати в іншому масиві
#     result = []
#     try:
#         for numbers in list_of_numbers:
#             numbers_list = numbers.split(',')
#             sum_of_numbers = sum(int(number) for number in numbers_list)
#             result.append(sum_of_numbers)
#     except ValueError:
#         result.append('Не можу це зробити')
#     print(f"Результат додавання об'єктів в середині масиву:\n{result}")
#
# calculate_numbers_of_list()