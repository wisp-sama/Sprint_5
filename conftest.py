import pytest
from selenium import webdriver

class InputValue:

    def __init__(self, email_field, password_field, name_field):
        self.email_field = email_field
        self.password_field = password_field
        self.name_field = name_field

class InputPath:

    def __init__(self, email_field, password_field, button_form, name_field):
        self.email_field = email_field
        self.password_field = password_field
        self.button_form = button_form
        self.name_field = name_field

class MenuElements:

    def __init__(self, right_button_before, right_button_after, button_cabinet, registration, entrance_aside_button, recovery_button):
        self.right_button_before = right_button_before
        self.right_button_after = right_button_after
        self.button_cabinet = button_cabinet
        self.registration = registration
        self.entrance_aside_button = entrance_aside_button
        self.recovery_button = recovery_button

@pytest.fixture
def registration_input_value():
    registration = InputValue(email_field = "felix_zhizhkin_11_439@yandex.ru",
                           password_field = "password123",
                              name_field = "Felix Zhizhkin")
    return registration

@pytest.fixture
def registration_input_path():
    registration = InputPath(email_field = "//form/*[position()=2]//input[@name='name']",
                           password_field = "//input[@type='password']",
                         button_form = "//button[text()='Зарегистрироваться']",
                             name_field = "//input[@name='name']")
    return registration

@pytest.fixture
def entrance_input_value():
    entrance = InputValue(email_field = "felix_zhizhkin_11_999@yandex.ru",
                           password_field = "password123",
                          name_field='')
    return entrance

@pytest.fixture
def entrance_input_path():
    entrance = InputPath(email_field = "//form/*[position()=1]//input[@name='name']",
                           password_field = "//input[@type='password']",
                         button_form = "//button[text()='Войти']",
                         name_field='')
    return entrance

@pytest.fixture
def main_menu():
    main_menu = MenuElements(right_button_before = "//button[text()='Войти в аккаунт']",
                           right_button_after = "//button[text()='Оформить заказ']",
                             button_cabinet = "//p[text()='Личный Кабинет']",
                             registration = "//a[text()='Зарегистрироваться']",
                             entrance_aside_button = "//a[text()='Войти']",
                             recovery_button = "//a[text()='Восстановить пароль']")
    return main_menu

@pytest.fixture
def driver_entrance():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')
    yield driver
    driver.quit()

@pytest.fixture
def driver_registration():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    yield driver
    driver.quit()

