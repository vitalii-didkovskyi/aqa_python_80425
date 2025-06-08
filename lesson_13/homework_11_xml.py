'''Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо'''

import xml.etree.ElementTree as ET
from pathlib import Path
import logging

# Створюємо шляхи
current_dir = Path(__file__).parent
xml_dir = current_dir / 'work_with_xml'
log_file = xml_dir / 'result_Mezentseva.log'

# Налаштовуємо логер
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def find_value(file_name, group_number):
    tree = ET.parse(file_name)
    root = tree.getroot()

    # Шукаємо всі елементи 'group' та перебираємо їх
    for group in root.findall('group'):
        number_elem = group.find('number')
        if number_elem is not None and number_elem.text == str(group_number):
            try:
                incoming_value = group.find('timingExbytes').find('incoming').text
                logging.info(f"Для групи {group_number}: incoming={incoming_value}")
                return incoming_value
            except AttributeError:
                logging.warning(f"Для групи {group_number} значення incoming - відсутнє.")
                return None

    # Якщо група не знайдена взагалі
    logging.error(f"Група {group_number} не існує в файлі")
    return None

if __name__ == '__main__':
    file_name = xml_dir / 'groups.xml'

    try:
        group_number = int(input("Введіть номер групи: "))
    except ValueError:
        print("Некоректне значення номера групи")
        exit()

    result = find_value(file_name, group_number)
    if result:
        print(f"Для групи {group_number} значення incoming: {result}")
    else:
        print(f"Не знайдено значення для групи {group_number}")
