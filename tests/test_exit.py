import logging
from selenium.webdriver.common.by import By
import time


class TestExit:

    def test_exit(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(2)

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        time.sleep(1)

        login_button.click()

        time.sleep(1)

        button_exit = driver.find_element(By.XPATH, locators_data.main_menu_path().get('exit_button'))
        button_exit.click()

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('enter_button'))
        except:
            raise Exception("Выход пользователя из профиля не был произведен.")

        logging.info("Выход пользователя из профиля был произведен.")

        driver.quit()
