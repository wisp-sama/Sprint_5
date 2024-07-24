import logging
from selenium.webdriver.common.by import By

class TestRegistration:

    def test_success(self, driver, locators_data, input_data, email_randomizer):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        # Заполняем поле "Имя"
        name_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('name_field'))
        name_field.send_keys(input_data.user_data_new(email_randomizer).get('name_field'))

        # Заполняем поле "Email"
        email_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('email_field'))
        email_field.send_keys(input_data.user_data_new(email_randomizer).get('email_field'))

        # Заполняем поле "Пароль"
        password_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('password_field'))
        password_field.send_keys(input_data.user_data_new(email_randomizer).get('password_field'))

        # Отправляем форму
        register_button = driver.find_element(By.XPATH, locators_data.registration_input_path().get('button_form'))
        register_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        # Проверка на уже зарегистрированного пользователя
        try:
            driver.find_element(By.XPATH, locators_data.registration_input_path().get('existing_user_hint'))
        except:
            pass
        else:
            raise Exception("Пользователь с такими данными уже зарегистрирован")

        # Проверка успешного сообщения
        success_message = driver.find_element(By.XPATH, locators_data.main_menu_path().get('enter_button'))
        assert success_message != "Вход"

        logging.info("Тест успешной регистрации пройден.")

        driver.quit()



    def test_password_too_short(self, driver, locators_data, input_data, email_randomizer):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        # Заполняем поле "Имя"
        name_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('name_field'))
        name_field.send_keys(input_data.user_data_new(email_randomizer).get('name_field'))

        # Заполняем поле "Email"
        email_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('email_field'))
        email_field.send_keys(input_data.user_data_new(email_randomizer).get('email_field'))

        # Заполняем поле "Пароль"
        password_field = driver.find_element(By.XPATH, locators_data.registration_input_path().get('password_field'))
        password_field.send_keys(input_data.user_data_new(email_randomizer).get('password_field')[0:3])

        # Отправляем форму
        register_button = driver.find_element(By.XPATH, locators_data.registration_input_path().get('button_form'))
        register_button.click()

        # Небольшая задержка для ожидания результата
        driver.implicitly_wait(1)

        # Проверка сообщения об ошибке
        error_message = driver.find_element(By.XPATH, locators_data.registration_input_path().get('wrong_password_hint'))
        assert error_message is not None, "Сообщение об ошибке не отображается"

        logging.info("Тест ошибки для некорректного пароля пройден.")

        driver.quit()