import logging
from selenium.webdriver.common.by import By

class TestEntrance:

    def test_main(self, driver, locators_data, input_data):
        # Нажмите кнопку "Войти в аккаунт" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('right_button_entrance'))
        login_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('right_button_order'))
        except:
            raise Exception("Тест входа по кнопке «Войти в аккаунт» на главной не пройден.")
        else:
            logging.info("Тест входа по кнопке «Войти в аккаунт» на главной пройден.")

        driver.quit()

    def test_cabinet(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('right_button_order'))
        except:
            raise Exception("Тест входа по кнопке «Войти в аккаунт» с личного кабинета не пройден.")

        logging.info("Тест входа по кнопке «Войти в аккаунт» с личного кабинета пройден.")

        driver.quit()

    def test_registration(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()

        registration_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('registration'))
        registration_button.click()

        entrance_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('entrance_aside_button'))
        entrance_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('right_button_order'))
        except:
            raise Exception("Тест входа по кнопке «Войти в аккаунт» из формы регистрации не пройден.")

        logging.info("Тест входа по кнопке «Войти в аккаунт» из формы регистрации пройден.")

        driver.quit()

    def test_recovery(self, driver, locators_data, input_data):
        # Нажмите кнопку "Личный Кабинет" на главной странице
        login_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('button_cabinet'))
        login_button.click()

        recovery_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('recovery_button'))
        recovery_button.click()

        entrance_button = driver.find_element(By.XPATH, locators_data.main_menu_path().get('entrance_aside_button'))
        entrance_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('email_field')).send_keys(
            input_data.user_data_existing().get('email_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('password_field')).send_keys(
            input_data.user_data_existing().get('password_field'))
        driver.find_element(By.XPATH, locators_data.entrance_input_path().get('button_form')).click()

        try:
            driver.find_element(By.XPATH, locators_data.main_menu_path().get('right_button_order'))
        except:
            raise Exception("Тест входа по кнопке «Войти в аккаунт» с формы восстановления не пройден.")

        logging.info("Тест входа по кнопке «Войти в аккаунт» с формы восстановления пройден.")

        driver.quit()