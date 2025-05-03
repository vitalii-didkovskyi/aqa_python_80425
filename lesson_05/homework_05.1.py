# [BLUE] ДЗ 5.1. Пошук автомобіля
'''Існує деяка інформація про автомобілі з кольором, роком випуску, об'ємом двигуна, типом автомобіля та ціною.
Маємо критерії пошуку у вигляді кортежу (рік ≥, об'єм двигуна ≥, ціна ≤). Напишіть код, який допоможе нам отримати
автомобілі, які відповідають критеріям пошуку. Автомобілі повинні бути відсортовані за зростанням ціни.
Ми повинні вивести до п'яти (5) перших знайдених елементів
'''

# [GREEN] Завдання:
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
# HACK: оптимальне рішення
search_criteria = (2017, 1.6, 36000)
def find_cars(car_data, search_criteria):
    print(f"Топ 5 авто, які відсортовано за ціною а також які задовільняють "
          f"критерії пошуку, а саме:\n"
          f"- від {search_criteria[0]} року включно;\n"
          f"- об'єм двигуна від {search_criteria[1]} включно;\n"
          f"- ціна від {search_criteria[2]} і нижче:\n")

    filtered_cars = []
    for car, details in car_data.items():
        year = details[1]
        engine_volume = details[2]
        price = details[4]
        if (year >= search_criteria[0]
                and engine_volume >= search_criteria[1]
                and price <= search_criteria[2]):
            filtered_cars.append((car, details))
            # print(car, details)

    sorted_cars = sorted(filtered_cars, key=lambda x: x[1][4])

    for car in sorted_cars[:5]:
        print(car)

find_cars(car_data, search_criteria)

# HACK: моє рішення
# def find_cars(car_data, search_criteria):
#     print(f"Топ 5 авто, які відсортовано за ціною а також які задовільняють "
#           f"критерії пошуку, а саме:\n"
#           f"- від {search_criteria[0]} року включно;\n"
#           f"- об'єм двигуна від {search_criteria[1]} включно;\n"
#           f"- ціна від {search_criteria[2]} і нижче:\n")
#     top_five_cars = []
#     sorted_cars = sorted(car_data.items(), key=lambda x: x[1][4])
#     for record in sorted_cars:
#         year = record[1][1]
#         engine_volume = record[1][2]
#         price = record[1][4]
#         if (year >= search_criteria[0]
#                 and engine_volume >= search_criteria[1]
#                 and price <= search_criteria[2]):
#             top_five_cars.append(record)
#             if len(top_five_cars) == 5:
#                 break
#     for car in top_five_cars:
#         print(car)
#
# find_cars(car_data, search_criteria)

# HACK: інше рішення
# for key, value in car_data.items():
#     print(key, value)
# for key, value in sorted(car_data.items(), key=lambda x: x[1][4]):
#     print(key, value)
# count = 0
# print(f"Топ 5 авто, який відсортовано за ціною а також які задовільняють критерії пошуку, а саме:"
#       f"- ≥ 2017 року; об'єм двигуна ≥ 1.6; ціна ≤ 36000:")
# for record in sorted(car_data.items(), key=lambda x: x[1][4]):
#     year = record[1][1]
#     engine_volume = record[1][2]
#     price = record[1][4]
#     if (year >= search_criteria[0]
#             and engine_volume >= search_criteria[1]
#             and price <= search_criteria[2]):
#         print(record)
#         count += 1
#         if count == 5:
#             break