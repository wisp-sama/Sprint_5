from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistration:

    def test_success(self, registration_input_value, registration_input_path, driver_registration):
        try:
            # Заполняем поле "Имя"
            name_field = driver_registration.find_element(By.XPATH, registration_input_path.name_field)
            name_field.send_keys(registration_input_value.name_field)

            # Заполняем поле "Email"
            email_field = driver_registration.find_element(By.XPATH, registration_input_path.email_field)
            email_field.send_keys(registration_input_value.email_field)

            # Заполняем поле "Пароль"
            password_field = driver_registration.find_element(By.XPATH, registration_input_path.password_field)
            password_field.send_keys(registration_input_value.password_field)

            # Отправляем форму
            register_button = driver_registration.find_element(By.XPATH, registration_input_path.button_form)
            register_button.click()

            # Небольшая задержка для ожидания результата
            driver_registration.implicitly_wait(1)

            # Проверка на уже зарегистрированного пользователя
            try:
                driver_registration.find_element(By.XPATH, "//p[text()='Такой пользователь уже существует']")
            except:
                pass
            else:
                raise Exception ("Пользователь с такими данными уже зарегистрирован")

            # Проверка успешного сообщения
            success_message = driver_registration.find_element(By.XPATH, "//h2[text()='Вход']")
            assert success_message != "Вход"

            print("Тест успешной регистрации пройден.")
        finally:
            driver_registration.quit()



    def test_password_too_short(self, registration_input_value, registration_input_path, driver_registration):
        try:
            # Заполняем поле "Имя"
            name_field = driver_registration.find_element(By.XPATH, registration_input_path.name_field)
            name_field.send_keys(registration_input_value.name_field)

            # Заполняем поле "Email"
            email_field = driver_registration.find_element(By.XPATH, registration_input_path.email_field)
            email_field.send_keys(registration_input_value.email_field)

            # Заполняем поле "Пароль"
            password_field = driver_registration.find_element(By.XPATH, registration_input_path.password_field)
            password_field.send_keys(registration_input_value.password_field[0:3])

            # Отправляем форму
            register_button = driver_registration.find_element(By.XPATH, registration_input_path.button_form)
            register_button.click()

            # Небольшая задержка для ожидания результата
            driver_registration.implicitly_wait(1)

            # Проверка сообщения об ошибке
            error_message = driver_registration.find_element(By.XPATH,
                                                "//p[text()='Некорректный пароль']")
            assert error_message is not None, "Сообщение об ошибке не отображается"

            print("Тест ошибки для некорректного пароля пройден.")

        finally:
            driver_registration.quit()