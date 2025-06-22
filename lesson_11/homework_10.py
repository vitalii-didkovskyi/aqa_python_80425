"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

@pytest.mark.parametrize('status', ["success", "expired", "failed"])
def test_login_event(status):
    # тестування входу з різними статусами
    user_name = "Stalker"
    log_event(user_name, status)

    with open('login_system.log', 'r') as file:
        logs_login_content = file.read()
        last_row = logs_login_content.split('\n')[-2]  # -2 бо останній рядок порожній
        assert f"Username: {user_name}, Status: {status}" in last_row

if __name__ == "__main__":
    pytest.main()
