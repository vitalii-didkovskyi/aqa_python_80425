# [GREEN] Завдання:
'''Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv'''

# [BLUE] Рішення завдання:

import csv
from pathlib import Path

# Створюємо шляхи
current_dir = Path(__file__).parent
csv_dir = current_dir / 'work_with_csv'
file1_path = csv_dir / 'random-michaels.csv'
file2_path = csv_dir / 'r-m-c.csv'
result_file = csv_dir / 'result_Mezentseva.csv'

def remove_duplicates(file_name):
    # Зчитуємо дані з файлу та видаляємо дублікати
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        all_rows = list(reader)
        unique_rows = list(set(tuple(row) for row in all_rows))
    return all_rows, unique_rows

def write_to_file(file_name, rows):
    # Записуємо унікальні дані у файл
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)

# Перевіряємо наявність дублікатів
all_rows1, unique_rows1 = remove_duplicates(file1_path)
all_rows2, unique_rows2 = remove_duplicates(file2_path)

# Об'єднуємо унікальні рядки з обох файлів та видаляємо дублікати
unique_rows = list(set(tuple(row) for row in all_rows1 + all_rows2))

# Записуємо результат у файл
write_to_file(result_file, unique_rows)