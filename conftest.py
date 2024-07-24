import pytest
import data
from random import randint
from selenium import webdriver


@pytest.fixture
def email_randomizer():
    #Генерируем адрес почты со случайными цифрами
    email_field = "feliks_zhizhkin_11_"
    for i in range(3):
        email_field += str(randint(0, 9))
    email_field += "@yandex.ru"
    return email_field

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')
    yield driver
    driver.quit()

@pytest.fixture
def locators_data():
    locators = data.Locators()
    return locators

@pytest.fixture
def input_data():
    input = data.InputValue()
    return input