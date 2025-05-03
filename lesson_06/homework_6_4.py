'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

lst1 = list(range(10))

# n = int(input("Введіть число, з якого буде складатись список: "))
# lst1 = [int(input(f"Введіть число {k+1}: ")) for k in range(n)]

print(f"Ваш список чисел для підрахунку:\n{lst1}\n")
records = []
for k in lst1:
    if k % 2 == 0: # парні числа в списку
        records.append(k)
lst2 = sum(records)

# lst2 = sum(k for k in lst1 if k % 2 == 0)
print(f"Сума парних чисел з списку: {lst2}")