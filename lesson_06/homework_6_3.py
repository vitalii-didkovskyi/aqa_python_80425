'''Є list з даними
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2),
який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими'''

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(f"Ваш список:\n{lst1}\n")
# lst2 = []
# for records in lst1:
#     if type(records) == str:
#         lst2.append(records)
#         # print(f"ляля:{records}")
#     else:
#         continue
# print(f"Відфільтрований список, в якому:\n"
#       f"- використовується лише тип даних -'str':\n{lst2}")

lst2 = [k for k in lst1 if type(k) == str ]
print(f"Відфільтрований список, в якому:\n"
      f"- використовується лише тип даних -'str':\n{lst2}")