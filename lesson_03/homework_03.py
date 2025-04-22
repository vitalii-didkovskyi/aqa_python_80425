print('Issue №1-3')
# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(f"{alice_in_wonderland}\n")
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
print('Issue №4')
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436402
azov_sea_square = 37800
print(f"Загальна площа Чорного та Азовського морів: {black_sea_square} км2 + {azov_sea_square} км2 = {black_sea_square + azov_sea_square} км2\n")
print('Issue №5')
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
global_storage = 375291    #сума всіх товарів на 3ьох складах
storage_1_and_2 = 250449   #сума товарів на 1ому та 2ому складах
storage_2_and_3 = 222950   #сума товарів на 2ому та 3ому складах

storage_1 = global_storage - storage_2_and_3            #сума товарів на 1ому складі
storage_3 = global_storage - storage_1_and_2            #сума товарів на 3ому складі
storage_2 = (global_storage - (storage_1 + storage_3))  #сума товарів на 2ому складі

print(f"Товарів на №1 складі: {global_storage} - {storage_2_and_3} = {storage_1} шт.\n"
      f"Товарів на №2 складі: {global_storage} - {storage_1} - {storage_3} = {storage_2} шт.\n"
      f"Товарів на №3 складі: {global_storage} - {storage_2_and_3} = {storage_3} шт.\n")
print('Issue №6')
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179      # місячна платня
total_paymant_months = 18   # загальна кількість місяців для повної виплати - півтора року
computer_price = monthly_payment * total_paymant_months    # загальна вартість комп’ютера
print (f"Загальна вартість комп'ютера за пітора року: {computer_price} грн.\n")
print('Issue №7')
# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# print (f"a = {8019 - (8019 // 8) * 8} \n"
#        f"b = {9907 - (9907 // 9) * 9}\n"
#        f"c = {2789 - (2789 // 5) * 5}\n"
#        f"d = {7248 - (7248 // 6) * 6}\n"
#        f"e = {7128 - (7128 // 5) * 5}\n"
#        f"f = {19224 - (19224 // 9) * 9}")
a = 8019 % 8  # остача при операції - 8019 : 8
b = 9907 % 9  # остача при операції - 9907 : 9
c = 2789 % 5  # остача при операції - 2789 : 5
d = 7248 % 6  # остача при операції - 7248 : 6
e = 7128 % 5  # остача при операції - 7128 : 5
f = 19224 % 9  # остача при операції - 19224 : 9
print(f"Остача від ділення чисел:\n"
      f"a) 8019 : 8 = {a}\n"
      f"b) 9907 : 9 = {b}\n"
      f"c) 2789 : 5 = {c}\n"
      f"d) 7248 : 6 = {d}\n"
      f"e) 7128 : 5 = {e}\n"
      f"f) 19224 : 9 = {f}\n")
print('Issue №8')
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_cost = 274
medium_pizza_cost = 218
juice_cost = 35
cake_cost = 350
water_cost = 21
amount_order = (4 * big_pizza_cost) + (2 * medium_pizza_cost) + (4 * juice_cost) + cake_cost + (3 * water_cost)
# print(f"Сума великих піц: 4 * 274 = {4 * 274} грн.\n"
#       f"Сума середніх піц: 2 * 218 = {2 * 218} грн.\n"
#       f"Сума соку: 4 * 35 = {4 * 35} грн.\n"
#       f"Сума тортів: 1 * 350 = {1 * 350} грн.\n"
#       f"Сума води: 3 * 21 = {3 * 21} грн.\n"
#       f"Загальна сума: {4 * 274} + {2 * 218} + {4 * 35} + {1 * 350} + {3 * 21} = {(4 * 274) + (2 * 218) + (4 * 35) + (1 * 350) + (3 * 21)} грн.")
print(f"Загальна сума всього замовлення {amount_order} грн.\n")
print('Issue №9')
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photot_count = 232
# photot_count = 233
photo_per_page = 8
total_pages_count = (photot_count // photo_per_page) # кількість сторінок
if photot_count % photo_per_page != 0:
    total_pages_count += 1                           # якщо при діленні є залишок - доадємо ще 1 сторінку
print(f"Загальна кількість сторінок, яка необхідна аби вклеїти всі фото - {total_pages_count} ст.\n")
print('Issue №10')
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
fuel_per_100 = 9
fuel_capacity = 48
fuel_per_distance = (total_distance * fuel_per_100) / 100   # необідна кількість л. бензину для подорожі
refueling_count = fuel_per_distance // fuel_capacity        # кількість повних заправок для подорожі
if fuel_per_distance % fuel_capacity != 0:
    refueling_count += 1                                    # якщо при діленні є залишок - доадємо ще 1 заправку
print (f"1) Для подорожі, відстанню {total_distance} км необхідно - {fuel_per_distance} л. пального.\n"
       f"2) Для подорожі, відстанню {total_distance} км необхідна кількість заправок - {int(refueling_count)} р.")