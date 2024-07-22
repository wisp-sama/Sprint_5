from selenium import webdriver
from selenium.webdriver.common.by import By

class TestEntrance:

    def test_main(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Войти в аккаунт" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.right_button_before)
            login_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            try:
                driver_entrance.find_element(By.XPATH, main_menu.right_button_after)
            except:
                raise Exception ("Тест входа по кнопке «Войти в аккаунт» на главной не пройден.")
            else:
                print("Тест входа по кнопке «Войти в аккаунт» на главной пройден.")
        finally:
            driver_entrance.quit()

    def test_cabinet(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Личный Кабинет" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.button_cabinet)
            login_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(
                entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(
                entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            try:
                driver_entrance.find_element(By.XPATH, main_menu.right_button_after)
            except:
                raise Exception("Тест входа по кнопке «Войти в аккаунт» с личного кабинета не пройден.")
            else:
                print("Тест входа по кнопке «Войти в аккаунт» с личного кабинета пройден.")
        finally:
            driver_entrance.quit()

    def test_registration(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Личный Кабинет" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.button_cabinet)
            login_button.click()

            registration_button = driver_entrance.find_element(By.XPATH, main_menu.registration)
            registration_button.click()

            entrance_button = driver_entrance.find_element(By.XPATH, main_menu.entrance_aside_button)
            entrance_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(
                entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(
                entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            try:
                driver_entrance.find_element(By.XPATH, main_menu.right_button_after)
            except:
                raise Exception("Тест входа по кнопке «Войти в аккаунт» из формы регистрации не пройден.")
            else:
                print("Тест входа по кнопке «Войти в аккаунт» из формы регистрации пройден.")
        finally:
            driver_entrance.quit()

    def test_recovery(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Личный Кабинет" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.button_cabinet)
            login_button.click()

            recovery_button = driver_entrance.find_element(By.XPATH, main_menu.recovery_button)
            recovery_button.click()

            entrance_button = driver_entrance.find_element(By.XPATH, main_menu.entrance_aside_button)
            entrance_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(
                entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(
                entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            try:
                driver_entrance.find_element(By.XPATH, main_menu.right_button_after)
            except:
                raise Exception("Тест входа по кнопке «Войти в аккаунт» с формы восстановления не пройден.")
            else:
                print("Тест входа по кнопке «Войти в аккаунт» с формы восстановления пройден.")
        finally:
            driver_entrance.quit()