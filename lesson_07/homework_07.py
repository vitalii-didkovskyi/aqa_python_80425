print(f"{'-' * 10}Issue №1{'-' * 90}")
# task 1
# [GREEN] Завдання:
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# [BLUE] Рішення завдання №1
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    print(f"Таблиця множення числа {number}:")
    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        # print(str(number) + "x" + str(multiplier) + "=" + str(result))
        print(f'{number}x{multiplier}={result}')

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

print()
print(f"{'-' * 10}Issue №2{'-' * 90}")
# task 2
# [GREEN] Завдання:
"""  Написати функцію, яка обчислює суму двох чисел.
"""
# [BLUE] Рішення завдання №2
def sum_of_numbers(a, b):
    return int(a) + int(b)

a = input("Введіть перше число:")
b = input("Введіть друге число:")

result = sum_of_numbers(a, b)
print(f"Cума введених чисел: {a} + {b} = {result}\n")

print(f"{'-' * 10}Issue №3{'-' * 90}")
# task 3
# [GREEN] Завдання:
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
# [BLUE] Рішення завдання №3
def average_of_list(list_of_numbers:list):
    return sum(list_of_numbers) / len(list_of_numbers)

list_of_numbers = list(range(10))
result = average_of_list(list_of_numbers)
print(f"Дано список чисел: {list_of_numbers}:\n"
      f"1. Сума всіх чисел списку: {list_of_numbers[0]} + ... + {list_of_numbers[-1]} = {sum(list_of_numbers)}\n"
      f"2. Кількість чисел в списку = {len(list_of_numbers)}\n"
      f"3. Середнє арифметичне списку: {sum(list_of_numbers)} / {len(list_of_numbers)} = {result}\n"
      f"Відповідь: {result}\n")

print(f"{'-' * 10}Issue №4{'-' * 90}")
# task 4
# [GREEN] Завдання:
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
# [BLUE] Рішення завдання №4
def reverse_string(text: str) -> str:
    return text[::-1]

text = input("Введіть щось: ")
result = reverse_string(text)
print(f"Ви ввели:\n'{text}'\n"
      f"Зворотній порядок введенного:\n"
      f"{result}\n")

print(f"{'-' * 10}Issue №5{'-' * 90}")
# task 5
# [GREEN] Завдання:
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# [BLUE] Рішення завдання №5
def find_longest_word(word:list[str]):
    return max(word, key=len)

some_text = (input("Введіть щось: "))
marks = '.,!?;:()-/\\"\'[]{}«»' # змінна знаків пунктуації
for mark in marks:
    some_text = some_text.replace(mark, ' ') # прибираю з тексту знаки пунктуації
list_of_worlds = some_text.split()

result=find_longest_word(list_of_worlds)
print(f"Ось список з введеними словами:\n{list_of_worlds}\n"
      f"Найдовше слово зі списку: {result}\n")

print(f"{'-' * 10}Issue №6{'-' * 90}")
# task 6
# [GREEN] Завдання:
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# [BLUE] Рішення завдання №6
def find_substring(str1, str2):
    if len(str2) > len(str1):
        return -1
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

print()
print("*" * 108)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

adwentures_of_tom_sawer = '''Tom gave up the brush with reluctance in his face but alacrity in his heart. 
And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel 
in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. 
There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash. 
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; 
and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, 
and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, 
stricken boy in the morning, Tom was literally rolling in wealth.'''

print(f"{'-' * 10}Issue №7{'-' * 90}")
# task 7
# [GREEN] Завдання:
# homework 4 - task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
# HACK: попередня реалізація
# print (f"Літера 'h' зустрічається - {adwentures_of_tom_sawer.count("h")} разів в даному тексті.\n")

# [BLUE] Рішення завдання №7
def count_letter_h(text: str) :
    """
    Рахує кількість літер 'h' у тексті
    """
    return text.lower().count('h')

text = adwentures_of_tom_sawer
result = count_letter_h(text)
print (f"Літера 'h' зустрічається - {result} разів в даному тексті.\n")

print(f"{'-' * 10}Issue №8{'-' * 90}")
# task 8
# [GREEN] Завдання:
# homework 4 - task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

# HACK: попередня реалізація
# count_words = 0
# for word in adwentures_of_tom_sawer.split():
#     if word.istitle():
#         # print(word)
#         count_words += 1
# print(f"В даному списку {count_words} слів починається з великої літери\n")

# [BLUE] Рішення завдання №8
def count_capitalized_words(text: str):
    """
    Рахує кількість слів, які починаються з великої літери
    """
    return sum(1 for word in text.split() if word.istitle())
text = adwentures_of_tom_sawer
result = count_capitalized_words(text)
print(f"В даному тексті {result} слів починається з великої літери\n")

print(f"{'-' * 10}Issue №9{'-' * 90}")
# task 9
# [GREEN] Завдання:
# homework 6.3
'''Є list з даними
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими'''

# HACK: попередня реалізація
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# print(f"Ваш список:\n{lst1}\n")
# lst2 = [k for k in lst1 if type(k) == str ]
# print(f"Відфільтрований список, в якому:\n"
#       f"- використовується лише тип даних -'str':\n{lst2}")

# [BLUE] Рішення завдання №9
def filter_strings(some_list: list):
    """
    Повертає список, що містить лише str значення з вхідного списку.
    """
    # return [item for item in items if isinstance(item, str)]
    return [k for k in some_list if type(k) == str]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)
print(f"Відфільтрований список, в якому використовується лише тип даних 'str':\n{lst2}\n")

print(f"{'-' * 10}Issue №10{'-' * 90}")
# task 10
# [GREEN] Завдання:
# homework 6.4
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

# HACK: попередня реалізація
# lst1 = list(range(10))
# print(f"Ваш список чисел для підрахунку:\n{lst1}\n")
# records = []
# for k in lst1:
#     if k % 2 == 0: # парні числа в списку
#         records.append(k)
# lst2 = sum(records)
#
# # lst2 = sum(k for k in lst1 if k % 2 == 0)
# print(f"Сума парних чисел з списку: {lst2}")

# [BLUE] Рішення завдання №10
def sum_even_numbers(numbers: list):
    """
    Рахує суму парних чисел у списку
    """
    return sum(k for k in numbers if k % 2 == 0)

lst1 = list(range(10))
result = sum_even_numbers(lst1)
print(f"Ваш список чисел для підрахунку:\n{lst1}\n"
      f"Сума парних чисел з списку: {result}")