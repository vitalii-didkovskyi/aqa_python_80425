# [GREEN] Завдання-1:
'''
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути
як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує
на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
'''
# [BLUE] Рішення завдання-1:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

def check_team_lead_attributes():
    team_lead = TeamLead('James Bond', 1000000, '007', 'Python', 5)
    assert hasattr(team_lead, 'name')
    assert hasattr(team_lead, 'salary')
    assert hasattr(team_lead, 'department')
    assert hasattr(team_lead, 'programming_language')
    assert hasattr(team_lead, 'team_size')

    # Додаткові перевірки значень
    assert team_lead.name == 'James Bond'
    assert team_lead.salary == 1000000
    assert team_lead.department == '007'
    assert team_lead.programming_language == 'Python'
    assert team_lead.team_size == 5

    print(f"Всі атрибути присутні та мають правильні значення:\n"
          f"    - ім'я: '{team_lead.name}',\n"
          f"    - зарплата: '{team_lead.salary}',\n"
          f"    - відділ: '{team_lead.department}',\n"
          f"    - мова програмування: '{team_lead.programming_language}',\n"
          f"    - кількість людей у команді: '{team_lead.team_size}'\n")

check_team_lead_attributes()
