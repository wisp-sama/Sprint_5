class Locators:

    def registration_input_path(self):
        registration = {}
        registration['email_field'] = "//form/*[position()=2]//input[@name='name']"
        registration['password_field'] = "//input[@type='password']"
        registration['button_form'] = "//button[text()='Зарегистрироваться']"
        registration['name_field'] = "//input[@name='name']"
        registration['existing_user_hint'] = "//p[text()='Такой пользователь уже существует']"
        registration['wrong_password_hint'] = "//p[text()='Некорректный пароль']"
        return registration

    def entrance_input_path(self):
        entrance = {}
        entrance['email_field'] = "//form/*[position()=1]//input[@name='name']"
        entrance['password_field'] = "//input[@type='password']"
        entrance['button_form'] = "//button[text()='Войти']"
        return entrance

    def main_menu_path(self):
        main_menu = {}
        main_menu['right_button_entrance'] = "//button[text()='Войти в аккаунт']"
        main_menu['right_button_order'] = "//button[text()='Оформить заказ']"
        main_menu['button_cabinet'] = "//p[text()='Личный Кабинет']"
        main_menu['registration'] = "//a[text()='Зарегистрироваться']"
        main_menu['entrance_aside_button'] = "//a[text()='Войти']"
        main_menu['recovery_button'] = "//a[text()='Восстановить пароль']"
        main_menu['exit_button'] = "//button[text()='Выход']"
        main_menu['enter_button'] = "//h2[text()='Вход']"
        main_menu['profile_button'] = "//a[text()='Профиль']"
        return main_menu

    def constructor_path(self):
        constructor = {}
        constructor['sauces'] = "//span[text()='Соусы']"
        constructor['rolls'] = "//span[text()='Булки']"
        constructor['fillings'] = "//span[text()='Начинки']"
        constructor['rolls_selected'] = "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/*[text()='Булки']"
        constructor['sauces_selected'] = "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/*[text()='Соусы']"
        constructor['fillings_selected'] = "//*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/*[text()='Начинки']"
        constructor['constructor'] = "//p[text()='Конструктор']"
        constructor['title'] = "//h1[text()='Соберите бургер']"
        return constructor

class InputValue:

    def user_data_existing(self):
        # Данные уже зарегистрированного пользователя
        user_data = {}
        user_data['email_field'] = "felix_zhizhkin_11_999@yandex.ru"
        user_data['password_field'] = "password123"
        user_data['name_field'] = "Felix Zhizhkin"
        return user_data

    def user_data_new(self, email):
        # Данные нового пользователя
        user_data = {}
        user_data['email_field'] = email
        user_data['password_field'] = "password123"
        user_data['name_field'] = "Felix Zhizhkin"
        return user_data