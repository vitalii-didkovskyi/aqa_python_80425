# [GREEN] Завдання:
'''Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log'''

# [BLUE] Рішення завдання:

import json
from pathlib import Path
import logging

# Створюємо шляхи
current_dir = Path(__file__).parent
json_dir = current_dir / 'work_with_json'
log_file = json_dir / 'result_Mezentseva.log'


# Налаштовуємо логер
logging.basicConfig(
    level=logging.ERROR,
    filename=log_file,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"Даний json файл '{file_path.name}' - валідний.")
        return True
    except json.JSONDecodeError as type_error:
        error_msg = f"Даний json файл '{file_path.name}' - невалідний. Помилка: {type_error}"
        logging.error(error_msg)
        print(error_msg)
        return False

json_files = json_dir.glob('*.json')
for file in json_files:
    validate_json(file)