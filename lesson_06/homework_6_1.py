'''Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True,
інакше - False. Строку отримати за допомогою функції input()'''
n = 10
print(f"Зараз ми почаклуємо, а саме:\n"
      f"- ми порахуємо кількість унікальних символів;\n"
      f"- якщо їх буде більше {n} - виведемо - True\n"
      f"- якщо їх буде меньше {n} - виведемо - False\n")
some_text = input("Введіть текст: ")
set_some_text = set(some_text)
count_unique_symbols = len(set_some_text)
if count_unique_symbols > n:
    print(f"True")
else:
    print(f"False")
print(f"Ви ввели:\n"
      f"- унікальні символи: {set_some_text}\n"
      f"- кількість інікальних символів: {count_unique_symbols}")