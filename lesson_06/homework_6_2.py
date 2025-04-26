'''Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''
search_criteria = ('h', 'H')
print(f"Перевірка тексту на наявність '{search_criteria[0]}' та '{search_criteria[1]}' літер:\n"
      f"- якщо дані символи будуть знайдені - цикл зупиниться;\n"
      f"- інакше - цикл буде продовжуватись.\n")
while True:
    some_text = input("Введіть текст: ")
    set_some_text = set(some_text)
    set_search_criteria = set(search_criteria)
    if set_search_criteria & set_some_text:
        print("Цикл зупинено через введення h/H символу/ів.")
        break
    else:
        print("Цикл продовжено.\n")
        continue