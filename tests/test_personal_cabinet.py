import logging
from selenium.webdriver.common.by import By
import time

class TestCabinet:

    def test_entrance_cabinet(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()
        driver.implicitly_wait(2)

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('enter_button'))
        except:
            raise Exception("Переход незарегистрированного пользователя на вход не был произведен.")

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        time.sleep(1)

        login_button.click()

        time.sleep(1)

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('profile_button'))
        except:
            raise Exception("Переход зарегистрированного пользователя в кабинет не был произведен.")

        logging.info("Переход зарегистрированного пользователя в кабинет был произведен.")

        driver.quit()