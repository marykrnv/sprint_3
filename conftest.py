import random

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def email():
    return f'mary_kir{random.randint(1, 1000000)}@mail.ru'


@pytest.fixture()
def password():
    return f'edbfibewir{random.randint(1, 10000000)}'
