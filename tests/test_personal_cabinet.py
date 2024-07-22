from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCabinet:

    def test_entrance_cabinet(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Личный Кабинет" на главной странице
            login_button = driver_entrance.find_element(By.XPATH, main_menu.button_cabinet)
            login_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(2)

            try:
                driver_entrance.find_element(By.XPATH, "//h2[text()='Вход']")
            except:
                raise Exception("Переход незарегистрированного пользователя на вход не был произведен.")

            driver_entrance.find_element(By.XPATH, entrance_input_path.email_field).send_keys(
                entrance_input_value.email_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.password_field).send_keys(
                entrance_input_value.password_field)
            driver_entrance.find_element(By.XPATH, entrance_input_path.button_form).click()

            login_button.click()

            try:
                driver_entrance.find_element(By.XPATH, "//a[text()='Профиль']")
            except:
                raise Exception("Переход зарегистрированного пользователя в кабинет не был произведен.")

            print("Переход зарегистрированного пользователя в кабинет был произведен.")

        finally:
            driver_entrance.quit()