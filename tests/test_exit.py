from selenium import webdriver
from selenium.webdriver.common.by import By

class TestExit:

    def test_exit(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Личный Кабинет" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.button_cabinet)
            login_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(2)

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(
                entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(
                entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            login_button.click()

            button_exit = driver_entrance.find_element(By.XPATH, "//button[text()='Выход']")
            button_exit.click()

            try:
                driver_entrance.find_element(By.XPATH, "//h2[text()='Вход']")
            except:
                raise Exception("Выход пользователя из профиля не был произведен.")

            print("Выход пользователя из профиля был произведен.")

        finally:
            driver_entrance.quit()