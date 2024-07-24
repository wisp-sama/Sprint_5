import logging
from selenium.webdriver.common.by import By

class TestTransitionToConstructor:

    def test_transition_to_constructor(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(2)

        constructor_button = driver.find_element(By.XPATH, locators_data.constructor_path().get('constructor'))
        constructor_button.click()

        try:
            driver.find_element(By.XPATH, locators_data.constructor_path().get('title'))
        except:
            raise Exception("Переход незарегистрированного пользователя в конструктор не был произведен.")

        login_button.click()

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        constructor_button.click()

        try:
            driver.find_element(By.XPATH, locators_data.constructor_path().get('title'))
        except:
            raise Exception("Переход зарегистрированного пользователя в конструктор не был произведен.")

        logging.info("Переход зарегистрированного пользователя в конструктор был произведен.")

        driver.quit()